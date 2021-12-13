#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Input numbers should only go up to 5 digits (+1 for \n, +1 for \0)
#define CHARS_PER_LINE 7

int main (){

  FILE* fileP;
  int parsedLines = 0;
  int incReadings = 0;
  // Need 4 buffers for file reading
  // Read 1st, 2nd, 3rd
  // Read      2nd, 3rd, 4th
  char cbOne[CHARS_PER_LINE];
  char cbTwo[CHARS_PER_LINE];
  char cbThree[CHARS_PER_LINE];
  char cbFour[CHARS_PER_LINE];

  // Exit if can't find input file
  fileP = fopen("puzzle1_input.txt", "r");
  if (fileP == NULL) {
    printf("Unable to read file\n");
    return 1;
  }

  // Set up buffer 1
  if (fgets(cbOne, CHARS_PER_LINE, fileP) == NULL) {
    printf("Unexpected end of input.\n");
    return 1;
  }

  // Set up buffer 2
  if (fgets(cbTwo, CHARS_PER_LINE, fileP) == NULL) {
    printf("Unexpected end of input.\n");
    return 1;
  }

  // Set up buffer 3
  if (fgets(cbThree, CHARS_PER_LINE, fileP) == NULL) {
    printf("Unexpected end of input.\n");
    return 1;
  }

  // Parse input
  while(fgets(cbFour, CHARS_PER_LINE, fileP) != NULL) {

    // Comapre 1+2+3 with 2+3+4
    int setOne = atoi(cbOne) + atoi(cbTwo) + atoi(cbThree);
    int setTwo = atoi(cbTwo) + atoi(cbThree) + atoi(cbFour);

    if (setTwo > setOne) {
      incReadings++;
    }

    // Copy 2 to 1
    strcpy(cbOne, cbTwo);
    // Copy 3 to 2
    strcpy(cbTwo, cbThree);
    // Copy 4 to 3
    strcpy(cbThree, cbFour);
  }

  printf("Readings: %i\n", incReadings);

  return 0;
}
