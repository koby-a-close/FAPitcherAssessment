# SpinRate.py
# Created on 10/17/2019 by KAC
def SpinRate(names, start_date, end_date, dictionary):

    """ The function takes pitcher names and dates to pull spin rate data from Statcast. A list of names is required
    under the current setting. A singl set of dates or list of dates can be supplied. Additionally, a dictionary of
    player names and their MLB IDs must be supplied. This dictionary can be created using other pybaseball functions.

    Returns a dataframe with spin rate data for four-seam fastball, curveball, and two-seam fastballs as well as
    two-seam fastball use and wOBA and total wOBA."""

    # import warnings filter and ignore warnings
    from warnings import simplefilter
    simplefilter(action='ignore', category=Warning)

    # Load packages for analysis
    import pandas as pd
    import pybaseball as pb
    import numpy as np

    player_dict = dictionary

    df_final = pd.DataFrame(columns=['Name', 'Total wOBA', 'FF Spin', 'CU/KC Spin', 'FT/SI Spin', 'FT/SI Use',
                                    'FT/SI wOBA'])
    if isinstance(names, list) and isinstance(start_date, list):
        for (name, sdt, edt) in zip(names, start_date, end_date):
            player_ID = player_dict[name]
            df_data = pb.statcast_pitcher(start_dt=sdt, end_dt=edt, player_id=player_ID)

            total_pitches = len(df_data)
            total_woba = np.mean(df_data.woba_value)

            FF_data = df_data[(df_data.pitch_type == 'FF')]
            CU_data = df_data[(df_data.pitch_type == 'KC') | (df_data.pitch_type == 'CU')]
            FT_data = df_data[(df_data.pitch_type == 'FT') | (df_data.pitch_type == 'SI')]

            FF_spin = np.mean(FF_data.release_spin_rate)
            CU_spin = np.mean(CU_data.release_spin_rate)
            FT_spin = np.mean(FT_data.release_spin_rate)

            FT_use = len(FT_data)/total_pitches

            FT_woba = np.mean(FT_data.woba_value)

            temp = [name, total_woba, FF_spin, CU_spin, FT_spin, FT_use, FT_woba]

            df_temp = pd.DataFrame([temp], columns=['Name', 'Total wOBA', 'FF Spin', 'CU/KC Spin', 'FT/SI Spin',
                                                    'FT/SI Use', 'FT/SI wOBA'])

            df_final = pd.concat([df_final, df_temp], axis=0)

        df_final = df_final.fillna(0.0)

    if isinstance(names, list):
        for name in names:
            player_ID = player_dict[name]
            if name == 'Will Smith':
                player_ID = 519293
            df_data = pb.statcast_pitcher(start_dt=start_date, end_dt=end_date, player_id=player_ID)

            total_pitches = len(df_data)
            total_woba = np.mean(df_data.woba_value)

            FF_data = df_data[(df_data.pitch_type == 'FF')]
            CU_data = df_data[(df_data.pitch_type == 'KC') | (df_data.pitch_type == 'CU')]
            FT_data = df_data[(df_data.pitch_type == 'FT') | (df_data.pitch_type == 'SI')]

            FF_spin = np.mean(FF_data.release_spin_rate)
            CU_spin = np.mean(CU_data.release_spin_rate)
            FT_spin = np.mean(FT_data.release_spin_rate)

            FT_use = len(FT_data)/total_pitches

            FT_woba = np.mean(FT_data.woba_value)

            temp = [name, total_woba, FF_spin, CU_spin, FT_spin, FT_use, FT_woba]

            df_temp = pd.DataFrame([temp], columns=['Name', 'Total wOBA', 'FF Spin', 'CU/KC Spin', 'FT/SI Spin',
                                                    'FT/SI Use', 'FT/SI wOBA'])

            df_final = pd.concat([df_final, df_temp], axis=0)

        df_final = df_final.fillna(0.0)

    return df_final
