
Feature: Virtual Page Turner has a pgm object

    Scenario: Properties of the pgm object
	Given vpt starts
	Then nPieces should be zero
	When I call GetPieces with a valid file
	Then nPieces should be greater than 0

    