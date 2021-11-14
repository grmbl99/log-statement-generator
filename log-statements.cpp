#include <iostream>
using namespace std;

void THIS_IS_AN_ID (int tubeTemp, string userMessage, float someValue) {
	cout << "this is a test" << endl
		<< "	tubeTemp: " << tubeTemp << endl
		<< "	userMessage: " << userMessage << endl
		<< "	someValue: " << someValue << endl;
}

void THIS_IS_AN_OTHER_ID (string EPX) {
	cout << "this is a another test" << endl
		<< "	EPX: " << EPX << endl;
}

int main() {
	THIS_IS_AN_ID(1, "hello", 2.0);
	THIS_IS_AN_OTHER_ID("EPX");
	return 0;
}