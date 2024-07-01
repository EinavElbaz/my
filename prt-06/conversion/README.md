# `dd_to_dms` Function Documentation

The `dd_to_dms` function converts decimal degrees to degrees, minutes, and seconds

## Function Signature

 python
def dd_to_dms(decimal_degrees):
    
    Convert decimal degrees to degrees, minutes, and seconds.

## Parameters:

* `decimal_degrees` (float): Decimal degrees to be converted.

## Returns:

* `degrees` (int): Integer part of the degrees.
*  `minutes` (int): Integer part of the minutes.
*  `seconds` (float): Decimal part of the minutes converted to seconds.

## Example Usage

### Example 1:

Convert 41.85 degrees to degrees, minutes, and seconds:

```python
degrees, minutes, seconds = dd_to_dms(41.85)
print(f"41.85 degrees = {degrees} degrees, {minutes} minutes, {seconds:.2f} seconds")
