#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char **argv)
{
  FILE *file = fopen(argv[1], "r");
  char line[1024];
  float n,m;

  while (fgets(line, 1024, file)) {
    n = atof(strtok(line, ","));
    m = atof(strtok(NULL, ","));
    printf("%i\n", (int)(((n / m  - floor(n / m)) * m)+0.5));
  }
  return 0;
}
