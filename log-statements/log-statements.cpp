#include "log-statements.h"

char* msTimeStamp(){
	auto timepoint = system_clock::now();
	auto coarse = system_clock::to_time_t(timepoint);
	auto fine = time_point_cast<milliseconds>(timepoint);

	static char buffer[sizeof "9999-12-31 23:59:59.999"];
	snprintf(
		buffer + strftime(buffer, sizeof buffer - 3, "%F %T.", localtime(&coarse)), 4, 
		"%03llu", fine.time_since_epoch().count() % 1000);

	return buffer;
}

void THIS_IS_AN_ID (string context, int tubeTemp, string userMessage, float someValue) {
	cout
		<< msTimeStamp() << endl
		<< "context: " << context << endl
		<< "this is a test" << endl
		<< "	tubeTemp: " << tubeTemp << endl
		<< "	userMessage: " << userMessage << endl
		<< "	someValue: " << someValue << endl;
}

void THIS_IS_AN_OTHER_ID (string context, string EPX) {
	cout
		<< msTimeStamp() << endl
		<< "context: " << context << endl
		<< "this is a another test" << endl
		<< "	EPX: " << EPX << endl;
}

