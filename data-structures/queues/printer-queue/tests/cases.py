from dataclasses import dataclass
from typing import List, Any, Optional

@dataclass
class TestCase:
    id: str
    operations: List[str]
    arguments: List[List[Any]]
    expected: List[Optional[Any]]

TEST_CASES = [
    TestCase(
        id="Basic Printer Queue",
        operations=["add_job", "add_job", "add_job", "process_job", 
                    "process_job", "process_job"],
        arguments=[["Document1"], ["Document2"], ["Picture1"], 
                   [], [], []],
        expected=[None, None, None, "Document1", "Document2", "Picture1"]
    ),
    TestCase(
        id="Empty Queue Check",
        operations=["is_queue_empty", "add_job", "is_queue_empty", 
                    "process_job", "is_queue_empty"],
        arguments=[[], ["Job1"], [], [], []],
        expected=[True, None, False, "Job1", True]
    ),
    TestCase(
        id="Queue Size Tracking",
        operations=["queue_size", "add_job", "queue_size", "add_job", 
                    "add_job", "queue_size", "process_job", "queue_size"],
        arguments=[[], ["A"], [], ["B"], ["C"], [], [], []],
        expected=[0, None, 1, None, None, 3, "A", 2]
    ),
    TestCase(
        id="Peek Without Processing",
        operations=["add_job", "add_job", "peek_next_job", "peek_next_job", 
                    "process_job", "peek_next_job"],
        arguments=[["First"], ["Second"], [], [], [], []],
        expected=[None, None, "First", "First", "First", "Second"]
    ),
    TestCase(
        id="Interleaved Operations",
        operations=["add_job", "add_job", "process_job", "add_job", 
                    "process_job", "process_job", "is_queue_empty"],
        arguments=[["Report.pdf"], ["Presentation.pptx"], [], 
                   ["Spreadsheet.xlsx"], [], [], []],
        expected=[None, None, "Report.pdf", None, 
                  "Presentation.pptx", "Spreadsheet.xlsx", True]
    ),
    TestCase(
        id="Get All Jobs",
        operations=["add_job", "add_job", "add_job", "get_all_jobs", 
                    "process_job", "get_all_jobs"],
        arguments=[["Job1"], ["Job2"], ["Job3"], [], [], []],
        expected=[None, None, None, ["Job1", "Job2", "Job3"], 
                  "Job1", ["Job2", "Job3"]]
    ),
    TestCase(
        id="Single Job",
        operations=["add_job", "queue_size", "peek_next_job", "process_job", 
                    "is_queue_empty"],
        arguments=[["OnlyJob"], [], [], [], []],
        expected=[None, 1, "OnlyJob", "OnlyJob", True]
    ),
    TestCase(
        id="Multiple Identical Jobs",
        operations=["add_job", "add_job", "add_job", "process_job", 
                    "process_job"],
        arguments=[["Duplicate"], ["Duplicate"], ["Duplicate"], [], []],
        expected=[None, None, None, "Duplicate", "Duplicate"]
    ),
    TestCase(
        id="Large Queue",
        operations=(["add_job"] * 50 + ["queue_size"] + 
                    ["process_job"] * 50 + ["is_queue_empty"]),
        arguments=([[f"Job{i}"] for i in range(50)] + [[]] + 
                   [[]] * 50 + [[]]),
        expected=([None] * 50 + [50] + 
                  [f"Job{i}" for i in range(50)] + [True])
    ),
    TestCase(
        id="Office Scenario",
        operations=["add_job", "add_job", "add_job", "get_all_jobs", 
                    "process_job", "add_job", "queue_size", 
                    "process_job", "process_job"],
        arguments=[["User1_Report.pdf"], ["User2_Invoice.doc"], 
                   ["User3_Presentation.ppt"], [], [], 
                   ["User1_Memo.txt"], [], [], []],
        expected=[None, None, None, 
                  ["User1_Report.pdf", "User2_Invoice.doc", 
                   "User3_Presentation.ppt"],
                  "User1_Report.pdf", None, 3,
                  "User2_Invoice.doc", "User3_Presentation.ppt"]
    ),
]
