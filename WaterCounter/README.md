# WaterCounter

# Usage
```
#include <stdio.h>
#include "src/water_count.h"

#define ARRAY_LENGTH(array) (sizeof(array) / sizeof(array[0]))

int main()
{
	/* column height values */
    int numbers[] = {3, 2, 1, 2, 3, 1, 1, 2};
    int result = water_count(numbers, ARRAY_LENGTH(numbers));
    printf("Count = %d\n", result);
    return 0;
}
```
