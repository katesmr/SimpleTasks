#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CLEAR(list, length) memset(list, 0, sizeof(list[0]) * (length))

#define MIN(num1, num2) ((num1)<(num2)) ? (num1) : (num2)

int max_inner_index(int *number_list, int *index_list, int length)
{
    int i;
    int tmp;
    int max_index;
    int max_number;
    max_index = *(index_list + 0);
    max_number = number_list[max_index];
    for(i = 1; i < length; ++i)
    {
        tmp = *(index_list + i);
        if(number_list[tmp] > max_number)
        {
            max_index = tmp;
            max_number = number_list[max_index];
        }
    }
    return max_index;
}

int compute_sum(int *numbers, int first_border, int last_border)
{
    /* choice smaller border, because water fillto the minimum value */
    int border_width = MIN(numbers[first_border], numbers[last_border]);
    int i;
    int sum = 0;
    for(i = first_border + 1; i < last_border; ++i)
    {
        sum += border_width - numbers[i];
    }
    return sum;
}

int water_count(int *number_list, int len)
{
    int is_find_border = 0;
    int first_border;
    int last_border = -1; /* condition of exit from inner cycle */
    int i;
    int j;
    int next;
    int current;
    int inner_number;
    int inner_index;
    int *inner_index_list = (int*)calloc(len, sizeof(int));
    int max_number;
    int max_index;
    int index = 0;
    int inner_index_list_length = 0;
    int res = 0;

    for(i = 0; i < len; ++i)
    {
        if(is_find_border)
        {
            if(last_border > 0 && last_border < len)
            {
                res += compute_sum(number_list, first_border, last_border);
                i = last_border;  /*  shift index on index of new element */
                is_find_border = 0;
                last_border = -1;
            }
            else
            {
                break;
            }
        }
        current = number_list[i];
        if(i != len - 1)
        {
            next = number_list[i + 1];
            if(current > next)
            {
                first_border = i;  /* the possible first index border */
                j = i + 1;  /* index of which will be considered where there is a deepening for water */
                while(j <= len)
                {
                    /* searching of last border must be only from second position from first border
                    in order to have a deepening for water*/
                    inner_index = j + 1;
                    inner_number = number_list[inner_index];
                    if(current == inner_number || current < inner_number) 
                    {
                        /* case when both borders have equals height
                        or last border higher */
                        last_border = inner_index;
                        CLEAR(inner_index_list, len); 
                        index = 0;
                        is_find_border = 1;
                        break;
                    }
                    else if(j == len && last_border == -1)
                    {
                        /* case when search of last border occures on the remaining part of list
                        then last border value will be less than fitborder and bigger others */
                        inner_index_list_length = ((number_list + len) - (number_list + i)) - 1;
                        max_index = max_inner_index(number_list, inner_index_list, inner_index_list_length);
                        max_number = number_list[max_index];
                        if(next < max_number)
                        {
                            last_border = max_index;
                            is_find_border = 1;
                        }
                        else
                        {
                            last_border = -1;
                            is_find_border = 0;
                            CLEAR(inner_index_list, len);
                            index = 0;
                        }
                        break;
                    }
                    *(inner_index_list + index) = j; /* save indexes of inner list */
                    j++;
                    index++;
                }
            }
        }
    }
    free(inner_index_list);
    return res;
}