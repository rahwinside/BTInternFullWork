The folder contains macro to generate stress reports for nodes and loops through all available subcases.

Macro Name - Nodal Stress Reporting Macro

Developed By - Enterprise Solutions Group(ESG), Altair India Pvt Ltd

Steps to execute - 
	1) Load model and result file in HyperView.
	2) Run 'Generate_Nodal_Stress_Report' script in HyperView.
	3) Select nodes for reporting the stress values.
	4) Click "Proceed" button.
	
Format of a csv report - 
	Stress values for each node is written in a seperate *.csv file, and the name of the file is formatted as - "Node_<Node_Id>_StressReport.csv".
	First row is the header, which lists the result components being reported. 
	Each subsequent row starts with a subcase name and followed by the the stress value of the node for the result component.
	
