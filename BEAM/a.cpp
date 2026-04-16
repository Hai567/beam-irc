#include <iostream>

bool isScholarshipEligible(float gpa, int trainingPoint, bool isRemoteArea, bool hasResearch) {
	if (hasResearch && gpa > 7.0f && trainingPoint > 70) {
		return true;
	}

	if (isRemoteArea) {;
		return gpa >= 7.5f && trainingPoint >= 75;
	}

	return gpa >= 8.0f && trainingPoint >= 80;
}

int main() {
	float gpa;
	int trainingPoint;
	bool isRemoteArea;
	bool hasResearch;

	std::cout << "Enter GPA: ";
	std::cin >> gpa;

	std::cout << "Enter training point: ";
	std::cin >> trainingPoint;

	std::cout << "Is from remote area (1 for true, 0 for false): ";
	std::cin >> isRemoteArea;

	std::cout << "Has research achievements (1 for true, 0 for false): ";
	std::cin >> hasResearch;

	if (isScholarshipEligible(gpa, trainingPoint, isRemoteArea, hasResearch)) {
		std::cout << "Eligible for scholarship\n";
	} else {
		std::cout << "Not eligible for scholarship\n";
	}

	return 0;
}