#include "test.h"
#include <memory>
#include <stdio.h>
#include <unordered_map>
int main(int argv, char *args[]) {
  printf("Hello World \n");
  std::shared_ptr<Test> t(new Test("0"));
  std::shared_ptr<Test> t1(new Test("1"));
  std::shared_ptr<Test> t2(new Test("2"));

  return 0;
}
