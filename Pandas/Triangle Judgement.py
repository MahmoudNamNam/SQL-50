import pandas as pd
import numpy as np

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    x, y, z = triangle['x'], triangle['y'], triangle['z']
    conditions = (x + y > z) & (y + z > x) & (x + z > y)
    triangle['triangle'] = np.where(conditions, 'Yes', 'No')
    return triangle




import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = triangle.apply(
        lambda t: 'Yes' if ((t.x + t.y > t.z) & (t.y + t.z > t.x) & (t.x + t.z > t.y)) else 'No', axis=1)

    return triangle