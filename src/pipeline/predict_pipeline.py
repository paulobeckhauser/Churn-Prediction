'''
This script aims to create the predict pipeline 
for a simple web application which will be interacting 
with the pkl files, such that we can make predictions 
by giving values of input features. 
'''


# Data manipulation.
import pandas as pd

class InputData:
    '''
    Class for handling input data for predictions.

    This class provides a structured representation 
    for input data that is meant to be used for 
    making predictions. 
    
    It maps input variables from HTML inputs to class 
    attributes and provides a method to convert the input 
    data into a DataFrame format suitable for making 
    predictions.
    '''

    def __init__(self,
                 customer_age: int,
                 gender: str,
                 dependent_count: int,
                 education_level: str,
                 marital_status: str,
                 income_category: str,
                 card_category: str,
                 months_on_book: int,
                 total_relationship_count: int,
                 months_inactive_12_mon: int,
                 contacts_count_12_mon: int,
                 credit_limit: float,
                 total_revolving_bal: int,
                 total_amt_chng_q4_q1: float,
                 total_trans_amt: int,
                 total_trans_ct: int,
                 total_ct_chng_q4_q1: float,
                 avg_utilization_ratio: float) -> None:
        
        # Map variables from html inputs.
        self.customer_age = customer_age
        self.gender = gender
        self.dependent_count = dependent_count
        self.education_level = education_level
        self.marital_status = marital_status
        self.income_category = income_category
        self.card_category = card_category
        self.months_on_book = months_on_book
        self.total_relationship_count = total_relationship_count
        self.months_inactive_12_mon = months_inactive_12_mon
        self.contacts_count_12_mon = contacts_count_12_mon
        self.credit_limit = credit_limit
        self.total_revolving_bal = total_revolving_bal
        self.total_amt_chng_q4_q1 = total_amt_chng_q4_q1
        self.total_trans_amt = total_trans_amt
        self.total_trans_ct = total_trans_ct
        self.total_ct_chng_q4_q1 = total_ct_chng_q4_q1
        self.avg_utilization_ratio = avg_utilization_ratio


    def get_input_data_df(self):
    try:
        input_data_dict = dict()

        # Map the variables to the form of a dataframe for being used in predictions.
        
        input_data_dict['customer_age'] = [self.customer_age]
        input_data_dict['gender'] = [self.gender]
        input_data_dict['dependent_count'] = [self.dependent_count]
        input_data_dict['education_level'] = [self.education_level]
        input_data_dict['marital_status'] = [self.marital_status]
        input_data_dict['income_category'] = [self.income_category]
        input_data_dict['card_category'] = [self.card_category]
        input_data_dict['months_on_book'] = [self.months_on_book]
        input_data_dict['total_relationship_count'] = [self.total_relationship_count]
        input_data_dict['months_inactive_12_mon'] = [self.months_inactive_12_mon]
        input_data_dict['contacts_count_12_mon'] = [self.contacts_count_12_mon]
        input_data_dict['credit_limit'] = [self.credit_limit]
        input_data_dict['total_revolving_bal'] = [self.total_revolving_bal]
        input_data_dict['total_amt_chng_q4_q1'] = [self.total_amt_chng_q4_q1]
        input_data_dict['total_trans_amt'] = [self.total_trans_amt]
        input_data_dict['total_trans_ct'] = [self.total_trans_ct]
        input_data_dict['total_ct_chng_q4_q1'] = [self.total_ct_chng_q4_q1]
        input_data_dict['avg_utilization_ratio'] = [self.avg_utilization_ratio]

        input_data_df = pd.DataFrame(input_data_dict)

        return input_data_df
    
    except Exception as e:
            raise CustomException(e, sys)