#include "main.h"

#define CHILD 0
#define ERROR -1
#define BUF_SIZE 100000

int main(int argc, char **argv)
{
	char *file = argv[1];
	int file_descriptor = open(file, O_RDONLY);
	char buffer[BUF_SIZE];

	if (-1 == file_descriptor) {
		perror("Error opening file");
	} else if (-1 == read(file_descriptor, buffer, BUF_SIZE)) {
		perror("Error reading file");
	} else if (-1 == close(file_descriptor)) {
		perror("Error closing file");
	} else {
		pid_t pid = fork();

		switch (pid) {
		case CHILD:
			printf("\nEl archivo tiene la siguiente cantidad de lineas:\n");
			execlp("wc", "wc", "-l", file, NULL);
			break;
		case ERROR:
			perror("Error forking");
			break;
		default:
			printf("El contenido es:\n%s", buffer);
			break;
		}
	}

	return errno;
}
