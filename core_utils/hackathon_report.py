# A Helper to print the test result in the following format:
# Task: <Task Number>, Test Name: <Test Name>, DOM Id:: <id>, Browser: <Browser>, Viewport: <Width x Height>, Device<Device type>, Status: <Pass | Fail>
#
# Example: Task: 1, Test Name: Search field is displayed, DOM Id: DIV__customsear__41, Browser: Chrome, Viewport: 1200 x 700, Device: Laptop, Status: Pass
#
# @param task                    int - 1, 2 or 3
# @param testName.               string - Something meaningful. E.g. 1.1 Search field is displayed
# @param domId                   string - DOM ID of the element
# @param comparisonResult        boolean - The result of comparing the "Expected" value and the "Actual" value.
# @return                        boolean - returns the same comparison result back so that it can be used for further Assertions in the test code.


def hackathon_report(task, testName, domId, comparisonResult, filename, setup):
    browser = setup[1]
    viewport = setup[2]
    device = setup[3]
    f = open( filename, "a" )

    report_content = "Task: {task}, Test Name: {test_name}, DOM Id: {dom_id},Browser: {browser}, Viewport: {viewport}, Device: {device}" \
                     ", Status: {status}\n".format( task=task, test_name=testName, dom_id=domId, browser=browser, viewport=viewport,
                                                    device=device, status=comparisonResult )
    f.write( report_content )

    f.close()

    # returns the result so that it can be used for further Assertions in the test code.
    return comparisonResult
