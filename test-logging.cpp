#include "log-lib.h"

int main() {
	THIS_IS_AN_ID(LOGCONTEXT, 2, "hello", 2.0);
	THIS_IS_AN_OTHER_ID(LOGCONTEXT, "test");
	return 0;
}