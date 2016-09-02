#if !defined(__TEST_H__)
#define __TEST_H__
class Test {
public:
  enum Number {
    NO1,
    NO2,
  };
  Test(const char *name);
  virtual ~Test();

private:
  const char *myName;
};

#endif // __TEST_H__
