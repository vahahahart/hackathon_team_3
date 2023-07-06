from rdkit import RDLogger
RDLogger.DisableLog('rdApp.*')

from pandas import DataFrame
from rdkit.ML.Descriptors import MoleculeDescriptors 



def add_desc_to_df(df: DataFrame, desc: list):
    calc = Descriptors.CalcMolDescriptors
    calc = MoleculeDescriptors.MolecularDescriptorCalculator(desc)
    desc_df = pd.DataFrame(
        df['SMILES'].map(lambda x: calc.CalcDescriptors(Chem.MolFromSmiles(x))).to_list()
    )
    desc_df.columns = desc
    return df.join(desc_df)


def fill_nan_desc(df: DataFrame, non_desc_cols: list = None):
    '''
    Fill NaN with calculated descriptors

    Parameters
    ----------
    df: DataFrame

    non_desc_cols: columns from df cant be calculated via rdkit 
    '''
    cols_to_drop = ['SMILES']
    cols_to_drop.extend(non_desc_cols)
    for col in df.drop(columns=cols_to_drop).columns:
        col_type = data[col].dtype
        calc = MoleculeDescriptors.MolecularDescriptorCalculator([col])
        mask = df[col].isna()
        df.loc[mask, col] = df.loc[mask, 'SMILES'].map(
            lambda x: calc.CalcDescriptors(Chem.MolFromSmiles(x))[0]
        ).astype(col_type)
    return df