#include <stdio.h>
#include <stdlib.h>

#define LOG_ENABLED

#ifdef LOG_ENABLED 
	#define LOG(...) \
		printf(__VA_ARGS__); 
#else
	#define LOG(...)
#endif

void handleCloseFile(FILE *file, const char *fileName);

void concatFiles(FILE *sourse, FILE *desination);

void main(int argc, char *argv[]) 
{
	int i;
	FILE *source;
	FILE *destination;
	int indexLastFile = argc - 1;

	if (argc <= 2) 
	{
		LOG("Too few parametrs!");
		return;
	}

	destination = fopen(argv[indexLastFile], "w");
	if (destination) 
	{
		for (i = 1; i < indexLastFile; ++i)
		{
			source = fopen(argv[i], "r");
			if (source) 
			{
				concatFiles(source, destination);
			} 
			else 
			{
				LOG("Can't open file: %s", argv[i]);
			}
			handleCloseFile(source, argv[i]);
		}
	}
	handleCloseFile(destination, argv[indexLastFile]);
}

void handleCloseFile(FILE *file, const char *fileName) 
{
	if (fclose(file)) 
	{
		LOG("Can't close file: %s", fileName);
	}
}

void concatFiles(FILE *sourse, FILE *destination) 
{
	int ch;
	int errorMessage;

	while (1) 
	{
		ch = fgetc(sourse);

		if (EOF == ch) 
		{
			break;
		} 
		else
		{
			putc(ch, destination);
		}
	}
	if (ferror(destination))
	{
		LOG("Error of writin to file");
	}
}
