#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
/**
 * infinite_while - writes the character c to stdout
 *
 * Return: On success 1.
 * On error, -1 is returned, and errno is set appropriately.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - writes the character c to stdout
 *
 * Return: On success 1.
 * On error, -1 is returned, and errno is set appropriately.
 */
int main(void)
{
	pid_t zombie;
	int index;

	for (index = 0; index < 5; index++)
	{
		zombie = fork();
		if (zombie > 0)
		{
			printf("Zombie process created, PID: %d\n", zombie);
		}
		else
		{
			exit(0);
		}
	}

	infinite_while();

	return (0);
}


