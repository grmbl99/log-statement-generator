#ifndef LOG_STATEMENTS_H_INCLUDED
#define LOG_STATEMENTS_H_INCLUDED

#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

#define LOGCONTEXT (string(__FILE__ " ") +  __FUNCTION__ + " " + to_string(__LINE__))

void THIS_IS_AN_ID (string context, int tubeTemp, string userMessage, float someValue);
void THIS_IS_AN_OTHER_ID (string context, string EPX);

#endif
