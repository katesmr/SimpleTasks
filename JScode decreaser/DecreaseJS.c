#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

#define SKIP_COMMENT \
	state = IS_IN_COMMENT; \
	GET_NEXT_SAFETY; \
	isGetNext = 1; \
	continue

#define GET_NEXT_SAFETY \
	next = fgetc(sourse); \
	if (EOF == next) break

#define EXIT_FROM_BLOCK(comparison) \
	(comparison) == token && !(escapeCounter & 1)

#define BUFFER_SIZE 2
static int buffer[BUFFER_SIZE + 1];

int bufferPosition = 0; 

enum
{
	SLASH = '/',
	ESCAPE = '\\',
	ASTERISK = '*',
	NEW_LINE = '\n',
	UNDERSCORE = '_',
	DOLLAR_ICON = '$',
	CLOSED_BRACE = '}',
	DOUBLE_QUOTE = '"',
	SINGLE_QUOTE = '\'',
	CLOSED_BRACKED = ')',
	CLOSED_SQUARE_BRACKED = ']'
};

enum
{
	IS_IN_CODE,
	IS_IN_COMMENT,
	IS_IN_STRING_OR_REGEX
} state;

int isAlnum(int ch);

int regexRecognizing();

void fillBuffer(int token);

void minify(FILE *sourse, FILE *destintion);

void main() {
	FILE *source;
	FILE *destination;

	destination = fopen("d.txt", "w");
	if (destination)
	{
		source = fopen("lab6.js", "r");
		if (source)
		{
			minify(source, destination);
		}
		fclose(source);
	}
	fclose(destination);
}

void minify(FILE *sourse, FILE *destintion)
{
	int next;
	int token;
	int closedChar;

	int isGetNext = 0;
	int isSingleComment = 0;
	int isMultipleComment = 0;

	int spaceCouner = 0;
	int escapeCounter = 0;
	int newLineCounter = 0;	

	state = IS_IN_CODE;

	while (1)
	{
 		if (!isGetNext)
		{
			token = fgetc(sourse);
		}
		else
		{
			token = next;
			isGetNext = 0;
		}
		if (EOF == token) 
		{
			break;
		}

		if (IS_IN_CODE == state)
		{
			escapeCounter = 0;
			if (isspace(token))
			{
				/*
					a special case when the end of the line is not symbol ';',
					and before new line stand spaces, then should not skip new line like repeateble symbol,
					becouse it will be a wrong
				*/
				if (NEW_LINE == token)
				{
					spaceCouner = 0;
					if (newLineCounter++)
					{
						continue;
					}
				}
				if (spaceCouner++)
				{
					continue;
				}
			}
			else
			{
				spaceCouner = 0;
				newLineCounter = 0;
				if (SINGLE_QUOTE == token || DOUBLE_QUOTE == token)
				{
					closedChar = token;
					state = IS_IN_STRING_OR_REGEX;
				}
				else if (SLASH == token)
				{
					next = fgetc(sourse); 
					isGetNext = 1;
					if (EOF == next)
					{
						/*
							when the last symbol in program is slash and check the next symbol,
							then command "breack" skip last symbol and don't write in file its
						*/
						putc(token, destintion);
						break;
					}
					else if (SLASH == next)
					{
						isSingleComment = 1;
						SKIP_COMMENT;
					}
					else if (ASTERISK == next)
					{
						isMultipleComment = 1;
						SKIP_COMMENT;
					}
					else 
					{
						if (!regexRecognizing()) 
						{
							state = IS_IN_STRING_OR_REGEX; /* determining opened symbol of regex */
							closedChar = SLASH;
						}

					}
				}
			}
		}
		else
		{
			if (IS_IN_STRING_OR_REGEX == state)
			{
				if (ESCAPE == token)
				{
					escapeCounter++;
				}
				else if (EXIT_FROM_BLOCK(closedChar))
				{
					state = IS_IN_CODE;
				}
				else
				{
					escapeCounter = 0;
				}
			}
			else if (IS_IN_COMMENT == state)
			{
				if (isSingleComment)
				{
					if (ESCAPE == token)
					{
						escapeCounter++;
						continue;
					}
					else if (EXIT_FROM_BLOCK(NEW_LINE))
					{
						state = IS_IN_CODE;
					}
					else
					{
						escapeCounter = 0;
						continue;
					}
				}
				else if (isMultipleComment)
				{
					if (ASTERISK == token)
					{
						GET_NEXT_SAFETY;
						isGetNext = 1;
						if (SLASH == next)
						{
							state = IS_IN_CODE;
							GET_NEXT_SAFETY;
							isGetNext = 1;
						}
					}
					continue;
				}
			}		
		}
		fillBuffer(token);
		putc(token, destintion);
	}
}

void fillBuffer(int token)
{
	if (BUFFER_SIZE == bufferPosition)
	{
		bufferPosition = 0;
	}
	buffer[bufferPosition] = token;
	bufferPosition++;
}

int regexRecognizing()
{
	int i;
	for (i = 0; i < BUFFER_SIZE; ++i)
	{
		/* check the operation of division between the brackets */
		if (isAlnum(buffer[i]) ||
			CLOSED_BRACKED == buffer[i] ||
			CLOSED_BRACE == buffer[i] ||
			CLOSED_SQUARE_BRACKED == buffer[i])
		{
			return 1;
		}
	}
	return 0;
}

int isAlnum(int ch)
{
	return isalnum(ch) || UNDERSCORE == ch || DOLLAR_ICON == ch || ch > 127; /* more of 127 it's other symbols */
}
