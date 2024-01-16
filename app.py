from typing import List, Tuple
from fastapi import FastAPI, HTTPException

def largest_rectangle(matrix: List[List[int]]) -> Tuple[int, int]:
    if not matrix or not matrix[0]:
        raise ValueError("Invalid matrix")

    rows, cols = len(matrix), len(matrix[0])
    max_area = 0
    max_num = None

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] != -9:
                num = matrix[r][c]
                width = 0
                while c + width < cols and matrix[r][c + width] == num:
                    width += 1

                height = 0
                for i in range(r, rows):
                    if matrix[i][c] == num:
                        height += 1
                    else:
                        break

                area = width * height
                if area > max_area:
                    max_area = area
                    max_num = num

    return max_num, max_area

app = FastAPI()

@app.post("/largest_rectangle")
async def calculate_largest_rectangle(matrix: List[List[int]]):
    try:
        result = largest_rectangle(matrix)
        return {"number": result[0], "area": result[1]}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))