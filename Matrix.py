import aiohttp
import asyncio

import re
import numpy as np

async def get_text(url:str) -> str:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.text()
    except aiohttp.ClientError as ex:
        return f"ClientError {ex}"
    except TimeoutError as ex:
        return f"TimeoutError {ex}"


def text_to_matrix(text:str) -> np.array:
    nums = re.findall(r"\d+", text)
    nums_list = [int(num) for num in nums]
    size = int(len(nums_list)**0.5)
    
    return np.array(nums_list).reshape(size, size)


def rotate_and_collect(matrix:np.array) -> list[int]:
    result = []
    while matrix.size > 0:
        matrix = np.rot90(matrix, -1)
        result.extend(matrix[0][::-1])
        matrix = np.delete(matrix, 0, axis=0)
    
    return result


async def get_matrix(url:str) -> list[int]:
    if type(url) != str:
        raise TypeError("Argument of get_matrix() must be string")

    pattern = r"^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
    if not re.search(pattern, url):
        raise ValueError("Argument of get_matrix() is not website address")

    text = await get_text(url)
    matrix = text_to_matrix(text)
    return rotate_and_collect(matrix)    


if __name__ == "__main__":
    try:
        asyncio.run(get_matrix(url)) 
    except Exception:
        print("Something went wrong in get_matrix()")   