import polars as pl
from polars.testing import assert_frame_equal

def test_sql_query_execution() -> None:
    df = pl.DataFrame(
        {
            "id": ["1", "2", "3"],
            "bar": [6.0, 7.0, 8.0],
        }
    )
    result = df.sql("SELECT COUNT(*) FROM self")
    expected = pl.DataFrame({"len": [3]}, schema={"len": pl.UInt32})
    assert_frame_equal(result, expected)
