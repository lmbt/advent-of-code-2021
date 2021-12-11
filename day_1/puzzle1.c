#include <stdio.h>

int main (){

  FILE* fileP;
  int parsedChars = 0;
  char lastLine [3];
  char currLine [3];

  // Exit if can't find input file
  fileP = fopen("puzzle1_input.txt", "r");
  if (fileP == NULL) {
    printf("Unable to read file\n");
    return 1;
  }

  // Grab next line, compare to last (fseek)

  return 0;
}