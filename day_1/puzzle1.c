#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Input numbers should only go up to 5 digits (+1 for \n, +1 for \0)
#define CHARS_PER_LINE 7

int main (){

  FILE* fileP;
  int parsedLines = 0;
  int incReadings = 0;
  char cbCurr[CHARS_PER_LINE];
  char cbNext[CHARS_PER_LINE];

  // Exit if can't find input file
  fileP = fopen("puzzle1_input.txt", "r");
  if (fileP == NULL) {
    printf("Unable to read file\n");
    return 1;
  }

  // Read first line
  if (fgets(cbCurr, CHARS_PER_LINE, fileP) == NULL) {
    printf("Unexpected end of input.\n");
    return 1;
  }

  // Do until EOF
  while(fgets(cbNext, CHARS_PER_LINE, fileP) != NULL) {

    // Compare next line to current line
    if (atoi(cbNext) > atoi(cbCurr)) {
      incReadings++;
    }

    strcpy(cbCurr, cbNext);
  }

  printf("Readings: %i\n", incReadings);

  return 0;
}