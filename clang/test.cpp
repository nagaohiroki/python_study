#include "test.h"
#include <stdio.h>
Test::Test(const char *name) : myName(name) {
  printf("Initialize %s\n", myName);
}
Test::~Test() { printf("Finalize %s\n", myName); }
