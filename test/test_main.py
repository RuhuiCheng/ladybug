import logging
import src.utils.log
from src import main


def test_run_case():
    main.run("case","kpi.agreement_overlap_check.hotel_count")

def test_run_group():
    main.run("group","sae.kpi")
    
def test_run_scenarios():
    main.run("scenarios","kpi")