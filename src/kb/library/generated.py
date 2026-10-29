# ruff: noqa
"""Auto-generated standalone scientific formula library.

Compiled directly from peer-reviewed research preprints in the Knowledge Base.
Each formula provides typed Python scalar execution and vectorized Polars expressions.
"""

from __future__ import annotations

import math

import polars as pl

__all__ = [
    "calc_miller2005_f0dbf0",
    "expr_miller2005_f0dbf0",
    "calc_miller2005_04a82a",
    "expr_miller2005_04a82a",
    "calc_miller2005_a3864f",
    "expr_miller2005_a3864f",
    "calc_miller2005_329993",
    "expr_miller2005_329993",
    "calc_miller2005_effa17",
    "expr_miller2005_effa17",
    "calc_jensen2009_33f50d",
    "expr_jensen2009_33f50d",
    "calc_val_0802_4317_formul",
    "expr_val_0802_4317_formul",
    "calc_val_1205_4750_1205_4",
    "expr_val_1205_4750_1205_4",
    "calc_val_1208_1725_1208_1",
    "expr_val_1208_1725_1208_1",
    "calc_w_a_r_q_1312_7",
    "expr_w_a_r_q_1312_7",
    "calc_w_p_c_t_p_r_s_r_a_1312_7",
    "expr_w_p_c_t_p_r_s_r_a_1312_7",
    "calc_val_1406_3402_1406_3",
    "expr_val_1406_3402_1406_3",
    "calc_val_1603_00050_1603_0",
    "expr_val_1603_00050_1603_0",
    "calc_d_a_h_1603_0",
    "expr_d_a_h_1603_0",
    "calc_val_1704_00823_1704_0",
    "expr_val_1704_00823_1704_0",
    "calc_val_1706_10272_1706_1",
    "expr_val_1706_10272_1706_1",
    "calc_val_2005_07742_2005_0",
    "expr_val_2005_07742_2005_0",
    "calc_val_1811_07259_1811_0",
    "expr_val_1811_07259_1811_0",
    "calc_val_2004_08428_2004_0",
    "expr_val_2004_08428_2004_0",
    "calc_val_2103_12094_2103_1",
    "expr_val_2103_12094_2103_1",
    "calc_val_2109_09287_2109_0",
    "expr_val_2109_09287_2109_0",
    "calc_val_2112_14846_2112_1",
    "expr_val_2112_14846_2112_1",
    "calc_val_2201_01168_2201_0",
    "expr_val_2201_01168_2201_0",
    "calc_val_2207_11332_2207_1",
    "expr_val_2207_11332_2207_1",
    "calc_t_2210_0",
    "expr_t_2210_0",
    "calc_val_2210_06724_2210_0",
    "expr_val_2210_06724_2210_0",
    "calc_val_2310_01184_2310_0",
    "expr_val_2310_01184_2310_0",
    "calc_val_2209_07274_2209_0",
    "expr_val_2209_07274_2209_0",
    "calc_val_2510_25961_2510_2",
    "expr_val_2510_25961_2510_2",
    "calc_val_2507_01238_2507_0",
    "expr_val_2507_01238_2507_0",
    "calc_val_2511_02815_2511_0",
    "expr_val_2511_02815_2511_0",
    "calc_val_2511_17733_2511_1",
    "expr_val_2511_17733_2511_1",
    "calc_w_1_2511_1",
    "expr_w_1_2511_1",
    "calc_l_x_2511_1",
    "expr_l_x_2511_1",
    "calc_r_x_2511_1",
    "expr_r_x_2511_1",
    "calc_f_l_x_2511_1",
    "expr_f_l_x_2511_1",
    "calc_f_r_x_2511_1",
    "expr_f_r_x_2511_1",
    "calc_i_n_de_x_2603_2",
    "expr_i_n_de_x_2603_2",
    "calc_beyond_runs_expectancy_jsm2014_beyond",
    "expr_beyond_runs_expectancy_jsm2014_beyond",
    "calc_brier_1950_mwr_brier_",
    "expr_brier_1950_mwr_brier_",
    "calc_p_brier_",
    "expr_p_brier_",
    "calc_p_t_brier_",
    "expr_p_t_brier_",
    "calc_r_i_j_brown_",
    "expr_r_i_j_brown_",
    "calc_v_a_r_x_1_i_x_2_i_brown_",
    "expr_v_a_r_x_1_i_x_2_i_brown_",
    "calc_p_i_brown_",
    "expr_p_i_brown_",
    "calc_bt_secondary_many_routes_2023_bt_sec",
    "expr_bt_secondary_many_routes_2023_bt_sec",
    "calc_p_i_j_p_i_j_p_j_k_p_j_k_bt_sec",
    "expr_p_i_j_p_i_j_p_j_k_p_j_k_bt_sec",
    "calc_f_x_bt_sec",
    "expr_f_x_bt_sec",
    "calc_p_i_j_bt_sec",
    "expr_p_i_j_bt_sec",
    "calc_c_i_j_bt_sec",
    "expr_c_i_j_bt_sec",
    "calc_c_bt_sec",
    "expr_c_bt_sec",
    "calc_val_1_diebol",
    "expr_val_1_diebol",
    "calc_diebold_mariano_1995_diebol",
    "expr_diebold_mariano_1995_diebol",
    "calc_f_diebol",
    "expr_f_diebol",
    "calc_r_diebol",
    "expr_r_diebol",
    "calc_efron_morris_1975_jasa_efron_",
    "expr_efron_morris_1975_jasa_efron_",
    "calc_a_p_m_efron_",
    "expr_a_p_m_efron_",
    "calc_egidi_2018_arxiv1802_egidi_",
    "expr_egidi_2018_arxiv1802_egidi_",
    "calc_b_p_egidi_",
    "expr_b_p_egidi_",
    "calc_glickman_2001_jas_dynamic_paired_glickm",
    "expr_glickman_2001_jas_dynamic_paired_glickm",
    "calc_s_s_k_i_l_l_n_gneiti",
    "expr_s_s_k_i_l_l_n_gneiti",
    "calc_s_c_p_1_gneiti",
    "expr_s_c_p_1_gneiti",
    "calc_g_p_gneiti",
    "expr_g_p_gneiti",
    "calc_gneiting_raftery_2007_jasa_gneiti",
    "expr_gneiting_raftery_2007_jasa_gneiti",
    "calc_b_gneiti",
    "expr_b_gneiti",
    "calc_l_o_b_g_gneiti",
    "expr_l_o_b_g_gneiti",
    "calc_guo_2017_calibration_guo_20",
    "expr_guo_2017_calibration_guo_20",
    "calc_s_2_harvey",
    "expr_s_2_harvey",
    "calc_harvey_leybourne_newbold_1997_harvey",
    "expr_harvey_leybourne_newbold_1997_harvey",
    "calc_val_1_12_2_harvey",
    "expr_val_1_12_2_harvey",
    "calc_maher_1982_maher_",
    "expr_maher_1982_maher_",
    "calc_c_i_maher_",
    "expr_c_i_maher_",
    "calc_z_l_y_u_c_c_u_x_i_k_2_j_r_maher_",
    "expr_z_l_y_u_c_c_u_x_i_k_2_j_r_maher_",
    "calc_maher_secondary_dependence_2021_maher_",
    "expr_maher_secondary_dependence_2021_maher_",
    "calc_math_0509698_form_f",
    "expr_math_0509698_form_f",
    "calc_math_0509698_form_9",
    "expr_math_0509698_form_9",
    "calc_math_0509698_form_7",
    "expr_math_0509698_form_7",
    "calc_math_0509698_form_d",
    "expr_math_0509698_form_d",
    "calc_miller_2005_pythag_derivation_form_9",
    "expr_miller_2005_pythag_derivation_form_9",
    "calc_miller_2005_pythag_derivation_form_d",
    "expr_miller_2005_pythag_derivation_form_d",
    "calc_miller_2005_pythag_derivation_form_8",
    "expr_miller_2005_pythag_derivation_form_8",
    "calc_miller_2005_pythag_derivation_form_2",
    "expr_miller_2005_pythag_derivation_form_2",
    "calc_miller_2007_pythag_weibull_form_1",
    "expr_miller_2007_pythag_weibull_form_1",
    "calc_miller_2007_pythag_weibull_form_2",
    "expr_miller_2007_pythag_weibull_form_2",
    "calc_miller_2007_pythag_weibull_form_5",
    "expr_miller_2007_pythag_weibull_form_5",
    "calc_miller_2007_pythag_weibull_form_3",
    "expr_miller_2007_pythag_weibull_form_3",
    "calc_naeini_2015_aaai_form_5",
    "expr_naeini_2015_aaai_form_5",
    "calc_naeini_2015_aaai_form_7",
    "expr_naeini_2015_aaai_form_7",
    "calc_t_form_c",
    "expr_t_form_c",
    "calc_f_x_form_5",
    "expr_f_x_form_5",
    "calc_niculescu_mizil_caruana_2005_form_d",
    "expr_niculescu_mizil_caruana_2005_form_d",
    "calc_niculescu_mizil_caruana_2005_form_2",
    "expr_niculescu_mizil_caruana_2005_form_2",
    "calc_niculescu_mizil_caruana_2005_form_c",
    "expr_niculescu_mizil_caruana_2005_form_c",
    "calc_niculescu_mizil_caruana_2005_form_b",
    "expr_niculescu_mizil_caruana_2005_form_b",
    "calc_retrosheet_lin_winning_advantage_form_6",
    "expr_retrosheet_lin_winning_advantage_form_6",
    "calc_retrosheet_lin_winning_advantage_form_d",
    "expr_retrosheet_lin_winning_advantage_form_d",
    "calc_shin_family_2024_cambridge_form_b",
    "expr_shin_family_2024_cambridge_form_b",
    "calc_h_p_form_6",
    "expr_h_p_form_6",
    "calc_val_2601_11904_form_c",
    "expr_val_2601_11904_form_c",
    "calc_val_2609_06739_form_9",
    "expr_val_2609_06739_form_9",
    "calc_val_2609_06739_form_f",
    "expr_val_2609_06739_form_f",
    "calc_val_2609_06739_form_4",
    "expr_val_2609_06739_form_4",
    "calc_val_2609_06739_form_c",
    "expr_val_2609_06739_form_c",
    "calc_val_2609_06739_form_d",
    "expr_val_2609_06739_form_d",
    "calc_val_2609_06739_form_2",
    "expr_val_2609_06739_form_2",
    "calc_val_2609_06739_form_1",
    "expr_val_2609_06739_form_1",
    "calc_val_2609_06739_form_5",
    "expr_val_2609_06739_form_5",
    "calc_q_s_form_9",
    "expr_q_s_form_9",
    "calc_val_2609_06739_form_0",
    "expr_val_2609_06739_form_0",
    "calc_val_2609_03786_form_5",
    "expr_val_2609_03786_form_5",
    "calc_val_2607_29041_form_1",
    "expr_val_2607_29041_form_1",
    "calc_w_e_s_form_9",
    "expr_w_e_s_form_9",
    "calc_val_2607_29041_form_8",
    "expr_val_2607_29041_form_8",
    "calc_val_2607_29041_form_d",
    "expr_val_2607_29041_form_d",
    "calc_val_2607_29041_form_2",
    "expr_val_2607_29041_form_2",
    "calc_val_2607_29041_form_5",
    "expr_val_2607_29041_form_5",
    "calc_val_2607_29041_form_f",
    "expr_val_2607_29041_form_f",
    "calc_val_2607_29041_form_6",
    "expr_val_2607_29041_form_6",
    "calc_val_2607_29041_form_c",
    "expr_val_2607_29041_form_c",
    "calc_val_2607_29041_form_e",
    "expr_val_2607_29041_form_e",
    "calc_val_2607_29041_form_b",
    "expr_val_2607_29041_form_b",
    "calc_v_v_1_form_e",
    "expr_v_v_1_form_e",
    "calc_val_2607_29041_form_9",
    "expr_val_2607_29041_form_9",
    "calc_val_2607_29041_form_4",
    "expr_val_2607_29041_form_4",
    "calc_eq_e_x_e_f_y_form_8",
    "expr_eq_e_x_e_f_y_form_8",
    "calc_val_2607_29041_form_7",
    "expr_val_2607_29041_form_7",
    "calc_l_z_form_a",
    "expr_l_z_form_a",
    "calc_val_2606_26780_form_1",
    "expr_val_2606_26780_form_1",
    "calc_begin_x_k_a_l_i_g_n_d_e_form_4",
    "expr_begin_x_k_a_l_i_g_n_d_e_form_4",
    "calc_p_i_j_form_6",
    "expr_p_i_j_form_6",
    "calc_val_2604_21851_form_8",
    "expr_val_2604_21851_form_8",
    "calc_w_a_p_form_9",
    "expr_w_a_p_form_9",
    "calc_val_1704_00823_form_4",
    "expr_val_1704_00823_form_4",
    "calc_val_1704_00823_form_3",
    "expr_val_1704_00823_form_3",
    "calc_val_0902_1360_form_e",
    "expr_val_0902_1360_form_e",
    "calc_i_n_de_x_form_0",
    "expr_i_n_de_x_form_0",
    "calc_val_2005_07742_form_d",
    "expr_val_2005_07742_form_d",
    "calc_val_2005_07742_form_f",
    "expr_val_2005_07742_form_f",
    "calc_val_2005_07742_form_5",
    "expr_val_2005_07742_form_5",
    "calc_val_2610_29565_form_4",
    "expr_val_2610_29565_form_4",
    "calc_val_2610_05080_form_4",
    "expr_val_2610_05080_form_4",
    "calc_val_2610_05080_form_9",
    "expr_val_2610_05080_form_9",
    "calc_val_2610_04813_form_c",
    "expr_val_2610_04813_form_c",
    "calc_s_form_e",
    "expr_s_form_e",
    "calc_val_2610_04813_form_b",
    "expr_val_2610_04813_form_b",
    "calc_val_2610_04813_form_3",
    "expr_val_2610_04813_form_3",
    "calc_val_2610_01307_form_3",
    "expr_val_2610_01307_form_3",
    "calc_val_2610_01307_form_b",
    "expr_val_2610_01307_form_b",
    "calc_val_2610_01307_form_7",
    "expr_val_2610_01307_form_7",
    "calc_val_2610_01307_form_8",
    "expr_val_2610_01307_form_8",
    "calc_val_2610_01307_form_9",
    "expr_val_2610_01307_form_9",
    "calc_val_2610_01307_form_e",
    "expr_val_2610_01307_form_e",
    "calc_l_a_a_i_form_6",
    "expr_l_a_a_i_form_6",
    "calc_val_2609_39852_form_9",
    "expr_val_2609_39852_form_9",
    "calc_val_2609_38730_form_b",
    "expr_val_2609_38730_form_b",
    "calc_val_2609_38730_form_5",
    "expr_val_2609_38730_form_5",
    "calc_val_2609_38730_form_c",
    "expr_val_2609_38730_form_c",
    "calc_z_form_4",
    "expr_z_form_4",
    "calc_l_v_a_l_form_4",
    "expr_l_v_a_l_form_4",
    "calc_val_2609_38730_form_9",
    "expr_val_2609_38730_form_9",
    "calc_e_r_e_c_n_o_form_c",
    "expr_e_r_e_c_n_o_form_c",
    "calc_e_b_a_e_s_form_3",
    "expr_e_b_a_e_s_form_3",
    "calc_e_f_i_n_a_l_form_e",
    "expr_e_f_i_n_a_l_form_e",
    "calc_g_s_p_e_c_t_r_a_l_form_5",
    "expr_g_s_p_e_c_t_r_a_l_form_5",
    "calc_val_2609_38730_form_2",
    "expr_val_2609_38730_form_2",
    "calc_val_2609_38730_form_3",
    "expr_val_2609_38730_form_3",
    "calc_l_f_m_form_8",
    "expr_l_f_m_form_8",
    "calc_l_b_a_e_s_form_a",
    "expr_l_b_a_e_s_form_a",
    "calc_val_2609_20558_form_f",
    "expr_val_2609_20558_form_f",
    "calc_p_u_form_5",
    "expr_p_u_form_5",
    "calc_y_r_s_h_s_y_p_s_form_1",
    "expr_y_r_s_h_s_y_p_s_form_1",
    "calc_h_y_form_2",
    "expr_h_y_form_2",
    "calc_val_2609_17701_form_8",
    "expr_val_2609_17701_form_8",
    "calc_val_2609_17701_form_3",
    "expr_val_2609_17701_form_3",
    "calc_l_0_p_w_form_0",
    "expr_l_0_p_w_form_0",
    "calc_l_g_a_p_w_form_8",
    "expr_l_g_a_p_w_form_8",
    "calc_a_t_w_o_w_a_o_form_9",
    "expr_a_t_w_o_w_a_o_form_9",
    "calc_val_2609_17701_form_6",
    "expr_val_2609_17701_form_6",
    "calc_u_l_s_o_form_4",
    "expr_u_l_s_o_form_4",
    "calc_val_2609_11476_form_8",
    "expr_val_2609_11476_form_8",
    "calc_val_2609_11476_form_4",
    "expr_val_2609_11476_form_4",
    "calc_val_2608_26548_form_b",
    "expr_val_2608_26548_form_b",
    "calc_val_2608_26548_form_8",
    "expr_val_2608_26548_form_8",
    "calc_val_1610_03464_form_e",
    "expr_val_1610_03464_form_e",
    "calc_val_1610_03464_form_b",
    "expr_val_1610_03464_form_b",
    "calc_r_s_form_6",
    "expr_r_s_form_6",
    "calc_val_2610_18361_form_d",
    "expr_val_2610_18361_form_d",
    "calc_val_2609_24299_form_6",
    "expr_val_2609_24299_form_6",
    "calc_l_form_9",
    "expr_l_form_9",
    "calc_val_2609_24299_form_c",
    "expr_val_2609_24299_form_c",
    "calc_m_q_q_form_5",
    "expr_m_q_q_form_5",
    "calc_c_p_form_a",
    "expr_c_p_form_a",
    "calc_c_t_form_0",
    "expr_c_t_form_0",
    "calc_val_2609_05500_form_4",
    "expr_val_2609_05500_form_4",
    "calc_val_2608_27423_form_9",
    "expr_val_2608_27423_form_9",
    "calc_val_2608_27423_form_0",
    "expr_val_2608_27423_form_0",
    "calc_l_form_c",
    "expr_l_form_c",
    "calc_val_2608_10387_form_d",
    "expr_val_2608_10387_form_d",
    "calc_val_2608_10387_form_9",
    "expr_val_2608_10387_form_9",
    "calc_val_2608_10387_form_2",
    "expr_val_2608_10387_form_2",
    "calc_val_2608_10387_form_1",
    "expr_val_2608_10387_form_1",
    "calc_val_2608_10387_form_4",
    "expr_val_2608_10387_form_4",
    "calc_val_2608_10387_form_a",
    "expr_val_2608_10387_form_a",
    "calc_val_2608_10387_form_3",
    "expr_val_2608_10387_form_3",
    "calc_ds_dw_form_d",
    "expr_ds_dw_form_d",
    "calc_w_form_a",
    "expr_w_form_a",
    "calc_dt_dw_form_f",
    "expr_dt_dw_form_f",
    "calc_j_form_5",
    "expr_j_form_5",
    "calc_val_2608_23163_form_e",
    "expr_val_2608_23163_form_e",
    "calc_val_2608_23163_form_a",
    "expr_val_2608_23163_form_a",
    "calc_val_2608_23163_form_1",
    "expr_val_2608_23163_form_1",
    "calc_val_2608_23163_form_3",
    "expr_val_2608_23163_form_3",
    "calc_p_b_a_s_e_l_i_e_n_form_9",
    "expr_p_b_a_s_e_l_i_e_n_form_9",
    "calc_val_2608_08157_form_8",
    "expr_val_2608_08157_form_8",
    "calc_val_2608_08157_form_a",
    "expr_val_2608_08157_form_a",
    "calc_val_2608_08157_form_d",
    "expr_val_2608_08157_form_d",
    "calc_val_2608_08157_form_6",
    "expr_val_2608_08157_form_6",
    "calc_val_2608_08157_form_1",
    "expr_val_2608_08157_form_1",
    "calc_a_l_r_form_a",
    "expr_a_l_r_form_a",
    "calc_val_2601_06439_form_9",
    "expr_val_2601_06439_form_9",
    "calc_val_2601_06439_form_f",
    "expr_val_2601_06439_form_f",
    "calc_c_2_s_r_z_form_9",
    "expr_c_2_s_r_z_form_9",
    "calc_a_form_2",
    "expr_a_form_2",
    "calc_val_2309_15318_form_3",
    "expr_val_2309_15318_form_3",
    "calc_val_2303_03898_form_4",
    "expr_val_2303_03898_form_4",
    "calc_p_m_form_9",
    "expr_p_m_form_9",
    "calc_c_p_form_f",
    "expr_c_p_form_f",
    "calc_p_s_form_b",
    "expr_p_s_form_b",
    "calc_p_s_form_5",
    "expr_p_s_form_5",
    "calc_t_s_p_i_n_do_n_w_form_c",
    "expr_t_s_p_i_n_do_n_w_form_c",
    "calc_val_1408_4306_form_f",
    "expr_val_1408_4306_form_f",
    "calc_x_form_c",
    "expr_x_form_c",
    "calc_y_form_f",
    "expr_y_form_f",
    "calc_l_form_6",
    "expr_l_form_6",
    "calc_d_f_form_4",
    "expr_d_f_form_4",
    "calc_f_form_4",
    "expr_f_form_4",
    "calc_f_r_form_4",
    "expr_f_r_form_4",
    "calc_d_form_6",
    "expr_d_form_6",
    "calc_a_w_form_3",
    "expr_a_w_form_3",
    "calc_dl_dt_form_3",
    "expr_dl_dt_form_3",
    "calc_a_j_h_form_8",
    "expr_a_j_h_form_8",
    "calc_e_v_form_3",
    "expr_e_v_form_3",
    "calc_f_m_a_x_form_9",
    "expr_f_m_a_x_form_9",
    "calc_o_form_c",
    "expr_o_form_c",
    "calc_val_2609_11733_form_3",
    "expr_val_2609_11733_form_3",
    "calc_p_i_t_form_6",
    "expr_p_i_t_form_6",
    "calc_c_g_f_r_form_c",
    "expr_c_g_f_r_form_c",
    "calc_val_2609_10457_form_c",
    "expr_val_2609_10457_form_c",
    "calc_l_r_o_l_l_j_o_i_n_form_9",
    "expr_l_r_o_l_l_j_o_i_n_form_9",
    "calc_l_r_o_l_l_e_x_c_e_s_s_form_c",
    "expr_l_r_o_l_l_e_x_c_e_s_s_form_c",
    "calc_val_2609_10457_form_d",
    "expr_val_2609_10457_form_d",
    "calc_val_2609_10457_form_8",
    "expr_val_2609_10457_form_8",
    "calc_p_c_i_j_form_9",
    "expr_p_c_i_j_form_9",
    "calc_val_2609_10457_form_0",
    "expr_val_2609_10457_form_0",
    "calc_val_2609_10457_form_f",
    "expr_val_2609_10457_form_f",
    "calc_val_2608_29935_form_7",
    "expr_val_2608_29935_form_7",
    "calc_k_1_form_3",
    "expr_k_1_form_3",
    "calc_val_2608_29935_form_e",
    "expr_val_2608_29935_form_e",
    "calc_s_w_form_8",
    "expr_s_w_form_8",
    "calc_w_b_x_form_1",
    "expr_w_b_x_form_1",
    "calc_w_b_r_form_3",
    "expr_w_b_r_form_3",
    "calc_val_2608_29935_form_8",
    "expr_val_2608_29935_form_8",
    "calc_w_c_x_form_9",
    "expr_w_c_x_form_9",
    "calc_w_c_r_form_1",
    "expr_w_c_r_form_1",
    "calc_val_2608_29935_form_a",
    "expr_val_2608_29935_form_a",
    "calc_val_2608_29935_form_3",
    "expr_val_2608_29935_form_3",
    "calc_w_b_r_form_0",
    "expr_w_b_r_form_0",
    "calc_q_dt_p_form_c",
    "expr_q_dt_p_form_c",
    "calc_r_m_d_i_form_5",
    "expr_r_m_d_i_form_5",
    "calc_val_2604_25278_form_2",
    "expr_val_2604_25278_form_2",
    "calc_val_2602_20850_form_b",
    "expr_val_2602_20850_form_b",
    "calc_val_2602_20850_form_5",
    "expr_val_2602_20850_form_5",
    "calc_e_p_form_3",
    "expr_e_p_form_3",
    "calc_f_c_d_m_form_a",
    "expr_f_c_d_m_form_a",
    "calc_val_2602_05895_form_e",
    "expr_val_2602_05895_form_e",
    "calc_e_form_1",
    "expr_e_form_1",
    "calc_val_2512_13304_form_5",
    "expr_val_2512_13304_form_5",
    "calc_val_2512_13304_form_1",
    "expr_val_2512_13304_form_1",
    "calc_val_2512_13304_form_a",
    "expr_val_2512_13304_form_a",
    "calc_h_a_p_e_x_form_b",
    "expr_h_a_p_e_x_form_b",
    "calc_val_2512_13304_form_d",
    "expr_val_2512_13304_form_d",
    "calc_e_p_form_1",
    "expr_e_p_form_1",
    "calc_t_p_x_p_y_p_z_1_form_5",
    "expr_t_p_x_p_y_p_z_1_form_5",
    "calc_val_2507_16328_form_6",
    "expr_val_2507_16328_form_6",
    "calc_val_2507_11037_form_2",
    "expr_val_2507_11037_form_2",
    "calc_val_2610_31563_form_8",
    "expr_val_2610_31563_form_8",
    "calc_val_2610_31153_form_8",
    "expr_val_2610_31153_form_8",
    "calc_val_2610_31563_form_f",
    "expr_val_2610_31563_form_f",
    "calc_val_2610_31563_form_a",
    "expr_val_2610_31563_form_a",
    "calc_val_2610_31563_form_5",
    "expr_val_2610_31563_form_5",
    "calc_val_2610_31563_form_b",
    "expr_val_2610_31563_form_b",
    "calc_j_p_form_d",
    "expr_j_p_form_d",
    "calc_val_2610_31153_form_6",
    "expr_val_2610_31153_form_6",
    "calc_val_2610_31153_form_d",
    "expr_val_2610_31153_form_d",
    "calc_val_2610_31153_form_7",
    "expr_val_2610_31153_form_7",
    "calc_val_2610_31153_form_e",
    "expr_val_2610_31153_form_e",
    "calc_val_2610_31153_form_0",
    "expr_val_2610_31153_form_0",
    "calc_val_2610_31153_form_b",
    "expr_val_2610_31153_form_b",
    "calc_val_2610_31153_form_2",
    "expr_val_2610_31153_form_2",
    "calc_val_2610_31153_form_f",
    "expr_val_2610_31153_form_f",
    "calc_val_2610_30212_form_a",
    "expr_val_2610_30212_form_a",
    "calc_val_2610_30212_form_9",
    "expr_val_2610_30212_form_9",
    "calc_val_2610_30212_form_e",
    "expr_val_2610_30212_form_e",
    "calc_val_2610_30212_form_f",
    "expr_val_2610_30212_form_f",
    "calc_val_2610_30212_form_0",
    "expr_val_2610_30212_form_0",
    "calc_val_2610_29685_form_6",
    "expr_val_2610_29685_form_6",
    "calc_val_2610_29685_form_5",
    "expr_val_2610_29685_form_5",
    "calc_val_2610_29685_form_1",
    "expr_val_2610_29685_form_1",
    "calc_val_2610_29685_form_e",
    "expr_val_2610_29685_form_e",
    "calc_val_2610_29685_form_c",
    "expr_val_2610_29685_form_c",
    "calc_val_2610_29066_form_1",
    "expr_val_2610_29066_form_1",
    "calc_val_2610_29066_form_5",
    "expr_val_2610_29066_form_5",
    "calc_val_2610_29066_form_d",
    "expr_val_2610_29066_form_d",
    "calc_val_2610_29066_form_b",
    "expr_val_2610_29066_form_b",
    "calc_val_2610_29066_form_4",
    "expr_val_2610_29066_form_4",
    "calc_val_2610_29066_form_9",
    "expr_val_2610_29066_form_9",
    "calc_c_e_x_a_c_t_form_f",
    "expr_c_e_x_a_c_t_form_f",
    "calc_val_2610_29066_form_6",
    "expr_val_2610_29066_form_6",
    "calc_val_2610_29049_form_a",
    "expr_val_2610_29049_form_a",
    "calc_val_2610_28285_form_9",
    "expr_val_2610_28285_form_9",
    "calc_val_2610_28285_form_1",
    "expr_val_2610_28285_form_1",
    "calc_u_o_t_v_form_c",
    "expr_u_o_t_v_form_c",
    "calc_val_2610_27416_form_0",
    "expr_val_2610_27416_form_0",
    "calc_val_2610_27416_form_a",
    "expr_val_2610_27416_form_a",
    "calc_val_2610_27416_form_6",
    "expr_val_2610_27416_form_6",
    "calc_val_2610_27416_form_2",
    "expr_val_2610_27416_form_2",
    "calc_val_2610_27416_form_1",
    "expr_val_2610_27416_form_1",
    "calc_val_2610_27416_form_f",
    "expr_val_2610_27416_form_f",
    "calc_val_2610_27416_form_e",
    "expr_val_2610_27416_form_e",
    "calc_val_2610_27416_form_8",
    "expr_val_2610_27416_form_8",
    "calc_val_2610_27416_form_3",
    "expr_val_2610_27416_form_3",
    "calc_a_form_4",
    "expr_a_form_4",
    "calc_val_2610_27416_form_d",
    "expr_val_2610_27416_form_d",
    "calc_val_2610_27057_form_8",
    "expr_val_2610_27057_form_8",
    "calc_val_2610_27057_form_5",
    "expr_val_2610_27057_form_5",
    "calc_l_v_r_r_e_e_2223_form_7",
    "expr_l_v_r_r_e_e_2223_form_7",
    "calc_val_2610_26568_form_b",
    "expr_val_2610_26568_form_b",
    "calc_val_2610_26568_form_2",
    "expr_val_2610_26568_form_2",
    "calc_l_i_m_i_n_f_n_b_n_form_0",
    "expr_l_i_m_i_n_f_n_b_n_form_0",
    "calc_val_2610_26568_form_a",
    "expr_val_2610_26568_form_a",
    "calc_val_2610_26568_form_7",
    "expr_val_2610_26568_form_7",
    "calc_val_2610_26568_form_d",
    "expr_val_2610_26568_form_d",
    "calc_val_2610_25605_form_d",
    "expr_val_2610_25605_form_d",
    "calc_val_2610_25605_form_5",
    "expr_val_2610_25605_form_5",
    "calc_val_2610_25605_form_e",
    "expr_val_2610_25605_form_e",
    "calc_z_m_i_x_form_7",
    "expr_z_m_i_x_form_7",
    "calc_e_j_form_6",
    "expr_e_j_form_6",
    "calc_p_form_2",
    "expr_p_form_2",
    "calc_val_2610_25581_form_f",
    "expr_val_2610_25581_form_f",
    "calc_val_2610_25581_form_d",
    "expr_val_2610_25581_form_d",
    "calc_val_2610_25581_form_3",
    "expr_val_2610_25581_form_3",
    "calc_val_2610_25581_form_0",
    "expr_val_2610_25581_form_0",
    "calc_val_2610_25581_form_c",
    "expr_val_2610_25581_form_c",
    "calc_val_2610_25581_form_7",
    "expr_val_2610_25581_form_7",
    "calc_r_p_o_s_form_9",
    "expr_r_p_o_s_form_9",
    "calc_val_2610_25581_form_e",
    "expr_val_2610_25581_form_e",
    "calc_u_2_s_1_form_f",
    "expr_u_2_s_1_form_f",
    "calc_u_2_s_3_form_2",
    "expr_u_2_s_3_form_2",
    "calc_u_2_s_4_form_7",
    "expr_u_2_s_4_form_7",
    "calc_val_2610_25581_form_5",
    "expr_val_2610_25581_form_5",
    "calc_val_2609_07617_form_8",
    "expr_val_2609_07617_form_8",
    "calc_val_2609_07617_form_0",
    "expr_val_2609_07617_form_0",
    "calc_d_q_form_2",
    "expr_d_q_form_2",
    "calc_eq_a_p_b_p_form_e",
    "expr_eq_a_p_b_p_form_e",
    "calc_val_2608_12291_form_f",
    "expr_val_2608_12291_form_f",
    "calc_val_2608_12291_form_7",
    "expr_val_2608_12291_form_7",
    "calc_val_2608_12291_form_1",
    "expr_val_2608_12291_form_1",
    "calc_val_2608_12291_form_4",
    "expr_val_2608_12291_form_4",
    "calc_s_form_c",
    "expr_s_form_c",
    "calc_val_2608_12291_form_c",
    "expr_val_2608_12291_form_c",
    "calc_val_2608_12291_form_8",
    "expr_val_2608_12291_form_8",
    "calc_val_2608_12291_form_d",
    "expr_val_2608_12291_form_d",
    "calc_val_2608_12291_form_0",
    "expr_val_2608_12291_form_0",
    "calc_v_n_t_k_x_form_4",
    "expr_v_n_t_k_x_form_4",
    "calc_val_2608_12291_form_e",
    "expr_val_2608_12291_form_e",
    "calc_val_2608_12291_form_b",
    "expr_val_2608_12291_form_b",
    "calc_val_2608_12291_form_9",
    "expr_val_2608_12291_form_9",
    "calc_f_s_form_5",
    "expr_f_s_form_5",
    "calc_f_s_form_8",
    "expr_f_s_form_8",
    "calc_t_x_x_form_2",
    "expr_t_x_x_form_2",
    "calc_t_a_b_form_d",
    "expr_t_a_b_form_d",
    "calc_t_a_b_form_6",
    "expr_t_a_b_form_6",
    "calc_t_a_b_form_b",
    "expr_t_a_b_form_b",
    "calc_val_2602_19513_form_5",
    "expr_val_2602_19513_form_5",
    "calc_val_2602_19513_form_2",
    "expr_val_2602_19513_form_2",
    "calc_val_2602_19513_form_6",
    "expr_val_2602_19513_form_6",
    "calc_val_2602_19513_form_e",
    "expr_val_2602_19513_form_e",
    "calc_val_2602_19513_form_3",
    "expr_val_2602_19513_form_3",
    "calc_val_2602_19513_form_c",
    "expr_val_2602_19513_form_c",
    "calc_val_2602_19513_form_d",
    "expr_val_2602_19513_form_d",
    "calc_val_2602_19513_form_7",
    "expr_val_2602_19513_form_7",
    "calc_val_2602_19513_form_0",
    "expr_val_2602_19513_form_0",
    "calc_p_w_t_form_9",
    "expr_p_w_t_form_9",
    "calc_val_2602_19513_form_8",
    "expr_val_2602_19513_form_8",
    "calc_t_a_b_form_0",
    "expr_t_a_b_form_0",
    "calc_val_2602_15673_form_3",
    "expr_val_2602_15673_form_3",
    "calc_k_p_form_c",
    "expr_k_p_form_c",
    "calc_val_2601_18774_form_a",
    "expr_val_2601_18774_form_a",
    "calc_val_2601_18774_form_c",
    "expr_val_2601_18774_form_c",
    "calc_val_2601_18774_form_5",
    "expr_val_2601_18774_form_5",
    "calc_val_2601_18774_form_7",
    "expr_val_2601_18774_form_7",
    "calc_p_t_form_4",
    "expr_p_t_form_4",
    "calc_val_2601_18774_form_9",
    "expr_val_2601_18774_form_9",
    "calc_val_2601_18774_form_f",
    "expr_val_2601_18774_form_f",
    "calc_val_2601_18774_form_1",
    "expr_val_2601_18774_form_1",
    "calc_val_2601_18774_form_0",
    "expr_val_2601_18774_form_0",
    "calc_val_2601_18774_form_b",
    "expr_val_2601_18774_form_b",
    "calc_val_2601_18774_form_8",
    "expr_val_2601_18774_form_8",
    "calc_f_m_x_form_1",
    "expr_f_m_x_form_1",
    "calc_val_2601_18774_form_d",
    "expr_val_2601_18774_form_d",
    "calc_val_2601_18774_form_e",
    "expr_val_2601_18774_form_e",
    "calc_p_0_x_form_5",
    "expr_p_0_x_form_5",
    "calc_f_form_e",
    "expr_f_form_e",
    "calc_val_2601_11492_form_8",
    "expr_val_2601_11492_form_8",
    "calc_f_s_form_0",
    "expr_f_s_form_0",
    "calc_b_p_k_form_0",
    "expr_b_p_k_form_0",
    "calc_val_2512_18467_form_0",
    "expr_val_2512_18467_form_0",
    "calc_o_n_e_t_h_i_r_df_o_m_r_form_1",
    "expr_o_n_e_t_h_i_r_df_o_m_r_form_1",
    "calc_t_w_o_t_h_i_r_df_o_m_r_form_e",
    "expr_t_w_o_t_h_i_r_df_o_m_r_form_e",
    "calc_val_2512_18467_form_2",
    "expr_val_2512_18467_form_2",
    "calc_val_2512_00312_form_3",
    "expr_val_2512_00312_form_3",
    "calc_x_l_o_form_d",
    "expr_x_l_o_form_d",
    "calc_r_form_5",
    "expr_r_form_5",
    "calc_p_r_i_w_i_n_s_o_v_e_j_r_form_f",
    "expr_p_r_i_w_i_n_s_o_v_e_j_r_form_f",
    "calc_r_w_c_i_form_4",
    "expr_r_w_c_i_form_4",
    "calc_g_x_form_9",
    "expr_g_x_form_9",
    "calc_val_2506_05866_form_5",
    "expr_val_2506_05866_form_5",
    "calc_val_2503_11669_form_5",
    "expr_val_2503_11669_form_5",
    "calc_val_2503_11669_form_3",
    "expr_val_2503_11669_form_3",
    "calc_val_2503_11669_form_9",
    "expr_val_2503_11669_form_9",
    "calc_val_2503_11669_form_c",
    "expr_val_2503_11669_form_c",
    "calc_val_2503_11669_form_8",
    "expr_val_2503_11669_form_8",
    "calc_val_2503_11669_form_b",
    "expr_val_2503_11669_form_b",
    "calc_val_2610_18417_form_a",
    "expr_val_2610_18417_form_a",
    "calc_val_2610_18417_form_6",
    "expr_val_2610_18417_form_6",
    "calc_val_2610_18417_form_5",
    "expr_val_2610_18417_form_5",
    "calc_val_2609_10498_form_d",
    "expr_val_2609_10498_form_d",
    "calc_val_2609_10498_form_e",
    "expr_val_2609_10498_form_e",
    "calc_val_2609_10498_form_1",
    "expr_val_2609_10498_form_1",
    "calc_val_2609_10498_form_b",
    "expr_val_2609_10498_form_b",
    "calc_val_2609_10498_form_c",
    "expr_val_2609_10498_form_c",
    "calc_val_2609_10498_form_8",
    "expr_val_2609_10498_form_8",
    "calc_val_2609_10498_form_5",
    "expr_val_2609_10498_form_5",
    "calc_val_2609_10498_form_a",
    "expr_val_2609_10498_form_a",
    "calc_val_2609_10498_form_f",
    "expr_val_2609_10498_form_f",
    "calc_val_2609_10498_form_0",
    "expr_val_2609_10498_form_0",
    "calc_c_p_q_form_c",
    "expr_c_p_q_form_c",
    "calc_f_r_e_q_p_i_t_c_h_form_1",
    "expr_f_r_e_q_p_i_t_c_h_form_1",
    "calc_val_2608_25621_form_6",
    "expr_val_2608_25621_form_6",
    "calc_m_t_form_d",
    "expr_m_t_form_d",
    "calc_k_p_form_8",
    "expr_k_p_form_8",
    "calc_c_l_form_b",
    "expr_c_l_form_b",
    "calc_c_a_b_form_0",
    "expr_c_a_b_form_0",
    "calc_s_form_1",
    "expr_s_form_1",
    "calc_c_l_form_3",
    "expr_c_l_form_3",
    "calc_openalex_saavedra2009_w2041165548_form_6",
    "expr_openalex_saavedra2009_w2041165548_form_6",
    "calc_q_i_j_form_9",
    "expr_q_i_j_form_9",
]


def calc_miller2005_f0dbf0(P: float, b: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from miller2005.

    **Source**:
    - Title: A Derivation of the Pythagorean Expectation for Baseball (2005)
    - Authors: Steven J. Miller
    - Citation Key: `miller2005`

    **KaTeX Formula**:
    $$
    Prob(X > Y ) = ∫ ∞ x=β ∫ x y=β f (x; αRS, β, γ)f (y; αRA, β, γ)dy dx = ∫ ∞ x=β ∫ x y=β γ αRS ( x - β αRS )γ-1 e-((x-β)/αRS)γ γ αRA ( y - β αRA )γ-1 e-((y-β)/αRA)γ dy dx = ∫ ∞ x=0 γ αRS ( x αRS )γ-1 e-(x/αRS)γ [∫ x y=0 γ αRA ( y αRA )γ-1 e-(y/αRA)γ dy] dx = ∫ ∞ x=0 γ αRS ( x αRS )γ-1 e-(x/αRS)γ [1 - e-(x/αRA)γ ] dx = 1- ∫ ∞ x=0 γ αRS ( x αRS )γ-1 e-(x/α)γ dx,
    $$

    Args:
        P (float): Input parameter `P`.
        b (float): Input parameter `b`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * b * o * r)


def expr_miller2005_f0dbf0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_miller2005_f0dbf0`."""
    return pl.col("P") * pl.col("b") * pl.col("o") * pl.col("r")


def calc_miller2005_04a82a(P: float, b: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from miller2005.

    **Source**:
    - Title: A Derivation of the Pythagorean Expectation for Baseball (2005)
    - Authors: Steven J. Miller
    - Citation Key: `miller2005`

    **KaTeX Formula**:
    $$
    Prob(X > Y ) = 1- αγ αγRS ∫ ∞ 0 γα ( xα )γ-1 e(x/α)γ dx = 1- αγ αγRS = 1- 1 αγRS αγRS αγRA αγRS + αγRA = αγRS αγRS + αγRA .
    $$

    Args:
        P (float): Input parameter `P`.
        b (float): Input parameter `b`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * b * o * r)


def expr_miller2005_04a82a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_miller2005_04a82a`."""
    return pl.col("P") * pl.col("b") * pl.col("o") * pl.col("r")


def calc_miller2005_a3864f(P: float, b: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from miller2005.

    **Source**:
    - Title: A Derivation of the Pythagorean Expectation for Baseball (2005)
    - Authors: Steven J. Miller
    - Citation Key: `miller2005`

    **KaTeX Formula**:
    $$
    Prob(X > Y ) = (R_{S} - β)γ (R_{S} - β)γ + (R_{A} - β)γ ,
    $$

    Args:
        P (float): Input parameter `P`.
        b (float): Input parameter `b`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * b * o * r)


def expr_miller2005_a3864f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_miller2005_a3864f`."""
    return pl.col("P") * pl.col("b") * pl.col("o") * pl.col("r")


def calc_miller2005_329993(X: float, r: float) -> float:
    r"""Compute mathematical metric extracted from miller2005.

    **Source**:
    - Title: A Derivation of the Pythagorean Expectation for Baseball (2005)
    - Authors: Steven J. Miller
    - Citation Key: `miller2005`

    **KaTeX Formula**:
    $$
    Xr,+ = 12∑ c=1 Or,c, X+,c = 12∑ r=1 Or,c.
    $$

    Args:
        X (float): Input parameter `X`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(X * r)


def expr_miller2005_329993() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_miller2005_329993`."""
    return pl.col("X") * pl.col("r")


def calc_miller2005_effa17(r: float) -> float:
    r"""Compute mathematical metric extracted from miller2005.

    **Source**:
    - Title: A Derivation of the Pythagorean Expectation for Baseball (2005)
    - Authors: Steven J. Miller
    - Citation Key: `miller2005`

    **KaTeX Formula**:
    $$
    Er,c = lim ℓ→∞ E(ℓ) r,c ;
    $$

    Args:
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e * r)


def expr_miller2005_effa17() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_miller2005_effa17`."""
    return math.e * pl.col("r")


def calc_jensen2009_33f50d(P: float) -> float:
    r"""Compute mathematical metric extracted from jensen2009.

    **Source**:
    - Title: Bayesball: A Bayesian Hierarchical Model for Evaluating Historic Baseball Players (2009)
    - Authors: Shane T. Jensen, Kenneth E. Shirley, Abraham J. Wyner
    - Citation Key: `jensen2009`

    **KaTeX Formula**:
    $$
    P (Sij = 1) = Φ(βi0 + βi1Dij + βi2Vij + βi3Fij ) (8) =Φ(Xij \cdot  βi),
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_jensen2009_33f50d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_jensen2009_33f50d`."""
    return pl.col("P")


def calc_val_0802_4317_formul(P: float) -> float:
    r"""Compute mathematical metric extracted from 0802_4317.

    **Source**:
    - Title: Bayesball: A Bayesian hierarchical model for evaluating fielding in major league baseball (2008)
    - Authors: Shane T. Jensen, Kenneth E. Shirley, Abraham J. Wyner
    - Citation Key: `0802_4317`

    **KaTeX Formula**:
    $$
    P (Sij = 1) = Φ(βi0 + βi1Dij + βi2Vij + βi3Fij ) (8) =Φ(Xij \cdot  βi),
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_0802_4317_formul() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_0802_4317_formul`."""
    return pl.col("P")


def calc_val_1205_4750_1205_4(r: float) -> float:
    r"""Compute mathematical metric extracted from 1205_4750.

    **Source**:
    - Title: First Order Approximations of the Pythagorean Won-Loss Formula for Predicting MLB Teams' Winning Percentages (2012)
    - Authors: Kevin D. Dayaratna, Steven J. Miller
    - Citation Key: `1205_4750`

    **KaTeX Formula**:
    $$
    midhorizellipsis + + + + - 3 2 1 = 1 1 r r r r
    $$

    Args:
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(11 * r**4)


def expr_val_1205_4750_1205_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1205_4750_1205_4`."""
    return 11 * pl.col("r") ** 4


def calc_val_1208_1725_1208_1(A: float, G: float, S: float) -> float:
    r"""Compute mathematical metric extracted from 1208_1725.

    **Source**:
    - Title: The Pythagorean Won-Loss Formula and Hockey: A Statistical Justification for Using the Classic Baseball Formula as an Evaluative Tool in Hockey (2012)
    - Authors: Kevin D. Dayaratna, Steven J. Miller
    - Citation Key: `1208_1725`

    **KaTeX Formula**:
    $$
    GA GA GS GS
    $$

    Args:
        A (float): Input parameter `A`.
        G (float): Input parameter `G`.
        S (float): Input parameter `S`.

    Returns:
        float: Calculated metric value.
    """
    return float(G * (A * (G * (A * (G * (S * (G * S)))))))


def expr_val_1208_1725_1208_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1208_1725_1208_1`."""
    return pl.col("G") * (
        pl.col("A")
        * (
            pl.col("G")
            * (pl.col("A") * (pl.col("G") * (pl.col("S") * (pl.col("G") * pl.col("S")))))
        )
    )


def calc_w_a_r_q_1312_7(
    A: float, R: float, e: float, l: float, p: float, q: float, r: float
) -> float:
    r"""Compute mathematical metric extracted from 1312_7158.

    **Source**:
    - Title: openWAR: An Open Source System for Evaluating Overall Player Performance in Major League Baseball (2013)
    - Authors: Benjamin S. Baumer, Shane T. Jensen, Gregory J. Matthews
    - Citation Key: `1312_7158`

    **KaTeX Formula**:
    $$
    WARq = RAAq -RAArepl q 10 ,
    $$

    Args:
        A (float): Input parameter `A`.
        R (float): Input parameter `R`.
        e (float): Input parameter `e`.
        l (float): Input parameter `l`.
        p (float): Input parameter `p`.
        q (float): Input parameter `q`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(-10 * A**2 * R * e * l * p * q * r + A**2 * R * q)


def expr_w_a_r_q_1312_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_a_r_q_1312_7`."""
    return -10 * pl.col("A") ** 2 * pl.col("R") * pl.col("e") * pl.col("l") * pl.col("p") * pl.col(
        "q"
    ) * pl.col("r") + pl.col("A") ** 2 * pl.col("R") * pl.col("q")


def calc_w_p_c_t_p_r_s_r_a_1312_7(R_A: float, R_S: float, p: float) -> float:
    r"""Compute mathematical metric extracted from 1312_7158.

    **Source**:
    - Title: openWAR: An Open Source System for Evaluating Overall Player Performance in Major League Baseball (2013)
    - Authors: Benjamin S. Baumer, Shane T. Jensen, Gregory J. Matthews
    - Citation Key: `1312_7158`

    **KaTeX Formula**:
    $$
    WPctp(R_{S},R_{A}) = 1 1 + ( R_{A} R_{S} )p
    $$

    Args:
        R_A (float): Input parameter `R_A`.
        R_S (float): Input parameter `R_S`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(p * (R_A * R_S) + 11)


def expr_w_p_c_t_p_r_s_r_a_1312_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_p_c_t_p_r_s_r_a_1312_7`."""
    return pl.col("p") * (pl.col("R_A") * pl.col("R_S")) + 11


def calc_val_1406_3402_1406_3(A: float, R: float, S: float) -> float:
    r"""Compute mathematical metric extracted from 1406_3402.

    **Source**:
    - Title: Relieving and Readjusting Pythagoras (2014)
    - Authors: Victor Luo, Steven J. Miller
    - Citation Key: `1406_3402`

    **KaTeX Formula**:
    $$
    Won-Loss Percentage = RS2 RS2 + RA2 ,
    $$

    Args:
        A (float): Input parameter `A`.
        R (float): Input parameter `R`.
        S (float): Input parameter `S`.

    Returns:
        float: Calculated metric value.
    """
    return float(R * (2 * A) + R * (S * (2 * (R * (2 * S)))))


def expr_val_1406_3402_1406_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1406_3402_1406_3`."""
    return pl.col("R") * (2 * pl.col("A")) + pl.col("R") * (
        pl.col("S") * (2 * (pl.col("R") * (2 * pl.col("S"))))
    )


def calc_val_1603_00050_1603_0(P: float) -> float:
    r"""Compute mathematical metric extracted from 1603_00050.

    **Source**:
    - Title: Learning, Visualizing, and Exploiting a Model for the Intrinsic Value of a Batted Ball (2016)
    - Authors: Glenn Healey
    - Citation Key: `1603_00050`

    **KaTeX Formula**:
    $$
    P(Rj|x) = p(x|Rj)P(Rj) p(x)
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_1603_00050_1603_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1603_00050_1603_0`."""
    return pl.col("P")


def calc_d_a_h_1603_0(A: float, D: float, H: float) -> float:
    r"""Compute mathematical metric extracted from 1603_00050.

    **Source**:
    - Title: Learning, Visualizing, and Exploiting a Model for the Intrinsic Value of a Batted Ball (2016)
    - Authors: Glenn Healey
    - Citation Key: `1603_00050`

    **KaTeX Formula**:
    $$
    DHA = DH - DA
    $$

    Args:
        A (float): Input parameter `A`.
        D (float): Input parameter `D`.
        H (float): Input parameter `H`.

    Returns:
        float: Calculated metric value.
    """
    return float(-A * D + D * H)


def expr_d_a_h_1603_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_a_h_1603_0`."""
    return -pl.col("A") * pl.col("D") + pl.col("D") * pl.col("H")


def calc_val_1704_00823_1704_0(g: float, l: float, o: float) -> float:
    r"""Compute mathematical metric extracted from 1704_00823.

    **Source**:
    - Title: A Hierarchical Bayesian Model of Pitch Framing (2017)
    - Authors: Sameer K. Deshpande, Abraham J. Wyner
    - Citation Key: `1704_00823`

    **KaTeX Formula**:
    $$
    log ( P(y = 1) P(y = 0) ) = Θu,B b +Θu,CA ca +Θu,P p +Θu,CO co + f u(x, z)
    $$

    Args:
        g (float): Input parameter `g`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.

    Returns:
        float: Calculated metric value.
    """
    return float(g * l * o)


def expr_val_1704_00823_1704_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1704_00823_1704_0`."""
    return pl.col("g") * pl.col("l") * pl.col("o")


def calc_val_1706_10272_1706_1(P: float) -> float:
    r"""Compute mathematical metric extracted from 1706_10272.

    **Source**:
    - Title: Nuclear penalized multinomial regression with an application to predicting at bat outcomes in baseball (2017)
    - Authors: Scott Powers, Trevor Hastie, Robert Tibshirani
    - Citation Key: `1706_10272`

    **KaTeX Formula**:
    $$
    P(Y = H_{R}|B, P) = eαHR+βHR B +γHR P 1 + eαHR+βHR B +γHR P .
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_1706_10272_1706_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1706_10272_1706_1`."""
    return pl.col("P")


def calc_val_2005_07742_2005_0(f: float, h: float) -> float:
    r"""Compute mathematical metric extracted from 2005_07742.

    **Source**:
    - Title: SEAM methodology for context-rich player matchup evaluations (2020)
    - Authors: Julia Wapner, David Dalpiaz, Daniel J. Eck
    - Citation Key: `2005_07742`

    **KaTeX Formula**:
    $$
    fh(y|x)) - f (y|x) = µ2(K)h′diag(Hf (y|x))h
    $$

    Args:
        f (float): Input parameter `f`.
        h (float): Input parameter `h`.

    Returns:
        float: Calculated metric value.
    """
    return float(f * h)


def expr_val_2005_07742_2005_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2005_07742_2005_0`."""
    return pl.col("f") * pl.col("h")


def calc_val_1811_07259_1811_0(P: float) -> float:
    r"""Compute mathematical metric extracted from 1811_07259.

    **Source**:
    - Title: Modeling Baseball Outcomes as Higher-Order Markov Chains (2018)
    - Authors: Jun Hee Kim
    - Citation Key: `1811_07259`

    **KaTeX Formula**:
    $$
    P(X (n) = xnew|X (n-1) = xn-1, X (n-2) = xn-2, \cdot  \cdot  \cdot  , X (1) = x1) = P(X (n) = xnew|X (n-1) = xn-1)
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_1811_07259_1811_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1811_07259_1811_0`."""
    return pl.col("P")


def calc_val_2004_08428_2004_0(L: float, P: float, S: float) -> float:
    r"""Compute mathematical metric extracted from 2004_08428.

    **Source**:
    - Title: Renormalizing individual performance metrics for cultural heritage management of sports records (2020)
    - Authors: Alexander M. Petersen, Orion Penner
    - Citation Key: `2004_08428`

    **KaTeX Formula**:
    $$
    PLS(X|p) ∝ pX /X ≈X-1 exp[-X/Xc] .
    $$

    Args:
        L (float): Input parameter `L`.
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * (L * S))


def expr_val_2004_08428_2004_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2004_08428_2004_0`."""
    return pl.col("P") * (pl.col("L") * pl.col("S"))


def calc_val_2103_12094_2103_1(i: float, k: float, p: float) -> float:
    r"""Compute mathematical metric extracted from 2103_12094.

    **Source**:
    - Title: Modelling intransitivity in pairwise comparisons with application to baseball data (2021)
    - Authors: Jess Spearing, Jonathan Tawn, David Irons et al.
    - Citation Key: `2103_12094`

    **KaTeX Formula**:
    $$
    pik := f (p(BT) ik , θik ) , ∀i ̸= k ∈ I,
    $$

    Args:
        i (float): Input parameter `i`.
        k (float): Input parameter `k`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(i * k * p)


def expr_val_2103_12094_2103_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2103_12094_2103_1`."""
    return pl.col("i") * pl.col("k") * pl.col("p")


def calc_val_2109_09287_2109_0(i: float, p: float) -> float:
    r"""Compute mathematical metric extracted from 2109_09287.

    **Source**:
    - Title: Park factor estimation improvement using pairwise comparison method (2021)
    - Authors: Eiji Konaka
    - Citation Key: `2109_09287`

    **KaTeX Formula**:
    $$
    pi,j,k = 1 1 + exp (- (bi - dj - rk)) .
    $$

    Args:
        i (float): Input parameter `i`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(i * p)


def expr_val_2109_09287_2109_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2109_09287_2109_0`."""
    return pl.col("i") * pl.col("p")


def calc_val_2112_14846_2112_1(
    a: float,
    c: float,
    dw: float,
    e: float,
    g: float,
    i: float,
    n: float,
    p: float,
    r: float,
    t: float,
    x: float,
) -> float:
    r"""Compute mathematical metric extracted from 2112_14846.

    **Source**:
    - Title: An Analysis of an Alternative Pythagorean Expected Win Percentage Model: Applications Using Major League Baseball Team Quality Simulations (2021)
    - Authors: Justin Ehrlich, Christopher Boudreaux, James Boudreau et al.
    - Citation Key: `2112_14846`

    **KaTeX Formula**:
    $$
    Expected win percentagei,j = rsi,j rsi,j 2 + rai,j 2
    $$

    Args:
        a (float): Input parameter `a`.
        c (float): Input parameter `c`.
        dw (float): Input parameter `dw`.
        e (float): Input parameter `e`.
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e * a * c**2 * dw * e**5 * g * i**2 * n**2 * p**2 * r * t**2 * x)


def expr_val_2112_14846_2112_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2112_14846_2112_1`."""
    return (
        math.e
        * pl.col("a")
        * pl.col("c") ** 2
        * pl.col("dw")
        * pl.col("e") ** 5
        * pl.col("g")
        * pl.col("i") ** 2
        * pl.col("n") ** 2
        * pl.col("p") ** 2
        * pl.col("r")
        * pl.col("t") ** 2
        * pl.col("x")
    )


def calc_val_2201_01168_2201_0(
    c: float, dw: float, e: float, i: float, n: float, p: float, s: float, t: float, x: float
) -> float:
    r"""Compute mathematical metric extracted from 2201_01168.

    **Source**:
    - Title: Application of the Pythagorean Expected Wins Percentage and Cross-Validation Methods in Estimating Team Quality (2021)
    - Authors: Christopher Boudreaux, Justin Ehrlich, Shankar Ghimire et al.
    - Citation Key: `2201_01168`

    **KaTeX Formula**:
    $$
    Expected winsi,j = rsi,j 𝛼 rsi,j 𝛼 + rai,j 𝛼
    $$

    Args:
        c (float): Input parameter `c`.
        dw (float): Input parameter `dw`.
        e (float): Input parameter `e`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e * c * dw * e**2 * i**2 * n * p * s * t * x)


def expr_val_2201_01168_2201_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2201_01168_2201_0`."""
    return (
        math.e
        * pl.col("c")
        * pl.col("dw")
        * pl.col("e") ** 2
        * pl.col("i") ** 2
        * pl.col("n")
        * pl.col("p")
        * pl.col("s")
        * pl.col("t")
        * pl.col("x")
    )


def calc_val_2207_11332_2207_1(F: float, X: float, i: float) -> float:
    r"""Compute mathematical metric extracted from 2207_11332.

    **Source**:
    - Title: Comparing baseball players across eras via novel Full House Modeling (2022)
    - Authors: Shen Yan, Adrian Burgos, Christopher Kinson et al.
    - Citation Key: `2207_11332`

    **KaTeX Formula**:
    $$
    F -1 Xi,(Ni-ni+j) (FUi,(j) (FYi (Yi,(j) | ˆ θi))) ≈ F -1 Xi,(Ni-ni+j) (FUi,(j) (Ui,(j) )) =Xi,(Ni-ni+j).
    $$

    Args:
        F (float): Input parameter `F`.
        X (float): Input parameter `X`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(F - X * i)


def expr_val_2207_11332_2207_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2207_11332_2207_1`."""
    return pl.col("F") - pl.col("X") * pl.col("i")


def calc_t_2210_0(B: float, U: float, m: float) -> float:
    r"""Compute mathematical metric extracted from 2210_02383.

    **Source**:
    - Title: Filling the Gaps: A Multiple Imputation Approach to Estimating Aging Curves in Baseball (2022)
    - Authors: Quang Nguyen, Gregory J. Matthews
    - Citation Key: `2210_02383`

    **KaTeX Formula**:
    $$
    T = U + (1 + 1m ) B ,
    $$

    Args:
        B (float): Input parameter `B`.
        U (float): Input parameter `U`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(B * (m + 1) + U)


def expr_t_2210_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_2210_0`."""
    return pl.col("B") * (pl.col("m") + 1) + pl.col("U")


def calc_val_2210_06724_2210_0(g: float, l: float, o: float) -> float:
    r"""Compute mathematical metric extracted from 2210_06724.

    **Source**:
    - Title: A Bayesian analysis of the time through the order penalty in baseball (2022)
    - Authors: Ryan S. Brill, Sameer K. Deshpande, Abraham J. Wyner
    - Citation Key: `2210_06724`

    **KaTeX Formula**:
    $$
    log ( P(yi = k) P(yi = 1) ) = α0k + α1kti + β2kI (ti ∈ 2TTO) + β3kI (ti ∈ 3TTO) + x⊤i ηk,
    $$

    Args:
        g (float): Input parameter `g`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.

    Returns:
        float: Calculated metric value.
    """
    return float(g * l * o)


def expr_val_2210_06724_2210_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2210_06724_2210_0`."""
    return pl.col("g") * pl.col("l") * pl.col("o")


def calc_val_2310_01184_2310_0(P: float, b: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from 2310_01184.

    **Source**:
    - Title: Applications of Improvements to the Pythagorean Won-Loss Expectation in Optimizing Rosters (2023)
    - Authors: Alexander F. Almeida, Kevin Dayaratna, Steven J. Miller et al.
    - Citation Key: `2310_01184`

    **KaTeX Formula**:
    $$
    Prob(X > Y ) = ∫ ∞ x=β ∫ x y=β f (x; αRS, β, γRS)f (y; αRA, β, γRA)dy dx = ∫ ∞ x=0 γRS αRS ( x αRS )γRS-1 exp (- ( x αRS )γRS ) \cdot  [∫ x y=0 γRA αRA ( y αRA )γRA-1 exp (- ( x αRA )γRA ) dy] dx = ∫ ∞ x=0 γRS αRS ( x αRS )γRS-1 exp (-(x/αRS)γRS ) [1 - exp (-(x/αRA)γRA )] dx = 1 - ∫ ∞ x=0 γRS αRS ( x αRS )γRS-1 exp [-(x/αRS)γRS - (x/αRA)γRA ] dx.
    $$

    Args:
        P (float): Input parameter `P`.
        b (float): Input parameter `b`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * b * o * r)


def expr_val_2310_01184_2310_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2310_01184_2310_0`."""
    return pl.col("P") * pl.col("b") * pl.col("o") * pl.col("r")


def calc_val_2209_07274_2209_0(X: float, i: float) -> float:
    r"""Compute mathematical metric extracted from 2209_07274.

    **Source**:
    - Title: Introducing Grid WAR: Rethinking WAR for Starting Pitchers (2022)
    - Authors: Ryan S. Brill, Abraham J. Wyner
    - Citation Key: `2209_07274`

    **KaTeX Formula**:
    $$
    Xi i.i.d. ∼ Poisson(λX) and Yi i.i.d. ∼ Poisson(λY).
    $$

    Args:
        X (float): Input parameter `X`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(X * i**2)


def expr_val_2209_07274_2209_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2209_07274_2209_0`."""
    return pl.col("X") * pl.col("i") ** 2


def calc_val_2510_25961_2510_2(P: float, r: float) -> float:
    r"""Compute mathematical metric extracted from 2510_25961.

    **Source**:
    - Title: Tractable Algorithms for Changepoint Detection in Player Performance Metrics (2025)
    - Authors: Amanda Glazer
    - Citation Key: `2510_25961`

    **KaTeX Formula**:
    $$
    Pr(yt = 1 | yt-1) = {p + ρ, yt-1 = 1, p-ρ, yt-1 = 0,
    $$

    Args:
        P (float): Input parameter `P`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * r)


def expr_val_2510_25961_2510_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2510_25961_2510_2`."""
    return pl.col("P") * pl.col("r")


def calc_val_2507_01238_2507_0(g: float, l: float, o: float) -> float:
    r"""Compute mathematical metric extracted from 2507_01238.

    **Source**:
    - Title: Swinging, Fast and Slow: Interpreting variation in baseball swing tracking metrics (2025)
    - Authors: Scott Powers, Ronald Yurko
    - Citation Key: `2507_01238`

    **KaTeX Formula**:
    $$
    log ( P(Y con i = 1) 1 - P(Y con i = 1) ) = log ( ˆ pcon i 1- ˆ pcon i ) + αcon + βcon BS \cdot  ˆ γBS bi +βcon SL \cdot  ˆ γ SL bi ,
    $$

    Args:
        g (float): Input parameter `g`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.

    Returns:
        float: Calculated metric value.
    """
    return float(g * l * o)


def expr_val_2507_01238_2507_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2507_01238_2507_0`."""
    return pl.col("g") * pl.col("l") * pl.col("o")


def calc_val_2511_02815_2511_0(
    a: float,
    c: float,
    d: float,
    e: float,
    l: float,
    n: float,
    o: float,
    r: float,
    s: float,
    u: float,
    w: float,
) -> float:
    r"""Compute mathematical metric extracted from 2511_02815.

    **Source**:
    - Title: Assessing win strength in MLB win prediction models (2025)
    - Authors: Morgan Allen, Paul Savala
    - Citation Key: `2511_02815`

    **KaTeX Formula**:
    $$
    runs scored 2 runs scored 2 + runs allowed 2 .
    $$

    Args:
        a (float): Input parameter `a`.
        c (float): Input parameter `c`.
        d (float): Input parameter `d`.
        e (float): Input parameter `e`.
        l (float): Input parameter `l`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.
        u (float): Input parameter `u`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(
        a * d * e * l**2 * n * o * r * s * u * w
        + 4 * c**2 * d**2 * e**2 * n**2 * o**2 * r**4 * s**4 * u**2
    )


def expr_val_2511_02815_2511_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2511_02815_2511_0`."""
    return (
        pl.col("a")
        * pl.col("d")
        * pl.col("e")
        * pl.col("l") ** 2
        * pl.col("n")
        * pl.col("o")
        * pl.col("r")
        * pl.col("s")
        * pl.col("u")
        * pl.col("w")
        + 4
        * pl.col("c") ** 2
        * pl.col("d") ** 2
        * pl.col("e") ** 2
        * pl.col("n") ** 2
        * pl.col("o") ** 2
        * pl.col("r") ** 4
        * pl.col("s") ** 4
        * pl.col("u") ** 2
    )


def calc_val_2511_17733_2511_1(K: float) -> float:
    r"""Compute mathematical metric extracted from 2511_17733.

    **Source**:
    - Title: The Impacts of Increasingly Complex Matchup Models on Baseball Win Probability (2025)
    - Authors: Tristan Mott, Caleb Bradshaw, David Grimsman et al.
    - Citation Key: `2511_17733`

    **KaTeX Formula**:
    $$
    28K. 0\%, ROI Lower Confidence = -18\%. 0\%, ROI Upper Confidence = +34\%. 0\%, Actual ROI = -15.5\%. 1.5\%, Bets Placed = 23. 1.5\%, Total Bets =
    $$

    Args:
        K (float): Input parameter `K`.

    Returns:
        float: Calculated metric value.
    """
    return float(28 * K)


def expr_val_2511_17733_2511_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2511_17733_2511_1`."""
    return 28 * pl.col("K")


def calc_w_1_2511_1(h: float, k: float) -> float:
    r"""Compute mathematical metric extracted from 2511_19642.

    **Source**:
    - Title: A Win-Expectancy Framework for Contextualizing Runs Batted In: Introducing ARBI and CRBI (2025)
    - Authors: Wuhuan Deng
    - Citation Key: `2511_19642`

    **KaTeX Formula**:
    $$
    w1 = 2hk +hk-1, w2 = hk +2hk-1.
    $$

    Args:
        h (float): Input parameter `h`.
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(3 * h * k - 1)


def expr_w_1_2511_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_1_2511_1`."""
    return 3 * pl.col("h") * pl.col("k") - 1


def calc_l_x_2511_1(x: float) -> float:
    r"""Compute mathematical metric extracted from 2511_19642.

    **Source**:
    - Title: A Win-Expectancy Framework for Contextualizing Runs Batted In: Introducing ARBI and CRBI (2025)
    - Authors: Wuhuan Deng
    - Citation Key: `2511_19642`

    **KaTeX Formula**:
    $$
    xL = x1, fL = y1, dL = m1,
    $$

    Args:
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(x)


def expr_l_x_2511_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_x_2511_1`."""
    return pl.col("x")


def calc_r_x_2511_1(n: float, x: float) -> float:
    r"""Compute mathematical metric extracted from 2511_19642.

    **Source**:
    - Title: A Win-Expectancy Framework for Contextualizing Runs Batted In: Introducing ARBI and CRBI (2025)
    - Authors: Wuhuan Deng
    - Citation Key: `2511_19642`

    **KaTeX Formula**:
    $$
    xR = xn, fR = yn, dR = mn.
    $$

    Args:
        n (float): Input parameter `n`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(n * x)


def expr_r_x_2511_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_x_2511_1`."""
    return pl.col("n") * pl.col("x")


def calc_f_l_x_2511_1(L: float, f: float) -> float:
    r"""Compute mathematical metric extracted from 2511_19642.

    **Source**:
    - Title: A Win-Expectancy Framework for Contextualizing Runs Batted In: Introducing ARBI and CRBI (2025)
    - Authors: Wuhuan Deng
    - Citation Key: `2511_19642`

    **KaTeX Formula**:
    $$
    f (x-L ) = fL, f ′ (x-L ) = dL, lim x→-∞ f (x) = 0.
    $$

    Args:
        L (float): Input parameter `L`.
        f (float): Input parameter `f`.

    Returns:
        float: Calculated metric value.
    """
    return float(L * f)


def expr_f_l_x_2511_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_l_x_2511_1`."""
    return pl.col("L") * pl.col("f")


def calc_f_r_x_2511_1(R: float, f: float) -> float:
    r"""Compute mathematical metric extracted from 2511_19642.

    **Source**:
    - Title: A Win-Expectancy Framework for Contextualizing Runs Batted In: Introducing ARBI and CRBI (2025)
    - Authors: Wuhuan Deng
    - Citation Key: `2511_19642`

    **KaTeX Formula**:
    $$
    f (x+R ) = fR, f ′ (x+R ) = dR, lim x→+∞ f (x) = 1.
    $$

    Args:
        R (float): Input parameter `R`.
        f (float): Input parameter `f`.

    Returns:
        float: Calculated metric value.
    """
    return float(R * f)


def expr_f_r_x_2511_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_r_x_2511_1`."""
    return pl.col("R") * pl.col("f")


def calc_i_n_de_x_2603_2(z: float) -> float:
    r"""Compute mathematical metric extracted from 2603_21163.

    **Source**:
    - Title: Simultaneous Estimation of Ballpark Effects and Team Defense Using Total Bases Residuals (2026)
    - Authors: Jhe-Jia Wu, Tian-Li Yan, Ting-Li Chen
    - Citation Key: `2603_21163`

    **KaTeX Formula**:
    $$
    Index = 100 + 20 \times  z.
    $$

    Args:
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(20 * z + 100)


def expr_i_n_de_x_2603_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_n_de_x_2603_2`."""
    return 20 * pl.col("z") + 100


def calc_beyond_runs_expectancy_jsm2014_beyond(P: float, b: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from beyond_runs_expectancy_jsm2014.

    **Source**:
    - Title: 311431_85069
    - Authors: Scientific Literature
    - Citation Key: `beyond_runs_expectancy_jsm2014`

    **KaTeX Formula**:
    $$
    P rob(R|T , B),
    $$

    Args:
        P (float): Input parameter `P`.
        b (float): Input parameter `b`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * b * o * r)


def expr_beyond_runs_expectancy_jsm2014_beyond() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_beyond_runs_expectancy_jsm2014_beyond`."""
    return pl.col("P") * pl.col("b") * pl.col("o") * pl.col("r")


def calc_brier_1950_mwr_brier_(r: float) -> float:
    r"""Compute mathematical metric extracted from brier_1950_mwr.

    **Source**:
    - Title: 078<0001:VOFEIT>2.0.CO;2 (1950)
    - Authors: Brier, G.W. 1950, Verification of forecasts expressed in terms of probability et al.
    - Citation Key: `brier_1950_mwr`

    **KaTeX Formula**:
    $$
    r .= 1 Z: fu=l, i=l ,2,3, . . . n
    $$

    Args:
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(r)


def expr_brier_1950_mwr_brier_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_brier_1950_mwr_brier_`."""
    return pl.col("r")


def calc_p_brier_(B: float, c: float, f: float, t: float, z: float) -> float:
    r"""Compute mathematical metric extracted from brier_1950_mwr.

    **Source**:
    - Title: 078<0001:VOFEIT>2.0.CO;2 (1950)
    - Authors: Brier, G.W. 1950, Verification of forecasts expressed in terms of probability et al.
    - Citation Key: `brier_1950_mwr`

    **KaTeX Formula**:
    $$
    P=- z B cft,-E*,)2 (2) 1 ' n j=1 i=l
    $$

    Args:
        B (float): Input parameter `B`.
        c (float): Input parameter `c`.
        f (float): Input parameter `f`.
        t (float): Input parameter `t`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(-B * c * f * t * z)


def expr_p_brier_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_brier_`."""
    return -pl.col("B") * pl.col("c") * pl.col("f") * pl.col("t") * pl.col("z")


def calc_p_t_brier_(i: float, l: float, p: float) -> float:
    r"""Compute mathematical metric extracted from brier_1950_mwr.

    **Source**:
    - Title: 078<0001:VOFEIT>2.0.CO;2 (1950)
    - Authors: Brier, G.W. 1950, Verification of forecasts expressed in terms of probability et al.
    - Citation Key: `brier_1950_mwr`

    **KaTeX Formula**:
    $$
    Pt=l- i p,2 (4) j=1
    $$

    Args:
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(-i * p + l)


def expr_p_t_brier_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_t_brier_`."""
    return -pl.col("i") * pl.col("p") + pl.col("l")


def calc_r_i_j_brown_(H: float, N: float, i: float, j: float) -> float:
    r"""Compute mathematical metric extracted from brown_2008_aoas.

    **Source**:
    - Title: Supplement to 'In-season prediction of batting averages...': Major league batting records for 2005 (2008)
    - Authors: Brown, L. D.
    - Citation Key: `brown_2008_aoas`

    **KaTeX Formula**:
    $$
    Rj i = Hj i Nj i .
    $$

    Args:
        H (float): Input parameter `H`.
        N (float): Input parameter `N`.
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.

    Returns:
        float: Calculated metric value.
    """
    return float(H * (j * (i * (N * (i * j)))))


def expr_r_i_j_brown_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_i_j_brown_`."""
    return pl.col("H") * (pl.col("j") * (pl.col("i") * (pl.col("N") * (pl.col("i") * pl.col("j")))))


def calc_v_a_r_x_1_i_x_2_i_brown_(N: float, i: float) -> float:
    r"""Compute mathematical metric extracted from brown_2008_aoas.

    **Source**:
    - Title: Supplement to 'In-season prediction of batting averages...': Major league batting records for 2005 (2008)
    - Authors: Brown, L. D.
    - Citation Key: `brown_2008_aoas`

    **KaTeX Formula**:
    $$
    Var(X2i - X1i ) = 1 4N2i + 1 4N1i .
    $$

    Args:
        N (float): Input parameter `N`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(14 * (N * (1 * i)) + 14 * (N * (2 * i)))


def expr_v_a_r_x_1_i_x_2_i_brown_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_a_r_x_1_i_x_2_i_brown_`."""
    return 14 * (pl.col("N") * (1 * pl.col("i"))) + 14 * (pl.col("N") * (2 * pl.col("i")))


def calc_p_i_brown_(U: float, i: float) -> float:
    r"""Compute mathematical metric extracted from brown_2008_aoas.

    **Source**:
    - Title: Supplement to 'In-season prediction of batting averages...': Major league batting records for 2005 (2008)
    - Authors: Brown, L. D.
    - Citation Key: `brown_2008_aoas`

    **KaTeX Formula**:
    $$
    Pi = 1 - Ui .
    $$

    Args:
        U (float): Input parameter `U`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(-U * i + 1)


def expr_p_i_brown_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_brown_`."""
    return -pl.col("U") * pl.col("i") + 1


def calc_bt_secondary_many_routes_2023_bt_sec(j: float, k: float, l: float, p: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    pjk > pjl,
    $$

    Args:
        j (float): Input parameter `j`.
        k (float): Input parameter `k`.
        l (float): Input parameter `l`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float((j * k * p > j * l * p))


def expr_bt_secondary_many_routes_2023_bt_sec() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_bt_secondary_many_routes_2023_bt_sec`."""
    return pl.col("j") * pl.col("k") * pl.col("p") > pl.col("j") * pl.col("l") * pl.col("p")


def calc_p_i_j_p_i_j_p_j_k_p_j_k_bt_sec(i: float, k: float, p: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    pij pji \times  pjk pkj = pik pki .
    $$

    Args:
        i (float): Input parameter `i`.
        k (float): Input parameter `k`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(i**2 * k**2 * p**2)


def expr_p_i_j_p_i_j_p_j_k_p_j_k_bt_sec() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_j_p_i_j_p_j_k_p_j_k_bt_sec`."""
    return pl.col("i") ** 2 * pl.col("k") ** 2 * pl.col("p") ** 2


def calc_f_x_bt_sec(x: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    f(x) = x 1 + x ,
    $$

    Args:
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(2 * x)


def expr_f_x_bt_sec() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_x_bt_sec`."""
    return 2 * pl.col("x")


def calc_p_i_j_bt_sec(P: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    pij = P(Xi > Xj ) = ∫ xi>xj dGπi (xi)dGπj (xj ) = πi πi + πj .
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_p_i_j_bt_sec() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_j_bt_sec`."""
    return pl.col("P")


def calc_c_i_j_bt_sec(a: float, i: float, j: float, s: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    cij = aisij ,
    $$

    Args:
        a (float): Input parameter `a`.
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * i**2 * j * s)


def expr_c_i_j_bt_sec() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_i_j_bt_sec`."""
    return pl.col("a") * pl.col("i") ** 2 * pl.col("j") * pl.col("s")


def calc_c_bt_sec(A: float, S: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    C = AS,
    $$

    Args:
        A (float): Input parameter `A`.
        S (float): Input parameter `S`.

    Returns:
        float: Calculated metric value.
    """
    return float(A * S)


def expr_c_bt_sec() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_bt_sec`."""
    return pl.col("A") * pl.col("S")


def calc_val_1_diebol(T: float) -> float:
    r"""Compute mathematical metric extracted from diebold_mariano_1995.

    **Source**:
    - Title: ; the file is the JBES 20(1):134-144 (Jan 2002) twentieth-anniversary reprint from JSTOR 1392155, running head 'July 1995' (1995)
    - Authors: Diebold, F.X. and Mariano, R.S. et al.
    - Citation Key: `diebold_mariano_1995`

    **KaTeX Formula**:
    $$
    1 = T
    $$

    Args:
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(T)


def expr_val_1_diebol() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1_diebol`."""
    return pl.col("T")


def calc_diebold_mariano_1995_diebol(S: float) -> float:
    r"""Compute mathematical metric extracted from diebold_mariano_1995.

    **Source**:
    - Title: ; the file is the JBES 20(1):134-144 (Jan 2002) twentieth-anniversary reprint from JSTOR 1392155, running head 'July 1995' (1995)
    - Authors: Diebold, F.X. and Mariano, R.S. et al.
    - Citation Key: `diebold_mariano_1995`

    **KaTeX Formula**:
    $$
    S2--.5T a S2a = .., N(O, 1).
    $$

    Args:
        S (float): Input parameter `S`.

    Returns:
        float: Calculated metric value.
    """
    return float(2 * S)


def expr_diebold_mariano_1995_diebol() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_diebold_mariano_1995_diebol`."""
    return 2 * pl.col("S")


def calc_f_diebol(T: float, e: float, i: float, j: float) -> float:
    r"""Compute mathematical metric extracted from diebold_mariano_1995.

    **Source**:
    - Title: ; the file is the JBES 20(1):134-144 (Jan 2002) twentieth-anniversary reprint from JSTOR 1392155, running head 'July 1995' (1995)
    - Authors: Diebold, F.X. and Mariano, R.S. et al.
    - Citation Key: `diebold_mariano_1995`

    **KaTeX Formula**:
    $$
    F = i i j e ej T
    $$

    Args:
        T (float): Input parameter `T`.
        e (float): Input parameter `e`.
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.

    Returns:
        float: Calculated metric value.
    """
    return float(T * e**2 * i**2 * j**2)


def expr_f_diebol() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_diebol`."""
    return pl.col("T") * pl.col("e") ** 2 * pl.col("i") ** 2 * pl.col("j") ** 2


def calc_r_diebol(P: float, p: float) -> float:
    r"""Compute mathematical metric extracted from diebold_mariano_1995.

    **Source**:
    - Title: ; the file is the JBES 20(1):134-144 (Jan 2002) twentieth-anniversary reprint from JSTOR 1392155, running head 'July 1995' (1995)
    - Authors: Diebold, F.X. and Mariano, R.S. et al.
    - Citation Key: `diebold_mariano_1995`

    **KaTeX Formula**:
    $$
    R = P p E[0, 1).
    $$

    Args:
        P (float): Input parameter `P`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e * P * p)


def expr_r_diebol() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_diebol`."""
    return math.e * pl.col("P") * pl.col("p")


def calc_efron_morris_1975_jasa_efron_(a: float, dx: float, n: float) -> float:
    r"""Compute mathematical metric extracted from efron_morris_1975_jasa.

    **Source**:
    - Title: Data analysis using Stein's estimator and its generalizations (1975)
    - Authors: Efron, B. and Morris, C.
    - Citation Key: `efron_morris_1975_jasa`

    **KaTeX Formula**:
    $$
    and x,(e, - N(e , , I), i = 1, . . . 1 2 7 (l.l)
    $$

    Args:
        a (float): Input parameter `a`.
        dx (float): Input parameter `dx`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * dx * n)


def expr_efron_morris_1975_jasa_efron_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_efron_morris_1975_jasa_efron_`."""
    return pl.col("a") * pl.col("dx") * pl.col("n")


def calc_a_p_m_efron_(P: float) -> float:
    r"""Compute mathematical metric extracted from efron_morris_1975_jasa.

    **Source**:
    - Title: Data analysis using Stein's estimator and its generalizations (1975)
    - Authors: Efron, B. and Morris, C.
    - Citation Key: `efron_morris_1975_jasa`

    **KaTeX Formula**:
    $$
    a ( p , m) = P(T > 3.84 p , m) ,
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_a_p_m_efron_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_p_m_efron_`."""
    return pl.col("P")


def calc_egidi_2018_arxiv1802_egidi_(a: float, t: float) -> float:
    r"""Compute mathematical metric extracted from egidi_2018_arxiv1802.

    **Source**:
    - Title: arxiv1802.08848
    - Authors: Scientific Literature
    - Citation Key: `egidi_2018_arxiv1802`

    **KaTeX Formula**:
    $$
    attt,τ ∼ N(µatt + attt,τ-1, σ2 att ) deft,τ ∼ N(µdef + deft,τ-1, σ2 def ),
    $$

    Args:
        a (float): Input parameter `a`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * t**3)


def expr_egidi_2018_arxiv1802_egidi_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_egidi_2018_arxiv1802_egidi_`."""
    return pl.col("a") * pl.col("t") ** 3


def calc_b_p_egidi_(P: float) -> float:
    r"""Compute mathematical metric extracted from egidi_2018_arxiv1802.

    **Source**:
    - Title: arxiv1802.08848
    - Authors: Scientific Literature
    - Citation Key: `egidi_2018_arxiv1802`

    **KaTeX Formula**:
    $$
    pB = P (T (yrep ) > T (y)|y).
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_b_p_egidi_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_b_p_egidi_`."""
    return pl.col("P")


def calc_glickman_2001_jas_dynamic_paired_glickm(m: float, t: float, u: float) -> float:
    r"""Compute mathematical metric extracted from glickman_2001_jas_dynamic_paired.

    **Source**:
    - Title: Dynamic paired comparison models with stochastic variances (2001)
    - Authors: Glickman, M. E.
    - Citation Key: `glickman_2001_jas_dynamic_paired`

    **KaTeX Formula**:
    $$
    u 2 (t) 5 ( 1 u 2 (t) + 1 m 2 ) 2 1
    $$

    Args:
        m (float): Input parameter `m`.
        t (float): Input parameter `t`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(2 * t * u * (210 * m + 210 * t * u))


def expr_glickman_2001_jas_dynamic_paired_glickm() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_glickman_2001_jas_dynamic_paired_glickm`."""
    return 2 * pl.col("t") * pl.col("u") * (210 * pl.col("m") + 210 * pl.col("t") * pl.col("u"))


def calc_s_s_k_i_l_l_n_gneiti(
    S: float,
    c: float,
    e: float,
    f: float,
    n: float,
    o: float,
    p: float,
    r: float,
    s: float,
    t: float,
) -> float:
    r"""Compute mathematical metric extracted from gneiting_raftery_2007_jasa.

    **Source**:
    - Title: gneiting2007jasa
    - Authors: Scientific Literature
    - Citation Key: `gneiting_raftery_2007_jasa`

    **KaTeX Formula**:
    $$
    S skill n = S fcst n -S ref n S opt n -S ref n ,
    $$

    Args:
        S (float): Input parameter `S`.
        c (float): Input parameter `c`.
        e (float): Input parameter `e`.
        f (float): Input parameter `f`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(
        -S * r * (e * (f * n))
        + (S * (f * (c * (s * (n * t)))) - S * r * (e * (f * (n * (S * (o * (p * (n * t))))))))
    )


def expr_s_s_k_i_l_l_n_gneiti() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_s_k_i_l_l_n_gneiti`."""
    return -pl.col("S") * pl.col("r") * (pl.col("e") * (pl.col("f") * pl.col("n"))) + (
        pl.col("S") * (pl.col("f") * (pl.col("c") * (pl.col("s") * (pl.col("n") * pl.col("t")))))
        - pl.col("S")
        * pl.col("r")
        * (
            pl.col("e")
            * (
                pl.col("f")
                * (
                    pl.col("n")
                    * (pl.col("S") * (pl.col("o") * (pl.col("p") * (pl.col("n") * pl.col("t")))))
                )
            )
        )
    )


def calc_s_c_p_1_gneiti(c: float) -> float:
    r"""Compute mathematical metric extracted from gneiting_raftery_2007_jasa.

    **Source**:
    - Title: gneiting2007jasa
    - Authors: Scientific Literature
    - Citation Key: `gneiting_raftery_2007_jasa`

    **KaTeX Formula**:
    $$
    Sc(p, 1) = (1 - c)1{p > c}, Sc(p,0) =c1{p\le c},
    $$

    Args:
        c (float): Input parameter `c`.

    Returns:
        float: Calculated metric value.
    """
    return float(1 * (1 - c))


def expr_s_c_p_1_gneiti() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_c_p_1_gneiti`."""
    return 1 * (1 - pl.col("c"))


def calc_g_p_gneiti(
    P: float,
    S: float,
    a: float,
    de: float,
    g: float,
    i: float,
    l: float,
    m: float,
    o: float,
    t: float,
) -> float:
    r"""Compute mathematical metric extracted from gneiting_raftery_2007_jasa.

    **Source**:
    - Title: gneiting2007jasa
    - Authors: Scientific Literature
    - Citation Key: `gneiting_raftery_2007_jasa`

    **KaTeX Formula**:
    $$
    G(P) = - log det Sigma1P - m,
    $$

    Args:
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.
        a (float): Input parameter `a`.
        de (float): Input parameter `de`.
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.
        o (float): Input parameter `o`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(-l * o * (g * (de * (t * (S * (i * (g * (m * ((1 * P) * a)))))))) - m)


def expr_g_p_gneiti() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_p_gneiti`."""
    return -pl.col("l") * pl.col("o") * (
        pl.col("g")
        * (
            pl.col("de")
            * (
                pl.col("t")
                * (
                    pl.col("S")
                    * (
                        pl.col("i")
                        * (pl.col("g") * (pl.col("m") * ((1 * pl.col("P")) * pl.col("a"))))
                    )
                )
            )
        )
    ) - pl.col("m")


def calc_gneiting_raftery_2007_jasa_gneiti(P: float) -> float:
    r"""Compute mathematical metric extracted from gneiting_raftery_2007_jasa.

    **Source**:
    - Title: gneiting2007jasa
    - Authors: Scientific Literature
    - Citation Key: `gneiting_raftery_2007_jasa`

    **KaTeX Formula**:
    $$
    2EP,Qg(X, Y) - EPg(X, X ′ ) - EQg(Y, Y ′ ) \ge  0.
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(2 * math.e * P)


def expr_gneiting_raftery_2007_jasa_gneiti() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_gneiting_raftery_2007_jasa_gneiti`."""
    return 2 * math.e * pl.col("P")


def calc_b_gneiti(P: float) -> float:
    r"""Compute mathematical metric extracted from gneiting_raftery_2007_jasa.

    **Source**:
    - Title: gneiting2007jasa
    - Authors: Scientific Literature
    - Citation Key: `gneiting_raftery_2007_jasa`

    **KaTeX Formula**:
    $$
    B = P(X|H1) P(X|H2) ,
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_b_gneiti() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_b_gneiti`."""
    return pl.col("P")


def calc_l_o_b_g_gneiti(H: float, L: float, g: float, o: float) -> float:
    r"""Compute mathematical metric extracted from gneiting_raftery_2007_jasa.

    **Source**:
    - Title: gneiting2007jasa
    - Authors: Scientific Literature
    - Citation Key: `gneiting_raftery_2007_jasa`

    **KaTeX Formula**:
    $$
    log B = LogS(H1, X) - LogS(H2, X).
    $$

    Args:
        H (float): Input parameter `H`.
        L (float): Input parameter `L`.
        g (float): Input parameter `g`.
        o (float): Input parameter `o`.

    Returns:
        float: Calculated metric value.
    """
    return float(-H * L * g * o)


def expr_l_o_b_g_gneiti() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_o_b_g_gneiti`."""
    return -pl.col("H") * pl.col("L") * pl.col("g") * pl.col("o")


def calc_guo_2017_calibration_guo_20(P: float) -> float:
    r"""Compute mathematical metric extracted from guo_2017_calibration.

    **Source**:
    - Title: arxiv1706.04599
    - Authors: Scientific Literature
    - Citation Key: `guo_2017_calibration`

    **KaTeX Formula**:
    $$
    P(S=s | D) = P(D | S=s) ∑s′∈S P(D | S=s′ ) .
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_guo_2017_calibration_guo_20() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_guo_2017_calibration_guo_20`."""
    return pl.col("P")


def calc_s_2_harvey(Z: float, n: float, r: float) -> float:
    r"""Compute mathematical metric extracted from harvey_leybourne_newbold_1997.

    **Source**:
    - Title: article3 (1997)
    - Authors: Scientific Literature
    - Citation Key: `harvey_leybourne_newbold_1997`

    **KaTeX Formula**:
    $$
    S 2 = [(1 - rZ)/(n - 1)]-1/2r,
    $$

    Args:
        Z (float): Input parameter `Z`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float((1 - Z * r) / (n - 1) - 1 / (2 * r))


def expr_s_2_harvey() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_2_harvey`."""
    return (1 - pl.col("Z") * pl.col("r")) / (pl.col("n") - 1) - 1 / (2 * pl.col("r"))


def calc_harvey_leybourne_newbold_1997_harvey(h: float) -> float:
    r"""Compute mathematical metric extracted from harvey_leybourne_newbold_1997.

    **Source**:
    - Title: article3 (1997)
    - Authors: Scientific Literature
    - Citation Key: `harvey_leybourne_newbold_1997`

    **KaTeX Formula**:
    $$
    h-, ~] l~'(d) = n- ' Yo + 2n-1 ~] (n - k)4/ , (5 / k=l
    $$

    Args:
        h (float): Input parameter `h`.

    Returns:
        float: Calculated metric value.
    """
    return float(h)


def expr_harvey_leybourne_newbold_1997_harvey() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_harvey_leybourne_newbold_1997_harvey`."""
    return pl.col("h")


def calc_val_1_12_2_harvey(n: float) -> float:
    r"""Compute mathematical metric extracted from harvey_leybourne_newbold_1997.

    **Source**:
    - Title: article3 (1997)
    - Authors: Scientific Literature
    - Citation Key: `harvey_leybourne_newbold_1997`

    **KaTeX Formula**:
    $$
    -1 2^2 = n ,~x t e t .
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(n)


def expr_val_1_12_2_harvey() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1_12_2_harvey`."""
    return pl.col("n")


def calc_maher_1982_maher_(i: float, j: float) -> float:
    r"""Compute mathematical metric extracted from maher_1982.

    **Source**:
    - Title: maher
    - Authors: Scientific Literature
    - Citation Key: `maher_1982`

    **KaTeX Formula**:
    $$
    i j + i
    $$

    Args:
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.

    Returns:
        float: Calculated metric value.
    """
    return float(i * j + i)


def expr_maher_1982_maher_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_maher_1982_maher_`."""
    return pl.col("i") * pl.col("j") + pl.col("i")


def calc_c_i_maher_(u: float, x: float) -> float:
    r"""Compute mathematical metric extracted from maher_1982.

    **Source**:
    - Title: maher
    - Authors: Scientific Literature
    - Citation Key: `maher_1982`

    **KaTeX Formula**:
    $$
    Ci= 1 xu/,& and j j= 1 xu/&, where &=I 1 xu. j + i i+. j i j=ei
    $$

    Args:
        u (float): Input parameter `u`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(u * x)


def expr_c_i_maher_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_i_maher_`."""
    return pl.col("u") * pl.col("x")


def calc_z_l_y_u_c_c_u_x_i_k_2_j_r_maher_(i: float, j: float) -> float:
    r"""Compute mathematical metric extracted from maher_1982.

    **Source**:
    - Title: maher
    - Authors: Scientific Literature
    - Citation Key: `maher_1982`

    **KaTeX Formula**:
    $$
    z: L Yu c c xu - r j * i k2=- i j * i
    $$

    Args:
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.

    Returns:
        float: Calculated metric value.
    """
    return float(-(i**2) * j)


def expr_z_l_y_u_c_c_u_x_i_k_2_j_r_maher_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_l_y_u_c_c_u_x_i_k_2_j_r_maher_`."""
    return -(pl.col("i") ** 2) * pl.col("j")


def calc_maher_secondary_dependence_2021_maher_(A: float, p: float, r: float) -> float:
    r"""Compute mathematical metric extracted from maher_secondary_dependence_2021.

    **Source**:
    - Title: arxiv_2103.07272
    - Authors: Scientific Literature
    - Citation Key: `maher_secondary_dependence_2021`

    **KaTeX Formula**:
    $$
    prA(xk = h, yk = a) = e-ψy(µk,h)ψy(µk, h)a a! e-λk λhk h! .
    $$

    Args:
        A (float): Input parameter `A`.
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(A * p * r)


def expr_maher_secondary_dependence_2021_maher_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_maher_secondary_dependence_2021_maher_`."""
    return pl.col("A") * pl.col("p") * pl.col("r")


def calc_math_0509698_form_f(P: float, b: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from math_0509698.

    **Source**:
    - Title: A Derivation of the Pythagorean Won-Loss Formula in Baseball (2005)
    - Authors: Steven J. Miller
    - Citation Key: `math_0509698`

    **KaTeX Formula**:
    $$
    Prob(X > Y ) = ∫ ∞ x=β ∫ x y=β f (x; αRS, β, γ)f (y; αRA, β, γ)dy dx = ∫ ∞ x=β ∫ x y=β γ αRS ( x - β αRS )γ-1 e-((x-β)/αRS)γ γ αRA ( y - β αRA )γ-1 e-((y-β)/αRA)γ dy dx = ∫ ∞ x=0 γ αRS ( x αRS )γ-1 e-(x/αRS)γ [∫ x y=0 γ αRA ( y αRA )γ-1 e-(y/αRA)γ dy] dx = ∫ ∞ x=0 γ αRS ( x αRS )γ-1 e-(x/αRS)γ [1 - e-(x/αRA)γ ] dx = 1- ∫ ∞ x=0 γ αRS ( x αRS )γ-1 e-(x/α)γ dx,
    $$

    Args:
        P (float): Input parameter `P`.
        b (float): Input parameter `b`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * b * o * r)


def expr_math_0509698_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_math_0509698_form_f`."""
    return pl.col("P") * pl.col("b") * pl.col("o") * pl.col("r")


def calc_math_0509698_form_9(P: float, b: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from math_0509698.

    **Source**:
    - Title: A Derivation of the Pythagorean Won-Loss Formula in Baseball (2005)
    - Authors: Steven J. Miller
    - Citation Key: `math_0509698`

    **KaTeX Formula**:
    $$
    Prob(X > Y ) = 1- αγ αγRS ∫ ∞ 0 γα ( xα )γ-1 e(x/α)γ dx = 1- αγ αγRS = 1- 1 αγRS αγRS αγRA αγRS + αγRA = αγRS αγRS + αγRA .
    $$

    Args:
        P (float): Input parameter `P`.
        b (float): Input parameter `b`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * b * o * r)


def expr_math_0509698_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_math_0509698_form_9`."""
    return pl.col("P") * pl.col("b") * pl.col("o") * pl.col("r")


def calc_math_0509698_form_7(P: float, b: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from math_0509698.

    **Source**:
    - Title: A Derivation of the Pythagorean Won-Loss Formula in Baseball (2005)
    - Authors: Steven J. Miller
    - Citation Key: `math_0509698`

    **KaTeX Formula**:
    $$
    Prob(X > Y ) = (R_{S} - β)γ (R_{S} - β)γ + (R_{A} - β)γ ,
    $$

    Args:
        P (float): Input parameter `P`.
        b (float): Input parameter `b`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * b * o * r)


def expr_math_0509698_form_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_math_0509698_form_7`."""
    return pl.col("P") * pl.col("b") * pl.col("o") * pl.col("r")


def calc_math_0509698_form_d(r: float) -> float:
    r"""Compute mathematical metric extracted from math_0509698.

    **Source**:
    - Title: A Derivation of the Pythagorean Won-Loss Formula in Baseball (2005)
    - Authors: Steven J. Miller
    - Citation Key: `math_0509698`

    **KaTeX Formula**:
    $$
    Er,c = lim ℓ→∞ E(ℓ) r,c ;
    $$

    Args:
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e * r)


def expr_math_0509698_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_math_0509698_form_d`."""
    return math.e * pl.col("r")


def calc_miller_2005_pythag_derivation_form_9(P: float, b: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from miller_2005_pythag_derivation.

    **Source**:
    - Title: 'A Derivation of the Pythagorean Won-Loss Formula in Baseball', arXiv math/0509698 (2005)
    - Authors: Miller, S.J.
    - Citation Key: `miller_2005_pythag_derivation`

    **KaTeX Formula**:
    $$
    Prob(X > Y ) = ∫ ∞ x=β ∫ x y=β f (x; αRS, β, γ)f (y; αRA, β, γ)dy dx = ∫ ∞ x=β ∫ x y=β γ αRS ( x - β αRS )γ-1 e-((x-β)/αRS)γ γ αRA ( y - β αRA )γ-1 e-((y-β)/αRA)γ dy dx = ∫ ∞ x=0 γ αRS ( x αRS )γ-1 e-(x/αRS)γ [∫ x y=0 γ αRA ( y αRA )γ-1 e-(y/αRA)γ dy] dx = ∫ ∞ x=0 γ αRS ( x αRS )γ-1 e-(x/αRS)γ [1 - e-(x/αRA)γ ] dx = 1- ∫ ∞ x=0 γ αRS ( x αRS )γ-1 e-(x/α)γ dx,
    $$

    Args:
        P (float): Input parameter `P`.
        b (float): Input parameter `b`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * b * o * r)


def expr_miller_2005_pythag_derivation_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_miller_2005_pythag_derivation_form_9`."""
    return pl.col("P") * pl.col("b") * pl.col("o") * pl.col("r")


def calc_miller_2005_pythag_derivation_form_d(P: float, b: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from miller_2005_pythag_derivation.

    **Source**:
    - Title: 'A Derivation of the Pythagorean Won-Loss Formula in Baseball', arXiv math/0509698 (2005)
    - Authors: Miller, S.J.
    - Citation Key: `miller_2005_pythag_derivation`

    **KaTeX Formula**:
    $$
    Prob(X > Y ) = 1- αγ αγRS ∫ ∞ 0 γα ( xα )γ-1 e(x/α)γ dx = 1- αγ αγRS = 1- 1 αγRS αγRS αγRA αγRS + αγRA = αγRS αγRS + αγRA .
    $$

    Args:
        P (float): Input parameter `P`.
        b (float): Input parameter `b`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * b * o * r)


def expr_miller_2005_pythag_derivation_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_miller_2005_pythag_derivation_form_d`."""
    return pl.col("P") * pl.col("b") * pl.col("o") * pl.col("r")


def calc_miller_2005_pythag_derivation_form_8(X: float, r: float) -> float:
    r"""Compute mathematical metric extracted from miller_2005_pythag_derivation.

    **Source**:
    - Title: 'A Derivation of the Pythagorean Won-Loss Formula in Baseball', arXiv math/0509698 (2005)
    - Authors: Miller, S.J.
    - Citation Key: `miller_2005_pythag_derivation`

    **KaTeX Formula**:
    $$
    Xr,+ = 12∑ c=1 Or,c, X+,c = 12∑ r=1 Or,c.
    $$

    Args:
        X (float): Input parameter `X`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(X * r)


def expr_miller_2005_pythag_derivation_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_miller_2005_pythag_derivation_form_8`."""
    return pl.col("X") * pl.col("r")


def calc_miller_2005_pythag_derivation_form_2(r: float) -> float:
    r"""Compute mathematical metric extracted from miller_2005_pythag_derivation.

    **Source**:
    - Title: 'A Derivation of the Pythagorean Won-Loss Formula in Baseball', arXiv math/0509698 (2005)
    - Authors: Miller, S.J.
    - Citation Key: `miller_2005_pythag_derivation`

    **KaTeX Formula**:
    $$
    Er,c = lim ℓ→∞ E(ℓ) r,c ;
    $$

    Args:
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e * r)


def expr_miller_2005_pythag_derivation_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_miller_2005_pythag_derivation_form_2`."""
    return math.e * pl.col("r")


def calc_miller_2007_pythag_weibull_form_1(P: float, b: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from miller_2007_pythag_weibull.

    **Source**:
    - Title: 40-48 (journal reference on the abs page) (2007)
    - Authors: Steven J. Miller, "A Derivation of the Pythagorean Won-Loss Formula in Baseball", arXiv:math/0509698v4 [math.ST] (v1 2005-09-29 et al.
    - Citation Key: `miller_2007_pythag_weibull`

    **KaTeX Formula**:
    $$
    Prob(X > Y ) = ∫ ∞ x=β ∫ x y=β f (x; αRS, β, γ)f (y; αRA, β, γ)dy dx = ∫ ∞ x=β ∫ x y=β γ αRS ( x - β αRS )γ-1 e-((x-β)/αRS)γ γ αRA ( y - β αRA )γ-1 e-((y-β)/αRA)γ dy dx = ∫ ∞ x=0 γ αRS ( x αRS )γ-1 e-(x/αRS)γ [∫ x y=0 γ αRA ( y αRA )γ-1 e-(y/αRA)γ dy] dx = ∫ ∞ x=0 γ αRS ( x αRS )γ-1 e-(x/αRS)γ [1 - e-(x/αRA)γ ] dx = 1- ∫ ∞ x=0 γ αRS ( x αRS )γ-1 e-(x/α)γ dx,
    $$

    Args:
        P (float): Input parameter `P`.
        b (float): Input parameter `b`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * b * o * r)


def expr_miller_2007_pythag_weibull_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_miller_2007_pythag_weibull_form_1`."""
    return pl.col("P") * pl.col("b") * pl.col("o") * pl.col("r")


def calc_miller_2007_pythag_weibull_form_2(P: float, b: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from miller_2007_pythag_weibull.

    **Source**:
    - Title: 40-48 (journal reference on the abs page) (2007)
    - Authors: Steven J. Miller, "A Derivation of the Pythagorean Won-Loss Formula in Baseball", arXiv:math/0509698v4 [math.ST] (v1 2005-09-29 et al.
    - Citation Key: `miller_2007_pythag_weibull`

    **KaTeX Formula**:
    $$
    Prob(X > Y ) = 1- αγ αγRS ∫ ∞ 0 γα ( xα )γ-1 e(x/α)γ dx = 1- αγ αγRS = 1- 1 αγRS αγRS αγRA αγRS + αγRA = αγRS αγRS + αγRA .
    $$

    Args:
        P (float): Input parameter `P`.
        b (float): Input parameter `b`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * b * o * r)


def expr_miller_2007_pythag_weibull_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_miller_2007_pythag_weibull_form_2`."""
    return pl.col("P") * pl.col("b") * pl.col("o") * pl.col("r")


def calc_miller_2007_pythag_weibull_form_5(P: float, b: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from miller_2007_pythag_weibull.

    **Source**:
    - Title: 40-48 (journal reference on the abs page) (2007)
    - Authors: Steven J. Miller, "A Derivation of the Pythagorean Won-Loss Formula in Baseball", arXiv:math/0509698v4 [math.ST] (v1 2005-09-29 et al.
    - Citation Key: `miller_2007_pythag_weibull`

    **KaTeX Formula**:
    $$
    Prob(X > Y ) = (R_{S} - β)γ (R_{S} - β)γ + (R_{A} - β)γ ,
    $$

    Args:
        P (float): Input parameter `P`.
        b (float): Input parameter `b`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * b * o * r)


def expr_miller_2007_pythag_weibull_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_miller_2007_pythag_weibull_form_5`."""
    return pl.col("P") * pl.col("b") * pl.col("o") * pl.col("r")


def calc_miller_2007_pythag_weibull_form_3(X: float, r: float) -> float:
    r"""Compute mathematical metric extracted from miller_2007_pythag_weibull.

    **Source**:
    - Title: 40-48 (journal reference on the abs page) (2007)
    - Authors: Steven J. Miller, "A Derivation of the Pythagorean Won-Loss Formula in Baseball", arXiv:math/0509698v4 [math.ST] (v1 2005-09-29 et al.
    - Citation Key: `miller_2007_pythag_weibull`

    **KaTeX Formula**:
    $$
    Xr,+ = 12∑ c=1 Or,c, X+,c = 12∑ r=1 Or,c.
    $$

    Args:
        X (float): Input parameter `X`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(X * r)


def expr_miller_2007_pythag_weibull_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_miller_2007_pythag_weibull_form_3`."""
    return pl.col("X") * pl.col("r")


def calc_naeini_2015_aaai_form_5(P: float) -> float:
    r"""Compute mathematical metric extracted from naeini_2015_aaai.

    **Source**:
    - Title: naeini2015
    - Authors: Scientific Literature
    - Citation Key: `naeini_2015_aaai`

    **KaTeX Formula**:
    $$
    P (D|M) = B∏ b=1 Γ( N ′ B ) Γ(Nb + N ′ B ) Γ(mb + αb) Γ(αb) Γ(nb + βb) Γ(βb) ,
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_naeini_2015_aaai_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_naeini_2015_aaai_form_5`."""
    return pl.col("P")


def calc_naeini_2015_aaai_form_7(P: float) -> float:
    r"""Compute mathematical metric extracted from naeini_2015_aaai.

    **Source**:
    - Title: naeini2015
    - Authors: Scientific Literature
    - Citation Key: `naeini_2015_aaai`

    **KaTeX Formula**:
    $$
    P (z = 1|y) = T∑ i=1 Score(Mi) ∑Tj=1 Score(Mj ) P (z = 1|y, Mi),
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_naeini_2015_aaai_form_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_naeini_2015_aaai_form_7`."""
    return pl.col("P")


def calc_t_form_c(B: float, U: float, m: float) -> float:
    r"""Compute mathematical metric extracted from nguyen_matthews_2022_aging.

    **Source**:
    - Title: 2210.02383
    - Authors: Scientific Literature
    - Citation Key: `nguyen_matthews_2022_aging`

    **KaTeX Formula**:
    $$
    T = U + (1 + 1m ) B ,
    $$

    Args:
        B (float): Input parameter `B`.
        U (float): Input parameter `U`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(B * (m + 1) + U)


def expr_t_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_form_c`."""
    return pl.col("B") * (pl.col("m") + 1) + pl.col("U")


def calc_f_x_form_5(P: float, g: float, l: float, o: float) -> float:
    r"""Compute mathematical metric extracted from niculescu_mizil_caruana_2005.

    **Source**:
    - Title: nmc2005
    - Authors: Scientific Literature
    - Citation Key: `niculescu_mizil_caruana_2005`

    **KaTeX Formula**:
    $$
    F(x) = 12 log P(y = 1|x) P (y = -1|x)
    $$

    Args:
        P (float): Input parameter `P`.
        g (float): Input parameter `g`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.

    Returns:
        float: Calculated metric value.
    """
    return float(12 * P * g * l * o)


def expr_f_x_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_x_form_5`."""
    return 12 * pl.col("P") * pl.col("g") * pl.col("l") * pl.col("o")


def calc_niculescu_mizil_caruana_2005_form_d(P: float) -> float:
    r"""Compute mathematical metric extracted from niculescu_mizil_caruana_2005.

    **Source**:
    - Title: nmc2005
    - Authors: Scientific Literature
    - Citation Key: `niculescu_mizil_caruana_2005`

    **KaTeX Formula**:
    $$
    P (y = 1|x) = 1 1 + exp(-2F (x))
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_niculescu_mizil_caruana_2005_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_niculescu_mizil_caruana_2005_form_d`."""
    return pl.col("P")


def calc_niculescu_mizil_caruana_2005_form_2(P: float) -> float:
    r"""Compute mathematical metric extracted from niculescu_mizil_caruana_2005.

    **Source**:
    - Title: nmc2005
    - Authors: Scientific Literature
    - Citation Key: `niculescu_mizil_caruana_2005`

    **KaTeX Formula**:
    $$
    P (y = 1|f ) = 1 1 + exp(Af + B)
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_niculescu_mizil_caruana_2005_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_niculescu_mizil_caruana_2005_form_2`."""
    return pl.col("P")


def calc_niculescu_mizil_caruana_2005_form_c(
    A: float, a: float, g: float, i: float, m: float, n: float, r: float
) -> float:
    r"""Compute mathematical metric extracted from niculescu_mizil_caruana_2005.

    **Source**:
    - Title: nmc2005
    - Authors: Scientific Literature
    - Citation Key: `niculescu_mizil_caruana_2005`

    **KaTeX Formula**:
    $$
    argmin A,B {- ∑ i yilog(pi) + (1- yi)log(1-pi)},
    $$

    Args:
        A (float): Input parameter `A`.
        a (float): Input parameter `a`.
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(A * a * g * i * m * n * r)


def expr_niculescu_mizil_caruana_2005_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_niculescu_mizil_caruana_2005_form_c`."""
    return (
        pl.col("A")
        * pl.col("a")
        * pl.col("g")
        * pl.col("i")
        * pl.col("m")
        * pl.col("n")
        * pl.col("r")
    )


def calc_niculescu_mizil_caruana_2005_form_b(y: float) -> float:
    r"""Compute mathematical metric extracted from niculescu_mizil_caruana_2005.

    **Source**:
    - Title: nmc2005
    - Authors: Scientific Literature
    - Citation Key: `niculescu_mizil_caruana_2005`

    **KaTeX Formula**:
    $$
    y+ = N+ + 1 N+ +2 ; y- = 1 N- + 2
    $$

    Args:
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(y)


def expr_niculescu_mizil_caruana_2005_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_niculescu_mizil_caruana_2005_form_b`."""
    return pl.col("y")


def calc_retrosheet_lin_winning_advantage_form_6(n: float, s: float) -> float:
    r"""Compute mathematical metric extracted from retrosheet_lin_winning_advantage.

    **Source**:
    - Title: winningadvantage
    - Authors: Scientific Literature
    - Citation Key: `retrosheet_lin_winning_advantage`

    **KaTeX Formula**:
    $$
    ns,w ns .
    $$

    Args:
        n (float): Input parameter `n`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(n * s)


def expr_retrosheet_lin_winning_advantage_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_retrosheet_lin_winning_advantage_form_6`."""
    return pl.col("n") * pl.col("s")


def calc_retrosheet_lin_winning_advantage_form_d(n: float, s: float) -> float:
    r"""Compute mathematical metric extracted from retrosheet_lin_winning_advantage.

    **Source**:
    - Title: winningadvantage
    - Authors: Scientific Literature
    - Citation Key: `retrosheet_lin_winning_advantage`

    **KaTeX Formula**:
    $$
    ns,w ns = ∑ t∈Ωs ns,t ns ns,t,w ns,t .
    $$

    Args:
        n (float): Input parameter `n`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(n * s)


def expr_retrosheet_lin_winning_advantage_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_retrosheet_lin_winning_advantage_form_d`."""
    return pl.col("n") * pl.col("s")


def calc_shin_family_2024_cambridge_form_b(e: float, h: float, r: float, w: float) -> float:
    r"""Compute mathematical metric extracted from shin_family_2024_cambridge.

    **Source**:
    - Title: shin_family_2024
    - Authors: Scientific Literature
    - Citation Key: `shin_family_2024_cambridge`

    **KaTeX Formula**:
    $$
    where
    $$

    Args:
        e (float): Input parameter `e`.
        h (float): Input parameter `h`.
        r (float): Input parameter `r`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(e**2 * h * r * w)


def expr_shin_family_2024_cambridge_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_shin_family_2024_cambridge_form_b`."""
    return pl.col("e") ** 2 * pl.col("h") * pl.col("r") * pl.col("w")


def calc_h_p_form_6(U: float, e: float) -> float:
    r"""Compute mathematical metric extracted from strumbelj_2014_ijf.

    **Source**:
    - Title: Strumbelj_WorkingPaper2013
    - Authors: Scientific Literature
    - Citation Key: `strumbelj_2014_ijf`

    **KaTeX Formula**:
    $$
    pH = 1 1 + e-U ,
    $$

    Args:
        U (float): Input parameter `U`.
        e (float): Input parameter `e`.

    Returns:
        float: Calculated metric value.
    """
    return float(-U + e + 11)


def expr_h_p_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_p_form_6`."""
    return -pl.col("U") + pl.col("e") + 11


def calc_val_2601_11904_form_c(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_11904.

    **Source**:
    - Title: Structure of Pitch-Pattern Motifs in Major League Baseball (2026)
    - Authors: Youngjai Park, Cheawoon Lim, Seung-Woo Son et al.
    - Citation Key: `arxiv_2601_11904`

    **KaTeX Formula**:
    $$
    P(S | G) = N(G∩S) N(G) = P(G∩S) P(G) , (B1)
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_2601_11904_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2601_11904_form_c`."""
    return pl.col("P")


def calc_val_2609_06739_form_9(b: float, h: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_06739.

    **Source**:
    - Title: The profit-bias identity in sports betting: bookmaker profit as the public's prediction error (2026)
    - Authors: Jacek P. Dmochowski
    - Citation Key: `arxiv_2609_06739`

    **KaTeX Formula**:
    $$
    bh,L(s) ≡ E[ Bh(s) | M < s ], bv,L(s) ≡ E[ Bv(s) | M > s ].
    $$

    Args:
        b (float): Input parameter `b`.
        h (float): Input parameter `h`.

    Returns:
        float: Calculated metric value.
    """
    return float(b * h)


def expr_val_2609_06739_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_06739_form_9`."""
    return pl.col("b") * pl.col("h")


def calc_val_2609_06739_form_f(B: float, g: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_06739.

    **Source**:
    - Title: The profit-bias identity in sports betting: bookmaker profit as the public's prediction error (2026)
    - Authors: Jacek P. Dmochowski
    - Citation Key: `arxiv_2609_06739`

    **KaTeX Formula**:
    $$
    Bg,t = β0 +βh hg,t +βW Wg +βhW (hg,t \times Wg) +ug + εg,t, ug ∼N(0, σ2u ),
    $$

    Args:
        B (float): Input parameter `B`.
        g (float): Input parameter `g`.

    Returns:
        float: Calculated metric value.
    """
    return float(B * g)


def expr_val_2609_06739_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_06739_form_f`."""
    return pl.col("B") * pl.col("g")


def calc_val_2609_06739_form_4(B: float, g: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_06739.

    **Source**:
    - Title: The profit-bias identity in sports betting: bookmaker profit as the public's prediction error (2026)
    - Authors: Jacek P. Dmochowski
    - Citation Key: `arxiv_2609_06739`

    **KaTeX Formula**:
    $$
    Bg,t+h - Bg,t-1 = βℓ→B h ∆ℓg,t +γh∆Bg,t-1 +ag + εg,t, (22) ℓg,t+h - ℓg,t-1 = βB→ℓ h ∆Bg,t +γ ′h ∆ℓg,t-1 +a′g + ε′g,t ,
    $$

    Args:
        B (float): Input parameter `B`.
        g (float): Input parameter `g`.

    Returns:
        float: Calculated metric value.
    """
    return float(B * g)


def expr_val_2609_06739_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_06739_form_4`."""
    return pl.col("B") * pl.col("g")


def calc_val_2609_06739_form_c(b: float, h: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_06739.

    **Source**:
    - Title: The profit-bias identity in sports betting: bookmaker profit as the public's prediction error (2026)
    - Authors: Jacek P. Dmochowski
    - Citation Key: `arxiv_2609_06739`

    **KaTeX Formula**:
    $$
    bh,L(s) = bh(s) + ¯ Fm(s) δ(s), bh,W (s) = bh(s) - Fm(s) δ(s),
    $$

    Args:
        b (float): Input parameter `b`.
        h (float): Input parameter `h`.

    Returns:
        float: Calculated metric value.
    """
    return float(b * h)


def expr_val_2609_06739_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_06739_form_c`."""
    return pl.col("b") * pl.col("h")


def calc_val_2609_06739_form_d(b: float, h: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_06739.

    **Source**:
    - Title: The profit-bias identity in sports betting: bookmaker profit as the public's prediction error (2026)
    - Authors: Jacek P. Dmochowski
    - Citation Key: `arxiv_2609_06739`

    **KaTeX Formula**:
    $$
    bh,L(s) = bh(s) = f, bv,L(s) = bv(s) = 1 - f,
    $$

    Args:
        b (float): Input parameter `b`.
        h (float): Input parameter `h`.

    Returns:
        float: Calculated metric value.
    """
    return float(b * h)


def expr_val_2609_06739_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_06739_form_d`."""
    return pl.col("b") * pl.col("h")


def calc_val_2609_06739_form_2(b: float, h: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_06739.

    **Source**:
    - Title: The profit-bias identity in sports betting: bookmaker profit as the public's prediction error (2026)
    - Authors: Jacek P. Dmochowski
    - Citation Key: `arxiv_2609_06739`

    **KaTeX Formula**:
    $$
    bh,L(s) = bh,W (s).
    $$

    Args:
        b (float): Input parameter `b`.
        h (float): Input parameter `h`.

    Returns:
        float: Calculated metric value.
    """
    return float(b * h)


def expr_val_2609_06739_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_06739_form_2`."""
    return pl.col("b") * pl.col("h")


def calc_val_2609_06739_form_1(b: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_06739.

    **Source**:
    - Title: The profit-bias identity in sports betting: bookmaker profit as the public's prediction error (2026)
    - Authors: Jacek P. Dmochowski
    - Citation Key: `arxiv_2609_06739`

    **KaTeX Formula**:
    $$
    bv,L(s) = 1 - bh,W (s).
    $$

    Args:
        b (float): Input parameter `b`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(b * v)


def expr_val_2609_06739_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_06739_form_1`."""
    return pl.col("b") * pl.col("v")


def calc_val_2609_06739_form_5(b: float, h: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_06739.

    **Source**:
    - Title: The profit-bias identity in sports betting: bookmaker profit as the public's prediction error (2026)
    - Authors: Jacek P. Dmochowski
    - Citation Key: `arxiv_2609_06739`

    **KaTeX Formula**:
    $$
    bh,L(s) - bh(s) = ¯ Fm(s) δ(s), bh(s) - bh,W (s) = Fm(s) δ(s). (S14)
    $$

    Args:
        b (float): Input parameter `b`.
        h (float): Input parameter `h`.

    Returns:
        float: Calculated metric value.
    """
    return float(b * h)


def expr_val_2609_06739_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_06739_form_5`."""
    return pl.col("b") * pl.col("h")


def calc_q_s_form_9(P: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_06739.

    **Source**:
    - Title: The profit-bias identity in sports betting: bookmaker profit as the public's prediction error (2026)
    - Authors: Jacek P. Dmochowski
    - Citation Key: `arxiv_2609_06739`

    **KaTeX Formula**:
    $$
    Q(s) = Pr(Y > s, M < s) + Pr(Y \le  s, M > s). (S19)
    $$

    Args:
        P (float): Input parameter `P`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * r)


def expr_q_s_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_s_form_9`."""
    return pl.col("P") * pl.col("r")


def calc_val_2609_06739_form_0(P: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_06739.

    **Source**:
    - Title: The profit-bias identity in sports betting: bookmaker profit as the public's prediction error (2026)
    - Authors: Jacek P. Dmochowski
    - Citation Key: `arxiv_2609_06739`

    **KaTeX Formula**:
    $$
    Pr(Y > s, M < s) = EX[Pr(Y > s | X) Pr(M < s | X)] ,
    $$

    Args:
        P (float): Input parameter `P`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * r)


def expr_val_2609_06739_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_06739_form_0`."""
    return pl.col("P") * pl.col("r")


def calc_val_2609_03786_form_5(P: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_03786.

    **Source**:
    - Title: Auditing Contextual Bias in Human Ball-Strike Calls Using KBO's Automated Umpiring Transition (2026)
    - Authors: Kichang Lee, JeongGil Ko
    - Citation Key: `arxiv_2609_03786`

    **KaTeX Formula**:
    $$
    Pr(Yi = 1) = logit-1 (α + fzone(xi , yi ; bi , hi) + λ ⊤Ci + γ ⊤Xi + δs(i)) ,
    $$

    Args:
        P (float): Input parameter `P`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * r)


def expr_val_2609_03786_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_03786_form_5`."""
    return pl.col("P") * pl.col("r")


def calc_val_2607_29041_form_1(P: float, g: float, l: float, o: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_29041.

    **Source**:
    - Title: Baseball, An Extensive-Form Game-Theoretic Duel (2026)
    - Authors: Sebastian E. Ferrando, Eli Kohn
    - Citation Key: `arxiv_2607_29041`

    **KaTeX Formula**:
    $$
    log P(AN = aN | AP = aP , A_{B} = aB) P(AN = a0N | AP = aP , A_{B} = aB) = ηaN (aP , aB), aN ̸= a0N ,
    $$

    Args:
        P (float): Input parameter `P`.
        g (float): Input parameter `g`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * g * l * o)


def expr_val_2607_29041_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2607_29041_form_1`."""
    return pl.col("P") * pl.col("g") * pl.col("l") * pl.col("o")


def calc_w_e_s_form_9(N: float, W: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2506_02351.

    **Source**:
    - Title: DIAMOND: An LLM-Driven Agent for Context-Aware Baseball Highlight Summarization (2025)
    - Authors: Jeonghun Kang, Soonmok Kwon, Joonseok Lee et al.
    - Citation Key: `arxiv_2506_02351`

    **KaTeX Formula**:
    $$
    WE(s) = Ws Ns
    $$

    Args:
        N (float): Input parameter `N`.
        W (float): Input parameter `W`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(W * (s * (N * s)))


def expr_w_e_s_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_e_s_form_9`."""
    return pl.col("W") * (pl.col("s") * (pl.col("N") * pl.col("s")))


def calc_val_2607_29041_form_8(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_29041.

    **Source**:
    - Title: Baseball, An Extensive-Form Game-Theoretic Duel (2026)
    - Authors: Sebastian E. Ferrando, Eli Kohn
    - Citation Key: `arxiv_2607_29041`

    **KaTeX Formula**:
    $$
    P := {Pitcher (P), Batter (B), Nature (N)}
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_2607_29041_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2607_29041_form_8`."""
    return pl.col("P")


def calc_val_2607_29041_form_d(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_29041.

    **Source**:
    - Title: Baseball, An Extensive-Form Game-Theoretic Duel (2026)
    - Authors: Sebastian E. Ferrando, Eli Kohn
    - Citation Key: `arxiv_2607_29041`

    **KaTeX Formula**:
    $$
    P(AkN = a | Fk).
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_2607_29041_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2607_29041_form_d`."""
    return pl.col("P")


def calc_val_2607_29041_form_2(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_29041.

    **Source**:
    - Title: Baseball, An Extensive-Form Game-Theoretic Duel (2026)
    - Authors: Sebastian E. Ferrando, Eli Kohn
    - Citation Key: `arxiv_2607_29041`

    **KaTeX Formula**:
    $$
    P(AkN = akN | Fk)(z∗ ) = P(AkN = akN | {AkP = ak∗ P } ∩ {AkB = ak∗ B }) (z∗ ).
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_2607_29041_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2607_29041_form_2`."""
    return pl.col("P")


def calc_val_2607_29041_form_5(R: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_29041.

    **Source**:
    - Title: Baseball, An Extensive-Form Game-Theoretic Duel (2026)
    - Authors: Sebastian E. Ferrando, Eli Kohn
    - Citation Key: `arxiv_2607_29041`

    **KaTeX Formula**:
    $$
    R := OB \times O, elements of R are denoted s = (ob, o).
    $$

    Args:
        R (float): Input parameter `R`.

    Returns:
        float: Calculated metric value.
    """
    return float(R)


def expr_val_2607_29041_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2607_29041_form_5`."""
    return pl.col("R")


def calc_val_2607_29041_form_f(f: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_29041.

    **Source**:
    - Title: Baseball, An Extensive-Form Game-Theoretic Duel (2026)
    - Authors: Sebastian E. Ferrando, Eli Kohn
    - Citation Key: `arxiv_2607_29041`

    **KaTeX Formula**:
    $$
    f ((ob, o), z) = (ob, o + 1).
    $$

    Args:
        f (float): Input parameter `f`.

    Returns:
        float: Calculated metric value.
    """
    return float(f)


def expr_val_2607_29041_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2607_29041_form_f`."""
    return pl.col("f")


def calc_val_2607_29041_form_6(f: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_29041.

    **Source**:
    - Title: Baseball, An Extensive-Form Game-Theoretic Duel (2026)
    - Authors: Sebastian E. Ferrando, Eli Kohn
    - Citation Key: `arxiv_2607_29041`

    **KaTeX Formula**:
    $$
    f ((ob, 2), z) = (∅, 3).
    $$

    Args:
        f (float): Input parameter `f`.

    Returns:
        float: Calculated metric value.
    """
    return float(f)


def expr_val_2607_29041_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2607_29041_form_6`."""
    return pl.col("f")


def calc_val_2607_29041_form_c(s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_29041.

    **Source**:
    - Title: Baseball, An Extensive-Form Game-Theoretic Duel (2026)
    - Authors: Sebastian E. Ferrando, Eli Kohn
    - Citation Key: `arxiv_2607_29041`

    **KaTeX Formula**:
    $$
    s+ = f (s-, z),
    $$

    Args:
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(s)


def expr_val_2607_29041_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2607_29041_form_c`."""
    return pl.col("s")


def calc_val_2607_29041_form_e(S: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_29041.

    **Source**:
    - Title: Baseball, An Extensive-Form Game-Theoretic Duel (2026)
    - Authors: Sebastian E. Ferrando, Eli Kohn
    - Citation Key: `arxiv_2607_29041`

    **KaTeX Formula**:
    $$
    Si := {∅} ∪ {σ ≡ σva | v ∈ Ui, a ∈ Ai(v)},
    $$

    Args:
        S (float): Input parameter `S`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(S * i)


def expr_val_2607_29041_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2607_29041_form_e`."""
    return pl.col("S") * pl.col("i")


def calc_val_2607_29041_form_b(P: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_29041.

    **Source**:
    - Title: Baseball, An Extensive-Form Game-Theoretic Duel (2026)
    - Authors: Sebastian E. Ferrando, Eli Kohn
    - Citation Key: `arxiv_2607_29041`

    **KaTeX Formula**:
    $$
    Px(z | v) := Px(z) Px(Av) (z ∈ Av), Px(Av′ | v) := Px(Av′) Px(Av) (v′ ⪰ v).
    $$

    Args:
        P (float): Input parameter `P`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * x)


def expr_val_2607_29041_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2607_29041_form_b`."""
    return pl.col("P") * pl.col("x")


def calc_v_v_1_form_e(a: float, m: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_29041.

    **Source**:
    - Title: Baseball, An Extensive-Form Game-Theoretic Duel (2026)
    - Authors: Sebastian E. Ferrando, Eli Kohn
    - Citation Key: `arxiv_2607_29041`

    **KaTeX Formula**:
    $$
    V (v1) = max{ Px(F | v1) ¯
    $$

    Args:
        a (float): Input parameter `a`.
        m (float): Input parameter `m`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * m * x)


def expr_v_v_1_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_v_1_form_e`."""
    return pl.col("a") * pl.col("m") * pl.col("x")


def calc_val_2607_29041_form_9(M: float, c: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_29041.

    **Source**:
    - Title: Baseball, An Extensive-Form Game-Theoretic Duel (2026)
    - Authors: Sebastian E. Ferrando, Eli Kohn
    - Citation Key: `arxiv_2607_29041`

    **KaTeX Formula**:
    $$
    Ms-(c)[aP , aB] := ∑ n∈AN βN(n | s-, c, aP , aB)Ws-(c, n).
    $$

    Args:
        M (float): Input parameter `M`.
        c (float): Input parameter `c`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(M * s - c)


def expr_val_2607_29041_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2607_29041_form_9`."""
    return pl.col("M") * pl.col("s") - pl.col("c")


def calc_val_2607_29041_form_4(B: float, G: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_29041.

    **Source**:
    - Title: Baseball, An Extensive-Form Game-Theoretic Duel (2026)
    - Authors: Sebastian E. Ferrando, Eli Kohn
    - Citation Key: `arxiv_2607_29041`

    **KaTeX Formula**:
    $$
    GB(s-, c, aB) := Vs-(c) - QB(s-, c, aB) \ge  0.
    $$

    Args:
        B (float): Input parameter `B`.
        G (float): Input parameter `G`.

    Returns:
        float: Calculated metric value.
    """
    return float(B * G)


def expr_val_2607_29041_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2607_29041_form_4`."""
    return pl.col("B") * pl.col("G")


def calc_eq_e_x_e_f_y_form_8(f: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_29041.

    **Source**:
    - Title: Baseball, An Extensive-Form Game-Theoretic Duel (2026)
    - Authors: Sebastian E. Ferrando, Eli Kohn
    - Citation Key: `arxiv_2607_29041`

    **KaTeX Formula**:
    $$
    Ex = e Fy = f
    $$

    Args:
        f (float): Input parameter `f`.

    Returns:
        float: Calculated metric value.
    """
    return float(f)


def expr_eq_e_x_e_f_y_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_eq_e_x_e_f_y_form_8`."""
    return pl.col("f")


def calc_val_2607_29041_form_7(i: float, m: float, n: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_29041.

    **Source**:
    - Title: Baseball, An Extensive-Form Game-Theoretic Duel (2026)
    - Authors: Sebastian E. Ferrando, Eli Kohn
    - Citation Key: `arxiv_2607_29041`

    **KaTeX Formula**:
    $$
    min y,p eT p s.t. ET p-Ay \ge  0, Fy = f, y \ge  0 max x,q f T q s.t. F T q -BT x \le  0, Ex = e, x \ge  0
    $$

    Args:
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(i * m * n * y)


def expr_val_2607_29041_form_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2607_29041_form_7`."""
    return pl.col("i") * pl.col("m") * pl.col("n") * pl.col("y")


def calc_l_z_form_a(y: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_12629.

    **Source**:
    - Title: Bivariate Isotonic Regression by Dynamic Programming (2026)
    - Authors: Pedro Afonso Fernandes
    - Citation Key: `arxiv_2607_12629`

    **KaTeX Formula**:
    $$
    L(z) = |z - y| .
    $$

    Args:
        y (float): Input parameter `y`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(abs(y - z))


def expr_l_z_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_z_form_a`."""
    return abs(pl.col("y") - pl.col("z"))


def calc_val_2606_26780_form_1(
    a: float,
    c: float,
    dt: float,
    e: float,
    g: float,
    i: float,
    k: float,
    label: float,
    n: float,
    phi_0: float,
    q: float,
    r: float,
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_26780.

    **Source**:
    - Title: Event-based Gaze Control System for Accurate Real-time Spin Estimation in Professional Ball Games (2026)
    - Authors: Yunpu Hu, Fabian Schilling, Valentina Cavinato et al.
    - Citation Key: `arxiv_2606_26780`

    **KaTeX Formula**:
    $$
    \label {eq:3dtracking} \phi _0, \phi _1 = \argmin _{\phi _0, \phi _1} \left \| z_t^{-1} K_c T_\text {vc} \mathbf {p}_t - \left [c_x, c_y, 1\right ]^\top \right \|
    $$

    Args:
        a (float): Input parameter `a`.
        c (float): Input parameter `c`.
        dt (float): Input parameter `dt`.
        e (float): Input parameter `e`.
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        k (float): Input parameter `k`.
        label (float): Input parameter `label`.
        n (float): Input parameter `n`.
        phi_0 (float): Input parameter `phi_0`.
        q (float): Input parameter `q`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(label * (phi_0 * ((e * q) / (3 * (dt * (r * (a * (c * (k * (i * (g * n)))))))))))


def expr_val_2606_26780_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2606_26780_form_1`."""
    return pl.col("label") * (
        pl.col("phi_0")
        * (
            (pl.col("e") * pl.col("q"))
            / (
                3
                * (
                    pl.col("dt")
                    * (
                        pl.col("r")
                        * (
                            pl.col("a")
                            * (
                                pl.col("c")
                                * (pl.col("k") * (pl.col("i") * (pl.col("g") * pl.col("n"))))
                            )
                        )
                    )
                )
            )
        )
    )


def calc_begin_x_k_a_l_i_g_n_d_e_form_4(c_x: float, r: float, u_k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_26780.

    **Source**:
    - Title: Event-based Gaze Control System for Accurate Real-time Spin Estimation in Professional Ball Games (2026)
    - Authors: Yunpu Hu, Fabian Schilling, Valentina Cavinato et al.
    - Citation Key: `arxiv_2606_26780`

    **KaTeX Formula**:
    $$
    \begin {aligned} x_k &= (u_k - c_x) / r, \quad y_k = (v_k - c_y) / r, \quad z_k = -\sqrt {1 - (x_k^2 + y_k^2)} \end {aligned} \label {eq:orthographic}
    $$

    Args:
        c_x (float): Input parameter `c_x`.
        r (float): Input parameter `r`.
        u_k (float): Input parameter `u_k`.

    Returns:
        float: Calculated metric value.
    """
    return float((-c_x + u_k) / r)


def expr_begin_x_k_a_l_i_g_n_d_e_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_begin_x_k_a_l_i_g_n_d_e_form_4`."""
    return (-pl.col("c_x") + pl.col("u_k")) / pl.col("r")


def calc_p_i_j_form_6(P: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_03805.

    **Source**:
    - Title: Regularization in Paired Comparison Models via Pseudo-Games and Phantom Players (2026)
    - Authors: Mark E. Glickman
    - Citation Key: `arxiv_2606_03805`

    **KaTeX Formula**:
    $$
    pij = Pr(Yij = 1) = F (θi - θj),
    $$

    Args:
        P (float): Input parameter `P`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * r)


def expr_p_i_j_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_j_form_6`."""
    return pl.col("P") * pl.col("r")


def calc_val_2604_21851_form_8(P: float, f: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2604_21851.

    **Source**:
    - Title: Betting on Bets: Anytime-Valid Tests for Stochastic Dominance (2026)
    - Authors: Sebastian Arnold, Yo Joong Choe, Marco Scarsini et al.
    - Citation Key: `arxiv_2604_21851`

    **KaTeX Formula**:
    $$
    Proof. 𝑆(𝜆, 𝑧) \ge  0, for any 𝜆 ∈ [0, 1], and 𝔼ℙ [𝑆(𝜆, 𝑧)] \le  1 for any ℙ ∈ ℋ0(𝑧).
    $$

    Args:
        P (float): Input parameter `P`.
        f (float): Input parameter `f`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * f * o**2 * r)


def expr_val_2604_21851_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2604_21851_form_8`."""
    return pl.col("P") * pl.col("f") * pl.col("o") ** 2 * pl.col("r")


def calc_w_a_p_form_9(
    W: float, a: float, b: float, e: float, f: float, o: float, r: float, t: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2506_02351.

    **Source**:
    - Title: DIAMOND: An LLM-Driven Agent for Context-Aware Baseball Highlight Summarization (2025)
    - Authors: Jeonghun Kang, Soonmok Kwon, Joonseok Lee et al.
    - Citation Key: `arxiv_2506_02351`

    **KaTeX Formula**:
    $$
    WPA = WEafter - WEbefore
    $$

    Args:
        W (float): Input parameter `W`.
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        e (float): Input parameter `e`.
        f (float): Input parameter `f`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e * W * a * e * f * r * t - math.e * W * b * e**2 * f * o * r)


def expr_w_a_p_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_a_p_form_9`."""
    return math.e * pl.col("W") * pl.col("a") * pl.col("e") * pl.col("f") * pl.col("r") * pl.col(
        "t"
    ) - math.e * pl.col("W") * pl.col("b") * pl.col("e") ** 2 * pl.col("f") * pl.col("o") * pl.col(
        "r"
    )


def calc_val_1704_00823_form_4(g: float, l: float, o: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1704_00823.

    **Source**:
    - Title: A Hierarchical Bayesian Model of Pitch Framing (2017)
    - Authors: Sameer K. Deshpande, Abraham J. Wyner
    - Citation Key: `arxiv_1704_00823`

    **KaTeX Formula**:
    $$
    log ( P(y = 1) P(y = 0) ) = Θu,B b +Θu,CA ca +Θu,P p +Θu,CO co + f u(x, z)
    $$

    Args:
        g (float): Input parameter `g`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.

    Returns:
        float: Calculated metric value.
    """
    return float(g * l * o)


def expr_val_1704_00823_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1704_00823_form_4`."""
    return pl.col("g") * pl.col("l") * pl.col("o")


def calc_val_1704_00823_form_3(g: float, l: float, o: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1704_00823.

    **Source**:
    - Title: A Hierarchical Bayesian Model of Pitch Framing (2017)
    - Authors: Sameer K. Deshpande, Abraham J. Wyner
    - Citation Key: `arxiv_1704_00823`

    **KaTeX Formula**:
    $$
    log ( P(yi = 1) P(yi = 0) ) = h⊤i Θu(i) 0 +LO⊤i Θu(i) LO +CO⊤i Θu(i) CO +CA⊤i Θu(i) CA +P⊤i Θu(i) P +B⊤i Θu(i) B
    $$

    Args:
        g (float): Input parameter `g`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.

    Returns:
        float: Calculated metric value.
    """
    return float(g * l * o)


def expr_val_1704_00823_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1704_00823_form_3`."""
    return pl.col("g") * pl.col("l") * pl.col("o")


def calc_val_0902_1360_form_e(p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_0902_1360.

    **Source**:
    - Title: Hierarchical Bayesian Modeling of Hitting Performance in Baseball (2009)
    - Authors: Shane T. Jensen, Blake McShane, Abraham J. Wyner
    - Citation Key: `arxiv_0902_1360`

    **KaTeX Formula**:
    $$
    p(Eit|Xi,t,ΘΘ) ∝ p(Xi,t|Eit,ΘΘ) \times  p(Eit|Xi,t-1,ΘΘ) ∝ p(Xi,t|Eit,ΘΘ) \times  1∑ e=0 p(Eit|Ei,t-1 = e,ΘΘ) \cdot  p(Ei,t-1 = e|Xi,t-1,ΘΘ)
    $$

    Args:
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(p)


def expr_val_0902_1360_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_0902_1360_form_e`."""
    return pl.col("p")


def calc_i_n_de_x_form_0(z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_21163.

    **Source**:
    - Title: Simultaneous Estimation of Ballpark Effects and Team Defense Using Total Bases Residuals (2026)
    - Authors: Jhe-Jia Wu, Tian-Li Yan, Ting-Li Chen
    - Citation Key: `arxiv_2603_21163`

    **KaTeX Formula**:
    $$
    Index = 100 + 20 \times  z.
    $$

    Args:
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(20 * z + 100)


def expr_i_n_de_x_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_n_de_x_form_0`."""
    return 20 * pl.col("z") + 100


def calc_val_2005_07742_form_d(f: float, p: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2005_07742.

    **Source**:
    - Title: SEAM methodology for context-rich player matchup evaluations (2020)
    - Authors: Julia Wapner, David Dalpiaz, Daniel J. Eck
    - Citation Key: `arxiv_2005_07742`

    **KaTeX Formula**:
    $$
    fsp,t(y|xb,t) = J∑ j=1 wp,j,tf (y|xp,j,t, xb,t).
    $$

    Args:
        f (float): Input parameter `f`.
        p (float): Input parameter `p`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(f * p * s)


def expr_val_2005_07742_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2005_07742_form_d`."""
    return pl.col("f") * pl.col("p") * pl.col("s")


def calc_val_2005_07742_form_f(b: float, f: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2005_07742.

    **Source**:
    - Title: SEAM methodology for context-rich player matchup evaluations (2020)
    - Authors: Julia Wapner, David Dalpiaz, Daniel J. Eck
    - Citation Key: `arxiv_2005_07742`

    **KaTeX Formula**:
    $$
    fsb,t(y|xp,t) = K∑ k=1 wb,k,tf (y|xp,t, xb,k,t).
    $$

    Args:
        b (float): Input parameter `b`.
        f (float): Input parameter `f`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(b * f * s)


def expr_val_2005_07742_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2005_07742_form_f`."""
    return pl.col("b") * pl.col("f") * pl.col("s")


def calc_val_2005_07742_form_5(f: float, h: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2005_07742.

    **Source**:
    - Title: SEAM methodology for context-rich player matchup evaluations (2020)
    - Authors: Julia Wapner, David Dalpiaz, Daniel J. Eck
    - Citation Key: `arxiv_2005_07742`

    **KaTeX Formula**:
    $$
    fh(y|x)) - f (y|x) = µ2(K)h′diag(Hf (y|x))h
    $$

    Args:
        f (float): Input parameter `f`.
        h (float): Input parameter `h`.

    Returns:
        float: Calculated metric value.
    """
    return float(f * h)


def expr_val_2005_07742_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2005_07742_form_5`."""
    return pl.col("f") * pl.col("h")


def calc_val_2610_29565_form_4(e: float, f: float, q: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29565.

    **Source**:
    - Title: Preserving Operator Intent Under Actuation Constraints: Teleoperation of Manipulators with Coupled Transmissions (2026)
    - Authors: Xuhan Miao, Zijin Han, Yutong Shen et al.
    - Citation Key: `arxiv_2610_29565`

    **KaTeX Formula**:
    $$
    qref,k+1 = qref,k +∆t ˙ q∗ k ,
    $$

    Args:
        e (float): Input parameter `e`.
        f (float): Input parameter `f`.
        q (float): Input parameter `q`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(e * f * q * r)


def expr_val_2610_29565_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_29565_form_4`."""
    return pl.col("e") * pl.col("f") * pl.col("q") * pl.col("r")


def calc_val_2610_05080_form_4(c: float, r: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_05080.

    **Source**:
    - Title: Tracing a Sparse Emotion-Control Circuit in LLM-Based Text-to-Speech (2026)
    - Authors: Hongfei Du, Jiacheng Shi, Yanfu Zhang et al.
    - Citation Key: `arxiv_2610_05080`

    **KaTeX Formula**:
    $$
    Essrc,k = Mk(τ patch ssrc ) -Mk(τ (n) ) Mk(τ (e) ) -Mk(τ (n) ) .
    $$

    Args:
        c (float): Input parameter `c`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e * c * r * s**2)


def expr_val_2610_05080_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_05080_form_4`."""
    return math.e * pl.col("c") * pl.col("r") * pl.col("s") ** 2


def calc_val_2610_05080_form_9(A: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_05080.

    **Source**:
    - Title: Tracing a Sparse Emotion-Control Circuit in LLM-Based Text-to-Speech (2026)
    - Authors: Hongfei Du, Jiacheng Shi, Yanfu Zhang et al.
    - Citation Key: `arxiv_2610_05080`

    **KaTeX Formula**:
    $$
    Ai,c,k = ∑ t 〈∆ai,c,t , ∇ai,c,t Rk(τ patch i,ssrc )〉 .
    $$

    Args:
        A (float): Input parameter `A`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(A * i)


def expr_val_2610_05080_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_05080_form_9`."""
    return pl.col("A") * pl.col("i")


def calc_val_2610_04813_form_c(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_04813.

    **Source**:
    - Title: A Markov Chain Approach to Modeling Rugby Union (2026)
    - Authors: Kenny Watts, Jonathan Pipping-Gamón
    - Citation Key: `arxiv_2610_04813`

    **KaTeX Formula**:
    $$
    P(Sn = snew | Sn-1 = sn-1, . . . , S1 = s1) = P(Sn = snew | Sn-1 = sn-1)
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_2610_04813_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_04813_form_c`."""
    return pl.col("P")


def calc_s_form_e(F: float, G: float, T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_04813.

    **Source**:
    - Title: A Markov Chain Approach to Modeling Rugby Union (2026)
    - Authors: Kenny Watts, Jonathan Pipping-Gamón
    - Citation Key: `arxiv_2610_04813`

    **KaTeX Formula**:
    $$
    S = T \times F \times G.
    $$

    Args:
        F (float): Input parameter `F`.
        G (float): Input parameter `G`.
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(G * (F * T))


def expr_s_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_form_e`."""
    return pl.col("G") * (pl.col("F") * pl.col("T"))


def calc_val_2610_04813_form_b(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_04813.

    **Source**:
    - Title: A Markov Chain Approach to Modeling Rugby Union (2026)
    - Authors: Kenny Watts, Jonathan Pipping-Gamón
    - Citation Key: `arxiv_2610_04813`

    **KaTeX Formula**:
    $$
    P(Sn+1 = sn+1 | Sn = sn) = psn, sn+1 , sn, sn+1 ∈ S.
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_2610_04813_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_04813_form_b`."""
    return pl.col("P")


def calc_val_2610_04813_form_3(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_04813.

    **Source**:
    - Title: A Markov Chain Approach to Modeling Rugby Union (2026)
    - Authors: Kenny Watts, Jonathan Pipping-Gamón
    - Citation Key: `arxiv_2610_04813`

    **KaTeX Formula**:
    $$
    P(Home Win | State) = Number of simulations where Home wins N
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_2610_04813_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_04813_form_3`."""
    return pl.col("P")


def calc_val_2610_01307_form_3(H: float, i: float, m: float, n: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    z[n] \ge Hmin, ∀n ∈ N.
    $$

    Args:
        H (float): Input parameter `H`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float((n * z >= H * i * m * n))


def expr_val_2610_01307_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_01307_form_3`."""
    return pl.col("n") * pl.col("z") >= pl.col("H") * pl.col("i") * pl.col("m") * pl.col("n")


def calc_val_2610_01307_form_b(f: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    f (yw[n, ℓ]) =  1 πσ2 0 [n] exp(- |yw[n, ℓ]|2 σ2 0 [n] ) , H0, 1 πσ2 1 [n] exp(- |yw[n, ℓ]|2 σ2 1 [n] ) , H1,
    $$

    Args:
        f (float): Input parameter `f`.

    Returns:
        float: Calculated metric value.
    """
    return float(f)


def expr_val_2610_01307_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_01307_form_b`."""
    return pl.col("f")


def calc_val_2610_01307_form_7(P: float, a: float, m: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    (P1) max P,V,A,Ω 1N N∑ n=1 log2(1 + ρ0 ˆ Fb(db[n], ω[n])) (40a)
    $$

    Args:
        P (float): Input parameter `P`.
        a (float): Input parameter `a`.
        m (float): Input parameter `m`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(P**2 * a * m * x)


def expr_val_2610_01307_form_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_01307_form_7`."""
    return pl.col("P") ** 2 * pl.col("a") * pl.col("m") * pl.col("x")


def calc_val_2610_01307_form_8(s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    s.t. p[1] = pI, p[N] = pF, (40b)
    $$

    Args:
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(s)


def expr_val_2610_01307_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_01307_form_8`."""
    return pl.col("s")


def calc_val_2610_01307_form_9(a: float, m: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    (P1.1): max P,V,A 1N N∑ n=1 Rlb b [n] (64a) s.t. (40b) - (40f), (40j), (40m) - (40p), (58), (61), (62), (63).
    $$

    Args:
        a (float): Input parameter `a`.
        m (float): Input parameter `m`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(1.1 / (a * m * x))


def expr_val_2610_01307_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_01307_form_9`."""
    return 1.1 / (pl.col("a") * pl.col("m") * pl.col("x"))


def calc_val_2610_01307_form_e(a: float, m: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    (P2): max P,V,A 1N N∑ n=1 ˘Rb(p[n], a[n]) (74a) s.t. ˘ C(p[n], a[n]) \le  √ 2ϵ L , ∀n ∈ N, (74b) S(a[n], a[n+1])\le δrot, ∀n∈N\{N}, (74c) (40b) - (40f), (40j), (40m) - (40p).
    $$

    Args:
        a (float): Input parameter `a`.
        m (float): Input parameter `m`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(2 / (a * m * x))


def expr_val_2610_01307_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_01307_form_e`."""
    return 2 / (pl.col("a") * pl.col("m") * pl.col("x"))


def calc_l_a_a_i_form_6(C: float, E: float, L: float, M: float, P: float, S: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_00735.

    **Source**:
    - Title: Articulatory Source-Filter TTS: Physically Grounded Control through Vocal Tract Kinematics (2026)
    - Authors: Jesuraj Bandekar, Shinji Watanabe, Prasanta Kumar Ghosh
    - Citation Key: `arxiv_2610_00735`

    **KaTeX Formula**:
    $$
    LAAI = LMSE + LPCC
    $$

    Args:
        C (float): Input parameter `C`.
        E (float): Input parameter `E`.
        L (float): Input parameter `L`.
        M (float): Input parameter `M`.
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.

    Returns:
        float: Calculated metric value.
    """
    return float(L * (P * (C * C)) + L * (M * (E * S)))


def expr_l_a_a_i_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_a_a_i_form_6`."""
    return pl.col("L") * (pl.col("P") * (pl.col("C") * pl.col("C"))) + pl.col("L") * (
        pl.col("M") * (pl.col("E") * pl.col("S"))
    )


def calc_val_2609_39852_form_9(m: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_39852.

    **Source**:
    - Title: Pitch Smoothing Using Relative Interval Networks (2026)
    - Authors: Chin-Yun Yu, Chi-Jen Peng, Li Su et al.
    - Citation Key: `arxiv_2609_39852`

    **KaTeX Formula**:
    $$
    rm,τ [n] = max (0, ¯Xτ [n]⊤ ¯X-τ [n - m]) ,
    $$

    Args:
        m (float): Input parameter `m`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(m * r)


def expr_val_2609_39852_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_39852_form_9`."""
    return pl.col("m") * pl.col("r")


def calc_val_2609_38730_form_b(X: float, e: float, i: float, n: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    Xinv e,s = F(e) s:s+L, Yinv e,s =U(e) s+L:s+L+H ,
    $$

    Args:
        X (float): Input parameter `X`.
        e (float): Input parameter `e`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(X * e * i * n * v)


def expr_val_2609_38730_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_38730_form_b`."""
    return pl.col("X") * pl.col("e") * pl.col("i") * pl.col("n") * pl.col("v")


def calc_val_2609_38730_form_5(X: float, de: float, f: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    Xfwd e,s =U(e) s:s+L, Yfwd e,s = F(e) s+L:s+L+H .
    $$

    Args:
        X (float): Input parameter `X`.
        de (float): Input parameter `de`.
        f (float): Input parameter `f`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(X * de * f * w)


def expr_val_2609_38730_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_38730_form_5`."""
    return pl.col("X") * pl.col("de") * pl.col("f") * pl.col("w")


def calc_val_2609_38730_form_c(h: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    h1, . . . , hL = GRUθt ( ˜Fs:s+L) , ˜Fs:s+L ∈ RL\times df ,
    $$

    Args:
        h (float): Input parameter `h`.

    Returns:
        float: Calculated metric value.
    """
    return float(h)


def expr_val_2609_38730_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_38730_form_c`."""
    return pl.col("h")


def calc_z_form_4(c: float, e: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    z = vec ([Re(ZK), Im(ZK)]) ∈ R2Kdf .
    $$

    Args:
        c (float): Input parameter `c`.
        e (float): Input parameter `e`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(c * e * v)


def expr_z_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_form_4`."""
    return pl.col("c") * pl.col("e") * pl.col("v")


def calc_l_v_a_l_form_4(L: float, i: float, k: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    Lval = Lkin,val + λF Lforce,val,
    $$

    Args:
        L (float): Input parameter `L`.
        i (float): Input parameter `i`.
        k (float): Input parameter `k`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(L * i * k * n)


def expr_l_v_a_l_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_v_a_l_form_4`."""
    return pl.col("L") * pl.col("i") * pl.col("k") * pl.col("n")


def calc_val_2609_38730_form_9(
    R: float, b: float, de: float, ds: float, n: float, o: float, u: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    Rbounded s,h,c = br tanh (Rraw s,h,c )
    $$

    Args:
        R (float): Input parameter `R`.
        b (float): Input parameter `b`.
        de (float): Input parameter `de`.
        ds (float): Input parameter `ds`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(R * b * de * ds * n * o * u)


def expr_val_2609_38730_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_38730_form_9`."""
    return (
        pl.col("R")
        * pl.col("b")
        * pl.col("de")
        * pl.col("ds")
        * pl.col("n")
        * pl.col("o")
        * pl.col("u")
    )


def calc_e_r_e_c_n_o_form_c(a: float, m: float, s: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    erecon = max s,h,c ∣∣∣ ̂ Us,h,c - ̂ U base s,h,c - ∆ ̂ Us,h,c ∣∣∣ .
    $$

    Args:
        a (float): Input parameter `a`.
        m (float): Input parameter `m`.
        s (float): Input parameter `s`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * m * s * x)


def expr_e_r_e_c_n_o_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_r_e_c_n_o_form_c`."""
    return pl.col("a") * pl.col("m") * pl.col("s") * pl.col("x")


def calc_e_b_a_e_s_form_3(s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    Ebase = Es,h,c [(Us,h,c - ̂ U base s,h,c)2] ,
    $$

    Args:
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e * s)


def expr_e_b_a_e_s_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_b_a_e_s_form_3`."""
    return math.e * pl.col("s")


def calc_e_f_i_n_a_l_form_e(s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    Efinal = Es,h,c [(Us,h,c - ̂ Us,h,c)2] .
    $$

    Args:
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e * s)


def expr_e_f_i_n_a_l_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_f_i_n_a_l_form_e`."""
    return math.e * pl.col("s")


def calc_g_s_p_e_c_t_r_a_l_form_5(
    a: float, b: float, e: float, f: float, i: float, l: float, n: float, s: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    Gspectral = 100 Ebase - Efinal Ebase .
    $$

    Args:
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        e (float): Input parameter `e`.
        f (float): Input parameter `f`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        n (float): Input parameter `n`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(-(a**2) * b * e * f * i * l * n * s * math.exp(2) + 100 * math.e * a * b * e * s)


def expr_g_s_p_e_c_t_r_a_l_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_s_p_e_c_t_r_a_l_form_5`."""
    return -(pl.col("a") ** 2) * pl.col("b") * pl.col("e") * pl.col("f") * pl.col("i") * pl.col(
        "l"
    ) * pl.col("n") * pl.col("s") * math.exp(2) + 100 * math.e * pl.col("a") * pl.col("b") * pl.col(
        "e"
    ) * pl.col("s")


def calc_val_2609_38730_form_2(h: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    rh,c = Es [∣∣∣∆ ̂ Us,h,c ∣∣∣] Es [∣∣∣ ̂ U base s,h,c ∣∣∣] + ϵ ,
    $$

    Args:
        h (float): Input parameter `h`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(h * r)


def expr_val_2609_38730_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_38730_form_2`."""
    return pl.col("h") * pl.col("r")


def calc_val_2609_38730_form_3(S: float, h: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    Sh,c = Es [Ss,h,c] ,
    $$

    Args:
        S (float): Input parameter `S`.
        h (float): Input parameter `h`.

    Returns:
        float: Calculated metric value.
    """
    return float(S * h)


def expr_val_2609_38730_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_38730_form_3`."""
    return pl.col("S") * pl.col("h")


def calc_l_f_m_form_8(t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_28906.

    **Source**:
    - Title: ReaFlow-TTS: Realization-Conditioned Flow Matching for High-Quality and Controllable Speech Synthesis (2026)
    - Authors: Junyi Zhao, Yihao Qin, Changsheng Ma
    - Citation Key: `arxiv_2609_28906`

    **KaTeX Formula**:
    $$
    LFM = Et,x0,x1 [∥vθ(xt, t) - v(x0, x1, t)∥22 ] .
    $$

    Args:
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e * t)


def expr_l_f_m_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_f_m_form_8`."""
    return math.e * pl.col("t")


def calc_l_b_a_e_s_form_a(c: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_28906.

    **Source**:
    - Title: ReaFlow-TTS: Realization-Conditioned Flow Matching for High-Quality and Controllable Speech Synthesis (2026)
    - Authors: Junyi Zhao, Yihao Qin, Changsheng Ma
    - Citation Key: `arxiv_2609_28906`

    **KaTeX Formula**:
    $$
    Lbase = Ec,t,x0,x1 [Ez∼qψ(z|x1) [∥vθ(xt, t, c, z) - v∥22 ] +βDKL(qψ(z | x1) ∥p(z)) ].
    $$

    Args:
        c (float): Input parameter `c`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e * c)


def expr_l_b_a_e_s_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_b_a_e_s_form_a`."""
    return math.e * pl.col("c")


def calc_val_2609_20558_form_f(L: float, e: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_20558.

    **Source**:
    - Title: Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction (2026)
    - Authors: Songyang Liu, Shuai Li
    - Citation Key: `arxiv_2609_20558`

    **KaTeX Formula**:
    $$
    Let
    $$

    Args:
        L (float): Input parameter `L`.
        e (float): Input parameter `e`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(L * e * t)


def expr_val_2609_20558_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_20558_form_f`."""
    return pl.col("L") * pl.col("e") * pl.col("t")


def calc_p_u_form_5(a: float, h: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_17701.

    **Source**:
    - Title: Barrier Functions Against Safety Drift in Shared Control (2026)
    - Authors: M. Yusuf Uzun, Yildiray Yildiz
    - Citation Key: `arxiv_2609_17701`

    **KaTeX Formula**:
    $$
    up = yh + ya,
    $$

    Args:
        a (float): Input parameter `a`.
        h (float): Input parameter `h`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * y + h * y)


def expr_p_u_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_u_form_5`."""
    return pl.col("a") * pl.col("y") + pl.col("h") * pl.col("y")


def calc_y_r_s_h_s_y_p_s_form_1(T: float, k: float, p: float, s: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_17701.

    **Source**:
    - Title: Barrier Functions Against Safety Drift in Shared Control (2026)
    - Authors: M. Yusuf Uzun, Yildiray Yildiz
    - Citation Key: `arxiv_2609_17701`

    **KaTeX Formula**:
    $$
    Yh(s) R(s) - Yp(s) = kp Tps + 1 Tz s + 1 ,
    $$

    Args:
        T (float): Input parameter `T`.
        k (float): Input parameter `k`.
        p (float): Input parameter `p`.
        s (float): Input parameter `s`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(T * k * p**2 * s + T * s * z + 1)


def expr_y_r_s_h_s_y_p_s_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_y_r_s_h_s_y_p_s_form_1`."""
    return (
        pl.col("T") * pl.col("k") * pl.col("p") ** 2 * pl.col("s")
        + pl.col("T") * pl.col("s") * pl.col("z")
        + 1
    )


def calc_h_y_form_2(c: float, dh: float, h: float, p: float, r: float, x: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_17701.

    **Source**:
    - Title: Barrier Functions Against Safety Drift in Shared Control (2026)
    - Authors: M. Yusuf Uzun, Yildiray Yildiz
    - Citation Key: `arxiv_2609_17701`

    **KaTeX Formula**:
    $$
    yh = ch xh + dh(r - yp), (10b)
    $$

    Args:
        c (float): Input parameter `c`.
        dh (float): Input parameter `dh`.
        h (float): Input parameter `h`.
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(c * h**2 * x + dh * (-p * y + r))


def expr_h_y_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_y_form_2`."""
    return pl.col("c") * pl.col("h") ** 2 * pl.col("x") + pl.col("dh") * (
        -pl.col("p") * pl.col("y") + pl.col("r")
    )


def calc_val_2609_17701_form_8(b: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_17701.

    **Source**:
    - Title: Barrier Functions Against Safety Drift in Shared Control (2026)
    - Authors: M. Yusuf Uzun, Yildiray Yildiz
    - Citation Key: `arxiv_2609_17701`

    **KaTeX Formula**:
    $$
    b1(x, wL, ρ) = wp(x, ρ) - wL(t), (16a)
    $$

    Args:
        b (float): Input parameter `b`.

    Returns:
        float: Calculated metric value.
    """
    return float(b)


def expr_val_2609_17701_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_17701_form_8`."""
    return pl.col("b")


def calc_val_2609_17701_form_3(b: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_17701.

    **Source**:
    - Title: Barrier Functions Against Safety Drift in Shared Control (2026)
    - Authors: M. Yusuf Uzun, Yildiray Yildiz
    - Citation Key: `arxiv_2609_17701`

    **KaTeX Formula**:
    $$
    b2(x, wU , ρ) = wU (t) - wp(x, ρ), (16b)
    $$

    Args:
        b (float): Input parameter `b`.

    Returns:
        float: Calculated metric value.
    """
    return float(2 * b)


def expr_val_2609_17701_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_17701_form_3`."""
    return 2 * pl.col("b")


def calc_l_0_p_w_form_0(y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_17701.

    **Source**:
    - Title: Barrier Functions Against Safety Drift in Shared Control (2026)
    - Authors: M. Yusuf Uzun, Yildiray Yildiz
    - Citation Key: `arxiv_2609_17701`

    **KaTeX Formula**:
    $$
    L0wp = 2 y0 y1 + 2 y1 y2, (22a)
    $$

    Args:
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(4 * y**2)


def expr_l_0_p_w_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_0_p_w_form_0`."""
    return 4 * pl.col("y") ** 2


def calc_l_g_a_p_w_form_8(A: float, B: float, H: float, a: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_17701.

    **Source**:
    - Title: Barrier Functions Against Safety Drift in Shared Control (2026)
    - Authors: M. Yusuf Uzun, Yildiray Yildiz
    - Citation Key: `arxiv_2609_17701`

    **KaTeX Formula**:
    $$
    Lga wp = 2 y1 (HABya ), (22b)
    $$

    Args:
        A (float): Input parameter `A`.
        B (float): Input parameter `B`.
        H (float): Input parameter `H`.
        a (float): Input parameter `a`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(2 * A * B * H * a * y**2)


def expr_l_g_a_p_w_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_g_a_p_w_form_8`."""
    return 2 * pl.col("A") * pl.col("B") * pl.col("H") * pl.col("a") * pl.col("y") ** 2


def calc_a_t_w_o_w_a_o_form_9(S: float, T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_17701.

    **Source**:
    - Title: Barrier Functions Against Safety Drift in Shared Control (2026)
    - Authors: M. Yusuf Uzun, Yildiray Yildiz
    - Citation Key: `arxiv_2609_17701`

    **KaTeX Formula**:
    $$
    ATWo + WoA = -STS,
    $$

    Args:
        S (float): Input parameter `S`.
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(-S * S * T)


def expr_a_t_w_o_w_a_o_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_t_w_o_w_a_o_form_9`."""
    return -pl.col("S") * pl.col("S") * pl.col("T")


def calc_val_2609_17701_form_6(b: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_17701.

    **Source**:
    - Title: Barrier Functions Against Safety Drift in Shared Control (2026)
    - Authors: M. Yusuf Uzun, Yildiray Yildiz
    - Citation Key: `arxiv_2609_17701`

    **KaTeX Formula**:
    $$
    b3(x, ¯x) = η2 - eTWo e, e = x- ¯x,
    $$

    Args:
        b (float): Input parameter `b`.

    Returns:
        float: Calculated metric value.
    """
    return float(3 * b)


def expr_val_2609_17701_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_17701_form_6`."""
    return 3 * pl.col("b")


def calc_u_l_s_o_form_4(a: float, p: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_11476.

    **Source**:
    - Title: 3D Euler-Angle Orientation Control for Two-Ray Fading Mitigation in Maritime Air-to-Sea Communications (2026)
    - Authors: Mohammed Bajja, Abdoul Karim A. H. Saliah, Hajar El Hammouti et al.
    - Citation Key: `arxiv_2609_11476`

    **KaTeX Formula**:
    $$
    uLoS = ps -pa,0 ∥ps -pa,0∥ , uref = pim s -pa,0 ∥pim s -pa,0∥ .
    $$

    Args:
        a (float): Input parameter `a`.
        p (float): Input parameter `p`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(-a * p + p * s)


def expr_u_l_s_o_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_l_s_o_form_4`."""
    return -pl.col("a") * pl.col("p") + pl.col("p") * pl.col("s")


def calc_val_2609_11476_form_8(P: float, f: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_11476.

    **Source**:
    - Title: 3D Euler-Angle Orientation Control for Two-Ray Fading Mitigation in Maritime Air-to-Sea Communications (2026)
    - Authors: Mohammed Bajja, Abdoul Karim A. H. Saliah, Hajar El Hammouti et al.
    - Citation Key: `arxiv_2609_11476`

    **KaTeX Formula**:
    $$
    Proof. See Appendix B. ■
    $$

    Args:
        P (float): Input parameter `P`.
        f (float): Input parameter `f`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * f * o**2 * r)


def expr_val_2609_11476_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_11476_form_8`."""
    return pl.col("P") * pl.col("f") * pl.col("o") ** 2 * pl.col("r")


def calc_val_2609_11476_form_4(N: float, r: float, s: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_11476.

    **Source**:
    - Title: 3D Euler-Angle Orientation Control for Two-Ray Fading Mitigation in Maritime Air-to-Sea Communications (2026)
    - Authors: Mohammed Bajja, Abdoul Karim A. H. Saliah, Hajar El Hammouti et al.
    - Citation Key: `arxiv_2609_11476`

    **KaTeX Formula**:
    $$
    {ur}N-1 s.t. x0 = x(tk), (15b) xr+1 = hd(xr, ur), r = 0, . . . ,N -1, (15c)
    $$

    Args:
        N (float): Input parameter `N`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(N * (r * u) - 1 * s)


def expr_val_2609_11476_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_11476_form_4`."""
    return pl.col("N") * (pl.col("r") * pl.col("u")) - 1 * pl.col("s")


def calc_val_2608_26548_form_b(h: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_26548.

    **Source**:
    - Title: Camera Calibration Using Inaccurate and Asynchronous Discrete GPS Trajectory from Drones (2026)
    - Authors: R. Yang, Y. Bar-Shalom, H. A. J. Huang
    - Citation Key: `arxiv_2608_26548`

    **KaTeX Formula**:
    $$
    hi(\cdot ) = f {T(α, ϵ, ρ)[x(ti + τ ) - [0 0 ℏ]′ - xs ]} = f(xCi ) = xIi i = 1, . . . , n
    $$

    Args:
        h (float): Input parameter `h`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(h * i)


def expr_val_2608_26548_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_26548_form_b`."""
    return pl.col("h") * pl.col("i")


def calc_val_2608_26548_form_8(j: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_26548.

    **Source**:
    - Title: Camera Calibration Using Inaccurate and Asynchronous Discrete GPS Trajectory from Drones (2026)
    - Authors: R. Yang, Y. Bar-Shalom, H. A. J. Huang
    - Citation Key: `arxiv_2608_26548`

    **KaTeX Formula**:
    $$
    vj,i \le  32
    $$

    Args:
        j (float): Input parameter `j`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(j * v)


def expr_val_2608_26548_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_26548_form_8`."""
    return pl.col("j") * pl.col("v")


def calc_val_1610_03464_form_e(a: float, b: float, l: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1610_03464.

    **Source**:
    - Title: Oblique Collisions of Baseballs and Softballs with a Bat (2016)
    - Authors: Jeffrey R. Kensrud, Alan M. Nathan, Lloyd V. Smith
    - Citation Key: `arxiv_1610_03464`

    **KaTeX Formula**:
    $$
    vball,n = [ 1 + ey 1 + ry ] vbat,n ,
    $$

    Args:
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        l (float): Input parameter `l`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * b * l**2 * v)


def expr_val_1610_03464_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1610_03464_form_e`."""
    return pl.col("a") * pl.col("b") * pl.col("l") ** 2 * pl.col("v")


def calc_val_1610_03464_form_b(a: float, b: float, l: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1610_03464.

    **Source**:
    - Title: Oblique Collisions of Baseballs and Softballs with a Bat (2016)
    - Authors: Jeffrey R. Kensrud, Alan M. Nathan, Lloyd V. Smith
    - Citation Key: `arxiv_1610_03464`

    **KaTeX Formula**:
    $$
    vball,t + rω = [ 1 + ex 1 + rx ] vbat,t ,
    $$

    Args:
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        l (float): Input parameter `l`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * b * l**2 * v)


def expr_val_1610_03464_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1610_03464_form_b`."""
    return pl.col("a") * pl.col("b") * pl.col("l") ** 2 * pl.col("v")


def calc_r_s_form_6(
    N: float, a: float, c: float, e: float, l: float, s: float, u: float, v: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29142.

    **Source**:
    - Title: State-Dependent Objective Coordination for End-to-End Balance and Navigation (2026)
    - Authors: Xuhao Huang, Xitao Xu, Yuxin Zheng et al.
    - Citation Key: `arxiv_2610_29142`

    **KaTeX Formula**:
    $$
    SR = Nsucc Neval .
    $$

    Args:
        N (float): Input parameter `N`.
        a (float): Input parameter `a`.
        c (float): Input parameter `c`.
        e (float): Input parameter `e`.
        l (float): Input parameter `l`.
        s (float): Input parameter `s`.
        u (float): Input parameter `u`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(N * (s * (u * (c * (c * (N * (e * (v * (a * l)))))))))


def expr_r_s_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_s_form_6`."""
    return pl.col("N") * (
        pl.col("s")
        * (
            pl.col("u")
            * (
                pl.col("c")
                * (
                    pl.col("c")
                    * (pl.col("N") * (pl.col("e") * (pl.col("v") * (pl.col("a") * pl.col("l")))))
                )
            )
        )
    )


def calc_val_2610_18361_form_d(J: float, N: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_18361.

    **Source**:
    - Title: Adaptive Handling of Deadline Misses via Stochastic MPC (2026)
    - Authors: Melanie Gallant, Paolo Pazzaglia, Christoph Mark et al.
    - Citation Key: `arxiv_2610_18361`

    **KaTeX Formula**:
    $$
    JN (x\cdot |k, u\cdot |k, T (θ(k), d(k))) = ∑ ℓ∈N θ(k),d(k) 0:N-1 pℓl(xℓ|k, uℓ|k) + ∑ ℓ∈N θ(k),d(k) N pℓJ f (xℓ|k, θℓ),
    $$

    Args:
        J (float): Input parameter `J`.
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(J * N)


def expr_val_2610_18361_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_18361_form_d`."""
    return pl.col("J") * pl.col("N")


def calc_val_2609_24299_form_6(x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    x, y, z Rx(ϕ) ---→ x′ , y′ , z ′ Rz(θ) ---→ x′′ , y′′ , z ′′ .
    $$

    Args:
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(x)


def expr_val_2609_24299_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_24299_form_6`."""
    return pl.col("x")


def calc_l_form_9(T: float, V: float, a: float, b: float, c: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    L = Tc + Tw + Tb + Ta - (Vc + Vw + Vb + Va).
    $$

    Args:
        T (float): Input parameter `T`.
        V (float): Input parameter `V`.
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        c (float): Input parameter `c`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(T * a + T * b + T * c + T * w - V * a - V * b - V * c - V * w)


def expr_l_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_form_9`."""
    return (
        pl.col("T") * pl.col("a")
        + pl.col("T") * pl.col("b")
        + pl.col("T") * pl.col("c")
        + pl.col("T") * pl.col("w")
        - pl.col("V") * pl.col("a")
        - pl.col("V") * pl.col("b")
        - pl.col("V") * pl.col("c")
        - pl.col("V") * pl.col("w")
    )


def calc_val_2609_24299_form_c(i: float, m: float, n: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    min u(\cdot ) J = ∫ tk+T tk (qs(s - sf)2 + qϕϕ2 + qθθ2 + ˙ηTQη ˙η + q˙s( ˙s - ˙sref)2 + q ˙ϕ ˙ϕ2 + q ˙ θ ˙ θ2 + uTRuu) dt + (x(tk + T ) - xf )TPf (x(tk + T ) - xf ) s.t. ˙x(t) = ¯ f(x(t), u(t)), x(tk) = xk, τ min w \le  τw(t) \le  τ max w , τ min a \le  τa(t) \le  τ max a , 0 \le  s(t) \le  L, |ϕ(t)| \le  ϕmax, |θ(t)| \le  θmax.
    $$

    Args:
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(i * m * n * u)


def expr_val_2609_24299_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_24299_form_c`."""
    return pl.col("i") * pl.col("m") * pl.col("n") * pl.col("u")


def calc_m_q_q_form_5(
    M: float, N: float, T: float, c: float, m: float, u: float, v: float, w: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    Mqq =Mc +muN T v Nv + mu N T w Nw, Mqs = mu N T v νv +muN T w νw, Msq =MT qs , Mqϕ = -[(mur sin ϕ + mabh sin ϕ cos θ)N T v - (mur cos ϕ + mabh cos ϕ cos θ)N T w ], Mϕq =M T qϕ , Mqθ = -[(mabh cos ϕ sin θ)N T v + (mabh sinϕsinθ)N T w ], Mθq =MT qθ , Mss = mu + muν 2 v +muν 2w + Iwz r2 , Msϕ = -[(mur sinϕ+mabh sinϕcos θ)νv - (mur cosϕ+mabhcosϕcos θ)νw ], Mϕs =Msϕ, Msθ = -[mabhcos θ + (mabhcosϕsinθ)νv + (mabh sinϕsinθ)νw ], Mθs =Msθ, Mϕϕ = mur2 + Iwx + Iax + (Ibx + mabh2) cos2 θ + Iby sin2 θ + 2mabhr cos θ, Mϕγ = Iax, Mγϕ = Iax, Mθθ = mabh2 + Ibz + Iaz, Mγγ = Iax.
    $$

    Args:
        M (float): Input parameter `M`.
        N (float): Input parameter `N`.
        T (float): Input parameter `T`.
        c (float): Input parameter `c`.
        m (float): Input parameter `m`.
        u (float): Input parameter `u`.
        v (float): Input parameter `v`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(
        m * (u * (N * (T * (w * (N * w))))) + (M * c + m * (u * (N * (T * (v * (N * v))))))
    )


def expr_m_q_q_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_q_q_form_5`."""
    return pl.col("m") * (
        pl.col("u") * (pl.col("N") * (pl.col("T") * (pl.col("w") * (pl.col("N") * pl.col("w")))))
    ) + (
        pl.col("M") * pl.col("c")
        + pl.col("m")
        * (
            pl.col("u")
            * (pl.col("N") * (pl.col("T") * (pl.col("v") * (pl.col("N") * pl.col("v")))))
        )
    )


def calc_c_p_form_a(P: float, U: float, i: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_05500.

    **Source**:
    - Title: Performance comparison of tethered and self-propelled models of fish locomotion using unsteady thin airfoil theory (2026)
    - Authors: Anshul Nayak, Emad Masroor, Hodjat Pendar
    - Citation Key: `arxiv_2609_05500`

    **KaTeX Formula**:
    $$
    CP = Pin 12 U 3 0 ,
    $$

    Args:
        P (float): Input parameter `P`.
        U (float): Input parameter `U`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(360 * P * U * i * n)


def expr_c_p_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_p_form_a`."""
    return 360 * pl.col("P") * pl.col("U") * pl.col("i") * pl.col("n")


def calc_c_t_form_0(T: float, U: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_05500.

    **Source**:
    - Title: Performance comparison of tethered and self-propelled models of fish locomotion using unsteady thin airfoil theory (2026)
    - Authors: Anshul Nayak, Emad Masroor, Hodjat Pendar
    - Citation Key: `arxiv_2609_05500`

    **KaTeX Formula**:
    $$
    CT = T 12 U 2 0
    $$

    Args:
        T (float): Input parameter `T`.
        U (float): Input parameter `U`.

    Returns:
        float: Calculated metric value.
    """
    return float(240 * T * U)


def expr_c_t_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_t_form_0`."""
    return 240 * pl.col("T") * pl.col("U")


def calc_val_2609_05500_form_4(C: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_05500.

    **Source**:
    - Title: Performance comparison of tethered and self-propelled models of fish locomotion using unsteady thin airfoil theory (2026)
    - Authors: Anshul Nayak, Emad Masroor, Hodjat Pendar
    - Citation Key: `arxiv_2609_05500`

    **KaTeX Formula**:
    $$
    Cp,pitch = Mz ˙ θ 12 U 3 0 , Cp,heave = Fy ˙h 12 U 3 0
    $$

    Args:
        C (float): Input parameter `C`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(C * p)


def expr_val_2609_05500_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_05500_form_4`."""
    return pl.col("C") * pl.col("p")


def calc_val_2608_27423_form_9(R: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_27423.

    **Source**:
    - Title: High-order stabilized matrix-free simulation of rotating mixing devices using the Mortar Element Method (2026)
    - Authors: B. Campos, P. Munch, V. O. Ferreira et al.
    - Citation Key: `arxiv_2608_27423`

    **KaTeX Formula**:
    $$
    R := [cos[θ(t)] -sin[θ(t)] sin[θ(t)] cos[θ(t)] ] ;
    $$

    Args:
        R (float): Input parameter `R`.

    Returns:
        float: Calculated metric value.
    """
    return float(R)


def expr_val_2608_27423_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_27423_form_9`."""
    return pl.col("R")


def calc_val_2608_27423_form_0(R: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_27423.

    **Source**:
    - Title: High-order stabilized matrix-free simulation of rotating mixing devices using the Mortar Element Method (2026)
    - Authors: B. Campos, P. Munch, V. O. Ferreira et al.
    - Citation Key: `arxiv_2608_27423`

    **KaTeX Formula**:
    $$
    R := cos[θ(t)] I + sin[θ(t)] W + (1 - cos[θ(t)]) r ⊗ r
    $$

    Args:
        R (float): Input parameter `R`.

    Returns:
        float: Calculated metric value.
    """
    return float(R)


def expr_val_2608_27423_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_27423_form_0`."""
    return pl.col("R")


def calc_l_form_c(L: float, a: float, de: float, i: float, l: float, m: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_27423.

    **Source**:
    - Title: High-order stabilized matrix-free simulation of rotating mixing devices using the Mortar Element Method (2026)
    - Authors: B. Campos, P. Munch, V. O. Ferreira et al.
    - Citation Key: `arxiv_2608_27423`

    **KaTeX Formula**:
    $$
    L = mmax Lideal .
    $$

    Args:
        L (float): Input parameter `L`.
        a (float): Input parameter `a`.
        de (float): Input parameter `de`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(L * a**2 * de * i * l * m**2 * x)


def expr_l_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_form_c`."""
    return (
        pl.col("L")
        * pl.col("a") ** 2
        * pl.col("de")
        * pl.col("i")
        * pl.col("l")
        * pl.col("m") ** 2
        * pl.col("x")
    )


def calc_val_2608_10387_form_d(dx: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    dx := dcosϕd
    $$

    Args:
        dx (float): Input parameter `dx`.

    Returns:
        float: Calculated metric value.
    """
    return float(dx)


def expr_val_2608_10387_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_10387_form_d`."""
    return pl.col("dx")


def calc_val_2608_10387_form_9(q: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    qs := [r, θ, ˙r, ˙ θ]T ∈ S := T(R+ \times  S1 ) (5a)
    $$

    Args:
        q (float): Input parameter `q`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(q * s)


def expr_val_2608_10387_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_10387_form_9`."""
    return pl.col("q") * pl.col("s")


def calc_val_2608_10387_form_2(a: float, q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    qa := [ϕ, ˙ϕ, ¯ τ]T ∈ A := TS1 \times R (5b)
    $$

    Args:
        a (float): Input parameter `a`.
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * q)


def expr_val_2608_10387_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_10387_form_2`."""
    return pl.col("a") * pl.col("q")


def calc_val_2608_10387_form_1(a: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    ar := √ ˙r2 + (r0 - r)2ω2 r .
    $$

    Args:
        a (float): Input parameter `a`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * r)


def expr_val_2608_10387_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_10387_form_1`."""
    return pl.col("a") * pl.col("r")


def calc_val_2608_10387_form_4(x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    x := [δ, a]T = hω(y) = [σ1 - ∆(ω)ψ a ]
    $$

    Args:
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(x)


def expr_val_2608_10387_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_10387_form_4`."""
    return pl.col("x")


def calc_val_2608_10387_form_a(R: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    R1 := tan3 (γψd e ) sec2 (γψd e )(8αδθ m¯ τ-b2 δeker0 cos2 (γψd e ) cot3 (γψd e )) b2r0 R2 := -4a2e b3 ¯ τ cos4 (γψd e ) cot2 (γψd e )+πa2e b4 r0ωr cos4 (γψd e ) cot3 (γψd e ) 16m¯ τ3ωr - 4b2 δeker0 ¯ τ 2 ωr cos2 (γψd e ) cot3 (γψd e ) 16m¯ τ3ωr - 4πb2 r0 ¯ τ 2 ωr cos2 (γψd e ) cot(γψd e )+16b¯ τ 3 cos2 (γψd e )+32αδθm¯ τ 3 ωr 16m¯ τ3ωr
    $$

    Args:
        R (float): Input parameter `R`.

    Returns:
        float: Calculated metric value.
    """
    return float(R)


def expr_val_2608_10387_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_10387_form_a`."""
    return pl.col("R")


def calc_val_2608_10387_form_3(A: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    A1 := 8mα¯ τ ∗ sec2 γψd e tan3 γψd e b2 r0 A2 := -bker0 cos2 γψd e cot3 γψd e 4m¯ τ ∗ A3 := b2 cos3 γψd e cot γψd e (-4¯ τ ∗ + bπr0ωr cot γψd e ) 4m(¯ τ ∗ )2ωr .
    $$

    Args:
        A (float): Input parameter `A`.

    Returns:
        float: Calculated metric value.
    """
    return float(A)


def expr_val_2608_10387_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_10387_form_3`."""
    return pl.col("A")


def calc_ds_dw_form_d(D: float, L: float, i: float, k: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_30305.

    **Source**:
    - Title: Exact turning invariants for projectile motion under quadratic drag and a vertical-axis Magnus force (2026)
    - Authors: Pragyaan Gaur
    - Citation Key: `arxiv_2609_30305`

    **KaTeX Formula**:
    $$
    dw ds = (ikL - kD ) w, so that w(s) = w0 e-(kD-ikL)s .
    $$

    Args:
        D (float): Input parameter `D`.
        L (float): Input parameter `L`.
        i (float): Input parameter `i`.
        k (float): Input parameter `k`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(w * (-D * k + L * i * k))


def expr_ds_dw_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_ds_dw_form_d`."""
    return pl.col("w") * (-pl.col("D") * pl.col("k") + pl.col("L") * pl.col("i") * pl.col("k"))


def calc_w_form_a(i: float, v: float, x: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_30305.

    **Source**:
    - Title: Exact turning invariants for projectile motion under quadratic drag and a vertical-axis Magnus force (2026)
    - Authors: Pragyaan Gaur
    - Citation Key: `arxiv_2609_30305`

    **KaTeX Formula**:
    $$
    w = vx + ivy.
    $$

    Args:
        i (float): Input parameter `i`.
        v (float): Input parameter `v`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(i * v * y + v * x)


def expr_w_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_form_a`."""
    return pl.col("i") * pl.col("v") * pl.col("y") + pl.col("v") * pl.col("x")


def calc_dt_dw_form_f(D: float, L: float, i: float, k: float, v: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_30305.

    **Source**:
    - Title: Exact turning invariants for projectile motion under quadratic drag and a vertical-axis Magnus force (2026)
    - Authors: Pragyaan Gaur
    - Citation Key: `arxiv_2609_30305`

    **KaTeX Formula**:
    $$
    dw dt = (ikL -kD ) |v|w.
    $$

    Args:
        D (float): Input parameter `D`.
        L (float): Input parameter `L`.
        i (float): Input parameter `i`.
        k (float): Input parameter `k`.
        v (float): Input parameter `v`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(w * (-D * k + L * i * k) * abs(v))


def expr_dt_dw_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_dt_dw_form_f`."""
    return (
        pl.col("w")
        * (-pl.col("D") * pl.col("k") + pl.col("L") * pl.col("i") * pl.col("k"))
        * abs(pl.col("v"))
    )


def calc_j_form_5(C: float, d: float, l: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_23163.

    **Source**:
    - Title: Spinning Quadrotor: Hover Thrust Augmentation with Passive Lifting Surfaces (2026)
    - Authors: Aniketh Parkala, Harikumar Kandath
    - Citation Key: `arxiv_2608_23163`

    **KaTeX Formula**:
    $$
    J = 0.50 Cl Cd + 0.30 Cl + 0.20 Cp,min
    $$

    Args:
        C (float): Input parameter `C`.
        d (float): Input parameter `d`.
        l (float): Input parameter `l`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(0.5 * C**2 * d * l + 0.3 * C * l + 0.2 * C * p)


def expr_j_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_form_5`."""
    return (
        0.5 * pl.col("C") ** 2 * pl.col("d") * pl.col("l")
        + 0.3 * pl.col("C") * pl.col("l")
        + 0.2 * pl.col("C") * pl.col("p")
    )


def calc_val_2608_23163_form_e(T: float, m: float, o: float, r: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_23163.

    **Source**:
    - Title: Spinning Quadrotor: Hover Thrust Augmentation with Passive Lifting Surfaces (2026)
    - Authors: Aniketh Parkala, Harikumar Kandath
    - Citation Key: `arxiv_2608_23163`

    **KaTeX Formula**:
    $$
    Tmotor,vert + Lwing = W.
    $$

    Args:
        T (float): Input parameter `T`.
        m (float): Input parameter `m`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(T * m * o**2 * r * t)


def expr_val_2608_23163_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_23163_form_e`."""
    return pl.col("T") * pl.col("m") * pl.col("o") ** 2 * pl.col("r") * pl.col("t")


def calc_val_2608_23163_form_a(i: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_23163.

    **Source**:
    - Title: Spinning Quadrotor: Hover Thrust Augmentation with Passive Lifting Surfaces (2026)
    - Authors: Aniketh Parkala, Harikumar Kandath
    - Citation Key: `arxiv_2608_23163`

    **KaTeX Formula**:
    $$
    vi,motor = √ Tmotor,vert 2ρAmotor ,
    $$

    Args:
        i (float): Input parameter `i`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(i * v)


def expr_val_2608_23163_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_23163_form_a`."""
    return pl.col("i") * pl.col("v")


def calc_val_2608_23163_form_1(P: float, m: float, o: float, r: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_23163.

    **Source**:
    - Title: Spinning Quadrotor: Hover Thrust Augmentation with Passive Lifting Surfaces (2026)
    - Authors: Aniketh Parkala, Harikumar Kandath
    - Citation Key: `arxiv_2608_23163`

    **KaTeX Formula**:
    $$
    Pmotor,thrust = Tmotor,vert vi,motor ηm ,
    $$

    Args:
        P (float): Input parameter `P`.
        m (float): Input parameter `m`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * m * o**2 * r * t)


def expr_val_2608_23163_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_23163_form_1`."""
    return pl.col("P") * pl.col("m") * pl.col("o") ** 2 * pl.col("r") * pl.col("t")


def calc_val_2608_23163_form_3(P: float, m: float, o: float, r: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_23163.

    **Source**:
    - Title: Spinning Quadrotor: Hover Thrust Augmentation with Passive Lifting Surfaces (2026)
    - Authors: Aniketh Parkala, Harikumar Kandath
    - Citation Key: `arxiv_2608_23163`

    **KaTeX Formula**:
    $$
    Pmotor,yaw = τmotor ω ηm ,
    $$

    Args:
        P (float): Input parameter `P`.
        m (float): Input parameter `m`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * m * o**2 * r * t)


def expr_val_2608_23163_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_23163_form_3`."""
    return pl.col("P") * pl.col("m") * pl.col("o") ** 2 * pl.col("r") * pl.col("t")


def calc_p_b_a_s_e_l_i_e_n_form_9(W: float, i: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_23163.

    **Source**:
    - Title: Spinning Quadrotor: Hover Thrust Augmentation with Passive Lifting Surfaces (2026)
    - Authors: Aniketh Parkala, Harikumar Kandath
    - Citation Key: `arxiv_2608_23163`

    **KaTeX Formula**:
    $$
    Pbaseline = W vi,baseline ηm , vi,baseline = √ W 2ρAmotor ,
    $$

    Args:
        W (float): Input parameter `W`.
        i (float): Input parameter `i`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(W * i * v)


def expr_p_b_a_s_e_l_i_e_n_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_b_a_s_e_l_i_e_n_form_9`."""
    return pl.col("W") * pl.col("i") * pl.col("v")


def calc_val_2608_08157_form_8(s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_08157.

    **Source**:
    - Title: Event-Time Hybrid Optimal Control for Robotic Table Tennis Serves (2026)
    - Authors: Thomas Gossard, Till Köpff, Andreas Ziegler
    - Citation Key: `arxiv_2608_08157`

    **KaTeX Formula**:
    $$
    s.t. eTz pwb (tflight) = 0,
    $$

    Args:
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(s)


def expr_val_2608_08157_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_08157_form_8`."""
    return pl.col("s")


def calc_val_2608_08157_form_a(T: float, n: float, r: float, v: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_08157.

    **Source**:
    - Title: Event-Time Hybrid Optimal Control for Robotic Table Tennis Serves (2026)
    - Authors: Thomas Gossard, Till Köpff, Andreas Ziegler
    - Citation Key: `arxiv_2608_08157`

    **KaTeX Formula**:
    $$
    nTr vw r \ge  0,
    $$

    Args:
        T (float): Input parameter `T`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.
        v (float): Input parameter `v`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float((T * n * r**2 * v * w >= 0))


def expr_val_2608_08157_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_08157_form_a`."""
    return pl.col("T") * pl.col("n") * pl.col("r") ** 2 * pl.col("v") * pl.col("w") >= 0


def calc_val_2608_08157_form_d(
    b: float, c: float, e: float, i: float, m: float, n: float, o: float, t: float, u: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_08157.

    **Source**:
    - Title: Event-Time Hybrid Optimal Control for Robotic Table Tennis Serves (2026)
    - Authors: Thomas Gossard, Till Köpff, Andreas Ziegler
    - Citation Key: `arxiv_2608_08157`

    **KaTeX Formula**:
    $$
    min tbounce, tnet, tflight, ϕwr , vw r β0 ∥vw r ∥22 +β1 ∥∥ωw+ b -ωtarget∥∥22 + β2 ∥pwb (tflight) - ptarget∥22 + β3tflight
    $$

    Args:
        b (float): Input parameter `b`.
        c (float): Input parameter `c`.
        e (float): Input parameter `e`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        t (float): Input parameter `t`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(b * c * e * i * m * n**2 * o * t * u)


def expr_val_2608_08157_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_08157_form_d`."""
    return (
        pl.col("b")
        * pl.col("c")
        * pl.col("e")
        * pl.col("i")
        * pl.col("m")
        * pl.col("n") ** 2
        * pl.col("o")
        * pl.col("t")
        * pl.col("u")
    )


def calc_val_2608_08157_form_6(s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_08157.

    **Source**:
    - Title: Event-Time Hybrid Optimal Control for Robotic Table Tennis Serves (2026)
    - Authors: Thomas Gossard, Till Köpff, Andreas Ziegler
    - Citation Key: `arxiv_2608_08157`

    **KaTeX Formula**:
    $$
    s.t. eTz pwb (tbounce) = 0,
    $$

    Args:
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(s)


def expr_val_2608_08157_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_08157_form_6`."""
    return pl.col("s")


def calc_val_2608_08157_form_1(s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_08157.

    **Source**:
    - Title: Event-Time Hybrid Optimal Control for Robotic Table Tennis Serves (2026)
    - Authors: Thomas Gossard, Till Köpff, Andreas Ziegler
    - Citation Key: `arxiv_2608_08157`

    **KaTeX Formula**:
    $$
    s.t. x0 = xinit,
    $$

    Args:
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(s)


def expr_val_2608_08157_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_08157_form_1`."""
    return pl.col("s")


def calc_a_l_r_form_a(L: float, R: float, a: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_08746.

    **Source**:
    - Title: Kinematics of Single-Winged Spinning Seeds: A Study on Mahogany and Buddha Coconut Samaras (2026)
    - Authors: Yogeshwaran G, Srisha M. V. Rao, Jagadeesh G
    - Citation Key: `arxiv_2603_08746`

    **KaTeX Formula**:
    $$
    ALR = [ aLR 1 aLR 2 aLR 3 ]
    $$

    Args:
        L (float): Input parameter `L`.
        R (float): Input parameter `R`.
        a (float): Input parameter `a`.

    Returns:
        float: Calculated metric value.
    """
    return float(6 * L**3 * R**3 * a**3)


def expr_a_l_r_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_l_r_form_a`."""
    return 6 * pl.col("L") ** 3 * pl.col("R") ** 3 * pl.col("a") ** 3


def calc_val_2601_06439_form_9(W: float, e: float, h: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_06439.

    **Source**:
    - Title: Deep Reinforcement Learning based Control Design for Aircraft Recovery from Loss-of-Control Scenario (2026)
    - Authors: Imran Sayyed, Aayush Konar, Nandan Kumar Sinha
    - Citation Key: `arxiv_2601_06439`

    **KaTeX Formula**:
    $$
    When [p, q, r] > 0.17 rad/sec rphase1 = -||ω||2 - wp1 (|pq| + |qr| + |pr|)
    $$

    Args:
        W (float): Input parameter `W`.
        e (float): Input parameter `e`.
        h (float): Input parameter `h`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(W * e * h * n)


def expr_val_2601_06439_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2601_06439_form_9`."""
    return pl.col("W") * pl.col("e") * pl.col("h") * pl.col("n")


def calc_val_2601_06439_form_f(W: float, e: float, h: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_06439.

    **Source**:
    - Title: Deep Reinforcement Learning based Control Design for Aircraft Recovery from Loss-of-Control Scenario (2026)
    - Authors: Imran Sayyed, Aayush Konar, Nandan Kumar Sinha
    - Citation Key: `arxiv_2601_06439`

    **KaTeX Formula**:
    $$
    When [p, q, r] < 0.17 rad/sec rphase2 = -e2α -wp21 eαq - wp22 (||ω||2 + |pq| + |qr| + |pr|)
    $$

    Args:
        W (float): Input parameter `W`.
        e (float): Input parameter `e`.
        h (float): Input parameter `h`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(W * e * h * n)


def expr_val_2601_06439_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2601_06439_form_f`."""
    return pl.col("W") * pl.col("e") * pl.col("h") * pl.col("n")


def calc_c_2_s_r_z_form_9(c: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2309_15318.

    **Source**:
    - Title: A Global 3-D Simulation of Magnetospheric Accretion: I. Magnetically Disrupted Disks and Surface Accretion (2023)
    - Authors: Zhaohuan Zhu, James M. Stone, Nuria Calvet
    - Citation Key: `arxiv_2309_15318`

    **KaTeX Formula**:
    $$
    c2s (R, z) = c2s (R = R0, z = 0) ( R R0 )q .
    $$

    Args:
        c (float): Input parameter `c`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(2 * c * s)


def expr_c_2_s_r_z_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_2_s_r_z_form_9`."""
    return 2 * pl.col("c") * pl.col("s")


def calc_a_form_2(c: float, m: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2309_15318.

    **Source**:
    - Title: A Global 3-D Simulation of Magnetospheric Accretion: I. Magnetically Disrupted Disks and Surface Accretion (2023)
    - Authors: Zhaohuan Zhu, James M. Stone, Nuria Calvet
    - Citation Key: `arxiv_2309_15318`

    **KaTeX Formula**:
    $$
    A= m\times  r r3 c ,
    $$

    Args:
        c (float): Input parameter `c`.
        m (float): Input parameter `m`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(3 * c * m * r**2)


def expr_a_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_form_2`."""
    return 3 * pl.col("c") * pl.col("m") * pl.col("r") ** 2


def calc_val_2309_15318_form_3(t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2309_15318.

    **Source**:
    - Title: A Global 3-D Simulation of Magnetospheric Accretion: I. Magnetically Disrupted Disks and Surface Accretion (2023)
    - Authors: Zhaohuan Zhu, James M. Stone, Nuria Calvet
    - Citation Key: `arxiv_2309_15318`

    **KaTeX Formula**:
    $$
    tII,mig = τvisc Mp ΣR2 = Ω-1h-2α-1 q ( ΣR2 M∗ )-1 .
    $$

    Args:
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(-t)


def expr_val_2309_15318_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2309_15318_form_3`."""
    return -pl.col("t")


def calc_val_2303_03898_form_4(b: float, i: float, m: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2303_03898.

    **Source**:
    - Title: Virtual Omnidirectional Perception for Downwash Prediction within a Team of Nano Multirotors Flying in Close Proximity (2023)
    - Authors: Akmaral Moldagalieva, Wolfgang Hönig
    - Citation Key: `arxiv_2303_03898`

    **KaTeX Formula**:
    $$
    bmin, bmax = min max ρi ˆh(Kˆh(TCRh(ρi))).
    $$

    Args:
        b (float): Input parameter `b`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(b * i * m * n)


def expr_val_2303_03898_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2303_03898_form_4`."""
    return pl.col("b") * pl.col("i") * pl.col("m") * pl.col("n")


def calc_p_m_form_9(V: float, i: float, m: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1709_07969.

    **Source**:
    - Title: Optimal-power Configurations for Hover Solutions in Mono-spinners (2017)
    - Authors: Mojtaba Hedayatpour, Mehran Mehrandezh, Farrokh Janabi-Sharifi
    - Citation Key: `arxiv_1709_07969`

    **KaTeX Formula**:
    $$
    Pm = Vmi
    $$

    Args:
        V (float): Input parameter `V`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(V * i * m)


def expr_p_m_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_m_form_9`."""
    return pl.col("V") * pl.col("i") * pl.col("m")


def calc_c_p_form_f(m: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1709_07969.

    **Source**:
    - Title: Optimal-power Configurations for Hover Solutions in Mono-spinners (2017)
    - Authors: Mojtaba Hedayatpour, Mehran Mehrandezh, Farrokh Janabi-Sharifi
    - Citation Key: `arxiv_1709_07969`

    **KaTeX Formula**:
    $$
    cp =0.03m , Rp =0.08m g = 9.81 m/s 2 , ρ = 1.225 kg/m 3 Kτm = 0.02 N.m/A , Kv = 0.02 V/rad/s γ = 9.75 \times  10-6 N.m.s/rad
    $$

    Args:
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(0.03 * m)


def expr_c_p_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_p_form_f`."""
    return 0.03 * pl.col("m")


def calc_p_s_form_b(N: float, W: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1709_07969.

    **Source**:
    - Title: Optimal-power Configurations for Hover Solutions in Mono-spinners (2017)
    - Authors: Mojtaba Hedayatpour, Mehran Mehrandezh, Farrokh Janabi-Sharifi
    - Citation Key: `arxiv_1709_07969`

    **KaTeX Formula**:
    $$
    Ps =1.3296W/N , ¯ωp =471.48 rad/s im =0.25A , ¯n = (0,0,1)T ¯ωB = (0,0,-104.52)T rad/s , Vm = 9.68V
    $$

    Args:
        N (float): Input parameter `N`.
        W (float): Input parameter `W`.

    Returns:
        float: Calculated metric value.
    """
    return float((1.3296 * W) / N)


def expr_p_s_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_s_form_b`."""
    return (1.3296 * pl.col("W")) / pl.col("N")


def calc_p_s_form_5(N: float, W: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1709_07969.

    **Source**:
    - Title: Optimal-power Configurations for Hover Solutions in Mono-spinners (2017)
    - Authors: Mojtaba Hedayatpour, Mehran Mehrandezh, Farrokh Janabi-Sharifi
    - Citation Key: `arxiv_1709_07969`

    **KaTeX Formula**:
    $$
    Ps =0.1325W/N , ¯ωp =-86.87 rad/s im =0.17A , ¯n = (0.002,0.017,0.999)T ¯ωB = (-0.1,-0.66,-38.77)T rad/s , Vm = 1.91V
    $$

    Args:
        N (float): Input parameter `N`.
        W (float): Input parameter `W`.

    Returns:
        float: Calculated metric value.
    """
    return float((0.1325 * W) / N)


def expr_p_s_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_s_form_5`."""
    return (0.1325 * pl.col("W")) / pl.col("N")


def calc_t_s_p_i_n_do_n_w_form_c(d: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1408_4306.

    **Source**:
    - Title: Effect of lift force on the aerodynamics of dust grains in the protoplanetary disk (2014)
    - Authors: Masaki S. Yamaguchi, Shigeo S. Kimura
    - Citation Key: `arxiv_1408_4306`

    **KaTeX Formula**:
    $$
    tspindown = 3.0 \times  103 r2d,1R1/4 1 sec.
    $$

    Args:
        d (float): Input parameter `d`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(618.0 * d * r)


def expr_t_s_p_i_n_do_n_w_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_s_p_i_n_do_n_w_form_c`."""
    return 618.0 * pl.col("d") * pl.col("r")


def calc_val_1408_4306_form_f(d: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1408_4306.

    **Source**:
    - Title: Effect of lift force on the aerodynamics of dust grains in the protoplanetary disk (2014)
    - Authors: Masaki S. Yamaguchi, Shigeo S. Kimura
    - Citation Key: `arxiv_1408_4306`

    **KaTeX Formula**:
    $$
    rd,min ≲ rd ≲ rd,max, where rd,min ≡ 9mcs,0 2σmolΣ0Ω0 Rq-p+3/2 1 , and rd,max ≡ 40√2πmR0 3(2p + 2q + 3)σmolΣ0 Rq+1 1 .
    $$

    Args:
        d (float): Input parameter `d`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(d * r)


def expr_val_1408_4306_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1408_4306_form_f`."""
    return pl.col("d") * pl.col("r")


def calc_x_form_c(D: float, L: float, g: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1408_4306.

    **Source**:
    - Title: Effect of lift force on the aerodynamics of dust grains in the protoplanetary disk (2014)
    - Authors: Masaki S. Yamaguchi, Shigeo S. Kimura
    - Citation Key: `arxiv_1408_4306`

    **KaTeX Formula**:
    $$
    x = -2gD g2D + (gL - 2)(gL - 1/2) ,
    $$

    Args:
        D (float): Input parameter `D`.
        L (float): Input parameter `L`.
        g (float): Input parameter `g`.

    Returns:
        float: Calculated metric value.
    """
    return float(-4 * D**2 * g**2 + (L * g - 2) * (L * g - 1 / 2))


def expr_x_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_form_c`."""
    return -4 * pl.col("D") ** 2 * pl.col("g") ** 2 + (pl.col("L") * pl.col("g") - 2) * (
        pl.col("L") * pl.col("g") - 1 / 2
    )


def calc_y_form_f(D: float, L: float, g: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1408_4306.

    **Source**:
    - Title: Effect of lift force on the aerodynamics of dust grains in the protoplanetary disk (2014)
    - Authors: Masaki S. Yamaguchi, Shigeo S. Kimura
    - Citation Key: `arxiv_1408_4306`

    **KaTeX Formula**:
    $$
    y = -1+ -2(gL -1/2) g2D + (gL - 2)(gL - 1/2) .
    $$

    Args:
        D (float): Input parameter `D`.
        L (float): Input parameter `L`.
        g (float): Input parameter `g`.

    Returns:
        float: Calculated metric value.
    """
    return float(-4 * D * g * (L * g - 1 / 2) + (L * g - 2) * (L * g - 1 / 2) - 1)


def expr_y_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_y_form_f`."""
    return (
        -4 * pl.col("D") * pl.col("g") * (pl.col("L") * pl.col("g") - 1 / 2)
        + (pl.col("L") * pl.col("g") - 2) * (pl.col("L") * pl.col("g") - 1 / 2)
        - 1
    )


def calc_l_form_6(b: float, d: float, dm: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1408_4306.

    **Source**:
    - Title: Effect of lift force on the aerodynamics of dust grains in the protoplanetary disk (2014)
    - Authors: Masaki S. Yamaguchi, Shigeo S. Kimura
    - Citation Key: `arxiv_1408_4306`

    **KaTeX Formula**:
    $$
    L = bvd-dmd 2 .
    $$

    Args:
        b (float): Input parameter `b`.
        d (float): Input parameter `d`.
        dm (float): Input parameter `dm`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(b * d * v - d * dm)


def expr_l_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_form_6`."""
    return pl.col("b") * pl.col("d") * pl.col("v") - pl.col("d") * pl.col("dm")


def calc_d_f_form_4(C: float, D: float, S: float, q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    {FD} = q*S*CD
    $$

    Args:
        C (float): Input parameter `C`.
        D (float): Input parameter `D`.
        S (float): Input parameter `S`.
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float((C * D) * (S * q))


def expr_d_f_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_f_form_4`."""
    return (pl.col("C") * pl.col("D")) * (pl.col("S") * pl.col("q"))


def calc_f_form_4(D: float, F: float, L: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    F = FD + FL
    $$

    Args:
        D (float): Input parameter `D`.
        F (float): Input parameter `F`.
        L (float): Input parameter `L`.

    Returns:
        float: Calculated metric value.
    """
    return float(D * F + F * L)


def expr_f_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_form_4`."""
    return pl.col("D") * pl.col("F") + pl.col("F") * pl.col("L")


def calc_f_r_form_4(R: float, k: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    FR = -kR*r
    $$

    Args:
        R (float): Input parameter `R`.
        k (float): Input parameter `k`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(-R * k * r)


def expr_f_r_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_r_form_4`."""
    return -pl.col("R") * pl.col("k") * pl.col("r")


def calc_d_form_6(A: float, C: float, G: float, R: float, e: float, p: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    D = RCG - RApex
    $$

    Args:
        A (float): Input parameter `A`.
        C (float): Input parameter `C`.
        G (float): Input parameter `G`.
        R (float): Input parameter `R`.
        e (float): Input parameter `e`.
        p (float): Input parameter `p`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(-A * R * e * p * x + C * G * R)


def expr_d_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_form_6`."""
    return -pl.col("A") * pl.col("R") * pl.col("e") * pl.col("p") * pl.col("x") + pl.col(
        "C"
    ) * pl.col("G") * pl.col("R")


def calc_a_w_form_3(V: float, W: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    WA = W - V
    $$

    Args:
        V (float): Input parameter `V`.
        W (float): Input parameter `W`.

    Returns:
        float: Calculated metric value.
    """
    return float(-V + W)


def expr_a_w_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_w_form_3`."""
    return -pl.col("V") + pl.col("W")


def calc_dl_dt_form_3(M: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    dL/dt = M
    $$

    Args:
        M (float): Input parameter `M`.

    Returns:
        float: Calculated metric value.
    """
    return float(M)


def expr_dl_dt_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_dl_dt_form_3`."""
    return pl.col("M")


def calc_a_j_h_form_8(
    a: float, di: float, i: float, l: float, m: float, n: float, r: float, s: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    AJh = 0.1129 milliradians
    $$

    Args:
        a (float): Input parameter `a`.
        di (float): Input parameter `di`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(0.1129 * a**2 * di * i**2 * l**2 * m * n * r * s)


def expr_a_j_h_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_j_h_form_8`."""
    return (
        0.1129
        * pl.col("a") ** 2
        * pl.col("di")
        * pl.col("i") ** 2
        * pl.col("l") ** 2
        * pl.col("m")
        * pl.col("n")
        * pl.col("r")
        * pl.col("s")
    )


def calc_e_v_form_3(m: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    E(v) = (m/2)*v2
    $$

    Args:
        m (float): Input parameter `m`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float((2 * v) * (m / 2))


def expr_e_v_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_v_form_3`."""
    return (2 * pl.col("v")) * (pl.col("m") / 2)


def calc_f_m_a_x_form_9(
    F: float,
    G: float,
    H: float,
    K: float,
    M: float,
    R: float,
    S: float,
    a: float,
    m: float,
    x: float,
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_02991.

    **Source**:
    - Title: Subject-Specific Predictive Musculoskeletal Simulations of Lower-Limb Exoskeleton Assistance: Metabolic and Biomechanical Effects of Joint Assistance Strategies (2026)
    - Authors: Neethan Ratnakumar, Mariya Tohfafarosh, Xianlian Zhou
    - Citation Key: `arxiv_2610_02991`

    **KaTeX Formula**:
    $$
    Fmax = F G max \times  M/H M G/HG \times  RMSK RGMSK
    $$

    Args:
        F (float): Input parameter `F`.
        G (float): Input parameter `G`.
        H (float): Input parameter `H`.
        K (float): Input parameter `K`.
        M (float): Input parameter `M`.
        R (float): Input parameter `R`.
        S (float): Input parameter `S`.
        a (float): Input parameter `a`.
        m (float): Input parameter `m`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(
        (R * (M * (S * (K * (R * (G * (M * (K * S))))))))
        * (((M * (F * (G * (m * (a * x))))) / (H * (G * M))) / (G * H))
    )


def expr_f_m_a_x_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_m_a_x_form_9`."""
    return (
        pl.col("R")
        * (
            pl.col("M")
            * (
                pl.col("S")
                * (
                    pl.col("K")
                    * (pl.col("R") * (pl.col("G") * (pl.col("M") * (pl.col("K") * pl.col("S")))))
                )
            )
        )
    ) * (
        (
            (
                pl.col("M")
                * (pl.col("F") * (pl.col("G") * (pl.col("m") * (pl.col("a") * pl.col("x")))))
            )
            / (pl.col("H") * (pl.col("G") * pl.col("M")))
        )
        / (pl.col("G") * pl.col("H"))
    )


def calc_o_form_c(p: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_20570.

    **Source**:
    - Title: Walking on the Slope: Stable Bipedal Gaits with Genetic-Algorithm-Optimized Trajectories (2026)
    - Authors: Madhav Rijal
    - Citation Key: `arxiv_2609_20570`

    **KaTeX Formula**:
    $$
    O = w+p, w = 8∑ n=1 ∫ τn ˙ θn dt, p = a\times 104 ,
    $$

    Args:
        p (float): Input parameter `p`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(p + w)


def expr_o_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_o_form_c`."""
    return pl.col("p") + pl.col("w")


def calc_val_2609_11733_form_3(
    a: float,
    c: float,
    e: float,
    l: float,
    m: float,
    n: float,
    o: float,
    r: float,
    s: float,
    t: float,
    u: float,
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_11733.

    **Source**:
    - Title: Reflex-Informed Neuromuscular Reinforcement Learning for Muscle-Driven Locomotion (2026)
    - Authors: Jian Zhou, Xingyu Zhang, Rui Ma et al.
    - Citation Key: `arxiv_2609_11733`

    **KaTeX Formula**:
    $$
    muscle moment arms,
    $$

    Args:
        a (float): Input parameter `a`.
        c (float): Input parameter `c`.
        e (float): Input parameter `e`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * c * e**2 * l * m**4 * n * o * r * s**2 * t * u)


def expr_val_2609_11733_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_11733_form_3`."""
    return (
        pl.col("a")
        * pl.col("c")
        * pl.col("e") ** 2
        * pl.col("l")
        * pl.col("m") ** 4
        * pl.col("n")
        * pl.col("o")
        * pl.col("r")
        * pl.col("s") ** 2
        * pl.col("t")
        * pl.col("u")
    )


def calc_p_i_t_form_6(i: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_11733.

    **Source**:
    - Title: Reflex-Informed Neuromuscular Reinforcement Learning for Muscle-Driven Locomotion (2026)
    - Authors: Jian Zhou, Xingyu Zhang, Rui Ma et al.
    - Citation Key: `arxiv_2609_11733`

    **KaTeX Formula**:
    $$
    pi(t) = pi,0(1 + λai(t)),
    $$

    Args:
        i (float): Input parameter `i`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(i * p)


def expr_p_i_t_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_t_form_6`."""
    return pl.col("i") * pl.col("p")


def calc_c_g_f_r_form_c(L: float, c: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_11733.

    **Source**:
    - Title: Reflex-Informed Neuromuscular Reinforcement Learning for Muscle-Driven Locomotion (2026)
    - Authors: Jian Zhou, Xingyu Zhang, Rui Ma et al.
    - Citation Key: `arxiv_2609_11733`

    **KaTeX Formula**:
    $$
    cgrf = [Lc - 1.2]+, ce = 1N ∥et -et-1∥2 2, cm = 1 da N∑ i=1 I[αi > 0.15] , cq = 1 J J∑ j=1 mean(∣∣∣τ lim j ∣∣∣) .
    $$

    Args:
        L (float): Input parameter `L`.
        c (float): Input parameter `c`.

    Returns:
        float: Calculated metric value.
    """
    return float(L * c - 1.2)


def expr_c_g_f_r_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_g_f_r_form_c`."""
    return pl.col("L") * pl.col("c") - 1.2


def calc_val_2609_10457_form_c(C: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    Ci,a = Mi-1,a(1 - Mi,a)Mi+1,a.
    $$

    Args:
        C (float): Input parameter `C`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(C * i)


def expr_val_2609_10457_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_10457_form_c`."""
    return pl.col("C") * pl.col("i")


def calc_l_r_o_l_l_j_o_i_n_form_9(R: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    Lroll-join = 1 2 R.2[ϕβ(∥Piei-1∥2), ϕβ(∥Piei+1∥2)] + 12 R.2[ϕβ(∥Pi(ei-1 + ei+1)∥2)] .
    $$

    Args:
        R (float): Input parameter `R`.

    Returns:
        float: Calculated metric value.
    """
    return float(12 * R)


def expr_l_r_o_l_l_j_o_i_n_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_r_o_l_l_j_o_i_n_form_9`."""
    return 12 * pl.col("R")


def calc_l_r_o_l_l_e_x_c_e_s_s_form_c(R: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    Lroll-excess = R.2[ϕβ ( [ˆκi - τi]+ τtail )] .
    $$

    Args:
        R (float): Input parameter `R`.

    Returns:
        float: Calculated metric value.
    """
    return float(R)


def expr_l_r_o_l_l_e_x_c_e_s_s_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_r_o_l_l_e_x_c_e_s_s_form_c`."""
    return pl.col("R")


def calc_val_2609_10457_form_d(a: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    ai,j = cos-1(clip( tr((Rci,j )⊤Rpi,j ) - 1 2 , -1, 1)) , bi,j = 1[ai,j > 0.15 rad].
    $$

    Args:
        a (float): Input parameter `a`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * i)


def expr_val_2609_10457_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_10457_form_d`."""
    return pl.col("a") * pl.col("i")


def calc_val_2609_10457_form_8(b: float, i: float, p: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    bsp i,j = bi,j ∨ ∨ k∈N ∗ (j) bi,k , btmp i,j = ∨ |u-i|\le 2 bsp u,j .
    $$

    Args:
        b (float): Input parameter `b`.
        i (float): Input parameter `i`.
        p (float): Input parameter `p`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(b * i * p * s)


def expr_val_2609_10457_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_10457_form_8`."""
    return pl.col("b") * pl.col("i") * pl.col("p") * pl.col("s")


def calc_p_c_i_j_form_9(J: float, c: float, i: float, j: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    pcij = Jcij - rci , PAJcij = PA(rci +pcij ).
    $$

    Args:
        J (float): Input parameter `J`.
        c (float): Input parameter `c`.
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(J * c * i * j - c * i * r)


def expr_p_c_i_j_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_c_i_j_form_9`."""
    return pl.col("J") * pl.col("c") * pl.col("i") * pl.col("j") - pl.col("c") * pl.col(
        "i"
    ) * pl.col("r")


def calc_val_2609_10457_form_0(J: float, i: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    Jit. = (mean i,j ∥∆2Jij∥2 +mean i,j ∥∆2 (Jij - ri)∥2) .
    $$

    Args:
        J (float): Input parameter `J`.
        i (float): Input parameter `i`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(J * i * t)


def expr_val_2609_10457_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_10457_form_0`."""
    return pl.col("J") * pl.col("i") * pl.col("t")


def calc_val_2609_10457_form_f(A: float, c: float, e: float, l: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    Accel. = 1 |Ω2| ∑ (n,i,j)∈Ω2 ∥f 2∆2ˆJnij - f 2∆2Jnij∥2,
    $$

    Args:
        A (float): Input parameter `A`.
        c (float): Input parameter `c`.
        e (float): Input parameter `e`.
        l (float): Input parameter `l`.

    Returns:
        float: Calculated metric value.
    """
    return float(A * c**2 * e * l)


def expr_val_2609_10457_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_10457_form_f`."""
    return pl.col("A") * pl.col("c") ** 2 * pl.col("e") * pl.col("l")


def calc_val_2608_29935_form_7(L: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    L(\cdot ) = ωx ωy ωz 0 0 0 0 ωx 0 ωy ωz 0 0 0 ωx 0 ωy ωz 
    $$

    Args:
        L (float): Input parameter `L`.

    Returns:
        float: Calculated metric value.
    """
    return float(L)


def expr_val_2608_29935_form_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_29935_form_7`."""
    return pl.col("L")


def calc_k_1_form_3(L: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    K1 = L4 L1 , K4 = L4 L2 K5 = L23 - L24 - L21 - L22 2L1L2
    $$

    Args:
        L (float): Input parameter `L`.

    Returns:
        float: Calculated metric value.
    """
    return float(4 * L**2)


def expr_k_1_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_1_form_3`."""
    return 4 * pl.col("L") ** 2


def calc_val_2608_29935_form_e(B: float, C: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    B wC,s = ντs(ϕd) e6
    $$

    Args:
        B (float): Input parameter `B`.
        C (float): Input parameter `C`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(B * C * w)


def expr_val_2608_29935_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_29935_form_e`."""
    return pl.col("B") * pl.col("C") * pl.col("w")


def calc_s_w_form_8(l: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    ws = 1 - wl
    $$

    Args:
        l (float): Input parameter `l`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(-l * w + 1)


def expr_s_w_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_w_form_8`."""
    return -pl.col("l") * pl.col("w") + 1


def calc_w_b_x_form_1(B: float, W: float, y: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    W xB = W yB \times  W zB
    $$

    Args:
        B (float): Input parameter `B`.
        W (float): Input parameter `W`.
        y (float): Input parameter `y`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(B**2 * W**2 * y * z)


def expr_w_b_x_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_b_x_form_1`."""
    return pl.col("B") ** 2 * pl.col("W") ** 2 * pl.col("y") * pl.col("z")


def calc_w_b_r_form_3(B: float, W: float, x: float, y: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    W RB = [W xB W yB W zB ] ,
    $$

    Args:
        B (float): Input parameter `B`.
        W (float): Input parameter `W`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(B**3 * W**3 * x * y * z)


def expr_w_b_r_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_b_r_form_3`."""
    return pl.col("B") ** 3 * pl.col("W") ** 3 * pl.col("x") * pl.col("y") * pl.col("z")


def calc_val_2608_29935_form_8(W: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    W rW,B = 12 ( ̂ PLA + ̂ PRA)
    $$

    Args:
        W (float): Input parameter `W`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(W**2 * r)


def expr_val_2608_29935_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_29935_form_8`."""
    return pl.col("W") ** 2 * pl.col("r")


def calc_w_c_x_form_9(C: float, W: float, y: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    W xC = W yC \times  W zC
    $$

    Args:
        C (float): Input parameter `C`.
        W (float): Input parameter `W`.
        y (float): Input parameter `y`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(C**2 * W**2 * y * z)


def expr_w_c_x_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_c_x_form_9`."""
    return pl.col("C") ** 2 * pl.col("W") ** 2 * pl.col("y") * pl.col("z")


def calc_w_c_r_form_1(C: float, W: float, x: float, y: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    W RC = [W xC W yC W zC ]
    $$

    Args:
        C (float): Input parameter `C`.
        W (float): Input parameter `W`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(C**3 * W**3 * x * y * z)


def expr_w_c_r_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_c_r_form_1`."""
    return pl.col("C") ** 3 * pl.col("W") ** 3 * pl.col("x") * pl.col("y") * pl.col("z")


def calc_val_2608_29935_form_a(
    C: float, c: float, e: float, h: float, o: float, r: float, t: float, v: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    the vector C rC,R as C rC,R = W R⊤C (W rW,R - W rW,C )
    $$

    Args:
        C (float): Input parameter `C`.
        c (float): Input parameter `c`.
        e (float): Input parameter `e`.
        h (float): Input parameter `h`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(C**2 * c * e**2 * h * o * r**2 * t**2 * v)


def expr_val_2608_29935_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_29935_form_a`."""
    return (
        pl.col("C") ** 2
        * pl.col("c")
        * pl.col("e") ** 2
        * pl.col("h")
        * pl.col("o")
        * pl.col("r") ** 2
        * pl.col("t") ** 2
        * pl.col("v")
    )


def calc_val_2608_29935_form_3(W: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    W rW,C = [ W rW,B[1], W rW,B[2], 0 ]⊤
    $$

    Args:
        W (float): Input parameter `W`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(W**2 * r)


def expr_val_2608_29935_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_29935_form_3`."""
    return pl.col("W") ** 2 * pl.col("r")


def calc_w_b_r_form_0(B: float, W: float, x: float, y: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    W RB = [W xB W yB W zB ]
    $$

    Args:
        B (float): Input parameter `B`.
        W (float): Input parameter `W`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(B**3 * W**3 * x * y * z)


def expr_w_b_r_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_b_r_form_0`."""
    return pl.col("B") ** 3 * pl.col("W") ** 3 * pl.col("x") * pl.col("y") * pl.col("z")


def calc_q_dt_p_form_c(a: float, c: float, dt: float, m: float, q: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_08059.

    **Source**:
    - Title: Perceptive Behavior Foundation Model: Adapting Human Motion Priors to Robot-Centric Terrain (2026)
    - Authors: Zifan Wang, Yizhao Li, Teli Ma et al.
    - Citation Key: `arxiv_2606_08059`

    **KaTeX Formula**:
    $$
    qpd t = qcmd t +at,
    $$

    Args:
        a (float): Input parameter `a`.
        c (float): Input parameter `c`.
        dt (float): Input parameter `dt`.
        m (float): Input parameter `m`.
        q (float): Input parameter `q`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * t + c * dt * m * q)


def expr_q_dt_p_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_dt_p_form_c`."""
    return pl.col("a") * pl.col("t") + pl.col("c") * pl.col("dt") * pl.col("m") * pl.col("q")


def calc_r_m_d_i_form_5(e: float, h: float, l: float, o: float, r: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_08059.

    **Source**:
    - Title: Perceptive Behavior Foundation Model: Adapting Human Motion Priors to Robot-Centric Terrain (2026)
    - Authors: Zifan Wang, Yizhao Li, Teli Ma et al.
    - Citation Key: `arxiv_2606_08059`

    **KaTeX Formula**:
    $$
    rmid = 12 (rtoe + rheel ), pmid f,t = pankle f,t +Rf,trmid .
    $$

    Args:
        e (float): Input parameter `e`.
        h (float): Input parameter `h`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(12 * e**2 * h * l * r + 12 * e * o * r * t)


def expr_r_m_d_i_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_m_d_i_form_5`."""
    return 12 * pl.col("e") ** 2 * pl.col("h") * pl.col("l") * pl.col("r") + 12 * pl.col(
        "e"
    ) * pl.col("o") * pl.col("r") * pl.col("t")


def calc_val_2604_25278_form_2(e: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2604_25278.

    **Source**:
    - Title: The GMRT High-Resolution Southern Sky Survey for pulsars and transients -- VIII: Orbital Variability and the Evolution of a 1-Day He-WD Millisecond Pulsar J2101-4802 (2026)
    - Authors: Ankita Ghosh, Bhaswati Bhattacharyya, David L. Kaplan et al.
    - Citation Key: `arxiv_2604_25278`

    **KaTeX Formula**:
    $$
    ne,sw = AAU [ 1 AU r ]2 ,
    $$

    Args:
        e (float): Input parameter `e`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(e * n)


def expr_val_2604_25278_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2604_25278_form_2`."""
    return pl.col("e") * pl.col("n")


def calc_val_2602_20850_form_b(D: float, o: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_20850.

    **Source**:
    - Title: KCFRC: Kinematic Collision-Aware Foothold Reachability Criteria for Legged Locomotion (2026)
    - Authors: Lei Ye, Haibo Gao, Huaiguang Yang et al.
    - Citation Key: `arxiv_2602_20850`

    **KaTeX Formula**:
    $$
    Do : {(x, y, z) ∈ X | z < fG(x, y), z > fC(x, y)}
    $$

    Args:
        D (float): Input parameter `D`.
        o (float): Input parameter `o`.

    Returns:
        float: Calculated metric value.
    """
    return float(D * o)


def expr_val_2602_20850_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2602_20850_form_b`."""
    return pl.col("D") * pl.col("o")


def calc_val_2602_20850_form_5(D: float, f: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_20850.

    **Source**:
    - Title: KCFRC: Kinematic Collision-Aware Foothold Reachability Criteria for Legged Locomotion (2026)
    - Authors: Lei Ye, Haibo Gao, Huaiguang Yang et al.
    - Citation Key: `arxiv_2602_20850`

    **KaTeX Formula**:
    $$
    Dfi : {(x, y, z, t) | (x, y, z) ∈ Ti(t), t0 < t < t1}
    $$

    Args:
        D (float): Input parameter `D`.
        f (float): Input parameter `f`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(D * f * i)


def expr_val_2602_20850_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2602_20850_form_5`."""
    return pl.col("D") * pl.col("f") * pl.col("i")


def calc_e_p_form_3(e: float, f: float, r: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_05895.

    **Source**:
    - Title: Residual Reinforcement Learning for Waste-Container Lifting Using Large-Scale Cranes with Underactuated Tools (2026)
    - Authors: Qi Li, Karsten Berns
    - Citation Key: `arxiv_2602_05895`

    **KaTeX Formula**:
    $$
    ep = xref - x, ev = vref - v, ei(t) = ∫ t 0 ep(τ ) dτ,
    $$

    Args:
        e (float): Input parameter `e`.
        f (float): Input parameter `f`.
        r (float): Input parameter `r`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(e * f * r * x - x)


def expr_e_p_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_p_form_3`."""
    return pl.col("e") * pl.col("f") * pl.col("r") * pl.col("x") - pl.col("x")


def calc_f_c_d_m_form_a(
    K: float, M: float, da: float, e: float, i: float, p: float, v: float, x: float, y: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_05895.

    **Source**:
    - Title: Residual Reinforcement Learning for Waste-Container Lifting Using Large-Scale Cranes with Underactuated Tools (2026)
    - Authors: Qi Li, Karsten Berns
    - Citation Key: `arxiv_2602_05895`

    **KaTeX Formula**:
    $$
    Fcmd = Kpep + Kvev + Kiei + Mdaxy ,
    $$

    Args:
        K (float): Input parameter `K`.
        M (float): Input parameter `M`.
        da (float): Input parameter `da`.
        e (float): Input parameter `e`.
        i (float): Input parameter `i`.
        p (float): Input parameter `p`.
        v (float): Input parameter `v`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(K * e * i**2 + K * e * p**2 + K * e * v**2 + M * da * x * y)


def expr_f_c_d_m_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_c_d_m_form_a`."""
    return (
        pl.col("K") * pl.col("e") * pl.col("i") ** 2
        + pl.col("K") * pl.col("e") * pl.col("p") ** 2
        + pl.col("K") * pl.col("e") * pl.col("v") ** 2
        + pl.col("M") * pl.col("da") * pl.col("x") * pl.col("y")
    )


def calc_val_2602_05895_form_e(dm: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_05895.

    **Source**:
    - Title: Residual Reinforcement Learning for Waste-Container Lifting Using Large-Scale Cranes with Underactuated Tools (2026)
    - Authors: Qi Li, Karsten Berns
    - Citation Key: `arxiv_2602_05895`

    **KaTeX Formula**:
    $$
    dm,k = ∥pref m -ptcp k ∥2, ⃗vk = pdk - ptcp k ,
    $$

    Args:
        dm (float): Input parameter `dm`.

    Returns:
        float: Calculated metric value.
    """
    return float(dm)


def expr_val_2602_05895_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2602_05895_form_e`."""
    return pl.col("dm")


def calc_e_form_1(e: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18161.

    **Source**:
    - Title: In-depth analysis of bar formation mechanisms of disk galaxies in halos of different concentrations (2026)
    - Authors: T. Worrakitpoonpon
    - Citation Key: `arxiv_2601_18161`

    **KaTeX Formula**:
    $$
    E = e0.2 e0.4 ,
    $$

    Args:
        e (float): Input parameter `e`.

    Returns:
        float: Calculated metric value.
    """
    return float(0.08 * e**2)


def expr_e_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_form_1`."""
    return 0.08 * pl.col("e") ** 2


def calc_val_2512_13304_form_5(n: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_13304.

    **Source**:
    - Title: Humanoid Robot Running Through Random Stepping Stones and Jumping Over Obstacles: Step Adaptation Using Spring-Mass Trajectories (2025)
    - Authors: Sait Sovukluk, Johannes Englsberger, Christian Ott
    - Citation Key: `arxiv_2512_13304`

    **KaTeX Formula**:
    $$
    p n,∗ c,TD = invkin(p n f,d , u n,∗ ),
    $$

    Args:
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(n * p)


def expr_val_2512_13304_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2512_13304_form_5`."""
    return pl.col("n") * pl.col("p")


def calc_val_2512_13304_form_1(d: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_13304.

    **Source**:
    - Title: Humanoid Robot Running Through Random Stepping Stones and Jumping Over Obstacles: Step Adaptation Using Spring-Mass Trajectories (2025)
    - Authors: Sait Sovukluk, Johannes Englsberger, Christian Ott
    - Citation Key: `arxiv_2512_13304`

    **KaTeX Formula**:
    $$
    d (\cdot ), p n-1 f , µ)).
    $$

    Args:
        d (float): Input parameter `d`.

    Returns:
        float: Calculated metric value.
    """
    return float(d)


def expr_val_2512_13304_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2512_13304_form_1`."""
    return pl.col("d")


def calc_val_2512_13304_form_a(f: float, n: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_13304.

    **Source**:
    - Title: Humanoid Robot Running Through Random Stepping Stones and Jumping Over Obstacles: Step Adaptation Using Spring-Mass Trajectories (2025)
    - Authors: Sait Sovukluk, Johannes Englsberger, Christian Ott
    - Citation Key: `arxiv_2512_13304`

    **KaTeX Formula**:
    $$
    p n-1 f,controlled = fwdkin( integration [t=LO n-2 →TD n-1 ] (Σflight, p n-2 c,LO , ˙p n-2 c,LO ), u ∗ + K∆x)
    $$

    Args:
        f (float): Input parameter `f`.
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(-f + n * p)


def expr_val_2512_13304_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2512_13304_form_a`."""
    return -pl.col("f") + pl.col("n") * pl.col("p")


def calc_h_a_p_e_x_form_b(c: float, m: float, o: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_13304.

    **Source**:
    - Title: Humanoid Robot Running Through Random Stepping Stones and Jumping Over Obstacles: Step Adaptation Using Spring-Mass Trajectories (2025)
    - Authors: Sait Sovukluk, Johannes Englsberger, Christian Ott
    - Citation Key: `arxiv_2512_13304`

    **KaTeX Formula**:
    $$
    hapex = pcom,z + vztrise - 0.5gt 2 rise .
    $$

    Args:
        c (float): Input parameter `c`.
        m (float): Input parameter `m`.
        o (float): Input parameter `o`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(c * m * o * p)


def expr_h_a_p_e_x_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_a_p_e_x_form_b`."""
    return pl.col("c") * pl.col("m") * pl.col("o") * pl.col("p")


def calc_val_2512_13304_form_d(h: float, l: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_13304.

    **Source**:
    - Title: Humanoid Robot Running Through Random Stepping Stones and Jumping Over Obstacles: Step Adaptation Using Spring-Mass Trajectories (2025)
    - Authors: Sait Sovukluk, Johannes Englsberger, Christian Ott
    - Citation Key: `arxiv_2512_13304`

    **KaTeX Formula**:
    $$
    lh,min < lh,new,i < lh,max,
    $$

    Args:
        h (float): Input parameter `h`.
        l (float): Input parameter `l`.

    Returns:
        float: Calculated metric value.
    """
    return float(h * l)


def expr_val_2512_13304_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2512_13304_form_d`."""
    return pl.col("h") * pl.col("l")


def calc_e_p_form_1(a: float, b: float, c: float, p: float, x: float, y: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_13304.

    **Source**:
    - Title: Humanoid Robot Running Through Random Stepping Stones and Jumping Over Obstacles: Step Adaptation Using Spring-Mass Trajectories (2025)
    - Authors: Sait Sovukluk, Johannes Englsberger, Christian Ott
    - Citation Key: `arxiv_2512_13304`

    **KaTeX Formula**:
    $$
    E(p) = px a 2 + py b 2 + pz c 2 - 1,
    $$

    Args:
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        c (float): Input parameter `c`.
        p (float): Input parameter `p`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float((p * (z * (2 * c)) + (p * (x * (2 * a)) + p * (y * (2 * b)))) - 1)


def expr_e_p_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_p_form_1`."""
    return (
        pl.col("p") * (pl.col("z") * (2 * pl.col("c")))
        + (
            pl.col("p") * (pl.col("x") * (2 * pl.col("a")))
            + pl.col("p") * (pl.col("y") * (2 * pl.col("b")))
        )
    ) - 1


def calc_t_p_x_p_y_p_z_1_form_5(C: float, T: float, u: float, v: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2507_16328.

    **Source**:
    - Title: Design and Dimensional Optimization of Legged Structures for Construction Robots (2025)
    - Authors: Xiao Liu, Xianlong Yang, Weijun Wang et al.
    - Citation Key: `arxiv_2507_16328`

    **KaTeX Formula**:
    $$
    [ px py pz 1]T =TC [u v w 1]T
    $$

    Args:
        C (float): Input parameter `C`.
        T (float): Input parameter `T`.
        u (float): Input parameter `u`.
        v (float): Input parameter `v`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(C * T**2 * u * v * w)


def expr_t_p_x_p_y_p_z_1_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_p_x_p_y_p_z_1_form_5`."""
    return pl.col("C") * pl.col("T") ** 2 * pl.col("u") * pl.col("v") * pl.col("w")


def calc_val_2507_16328_form_6(s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2507_16328.

    **Source**:
    - Title: Design and Dimensional Optimization of Legged Structures for Construction Robots (2025)
    - Authors: Xiao Liu, Xianlong Yang, Weijun Wang et al.
    - Citation Key: `arxiv_2507_16328`

    **KaTeX Formula**:
    $$
    s.t .  l1 \ge  0, l2 \ge  0, l3 \ge  0 l1 + l2 + l3 = 1000 -60◦ \le  θ2 \le  60◦ -135◦ \le  θ3 \le  -15◦
    $$

    Args:
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(s)


def expr_val_2507_16328_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2507_16328_form_6`."""
    return pl.col("s")


def calc_val_2507_11037_form_2(C: float, D: float, L: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2507_11037.

    **Source**:
    - Title: A Multi-View High-Resolution Foot-Ankle Complex Point Cloud Dataset During Gait for Occlusion-Robust 3D Completion (2025)
    - Authors: Jie-Wen Li, Zi-Han Ye, Qingyuan Zhou et al.
    - Citation Key: `arxiv_2507_11037`

    **KaTeX Formula**:
    $$
    CDL1(S1, S2) = 1 2|S1| ∑ x∈S1 min y∈S2∥x- y∥2 + 1 2|S2| ∑ y∈S2 min x∈S1∥y - x∥2, CDL2(S1, S2) = 1 |S1| ∑ x∈S1 min y∈S2 ∥x- y∥22 + 1 |S2| ∑ y∈S2 min x∈S1∥y - x∥22 .
    $$

    Args:
        C (float): Input parameter `C`.
        D (float): Input parameter `D`.
        L (float): Input parameter `L`.

    Returns:
        float: Calculated metric value.
    """
    return float(C * D * L)


def expr_val_2507_11037_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2507_11037_form_2`."""
    return pl.col("C") * pl.col("D") * pl.col("L")


def calc_val_2610_31563_form_8(D: float, O: float, P: float, S: float, T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    TOPSD(a | ht) = S(a | ht, y∗ )
    $$

    Args:
        D (float): Input parameter `D`.
        O (float): Input parameter `O`.
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(T * (O * (P * (D * S))))


def expr_val_2610_31563_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_31563_form_8`."""
    return pl.col("T") * (pl.col("O") * (pl.col("P") * (pl.col("D") * pl.col("S"))))


def calc_val_2610_31153_form_8(a: float, b: float, i: float, j: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31153.

    **Source**:
    - Title: Balanced Posted Prices in Stationary Two-Sided Markets (2026)
    - Authors: Ilan Reuven Cohen
    - Citation Key: `arxiv_2610_31153`

    **KaTeX Formula**:
    $$
    (bj - ai) + \le  (bj - τ ) + + (τ - ai) +.
    $$

    Args:
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.

    Returns:
        float: Calculated metric value.
    """
    return float(-a * i + b * j)


def expr_val_2610_31153_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_31153_form_8`."""
    return -pl.col("a") * pl.col("i") + pl.col("b") * pl.col("j")


def calc_val_2610_31563_form_f(A: float, D: float, O: float, P: float, S: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    S+ AOPD (a | h) = S(a | h) +ηT(a | h)A S (h, a) 1 + η Ea∼T [A S (h, a)] . (B.2)
    $$

    Args:
        A (float): Input parameter `A`.
        D (float): Input parameter `D`.
        O (float): Input parameter `O`.
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.

    Returns:
        float: Calculated metric value.
    """
    return float(A * (O * (D * P)) + S)


def expr_val_2610_31563_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_31563_form_f`."""
    return pl.col("A") * (pl.col("O") * (pl.col("D") * pl.col("P"))) + pl.col("S")


def calc_val_2610_31563_form_a(S: float, c: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    S+ c (a | h) = S(a | h) +η˜ T(a | h)A S (h, a) 1+η∑b ˜ T(b | h)A S (h, b) .
    $$

    Args:
        S (float): Input parameter `S`.
        c (float): Input parameter `c`.

    Returns:
        float: Calculated metric value.
    """
    return float(S + c)


def expr_val_2610_31563_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_31563_form_a`."""
    return pl.col("S") + pl.col("c")


def calc_val_2610_31563_form_5(R: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    R(S+
    $$

    Args:
        R (float): Input parameter `R`.

    Returns:
        float: Calculated metric value.
    """
    return float(R)


def expr_val_2610_31563_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_31563_form_5`."""
    return pl.col("R")


def calc_val_2610_31563_form_b(v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    v(a | h) = S(a | h)A S (h, a) +λ(T(a | h) -S(a | h)). (B.3)
    $$

    Args:
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(v)


def expr_val_2610_31563_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_31563_form_b`."""
    return pl.col("v")


def calc_j_p_form_d(A: float, W: float, j: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31153.

    **Source**:
    - Title: Balanced Posted Prices in Stationary Two-Sided Markets (2026)
    - Authors: Ilan Reuven Cohen
    - Citation Key: `arxiv_2610_31153`

    **KaTeX Formula**:
    $$
    pj = Wj +Aj 2xj
    $$

    Args:
        A (float): Input parameter `A`.
        W (float): Input parameter `W`.
        j (float): Input parameter `j`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(2 * A * j**2 * x + W * j)


def expr_j_p_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_p_form_d`."""
    return 2 * pl.col("A") * pl.col("j") ** 2 * pl.col("x") + pl.col("W") * pl.col("j")


def calc_val_2610_31153_form_6(i: float, j: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31153.

    **Source**:
    - Title: Balanced Posted Prices in Stationary Two-Sided Markets (2026)
    - Authors: Ilan Reuven Cohen
    - Citation Key: `arxiv_2610_31153`

    **KaTeX Formula**:
    $$
    xij := (αiλi)(βjγj) R .
    $$

    Args:
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(i * j * x)


def expr_val_2610_31153_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_31153_form_6`."""
    return pl.col("i") * pl.col("j") * pl.col("x")


def calc_val_2610_31153_form_d(B: float, j: float, q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31153.

    **Source**:
    - Title: Balanced Posted Prices in Stationary Two-Sided Markets (2026)
    - Authors: Ilan Reuven Cohen
    - Citation Key: `arxiv_2610_31153`

    **KaTeX Formula**:
    $$
    qB j := Pr[Nj > 0], qS j := Pr[Nj < Cj].
    $$

    Args:
        B (float): Input parameter `B`.
        j (float): Input parameter `j`.
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float(B * j * q)


def expr_val_2610_31153_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_31153_form_d`."""
    return pl.col("B") * pl.col("j") * pl.col("q")


def calc_val_2610_31153_form_7(y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31153.

    **Source**:
    - Title: Balanced Posted Prices in Stationary Two-Sided Markets (2026)
    - Authors: Ilan Reuven Cohen
    - Citation Key: `arxiv_2610_31153`

    **KaTeX Formula**:
    $$
    S(y) := {(k, S) : ykS > 0}
    $$

    Args:
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(y)


def expr_val_2610_31153_form_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_31153_form_7`."""
    return pl.col("y")


def calc_val_2610_31153_form_e(A: float, T: float, k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31153.

    **Source**:
    - Title: Balanced Posted Prices in Stationary Two-Sided Markets (2026)
    - Authors: Ilan Reuven Cohen
    - Citation Key: `arxiv_2610_31153`

    **KaTeX Formula**:
    $$
    TkS(A) := {j ∈ S ∩ A : wkS j \ge  pj}.
    $$

    Args:
        A (float): Input parameter `A`.
        T (float): Input parameter `T`.
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(A * T * k)


def expr_val_2610_31153_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_31153_form_e`."""
    return pl.col("A") * pl.col("T") * pl.col("k")


def calc_val_2610_31153_form_0(P: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31153.

    **Source**:
    - Title: Balanced Posted Prices in Stationary Two-Sided Markets (2026)
    - Authors: Ilan Reuven Cohen
    - Citation Key: `arxiv_2610_31153`

    **KaTeX Formula**:
    $$
    Pr[Nj = 0] = Pr[Nj = Cj ], qB j = qS j \ge  1 2
    $$

    Args:
        P (float): Input parameter `P`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * r)


def expr_val_2610_31153_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_31153_form_0`."""
    return pl.col("P") * pl.col("r")


def calc_val_2610_31153_form_b(j: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31153.

    **Source**:
    - Title: Balanced Posted Prices in Stationary Two-Sided Markets (2026)
    - Authors: Ilan Reuven Cohen
    - Citation Key: `arxiv_2610_31153`

    **KaTeX Formula**:
    $$
    pj := Wj +Aj 2xj ;
    $$

    Args:
        j (float): Input parameter `j`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(j * p)


def expr_val_2610_31153_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_31153_form_b`."""
    return pl.col("j") * pl.col("p")


def calc_val_2610_31153_form_2(S: float, T: float, k: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31153.

    **Source**:
    - Title: Balanced Posted Prices in Stationary Two-Sided Markets (2026)
    - Authors: Ilan Reuven Cohen
    - Citation Key: `arxiv_2610_31153`

    **KaTeX Formula**:
    $$
    yT kS := E[YkS(T)] T , zT jr := E[ ̂ Pjr (T )] T .
    $$

    Args:
        S (float): Input parameter `S`.
        T (float): Input parameter `T`.
        k (float): Input parameter `k`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(y * (T * (S * k)))


def expr_val_2610_31153_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_31153_form_2`."""
    return pl.col("y") * (pl.col("T") * (pl.col("S") * pl.col("k")))


def calc_val_2610_31153_form_f(a: float, j: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31153.

    **Source**:
    - Title: Balanced Posted Prices in Stationary Two-Sided Markets (2026)
    - Authors: Ilan Reuven Cohen
    - Citation Key: `arxiv_2610_31153`

    **KaTeX Formula**:
    $$
    aj := min r∈Rj ajr, vj :=max k∈K vk({j}), J := {j ∈M : aj < vj}.
    $$

    Args:
        a (float): Input parameter `a`.
        j (float): Input parameter `j`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * j)


def expr_val_2610_31153_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_31153_form_f`."""
    return pl.col("a") * pl.col("j")


def calc_val_2610_30212_form_a(
    e: float, h: float, m: float, n: float, o: float, p: float, r: float, t: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_30212.

    **Source**:
    - Title: A Consolidated Deployment Edition of a Microservice Core-Banking Platform: Composing Services by Reference into Three Hosts (2026)
    - Authors: Tomisin Fagbola
    - Citation Key: `arxiv_2610_30212`

    **KaTeX Formula**:
    $$
    per month, Nine-service = 81.09.
    $$

    Args:
        e (float): Input parameter `e`.
        h (float): Input parameter `h`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(e * h * m * n * o * p * r * t)


def expr_val_2610_30212_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_30212_form_a`."""
    return (
        pl.col("e")
        * pl.col("h")
        * pl.col("m")
        * pl.col("n")
        * pl.col("o")
        * pl.col("p")
        * pl.col("r")
        * pl.col("t")
    )


def calc_val_2610_30212_form_9(
    e: float, h: float, m: float, n: float, o: float, p: float, r: float, t: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_30212.

    **Source**:
    - Title: A Consolidated Deployment Edition of a Microservice Core-Banking Platform: Composing Services by Reference into Three Hosts (2026)
    - Authors: Tomisin Fagbola
    - Citation Key: `arxiv_2610_30212`

    **KaTeX Formula**:
    $$
    per month, Edition = 63.07.
    $$

    Args:
        e (float): Input parameter `e`.
        h (float): Input parameter `h`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(e * h * m * n * o * p * r * t)


def expr_val_2610_30212_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_30212_form_9`."""
    return (
        pl.col("e")
        * pl.col("h")
        * pl.col("m")
        * pl.col("n")
        * pl.col("o")
        * pl.col("p")
        * pl.col("r")
        * pl.col("t")
    )


def calc_val_2610_30212_form_e(
    a: float, g: float, h: float, i: float, m: float, n: float, o: float, s: float, t: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_30212.

    **Source**:
    - Title: A Consolidated Deployment Edition of a Microservice Core-Banking Platform: Composing Services by Reference into Three Hosts (2026)
    - Authors: Tomisin Fagbola
    - Citation Key: `arxiv_2610_30212`

    **KaTeX Formula**:
    $$
    72.08 a month against
    $$

    Args:
        a (float): Input parameter `a`.
        g (float): Input parameter `g`.
        h (float): Input parameter `h`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(72.08 * a**3 * g * h * i * m * n**2 * o * s * t**2)


def expr_val_2610_30212_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_30212_form_e`."""
    return (
        72.08
        * pl.col("a") ** 3
        * pl.col("g")
        * pl.col("h")
        * pl.col("i")
        * pl.col("m")
        * pl.col("n") ** 2
        * pl.col("o")
        * pl.col("s")
        * pl.col("t") ** 2
    )


def calc_val_2610_30212_form_f(a: float, g: float, i: float, n: float, s: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_30212.

    **Source**:
    - Title: A Consolidated Deployment Edition of a Microservice Core-Banking Platform: Composing Services by Reference into Three Hosts (2026)
    - Authors: Tomisin Fagbola
    - Citation Key: `arxiv_2610_30212`

    **KaTeX Formula**:
    $$
    63.07 against
    $$

    Args:
        a (float): Input parameter `a`.
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(63.07 * a**2 * g * i * n * s * t)


def expr_val_2610_30212_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_30212_form_f`."""
    return (
        63.07
        * pl.col("a") ** 2
        * pl.col("g")
        * pl.col("i")
        * pl.col("n")
        * pl.col("s")
        * pl.col("t")
    )


def calc_val_2610_30212_form_0(a: float, g: float, i: float, n: float, s: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_30212.

    **Source**:
    - Title: A Consolidated Deployment Edition of a Microservice Core-Banking Platform: Composing Services by Reference into Three Hosts (2026)
    - Authors: Tomisin Fagbola
    - Citation Key: `arxiv_2610_30212`

    **KaTeX Formula**:
    $$
    57.67 against
    $$

    Args:
        a (float): Input parameter `a`.
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(57.67 * a**2 * g * i * n * s * t)


def expr_val_2610_30212_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_30212_form_0`."""
    return (
        57.67
        * pl.col("a") ** 2
        * pl.col("g")
        * pl.col("i")
        * pl.col("n")
        * pl.col("s")
        * pl.col("t")
    )


def calc_val_2610_29685_form_6(T: float, a: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    Ta,⃗n ≡ T⃗n(⃗ θa),
    $$

    Args:
        T (float): Input parameter `T`.
        a (float): Input parameter `a`.

    Returns:
        float: Calculated metric value.
    """
    return float(T * a)


def expr_val_2610_29685_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_29685_form_6`."""
    return pl.col("T") * pl.col("a")


def calc_val_2610_29685_form_5(W: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    W -1
    $$

    Args:
        W (float): Input parameter `W`.

    Returns:
        float: Calculated metric value.
    """
    return float(W - 1)


def expr_val_2610_29685_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_29685_form_5`."""
    return pl.col("W") - 1


def calc_val_2610_29685_form_1(W: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    W -1
    $$

    Args:
        W (float): Input parameter `W`.

    Returns:
        float: Calculated metric value.
    """
    return float(W - 1)


def expr_val_2610_29685_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_29685_form_1`."""
    return pl.col("W") - 1


def calc_val_2610_29685_form_e(
    N: float, c: float, e: float, f: float, i: float, n: float, o: float, s: float, t: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    Ncoefficients(K = 0) = 1, (84) Ncoefficients(K = 1) = Npars, Ncoefficients(K = 2) = Npars(Npars + 1)/2, Ncoefficients(K = 3) = Npars(Npars + 1)(Npars + 2)/6, ...
    $$

    Args:
        N (float): Input parameter `N`.
        c (float): Input parameter `c`.
        e (float): Input parameter `e`.
        f (float): Input parameter `f`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(N * (c * (o * (e * (f * (f * (i * (c * (i * (e * (n * (s * t))))))))))))


def expr_val_2610_29685_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_29685_form_e`."""
    return pl.col("N") * (
        pl.col("c")
        * (
            pl.col("o")
            * (
                pl.col("e")
                * (
                    pl.col("f")
                    * (
                        pl.col("f")
                        * (
                            pl.col("i")
                            * (
                                pl.col("c")
                                * (
                                    pl.col("i")
                                    * (pl.col("e") * (pl.col("n") * (pl.col("s") * pl.col("t"))))
                                )
                            )
                        )
                    )
                )
            )
        )
    )


def calc_val_2610_29685_form_c(
    N: float, c: float, e: float, f: float, i: float, n: float, o: float, s: float, t: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    Ncoefficients(K \le  0) = 1, (85) Ncoefficients(K \le  1) = Npars + 1, Ncoefficients(K \le  2) = (Npars +1)(Npars +2)/2, Ncoefficients(K \le  3) = (Npars +1)((Npars +2)(Npars +3)/6, ...
    $$

    Args:
        N (float): Input parameter `N`.
        c (float): Input parameter `c`.
        e (float): Input parameter `e`.
        f (float): Input parameter `f`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(N * (c * (o * (e * (f * (f * (i * (c * (i * (e * (n * (s * t))))))))))))


def expr_val_2610_29685_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_29685_form_c`."""
    return pl.col("N") * (
        pl.col("c")
        * (
            pl.col("o")
            * (
                pl.col("e")
                * (
                    pl.col("f")
                    * (
                        pl.col("f")
                        * (
                            pl.col("i")
                            * (
                                pl.col("c")
                                * (
                                    pl.col("i")
                                    * (pl.col("e") * (pl.col("n") * (pl.col("s") * pl.col("t"))))
                                )
                            )
                        )
                    )
                )
            )
        )
    )


def calc_val_2610_29066_form_1(P: float, f: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29066.

    **Source**:
    - Title: Zero Knowledge for Free up to Linear Query Bounds: Quasilinear-Size Constant-Query Zero-Knowledge PCPs (2026)
    - Authors: Inhyuk Park, Chenglin Fan
    - Citation Key: `arxiv_2610_29066`

    **KaTeX Formula**:
    $$
    Proof. F\times  is cyclic of order q -1; the rest holds in every cyclic group.
    $$

    Args:
        P (float): Input parameter `P`.
        f (float): Input parameter `f`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * f * o**2 * r)


def expr_val_2610_29066_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_29066_form_1`."""
    return pl.col("P") * pl.col("f") * pl.col("o") ** 2 * pl.col("r")


def calc_val_2610_29066_form_5(c: float, i: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29066.

    **Source**:
    - Title: Zero Knowledge for Free up to Linear Query Bounds: Quasilinear-Size Constant-Query Zero-Knowledge PCPs (2026)
    - Authors: Inhyuk Park, Chenglin Fan
    - Citation Key: `arxiv_2610_29066`

    **KaTeX Formula**:
    $$
    cit := 2d⌈tD/2⌉ D , EL := log2 cit, EC := log2 CD.
    $$

    Args:
        c (float): Input parameter `c`.
        i (float): Input parameter `i`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(c * i * t)


def expr_val_2610_29066_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_29066_form_5`."""
    return pl.col("c") * pl.col("i") * pl.col("t")


def calc_val_2610_29066_form_d(C: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29066.

    **Source**:
    - Title: Zero Knowledge for Free up to Linear Query Bounds: Quasilinear-Size Constant-Query Zero-Knowledge PCPs (2026)
    - Authors: Inhyuk Park, Chenglin Fan
    - Citation Key: `arxiv_2610_29066`

    **KaTeX Formula**:
    $$
    C := 26.38 (EC + EL) + 122,
    $$

    Args:
        C (float): Input parameter `C`.

    Returns:
        float: Calculated metric value.
    """
    return float(C)


def expr_val_2610_29066_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_29066_form_d`."""
    return pl.col("C")


def calc_val_2610_29066_form_b(K: float, L: float, c: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29066.

    **Source**:
    - Title: Zero Knowledge for Free up to Linear Query Bounds: Quasilinear-Size Constant-Query Zero-Knowledge PCPs (2026)
    - Authors: Inhyuk Park, Chenglin Fan
    - Citation Key: `arxiv_2610_29066`

    **KaTeX Formula**:
    $$
    L1L2 (3 \cdot  2-1/3K1/3 c1/3 +6c) < 1 L2 + 1 - 2c.
    $$

    Args:
        K (float): Input parameter `K`.
        L (float): Input parameter `L`.
        c (float): Input parameter `c`.

    Returns:
        float: Calculated metric value.
    """
    return float((L**2 * (12 * c + 12 - (2 / 27) / (K * c)) < 2 * L - 2 * c + 1))


def expr_val_2610_29066_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_29066_form_b`."""
    return (
        pl.col("L") ** 2 * (12 * pl.col("c") + 12 - (2 / 27) / (pl.col("K") * pl.col("c")))
        < 2 * pl.col("L") - 2 * pl.col("c") + 1
    )


def calc_val_2610_29066_form_4(P: float, f: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29066.

    **Source**:
    - Title: Zero Knowledge for Free up to Linear Query Bounds: Quasilinear-Size Constant-Query Zero-Knowledge PCPs (2026)
    - Authors: Inhyuk Park, Chenglin Fan
    - Citation Key: `arxiv_2610_29066`

    **KaTeX Formula**:
    $$
    Proof. f mod (Xn - b) = ∑t Xtft(b).
    $$

    Args:
        P (float): Input parameter `P`.
        f (float): Input parameter `f`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * f * o**2 * r)


def expr_val_2610_29066_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_29066_form_4`."""
    return pl.col("P") * pl.col("f") * pl.col("o") ** 2 * pl.col("r")


def calc_val_2610_29066_form_9(P: float, f: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29066.

    **Source**:
    - Title: Zero Knowledge for Free up to Linear Query Bounds: Quasilinear-Size Constant-Query Zero-Knowledge PCPs (2026)
    - Authors: Inhyuk Park, Chenglin Fan
    - Citation Key: `arxiv_2610_29066`

    **KaTeX Formula**:
    $$
    Proof. Σ = spanev(Sh) ⊆ spanΦ and spanΨ = spanΨ′ +Σ; apply the modular law X ∩ (Y +Σ) = (X ∩ Y ) + Σ for Σ ⊆ X.
    $$

    Args:
        P (float): Input parameter `P`.
        f (float): Input parameter `f`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * f * o**2 * r)


def expr_val_2610_29066_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_29066_form_9`."""
    return pl.col("P") * pl.col("f") * pl.col("o") ** 2 * pl.col("r")


def calc_c_e_x_a_c_t_form_f(C: float, L: float, a: float, g: float, l: float, o: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29066.

    **Source**:
    - Title: Zero Knowledge for Free up to Linear Query Bounds: Quasilinear-Size Constant-Query Zero-Knowledge PCPs (2026)
    - Authors: Inhyuk Park, Chenglin Fan
    - Citation Key: `arxiv_2610_29066`

    **KaTeX Formula**:
    $$
    Cexact = 27 + log2 80 + log2 a + (15 + log2 2660) (EC + EL),
    $$

    Args:
        C (float): Input parameter `C`.
        L (float): Input parameter `L`.
        a (float): Input parameter `a`.
        g (float): Input parameter `g`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.

    Returns:
        float: Calculated metric value.
    """
    return float(
        2 * a * g * l * o
        + 280 * g * l * o
        + (math.e * C + math.e * L) * (22660 * g * l * o + 15)
        + 27
    )


def expr_c_e_x_a_c_t_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_e_x_a_c_t_form_f`."""
    return (
        2 * pl.col("a") * pl.col("g") * pl.col("l") * pl.col("o")
        + 280 * pl.col("g") * pl.col("l") * pl.col("o")
        + (math.e * pl.col("C") + math.e * pl.col("L"))
        * (22660 * pl.col("g") * pl.col("l") * pl.col("o") + 15)
        + 27
    )


def calc_val_2610_29066_form_6(L: float, R: float, c: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29066.

    **Source**:
    - Title: Zero Knowledge for Free up to Linear Query Bounds: Quasilinear-Size Constant-Query Zero-Knowledge PCPs (2026)
    - Authors: Inhyuk Park, Chenglin Fan
    - Citation Key: `arxiv_2610_29066`

    **KaTeX Formula**:
    $$
    (R1) c < 1 4L1L2 2 , (R2) c \le  1 8 , (R3) 3 \cdot  2 2/3 (L1L2 + L2(1 + c) 1/3 )c1/3 \le  2(1 - 2c).
    $$

    Args:
        L (float): Input parameter `L`.
        R (float): Input parameter `R`.
        c (float): Input parameter `c`.

    Returns:
        float: Calculated metric value.
    """
    return float((R * c < 308 * L**2))


def expr_val_2610_29066_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_29066_form_6`."""
    return pl.col("R") * pl.col("c") < 308 * pl.col("L") ** 2


def calc_val_2610_29049_form_a(P: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29049.

    **Source**:
    - Title: ART-MPG: Autoregressive R/T Manifold Path Guiding (2026)
    - Authors: Zehao Zhao, Yanyang Yang, Xiaole Zhang et al.
    - Citation Key: `arxiv_2610_29049`

    **KaTeX Formula**:
    $$
    Pr[Jd > M] = (1 - R)M \le  (1 - qT R)M = Pr[Jn > M].
    $$

    Args:
        P (float): Input parameter `P`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * r)


def expr_val_2610_29049_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_29049_form_a`."""
    return pl.col("P") * pl.col("r")


def calc_val_2610_28285_form_9(K: float, g: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_28285.

    **Source**:
    - Title: Conformal Koopman Certificates for Nonlinear Multi-Agent Consensus on Time-Evolving Graphs (2026)
    - Authors: Indrakshi Dey, Nicola Marchetti
    - Citation Key: `arxiv_2610_28285`

    **KaTeX Formula**:
    $$
    (Kg)(x, m) := E[g(zk+1) ∣∣ zk = (x, m)] = ∑ m′∈MPmm′ g(Fm(x),m′ ).
    $$

    Args:
        K (float): Input parameter `K`.
        g (float): Input parameter `g`.

    Returns:
        float: Calculated metric value.
    """
    return float(K * g)


def expr_val_2610_28285_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_28285_form_9`."""
    return pl.col("K") * pl.col("g")


def calc_val_2610_28285_form_1(P: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_28285.

    **Source**:
    - Title: Conformal Koopman Certificates for Nonlinear Multi-Agent Consensus on Time-Evolving Graphs (2026)
    - Authors: Indrakshi Dey, Nicola Marchetti
    - Citation Key: `arxiv_2610_28285`

    **KaTeX Formula**:
    $$
    Pr {dk \le  q1-δ ̂ ρ k d0, ∀k ∈ [k0,Kcal]} \ge  1- δ.
    $$

    Args:
        P (float): Input parameter `P`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * r)


def expr_val_2610_28285_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_28285_form_1`."""
    return pl.col("P") * pl.col("r")


def calc_u_o_t_v_form_c(T: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_28203.

    **Source**:
    - Title: JAXbounce: A Continuous-Control Pong-Like Benchmark for Active Inference Beyond Low Dimensional Environments (2026)
    - Authors: Chaitanya Kaul, Markus Klar, Sebastian Stein et al.
    - Citation Key: `arxiv_2610_28203`

    **KaTeX Formula**:
    $$
    uov t = r + T2 - | yf,t - ˜ ybat |,
    $$

    Args:
        T (float): Input parameter `T`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(2 * T + r)


def expr_u_o_t_v_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_o_t_v_form_c`."""
    return 2 * pl.col("T") + pl.col("r")


def calc_val_2610_27416_form_0(a: float, f: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27416.

    **Source**:
    - Title: Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization (2026)
    - Authors: Koichi Miyamoto
    - Citation Key: `arxiv_2610_27416`

    **KaTeX Formula**:
    $$
    f a,c,n MAdd (i) := {(i + c -a mod 2n -a+1) +a ; i \ge  a i ; otherwise ,
    $$

    Args:
        a (float): Input parameter `a`.
        f (float): Input parameter `f`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * f)


def expr_val_2610_27416_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_27416_form_0`."""
    return pl.col("a") * pl.col("f")


def calc_val_2610_27416_form_a(A: float, j: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27416.

    **Source**:
    - Title: Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization (2026)
    - Authors: Koichi Miyamoto
    - Citation Key: `arxiv_2610_27416`

    **KaTeX Formula**:
    $$
    Aj,j-2,k,l i1,...,ij ,i′1 ,...,i′j-2 (t) := δi1,i′1 \cdot  \cdot  \cdot  δik-1,i′k-1 δik+1,i′k \cdot  \cdot  \cdot  δil-1,i′l-2 δil+1,i′l-1 \cdot  δij,i′j-2 ( ˆB(t) ˆBT (t))ik,il .
    $$

    Args:
        A (float): Input parameter `A`.
        j (float): Input parameter `j`.

    Returns:
        float: Calculated metric value.
    """
    return float(A * j)


def expr_val_2610_27416_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_27416_form_a`."""
    return pl.col("A") * pl.col("j")


def calc_val_2610_27416_form_6(A: float, j: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27416.

    **Source**:
    - Title: Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization (2026)
    - Authors: Koichi Miyamoto
    - Citation Key: `arxiv_2610_27416`

    **KaTeX Formula**:
    $$
    Aj,j-1,l (t) := j-1∑ k=0 I ⊗k ⊗ ˆB:,l(t) ⊗ I ⊗(j-k-1) ,
    $$

    Args:
        A (float): Input parameter `A`.
        j (float): Input parameter `j`.

    Returns:
        float: Calculated metric value.
    """
    return float(A * j)


def expr_val_2610_27416_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_27416_form_6`."""
    return pl.col("A") * pl.col("j")


def calc_val_2610_27416_form_2(A: float, j: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27416.

    **Source**:
    - Title: Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization (2026)
    - Authors: Koichi Miyamoto
    - Citation Key: `arxiv_2610_27416`

    **KaTeX Formula**:
    $$
    Aj,j+s-1 (t) := j∑ k=1 I ⊗(k-1) ⊗ ˆ F (t) ⊗ I ⊗(j-k) .
    $$

    Args:
        A (float): Input parameter `A`.
        j (float): Input parameter `j`.

    Returns:
        float: Calculated metric value.
    """
    return float(A * j)


def expr_val_2610_27416_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_27416_form_2`."""
    return pl.col("A") * pl.col("j")


def calc_val_2610_27416_form_1(Y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27416.

    **Source**:
    - Title: Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization (2026)
    - Authors: Koichi Miyamoto
    - Citation Key: `arxiv_2610_27416`

    **KaTeX Formula**:
    $$
    Y := Y1 ...YJ  ,
    $$

    Args:
        Y (float): Input parameter `Y`.

    Returns:
        float: Calculated metric value.
    """
    return float(Y)


def expr_val_2610_27416_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_27416_form_1`."""
    return pl.col("Y")


def calc_val_2610_27416_form_f(U: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27416.

    **Source**:
    - Title: Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization (2026)
    - Authors: Koichi Miyamoto
    - Citation Key: `arxiv_2610_27416`

    **KaTeX Formula**:
    $$
    U := 2 (√3 log (20LS) + 2) √σ2T ,
    $$

    Args:
        U (float): Input parameter `U`.

    Returns:
        float: Calculated metric value.
    """
    return float(U)


def expr_val_2610_27416_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_27416_form_f`."""
    return pl.col("U")


def calc_val_2610_27416_form_e(
    V: float, Y: float, h: float, i: float, m: float, s: float, t: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27416.

    **Source**:
    - Title: Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization (2026)
    - Authors: Koichi Miyamoto
    - Citation Key: `arxiv_2610_27416`

    **KaTeX Formula**:
    $$
    V hist mY,ϵ |0⟩ |0⟩ |0⟩ = |Ψhist mY,ϵ ⟩ := |0⟩ ∣∣∣ ˜˜MY,hist〉 + |0⊥⟩ .
    $$

    Args:
        V (float): Input parameter `V`.
        Y (float): Input parameter `Y`.
        h (float): Input parameter `h`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(V * Y * h * i * m * s * t)


def expr_val_2610_27416_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_27416_form_e`."""
    return (
        pl.col("V")
        * pl.col("Y")
        * pl.col("h")
        * pl.col("i")
        * pl.col("m")
        * pl.col("s")
        * pl.col("t")
    )


def calc_val_2610_27416_form_8(M: float, Y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27416.

    **Source**:
    - Title: Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization (2026)
    - Authors: Koichi Miyamoto
    - Citation Key: `arxiv_2610_27416`

    **KaTeX Formula**:
    $$
    MY,hist = (Mn,i Y,hist)n∈[r]0,i∈[N] := (mY(t0))T . . . (mY (tr ))T  .
    $$

    Args:
        M (float): Input parameter `M`.
        Y (float): Input parameter `Y`.

    Returns:
        float: Calculated metric value.
    """
    return float(M * Y)


def expr_val_2610_27416_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_27416_form_8`."""
    return pl.col("M") * pl.col("Y")


def calc_val_2610_27416_form_3(f: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27416.

    **Source**:
    - Title: Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization (2026)
    - Authors: Koichi Miyamoto
    - Citation Key: `arxiv_2610_27416`

    **KaTeX Formula**:
    $$
    f := r∑ n=1 N∑ i=1 Cn,iXi tn ,
    $$

    Args:
        f (float): Input parameter `f`.

    Returns:
        float: Calculated metric value.
    """
    return float(f)


def expr_val_2610_27416_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_27416_form_3`."""
    return pl.col("f")


def calc_a_form_4(m: float, x: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27416.

    **Source**:
    - Title: Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization (2026)
    - Authors: Koichi Miyamoto
    - Citation Key: `arxiv_2610_27416`

    **KaTeX Formula**:
    $$
    A = ( m2x m2xy m2xy m2y ) , B = (σx 0 0 σy ) , F = (λx 0 0 0 0 0 0 0 0 0 0 0 0 0 0 λy ) ,
    $$

    Args:
        m (float): Input parameter `m`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(16 * m**4 * x**3 * y**3)


def expr_a_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_form_4`."""
    return 16 * pl.col("m") ** 4 * pl.col("x") ** 3 * pl.col("y") ** 3


def calc_val_2610_27416_form_d(N: float, dS: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27416.

    **Source**:
    - Title: Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization (2026)
    - Authors: Koichi Miyamoto
    - Citation Key: `arxiv_2610_27416`

    **KaTeX Formula**:
    $$
    dSN-1(u, u′ ) := 2√ σ2T L ∥u-u′∥,
    $$

    Args:
        N (float): Input parameter `N`.
        dS (float): Input parameter `dS`.

    Returns:
        float: Calculated metric value.
    """
    return float(N * dS - 1)


def expr_val_2610_27416_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_27416_form_d`."""
    return pl.col("N") * pl.col("dS") - 1


def calc_val_2610_27057_form_8(B: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27057.

    **Source**:
    - Title: Probing Lepton Flavor Violation at FCC-ee (2026)
    - Authors: L. Allwicher, R. Bartocci, M. Cepeda et al.
    - Citation Key: `arxiv_2610_27057`

    **KaTeX Formula**:
    $$
    (B5) ) + \cdot  \cdot  \cdot  ,
    $$

    Args:
        B (float): Input parameter `B`.

    Returns:
        float: Calculated metric value.
    """
    return float(5 * B)


def expr_val_2610_27057_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_27057_form_8`."""
    return 5 * pl.col("B")


def calc_val_2610_27057_form_5(C: float, e: float, i: float, j: float, k: float, l: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27057.

    **Source**:
    - Title: Probing Lepton Flavor Violation at FCC-ee (2026)
    - Authors: L. Allwicher, R. Bartocci, M. Cepeda et al.
    - Citation Key: `arxiv_2610_27057`

    **KaTeX Formula**:
    $$
    +C ee kkij +C le kkij ) + \cdot  \cdot  \cdot  , (B7)
    $$

    Args:
        C (float): Input parameter `C`.
        e (float): Input parameter `e`.
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.
        k (float): Input parameter `k`.
        l (float): Input parameter `l`.

    Returns:
        float: Calculated metric value.
    """
    return float(C * e**2 * i * j * k**2 + C * e * i * j * k**2 * l)


def expr_val_2610_27057_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_27057_form_5`."""
    return pl.col("C") * pl.col("e") ** 2 * pl.col("i") * pl.col("j") * pl.col("k") ** 2 + pl.col(
        "C"
    ) * pl.col("e") * pl.col("i") * pl.col("j") * pl.col("k") ** 2 * pl.col("l")


def calc_l_v_r_r_e_e_2223_form_7(
    C: float, H: float, Z: float, e: float, g: float, m: float, v: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27057.

    **Source**:
    - Title: Probing Lepton Flavor Violation at FCC-ee (2026)
    - Authors: L. Allwicher, R. Bartocci, M. Cepeda et al.
    - Citation Key: `arxiv_2610_27057`

    **KaTeX Formula**:
    $$
    LVRR ee 2223 = g2 1 v2 2m2Z CHe 23 +C ee 2223 . (B29)
    $$

    Args:
        C (float): Input parameter `C`.
        H (float): Input parameter `H`.
        Z (float): Input parameter `Z`.
        e (float): Input parameter `e`.
        g (float): Input parameter `g`.
        m (float): Input parameter `m`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(21252 * C * H * Z * e * g * m * v + 8 * C * e**2)


def expr_l_v_r_r_e_e_2223_form_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_v_r_r_e_e_2223_form_7`."""
    return (
        21252
        * pl.col("C")
        * pl.col("H")
        * pl.col("Z")
        * pl.col("e")
        * pl.col("g")
        * pl.col("m")
        * pl.col("v")
        + 8 * pl.col("C") * pl.col("e") ** 2
    )


def calc_val_2610_26568_form_b(t: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_26568.

    **Source**:
    - Title: Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games (2026)
    - Authors: Durgam Latha, Dion Reji, Dorde Zikelic et al.
    - Citation Key: `arxiv_2610_26568`

    **KaTeX Formula**:
    $$
    xt,1 → y1 → x\cdot ,2 → y2 → \cdot  \cdot  \cdot  → yk-1 → x\cdot ,k → s′
    $$

    Args:
        t (float): Input parameter `t`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(t * x)


def expr_val_2610_26568_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_26568_form_b`."""
    return pl.col("t") * pl.col("x")


def calc_val_2610_26568_form_2(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_26568.

    **Source**:
    - Title: Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games (2026)
    - Authors: Durgam Latha, Dion Reji, Dorde Zikelic et al.
    - Citation Key: `arxiv_2610_26568`

    **KaTeX Formula**:
    $$
    P (Cyl(u+)) = P (Cyl(u)) \cdot  f, f = σ(hmax G (u))(a) δ(s, a)(t)π(w-o)(t)(b) δ(t, b)(s′ ).
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_2610_26568_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_26568_form_2`."""
    return pl.col("P")


def calc_l_i_m_i_n_f_n_b_n_form_0(
    A: float, f: float, i: float, k: float, l: float, m: float, n: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_26568.

    **Source**:
    - Title: Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games (2026)
    - Authors: Durgam Latha, Dion Reji, Dorde Zikelic et al.
    - Citation Key: `arxiv_2610_26568`

    **KaTeX Formula**:
    $$
    lim inf n Bn = 1k liminf m Am, lim sup n Bn = 1k limsup m Am.
    $$

    Args:
        A (float): Input parameter `A`.
        f (float): Input parameter `f`.
        i (float): Input parameter `i`.
        k (float): Input parameter `k`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(A * f * i**2 * k * l * m**3 * n)


def expr_l_i_m_i_n_f_n_b_n_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_i_m_i_n_f_n_b_n_form_0`."""
    return (
        pl.col("A")
        * pl.col("f")
        * pl.col("i") ** 2
        * pl.col("k")
        * pl.col("l")
        * pl.col("m") ** 3
        * pl.col("n")
    )


def calc_val_2610_26568_form_a(X: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_26568.

    **Source**:
    - Title: Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games (2026)
    - Authors: Durgam Latha, Dion Reji, Dorde Zikelic et al.
    - Citation Key: `arxiv_2610_26568`

    **KaTeX Formula**:
    $$
    X
    $$

    Args:
        X (float): Input parameter `X`.

    Returns:
        float: Calculated metric value.
    """
    return float(X)


def expr_val_2610_26568_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_26568_form_a`."""
    return pl.col("X")


def calc_val_2610_26568_form_7(f: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_26568.

    **Source**:
    - Title: Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games (2026)
    - Authors: Durgam Latha, Dion Reji, Dorde Zikelic et al.
    - Citation Key: `arxiv_2610_26568`

    **KaTeX Formula**:
    $$
    fx,a(V ) = ∑ y δ(x, a)(y)(r(x, a, y) + γV (y)),
    $$

    Args:
        f (float): Input parameter `f`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(f * x)


def expr_val_2610_26568_form_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_26568_form_7`."""
    return pl.col("f") * pl.col("x")


def calc_val_2610_26568_form_d(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_26568.

    **Source**:
    - Title: Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games (2026)
    - Authors: Durgam Latha, Dion Reji, Dorde Zikelic et al.
    - Citation Key: `arxiv_2610_26568`

    **KaTeX Formula**:
    $$
    P((t, τ ), ⊤) = conv{ˆ δt,b : b ∈ A(t)}, ˆ δt,b((y, b)) = δ(t, b)(y).
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_2610_26568_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_26568_form_d`."""
    return pl.col("P")


def calc_val_2610_25605_form_d(ds: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    ds(xi, xj ) = ∥∥∥˜ π(s) (xi) - ˜ π(s) (xj)∥∥∥2 .
    $$

    Args:
        ds (float): Input parameter `ds`.

    Returns:
        float: Calculated metric value.
    """
    return float(ds)


def expr_val_2610_25605_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_25605_form_d`."""
    return pl.col("ds")


def calc_val_2610_25605_form_5(ds: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    ds(xi, xj ) = 1 - Tanimoto (π(s) (xi), π(s) (xj )) .
    $$

    Args:
        ds (float): Input parameter `ds`.

    Returns:
        float: Calculated metric value.
    """
    return float(ds)


def expr_val_2610_25605_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_25605_form_5`."""
    return pl.col("ds")


def calc_val_2610_25605_form_e(S: float, dT: float, dl: float, g: float, o: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    d log S dT
    $$

    Args:
        S (float): Input parameter `S`.
        dT (float): Input parameter `dT`.
        dl (float): Input parameter `dl`.
        g (float): Input parameter `g`.
        o (float): Input parameter `o`.

    Returns:
        float: Calculated metric value.
    """
    return float(dl * (o * (g * (S * dT))))


def expr_val_2610_25605_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_25605_form_e`."""
    return pl.col("dl") * (pl.col("o") * (pl.col("g") * (pl.col("S") * pl.col("dT"))))


def calc_z_m_i_x_form_7(
    a: float, de: float, i: float, l: float, n: float, o: float, z: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    zmix = zideal + znonideal,
    $$

    Args:
        a (float): Input parameter `a`.
        de (float): Input parameter `de`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * de * i * l * n**2 * o * z + a * de * i * l * z)


def expr_z_m_i_x_form_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_m_i_x_form_7`."""
    return pl.col("a") * pl.col("de") * pl.col("i") * pl.col("l") * pl.col("n") ** 2 * pl.col(
        "o"
    ) * pl.col("z") + pl.col("a") * pl.col("de") * pl.col("i") * pl.col("l") * pl.col("z")


def calc_e_j_form_6(R: float, T: float, e: float, j: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25581.

    **Source**:
    - Title: Characterization of integrating-sphere systematic effects for photon calibration of the KAGRA gravitational wave detector (2026)
    - Authors: Shingo Hido, Misato Onishi, Shinji Miyoki et al.
    - Citation Key: `arxiv_2610_25581`

    **KaTeX Formula**:
    $$
    ej = eTjeRj,
    $$

    Args:
        R (float): Input parameter `R`.
        T (float): Input parameter `T`.
        e (float): Input parameter `e`.
        j (float): Input parameter `j`.

    Returns:
        float: Calculated metric value.
    """
    return float(R * T * e**2 * j**2)


def expr_e_j_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_j_form_6`."""
    return pl.col("R") * pl.col("T") * pl.col("e") ** 2 * pl.col("j") ** 2


def calc_p_form_2(M: float, P: float, T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25581.

    **Source**:
    - Title: Characterization of integrating-sphere systematic effects for photon calibration of the KAGRA gravitational wave detector (2026)
    - Authors: Shingo Hido, Misato Onishi, Shinji Miyoki et al.
    - Citation Key: `arxiv_2610_25581`

    **KaTeX Formula**:
    $$
    P = PTM1 + PTM2
    $$

    Args:
        M (float): Input parameter `M`.
        P (float): Input parameter `P`.
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(3 * M * P * T)


def expr_p_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_form_2`."""
    return 3 * pl.col("M") * pl.col("P") * pl.col("T")


def calc_val_2610_25581_form_f(R: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25581.

    **Source**:
    - Title: Characterization of integrating-sphere systematic effects for photon calibration of the KAGRA gravitational wave detector (2026)
    - Authors: Shingo Hido, Misato Onishi, Shinji Miyoki et al.
    - Citation Key: `arxiv_2610_25581`

    **KaTeX Formula**:
    $$
    RRx,j = V A,Rx,j - VRxPD,d V A,Tx,j - VTx,j,d ,
    $$

    Args:
        R (float): Input parameter `R`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(R**2 * x)


def expr_val_2610_25581_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_25581_form_f`."""
    return pl.col("R") ** 2 * pl.col("x")


def calc_val_2610_25581_form_d(K: float, R: float, S: float, W: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25581.

    **Source**:
    - Title: Characterization of integrating-sphere systematic effects for photon calibration of the KAGRA gravitational wave detector (2026)
    - Authors: Shingo Hido, Misato Onishi, Shinji Miyoki et al.
    - Citation Key: `arxiv_2610_25581`

    **KaTeX Formula**:
    $$
    RWSK,j = κWSK (V B,WSK,j - VWSK,d) V B,Tx,j - VTx,j,d .
    $$

    Args:
        K (float): Input parameter `K`.
        R (float): Input parameter `R`.
        S (float): Input parameter `S`.
        W (float): Input parameter `W`.

    Returns:
        float: Calculated metric value.
    """
    return float(R * (W * (K * S)))


def expr_val_2610_25581_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_25581_form_d`."""
    return pl.col("R") * (pl.col("W") * (pl.col("K") * pl.col("S")))


def calc_val_2610_25581_form_3(K: float, R: float, S: float, W: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25581.

    **Source**:
    - Title: Characterization of integrating-sphere systematic effects for photon calibration of the KAGRA gravitational wave detector (2026)
    - Authors: Shingo Hido, Misato Onishi, Shinji Miyoki et al.
    - Citation Key: `arxiv_2610_25581`

    **KaTeX Formula**:
    $$
    RWSK,Rx,j = V B,WSK,j - VWSK,d V B,Tx,j - VTx,j,d ,
    $$

    Args:
        K (float): Input parameter `K`.
        R (float): Input parameter `R`.
        S (float): Input parameter `S`.
        W (float): Input parameter `W`.

    Returns:
        float: Calculated metric value.
    """
    return float(R * (W * (K * S)))


def expr_val_2610_25581_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_25581_form_3`."""
    return pl.col("R") * (pl.col("W") * (pl.col("K") * pl.col("S")))


def calc_val_2610_25581_form_0(R: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25581.

    **Source**:
    - Title: Characterization of integrating-sphere systematic effects for photon calibration of the KAGRA gravitational wave detector (2026)
    - Authors: Shingo Hido, Misato Onishi, Shinji Miyoki et al.
    - Citation Key: `arxiv_2610_25581`

    **KaTeX Formula**:
    $$
    Ri,pol(Θ) = 〈 V i,Θ - ⟨V Θ,d⟩ V i,ref,Θ - ⟨V ref,Θ,d⟩ 〉 ,
    $$

    Args:
        R (float): Input parameter `R`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(R * i)


def expr_val_2610_25581_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_25581_form_0`."""
    return pl.col("R") * pl.col("i")


def calc_val_2610_25581_form_c(G: float, P: float, S: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25581.

    **Source**:
    - Title: Characterization of integrating-sphere systematic effects for photon calibration of the KAGRA gravitational wave detector (2026)
    - Authors: Shingo Hido, Misato Onishi, Shinji Miyoki et al.
    - Citation Key: `arxiv_2610_25581`

    **KaTeX Formula**:
    $$
    uGPS,pol = 0.087\%,
    $$

    Args:
        G (float): Input parameter `G`.
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(u * (G * (P * S)))


def expr_val_2610_25581_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_25581_form_c`."""
    return pl.col("u") * (pl.col("G") * (pl.col("P") * pl.col("S")))


def calc_val_2610_25581_form_7(R: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25581.

    **Source**:
    - Title: Characterization of integrating-sphere systematic effects for photon calibration of the KAGRA gravitational wave detector (2026)
    - Authors: Shingo Hido, Misato Onishi, Shinji Miyoki et al.
    - Citation Key: `arxiv_2610_25581`

    **KaTeX Formula**:
    $$
    Ri,pos = 〈 V i,pos - ⟨V pos,d⟩ V i,ref,pos - ⟨V ref,pos,d⟩ 〉 ,
    $$

    Args:
        R (float): Input parameter `R`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(R * i)


def expr_val_2610_25581_form_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_25581_form_7`."""
    return pl.col("R") * pl.col("i")


def calc_r_p_o_s_form_9(R: float, c: float, o: float, p: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25581.

    **Source**:
    - Title: Characterization of integrating-sphere systematic effects for photon calibration of the KAGRA gravitational wave detector (2026)
    - Authors: Shingo Hido, Misato Onishi, Shinji Miyoki et al.
    - Citation Key: `arxiv_2610_25581`

    **KaTeX Formula**:
    $$
    rpos = Rpos Rc ,
    $$

    Args:
        R (float): Input parameter `R`.
        c (float): Input parameter `c`.
        o (float): Input parameter `o`.
        p (float): Input parameter `p`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(R**2 * c * o * p * s)


def expr_r_p_o_s_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_p_o_s_form_9`."""
    return pl.col("R") ** 2 * pl.col("c") * pl.col("o") * pl.col("p") * pl.col("s")


def calc_val_2610_25581_form_e(G: float, P: float, S: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25581.

    **Source**:
    - Title: Characterization of integrating-sphere systematic effects for photon calibration of the KAGRA gravitational wave detector (2026)
    - Authors: Shingo Hido, Misato Onishi, Shinji Miyoki et al.
    - Citation Key: `arxiv_2610_25581`

    **KaTeX Formula**:
    $$
    uGPS,pos|full = 0.21\%,
    $$

    Args:
        G (float): Input parameter `G`.
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(u * (G * (P * S)))


def expr_val_2610_25581_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_25581_form_e`."""
    return pl.col("u") * (pl.col("G") * (pl.col("P") * pl.col("S")))


def calc_u_2_s_1_form_f(L: float, M: float, P: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25581.

    **Source**:
    - Title: Characterization of integrating-sphere systematic effects for photon calibration of the KAGRA gravitational wave detector (2026)
    - Authors: Shingo Hido, Misato Onishi, Shinji Miyoki et al.
    - Citation Key: `arxiv_2610_25581`

    **KaTeX Formula**:
    $$
    u2s1 = u2LPM,ang|0 + u2LPM,pos,GSK + u2GPS,ang|0 + u2GPS,pos,WSK@U.Toyama
    $$

    Args:
        L (float): Input parameter `L`.
        M (float): Input parameter `M`.
        P (float): Input parameter `P`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(2 * L * M * P * u)


def expr_u_2_s_1_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_2_s_1_form_f`."""
    return 2 * pl.col("L") * pl.col("M") * pl.col("P") * pl.col("u")


def calc_u_2_s_3_form_2(G: float, P: float, S: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25581.

    **Source**:
    - Title: Characterization of integrating-sphere systematic effects for photon calibration of the KAGRA gravitational wave detector (2026)
    - Authors: Shingo Hido, Misato Onishi, Shinji Miyoki et al.
    - Citation Key: `arxiv_2610_25581`

    **KaTeX Formula**:
    $$
    u2s3 = u2GPS,ang|0 + u2GPS,pol + u2GPS,pos,WSK@Tx .
    $$

    Args:
        G (float): Input parameter `G`.
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(u * (2 * (G * (P * S))))


def expr_u_2_s_3_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_2_s_3_form_2`."""
    return pl.col("u") * (2 * (pl.col("G") * (pl.col("P") * pl.col("S"))))


def calc_u_2_s_4_form_7(G: float, P: float, S: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25581.

    **Source**:
    - Title: Characterization of integrating-sphere systematic effects for photon calibration of the KAGRA gravitational wave detector (2026)
    - Authors: Shingo Hido, Misato Onishi, Shinji Miyoki et al.
    - Citation Key: `arxiv_2610_25581`

    **KaTeX Formula**:
    $$
    u2s4 = 2u2GPS,ang|0 + 2u2GPS,pol + u2GPS,pos,WSK@Rx + u2GPS,pos,WSK@Tx .
    $$

    Args:
        G (float): Input parameter `G`.
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(2 * (u * (2 * (G * (P * S)))))


def expr_u_2_s_4_form_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_2_s_4_form_7`."""
    return 2 * (pl.col("u") * (2 * (pl.col("G") * (pl.col("P") * pl.col("S")))))


def calc_val_2610_25581_form_5(G: float, P: float, S: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25581.

    **Source**:
    - Title: Characterization of integrating-sphere systematic effects for photon calibration of the KAGRA gravitational wave detector (2026)
    - Authors: Shingo Hido, Misato Onishi, Shinji Miyoki et al.
    - Citation Key: `arxiv_2610_25581`

    **KaTeX Formula**:
    $$
    uGPS,pos,WSK@Rx = uGPS,pos,RxPD = uGPS,pos|±14 mm = 0.21\%.
    $$

    Args:
        G (float): Input parameter `G`.
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(u * (G * (P * S)))


def expr_val_2610_25581_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_25581_form_5`."""
    return pl.col("u") * (pl.col("G") * (pl.col("P") * pl.col("S")))


def calc_val_2609_07617_form_8(i: float, q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_07617.

    **Source**:
    - Title: Forecasting the Winner of a Live Tennis Match (2026)
    - Authors: Charles Xie, Aneesh Muppidi
    - Citation Key: `arxiv_2609_07617`

    **KaTeX Formula**:
    $$
    qi,t = 1 1 + 10(Rj,t-Ri,t)/400 ,
    $$

    Args:
        i (float): Input parameter `i`.
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float(i * q)


def expr_val_2609_07617_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_07617_form_8`."""
    return pl.col("i") * pl.col("q")


def calc_val_2609_07617_form_0(R: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_07617.

    **Source**:
    - Title: Forecasting the Winner of a Live Tennis Match (2026)
    - Authors: Charles Xie, Aneesh Muppidi
    - Citation Key: `arxiv_2609_07617`

    **KaTeX Formula**:
    $$
    Ri,t+1 = Ri,t +Ki,t(Si,t -qi,t), Ki,t = 250 (mi,t + 5)0.4 ,
    $$

    Args:
        R (float): Input parameter `R`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(R * i)


def expr_val_2609_07617_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_07617_form_0`."""
    return pl.col("R") * pl.col("i")


def calc_d_q_form_2(q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_07617.

    **Source**:
    - Title: Forecasting the Winner of a Live Tennis Match (2026)
    - Authors: Charles Xie, Aneesh Muppidi
    - Citation Key: `arxiv_2609_07617`

    **KaTeX Formula**:
    $$
    D(q) = q2 q2 + (1 - q)2 ,
    $$

    Args:
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float(4 * q**2 - 2 * q + 2)


def expr_d_q_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_q_form_2`."""
    return 4 * pl.col("q") ** 2 - 2 * pl.col("q") + 2


def calc_eq_a_p_b_p_form_e(p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_07617.

    **Source**:
    - Title: Forecasting the Winner of a Live Tennis Match (2026)
    - Authors: Charles Xie, Aneesh Muppidi
    - Citation Key: `arxiv_2609_07617`

    **KaTeX Formula**:
    $$
    pa = pb = p.
    $$

    Args:
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(p)


def expr_eq_a_p_b_p_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_eq_a_p_b_p_form_e`."""
    return pl.col("p")


def calc_val_2608_12291_form_f(T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    T := lim s↗S A(s) ∈ (0, ∞].
    $$

    Args:
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(T)


def expr_val_2608_12291_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_12291_form_f`."""
    return pl.col("T")


def calc_val_2608_12291_form_7(X: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    Xt := ΠΓ(t), t < T.
    $$

    Args:
        X (float): Input parameter `X`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(X * t)


def expr_val_2608_12291_form_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_12291_form_7`."""
    return pl.col("X") * pl.col("t")


def calc_val_2608_12291_form_1(T: float, X: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    XT := lim t↑T Xt = lim s↑S Πs = ΠS-.
    $$

    Args:
        T (float): Input parameter `T`.
        X (float): Input parameter `X`.

    Returns:
        float: Calculated metric value.
    """
    return float(T * X)


def expr_val_2608_12291_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_12291_form_1`."""
    return pl.col("T") * pl.col("X")


def calc_val_2608_12291_form_4(C: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    C := {(t, x) ∈ S : V (t, x) < g(x)}, D := {(t, x) ∈ S : V (t, x) = g(x)}.
    $$

    Args:
        C (float): Input parameter `C`.

    Returns:
        float: Calculated metric value.
    """
    return float(C)


def expr_val_2608_12291_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_12291_form_4`."""
    return pl.col("C")


def calc_s_form_c(R: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    S = R+ \times  [0, 1].
    $$

    Args:
        R (float): Input parameter `R`.

    Returns:
        float: Calculated metric value.
    """
    return float(R)


def expr_s_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_form_c`."""
    return pl.col("R")


def calc_val_2608_12291_form_c(T: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    TT-t := {τ ∈ T : τ \le  T - t}.
    $$

    Args:
        T (float): Input parameter `T`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(T**2 - t)


def expr_val_2608_12291_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_12291_form_c`."""
    return pl.col("T") ** 2 - pl.col("t")


def calc_val_2608_12291_form_8(S: float, T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    ST := [0, T] \times  [0, 1].
    $$

    Args:
        S (float): Input parameter `S`.
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(S * T)


def expr_val_2608_12291_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_12291_form_8`."""
    return pl.col("S") * pl.col("T")


def calc_val_2608_12291_form_d(U: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    U := {(t, x) ∈ S : Lg(x) < -c(t)}.
    $$

    Args:
        U (float): Input parameter `U`.

    Returns:
        float: Calculated metric value.
    """
    return float(U)


def expr_val_2608_12291_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_12291_form_d`."""
    return pl.col("U")


def calc_val_2608_12291_form_0(K: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    Kr := {(t + s,Xx s ) : 0 \le  s \le  r}
    $$

    Args:
        K (float): Input parameter `K`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(K * r)


def expr_val_2608_12291_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_12291_form_0`."""
    return pl.col("K") * pl.col("r")


def calc_v_n_t_k_x_form_4(i: float, m: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    vn T (k, x) = min {g(x), ∫ ∆ 0 c(t + k∆ + u) du + P∆vn T (k + 1, \cdot )(x)}
    $$

    Args:
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(i * m * n)


def expr_v_n_t_k_x_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_n_t_k_x_form_4`."""
    return pl.col("i") * pl.col("m") * pl.col("n")


def calc_val_2608_12291_form_e(D: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    Dt := L˜x t -L˜ y t = ˜x- ˜ y + ∫ t 0 (µ(L˜x s ) - µ(L˜ y s )) ds.
    $$

    Args:
        D (float): Input parameter `D`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(D * t)


def expr_val_2608_12291_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_12291_form_e`."""
    return pl.col("D") * pl.col("t")


def calc_val_2608_12291_form_b(A: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    A := σ′ (x)σ(x)z∂xz + σ2 (x) 2 ∂xx + (σ′ (x)z)2 2 ∂zz.
    $$

    Args:
        A (float): Input parameter `A`.

    Returns:
        float: Calculated metric value.
    """
    return float(A)


def expr_val_2608_12291_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_12291_form_b`."""
    return pl.col("A")


def calc_val_2608_12291_form_9(
    P: float, i: float, n: float, o: float, p: float, r: float, s: float, t: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    Proposition 6.22. For any T <∞, let ((tn, xn))n∈N be a sequence as in Lemma 6.20. Then lim
    $$

    Args:
        P (float): Input parameter `P`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(6.2 * P * i**2 * n * o**3 * p * r * s * t)


def expr_val_2608_12291_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_12291_form_9`."""
    return (
        6.2
        * pl.col("P")
        * pl.col("i") ** 2
        * pl.col("n")
        * pl.col("o") ** 3
        * pl.col("p")
        * pl.col("r")
        * pl.col("s")
        * pl.col("t")
    )


def calc_f_s_form_5(S: float, c: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    f(s) = c0 S - s ,
    $$

    Args:
        S (float): Input parameter `S`.
        c (float): Input parameter `c`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float((0 * S) * c - s)


def expr_f_s_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_s_form_5`."""
    return (0 * pl.col("S")) * pl.col("c") - pl.col("s")


def calc_f_s_form_8(k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    f (s) = k, c(t) = ke-t ,
    $$

    Args:
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(k)


def expr_f_s_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_s_form_8`."""
    return pl.col("k")


def calc_t_x_x_form_2(c: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    T (x, x) = c
    $$

    Args:
        c (float): Input parameter `c`.

    Returns:
        float: Calculated metric value.
    """
    return float(c)


def expr_t_x_x_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_x_x_form_2`."""
    return pl.col("c")


def calc_t_a_b_form_d(a: float, b: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    T (a, b) = a - b, c = 0.
    $$

    Args:
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.

    Returns:
        float: Calculated metric value.
    """
    return float(a - b)


def expr_t_a_b_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_a_b_form_d`."""
    return pl.col("a") - pl.col("b")


def calc_t_a_b_form_6(a: float, b: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    T (a, b) = ab .
    $$

    Args:
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * b)


def expr_t_a_b_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_a_b_form_6`."""
    return pl.col("a") * pl.col("b")


def calc_t_a_b_form_b(a: float, b: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    T (a, b) = (2 - ba ) 1{a\ge b} + ab 1{b>a}, c = 1.
    $$

    Args:
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.

    Returns:
        float: Calculated metric value.
    """
    return float(-a * b + 2)


def expr_t_a_b_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_a_b_form_b`."""
    return -pl.col("a") * pl.col("b") + 2


def calc_val_2602_19513_form_5(S: float, k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    Sk := (Sk 1 , . . . , Sk d )⊤.
    $$

    Args:
        S (float): Input parameter `S`.
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(S * k)


def expr_val_2602_19513_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2602_19513_form_5`."""
    return pl.col("S") * pl.col("k")


def calc_val_2602_19513_form_2(F: float, S: float, T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    TFS := α0,
    $$

    Args:
        F (float): Input parameter `F`.
        S (float): Input parameter `S`.
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(T * (F * S))


def expr_val_2602_19513_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2602_19513_form_2`."""
    return pl.col("T") * (pl.col("F") * pl.col("S"))


def calc_val_2602_19513_form_6(S: float, T: float, k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    TSSk := Fα(Sk 1 , . . . , Sk d ),
    $$

    Args:
        S (float): Input parameter `S`.
        T (float): Input parameter `T`.
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(T * (S * (S * k)))


def expr_val_2602_19513_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2602_19513_form_6`."""
    return pl.col("T") * (pl.col("S") * (pl.col("S") * pl.col("k")))


def calc_val_2602_19513_form_e(P: float, S: float, k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    PSSk,j = fα(Sk,j 1 , . . . Sk,j d ), j = 1, 2, . . . , J,
    $$

    Args:
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * (S * (S * k)))


def expr_val_2602_19513_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2602_19513_form_e`."""
    return pl.col("P") * (pl.col("S") * (pl.col("S") * pl.col("k")))


def calc_val_2602_19513_form_3(C: float, P: float, S: float, k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    PCSk,j := α0 J +α0 PSSk,j - TSSk /J Dk 1{Dk>0},
    $$

    Args:
        C (float): Input parameter `C`.
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * (C * (S * k)))


def expr_val_2602_19513_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2602_19513_form_3`."""
    return pl.col("P") * (pl.col("C") * (pl.col("S") * pl.col("k")))


def calc_val_2602_19513_form_c(i: float, m: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    mi := E[˜ Si(1)], v2 i := Var(˜ Si(1)).
    $$

    Args:
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(i * m)


def expr_val_2602_19513_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2602_19513_form_c`."""
    return pl.col("i") * pl.col("m")


def calc_val_2602_19513_form_d(F: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    Ft := σ(S(s), a(s), b(s) : s \le  t).
    $$

    Args:
        F (float): Input parameter `F`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(F * t)


def expr_val_2602_19513_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2602_19513_form_d`."""
    return pl.col("F") * pl.col("t")


def calc_val_2602_19513_form_7(T: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    pT (u|t) := T∗(t, a, b) + {mT (u) - mT (t)} ,
    $$

    Args:
        T (float): Input parameter `T`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(T * p)


def expr_val_2602_19513_form_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2602_19513_form_7`."""
    return pl.col("T") * pl.col("p")


def calc_val_2602_19513_form_0(T: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    pT(u|t) = T∗(t, a, b) ︸ ︷︷ ︸ current benchmark + mT (u) - mT (t) ︸ ︷︷ ︸ future fluctuation
    $$

    Args:
        T (float): Input parameter `T`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(T * p)


def expr_val_2602_19513_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2602_19513_form_0`."""
    return pl.col("T") * pl.col("p")


def calc_p_w_t_form_9(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    PWt = P (pT(1|t) > c | Ft) = 1-Φ ( c - T∗(t, a(t), b(t)) √(1 - t)(τ 2 + σ2 ) ) .
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_p_w_t_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_w_t_form_9`."""
    return pl.col("P")


def calc_val_2602_19513_form_8(P: float, S: float, T: float, j: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    PTSj := 1n n∑ k=1 [PCSk,j + h(Xk,j )],
    $$

    Args:
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.
        T (float): Input parameter `T`.
        j (float): Input parameter `j`.

    Returns:
        float: Calculated metric value.
    """
    return float(P * (T * (S * j)))


def expr_val_2602_19513_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2602_19513_form_8`."""
    return pl.col("P") * (pl.col("T") * (pl.col("S") * pl.col("j")))


def calc_t_a_b_form_0(a: float, b: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    T (a, b) = (2 - ba ) 1{a\ge b} + ab 1{b>a}.
    $$

    Args:
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.

    Returns:
        float: Calculated metric value.
    """
    return float(-a * b + 2)


def expr_t_a_b_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_a_b_form_0`."""
    return -pl.col("a") * pl.col("b") + 2


def calc_val_2602_15673_form_3(G: float, a: float, e: float, m: float, t: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_15673.

    **Source**:
    - Title: Leicester's Tale: Another Perspective on the EPL 2015/16 Through Expected Goals (xG) Modelling (2026)
    - Authors: Sheikh Badar Ud Din Tahir, Leonardo Egidi, Nicola Torelli
    - Citation Key: `arxiv_2602_15673`

    **KaTeX Formula**:
    $$
    xGteam, match = N∑ i=1 pi,
    $$

    Args:
        G (float): Input parameter `G`.
        a (float): Input parameter `a`.
        e (float): Input parameter `e`.
        m (float): Input parameter `m`.
        t (float): Input parameter `t`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(G * a * e * m * t * x)


def expr_val_2602_15673_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2602_15673_form_3`."""
    return pl.col("G") * pl.col("a") * pl.col("e") * pl.col("m") * pl.col("t") * pl.col("x")


def calc_k_p_form_c(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    pk = P(Y = 1 | Fk), k = 0, 1, . . . , N,
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_k_p_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_p_form_c`."""
    return pl.col("P")


def calc_val_2601_18774_form_a(M: float, N: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    MN := max 0\le k\le N pk, M := sup t∈[0,1] pt
    $$

    Args:
        M (float): Input parameter `M`.
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(M * N)


def expr_val_2601_18774_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2601_18774_form_a`."""
    return pl.col("M") * pl.col("N")


def calc_val_2601_18774_form_c(F: float, M: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    FM|Y=0(x) = 1 - p0 1 - p0 \cdot  1 -x x ,
    $$

    Args:
        F (float): Input parameter `F`.
        M (float): Input parameter `M`.

    Returns:
        float: Calculated metric value.
    """
    return float(F * M)


def expr_val_2601_18774_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2601_18774_form_c`."""
    return pl.col("F") * pl.col("M")


def calc_val_2601_18774_form_5(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    P(MN \ge  x | Y = 0) = p0 1 - p0 \cdot  1 -x x - C1(x) - C2(x),
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_2601_18774_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2601_18774_form_5`."""
    return pl.col("P")


def calc_val_2601_18774_form_7(C: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    C1(x) := 1 x(1 - p0) E[(pτx -x) 1{τx < N}], C2(x) := 1 -x x(1 - p0) P(τx = N).
    $$

    Args:
        C (float): Input parameter `C`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(C * x)


def expr_val_2601_18774_form_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2601_18774_form_7`."""
    return pl.col("C") * pl.col("x")


def calc_p_t_form_4(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    pt = P(Y = 1 | Ft) and qt = 1 -pt = P(Y = 0 | Ft)
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_p_t_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_t_form_4`."""
    return pl.col("P")


def calc_val_2601_18774_form_9(U: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    Ui := FMλ (mi; p0,i).
    $$

    Args:
        U (float): Input parameter `U`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(U * i)


def expr_val_2601_18774_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2601_18774_form_9`."""
    return pl.col("U") * pl.col("i")


def calc_val_2601_18774_form_f(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    P(Ui \ge  1 - α) \le  α.
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_2601_18774_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2601_18774_form_f`."""
    return pl.col("P")


def calc_val_2601_18774_form_1(D: float, e: float, n: float, p: float, r: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    Dupper n := sup 0\le t\le 1{t - ˆ FU (t-)}.
    $$

    Args:
        D (float): Input parameter `D`.
        e (float): Input parameter `e`.
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(D * e * n * p**2 * r * u)


def expr_val_2601_18774_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2601_18774_form_1`."""
    return pl.col("D") * pl.col("e") * pl.col("n") * pl.col("p") ** 2 * pl.col("r") * pl.col("u")


def calc_val_2601_18774_form_0(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    P(MN < x) \ge  1 - p0 x ,
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_2601_18774_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2601_18774_form_0`."""
    return pl.col("P")


def calc_val_2601_18774_form_b(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    P(MN \ge  x) \le  p0 x ⇒ P(MN < x) \ge  1 - p0 x .
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_2601_18774_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2601_18774_form_b`."""
    return pl.col("P")


def calc_val_2601_18774_form_8(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    P(MN \ge  x) = P(Y = 1) + P(Y = 0)P(MN \ge  x | Y = 0) = p0 + (1 - p0)P(MN \ge  x | Y = 0).
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_2601_18774_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2601_18774_form_8`."""
    return pl.col("P")


def calc_f_m_x_form_1(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    FM(x) = P(M \le  x) = 1 - p0 x ,
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_f_m_x_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_m_x_form_1`."""
    return pl.col("P")


def calc_val_2601_18774_form_d(F: float, M: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    FM|Y=0(x) = P(M \le  x | Y = 0) = 1 - ( p0 1 - p0 )( 1 - x x ),
    $$

    Args:
        F (float): Input parameter `F`.
        M (float): Input parameter `M`.

    Returns:
        float: Calculated metric value.
    """
    return float(F * M)


def expr_val_2601_18774_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2601_18774_form_d`."""
    return pl.col("F") * pl.col("M")


def calc_val_2601_18774_form_e(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    P(M \ge  x) = P(Y = 1) + (1 - p0)P(M \ge  x | Y = 0) = p0 + (1 - p0)P(M \ge  x | Y = 0).
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_2601_18774_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2601_18774_form_e`."""
    return pl.col("P")


def calc_p_0_x_form_5(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    p0 x = p0 + (1 - p0)P(M \ge  x | Y = 0) ⇒ P(M \ge  x | Y = 0) = ( p0 1 - p0 )( 1 - x x ).
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_p_0_x_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_0_x_form_5`."""
    return pl.col("P")


def calc_f_form_e(f: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_11492.

    **Source**:
    - Title: BoxMind: Closed-loop AI strategy optimization for elite boxing validated in the 2024 Olympics (2026)
    - Authors: Kaiwen Wang, Kaili Zheng, Rongrong Deng et al.
    - Citation Key: `arxiv_2601_11492`

    **KaTeX Formula**:
    $$
    F = ft(reshape(X, [T, J \times  5])) ∈ RT\times d (S1)
    $$

    Args:
        f (float): Input parameter `f`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(f * t)


def expr_f_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_form_e`."""
    return pl.col("f") * pl.col("t")


def calc_val_2601_11492_form_8(p: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_11492.

    **Source**:
    - Title: BoxMind: Closed-loop AI strategy optimization for elite boxing validated in the 2024 Olympics (2026)
    - Authors: Kaiwen Wang, Kaili Zheng, Rongrong Deng et al.
    - Citation Key: `arxiv_2601_11492`

    **KaTeX Formula**:
    $$
    pt, bst , bet = Head(Ft) (S2)
    $$

    Args:
        p (float): Input parameter `p`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(p * t)


def expr_val_2601_11492_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2601_11492_form_8`."""
    return pl.col("p") * pl.col("t")


def calc_f_s_form_0(f: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_11492.

    **Source**:
    - Title: BoxMind: Closed-loop AI strategy optimization for elite boxing validated in the 2024 Olympics (2026)
    - Authors: Kaiwen Wang, Kaili Zheng, Rongrong Deng et al.
    - Citation Key: `arxiv_2601_11492`

    **KaTeX Formula**:
    $$
    Fs = fs(reshape(X, [T, J \times  5])) ∈ Rds (S3)
    $$

    Args:
        f (float): Input parameter `f`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(f * s)


def expr_f_s_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_s_form_0`."""
    return pl.col("f") * pl.col("s")


def calc_b_p_k_form_0(a: float, m: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_11492.

    **Source**:
    - Title: BoxMind: Closed-loop AI strategy optimization for elite boxing validated in the 2024 Olympics (2026)
    - Authors: Kaiwen Wang, Kaili Zheng, Rongrong Deng et al.
    - Citation Key: `arxiv_2601_11492`

    **KaTeX Formula**:
    $$
    p(k) b =max (P (KDE1D(i(k) b ) > KDE1D(i(k) level )) , P (u > v)) (S8)
    $$

    Args:
        a (float): Input parameter `a`.
        m (float): Input parameter `m`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * m * x)


def expr_b_p_k_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_b_p_k_form_0`."""
    return pl.col("a") * pl.col("m") * pl.col("x")


def calc_val_2512_18467_form_0(S: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_18467.

    **Source**:
    - Title: Analysing Skill Predominance in Generalized Fantasy Cricket (2025)
    - Authors: Supratim Das, Sarthak Sarkar, Subhamoy Maitra et al.
    - Citation Key: `arxiv_2512_18467`

    **KaTeX Formula**:
    $$
    Si i.i.d. ∼ DirichletMin(α), i = 1, 2, . . . , n.
    $$

    Args:
        S (float): Input parameter `S`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(S * (i * i))


def expr_val_2512_18467_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2512_18467_form_0`."""
    return pl.col("S") * (pl.col("i") * pl.col("i"))


def calc_o_n_e_t_h_i_r_df_o_m_r_form_1(
    C: float,
    F: float,
    P: float,
    a: float,
    e: float,
    i: float,
    m: float,
    n: float,
    o: float,
    r: float,
    s: float,
    t: float,
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_18467.

    **Source**:
    - Title: Analysing Skill Predominance in Generalized Fantasy Cricket (2025)
    - Authors: Supratim Das, Sarthak Sarkar, Subhamoy Maitra et al.
    - Citation Key: `arxiv_2512_18467`

    **KaTeX Formula**:
    $$
    OneThirdForm= 13 \cdot  Form+ 23 \cdot  Career Points,
    $$

    Args:
        C (float): Input parameter `C`.
        F (float): Input parameter `F`.
        P (float): Input parameter `P`.
        a (float): Input parameter `a`.
        e (float): Input parameter `e`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(
        23 * (C * (a * (r * (e * (e * (r * (P * (o * (i * (n * (s * t)))))))))))
        + 13 * (F * (o * (m * r)))
    )


def expr_o_n_e_t_h_i_r_df_o_m_r_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_o_n_e_t_h_i_r_df_o_m_r_form_1`."""
    return 23 * (
        pl.col("C")
        * (
            pl.col("a")
            * (
                pl.col("r")
                * (
                    pl.col("e")
                    * (
                        pl.col("e")
                        * (
                            pl.col("r")
                            * (
                                pl.col("P")
                                * (
                                    pl.col("o")
                                    * (pl.col("i") * (pl.col("n") * (pl.col("s") * pl.col("t"))))
                                )
                            )
                        )
                    )
                )
            )
        )
    ) + 13 * (pl.col("F") * (pl.col("o") * (pl.col("m") * pl.col("r"))))


def calc_t_w_o_t_h_i_r_df_o_m_r_form_e(
    C: float,
    F: float,
    P: float,
    a: float,
    e: float,
    i: float,
    m: float,
    n: float,
    o: float,
    r: float,
    s: float,
    t: float,
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_18467.

    **Source**:
    - Title: Analysing Skill Predominance in Generalized Fantasy Cricket (2025)
    - Authors: Supratim Das, Sarthak Sarkar, Subhamoy Maitra et al.
    - Citation Key: `arxiv_2512_18467`

    **KaTeX Formula**:
    $$
    TwoThirdForm= 23 \cdot  Form+ 13 \cdot  Career Points.
    $$

    Args:
        C (float): Input parameter `C`.
        F (float): Input parameter `F`.
        P (float): Input parameter `P`.
        a (float): Input parameter `a`.
        e (float): Input parameter `e`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(13 * C * P * a * e**2 * i * n * o * r**2 * s * t + 23 * F * m * o * r)


def expr_t_w_o_t_h_i_r_df_o_m_r_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_w_o_t_h_i_r_df_o_m_r_form_e`."""
    return 13 * pl.col("C") * pl.col("P") * pl.col("a") * pl.col("e") ** 2 * pl.col("i") * pl.col(
        "n"
    ) * pl.col("o") * pl.col("r") ** 2 * pl.col("s") * pl.col("t") + 23 * pl.col("F") * pl.col(
        "m"
    ) * pl.col("o") * pl.col("r")


def calc_val_2512_18467_form_2(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_18467.

    **Source**:
    - Title: Analysing Skill Predominance in Generalized Fantasy Cricket (2025)
    - Authors: Supratim Das, Sarthak Sarkar, Subhamoy Maitra et al.
    - Citation Key: `arxiv_2512_18467`

    **KaTeX Formula**:
    $$
    P ( max 1\le i\le n |pi - πi| \ge  β) \le  n∑ i=1 P(|pi - πi| \ge  β) \le  δ,
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_2512_18467_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2512_18467_form_2`."""
    return pl.col("P")


def calc_val_2512_00312_form_3(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_00312.

    **Source**:
    - Title: Kicking for Goal or Touch? An Expected Points Framework for Penalty Decisions in Rugby Union (2025)
    - Authors: Kenny Watts, Jonathan Pipping-Gamón
    - Citation Key: `arxiv_2512_00312`

    **KaTeX Formula**:
    $$
    P(make | d, θ) = logit-1{β0 + f(d, θ)},
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_val_2512_00312_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2512_00312_form_3`."""
    return pl.col("P")


def calc_x_l_o_form_d(a: float, m: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_00312.

    **Source**:
    - Title: Kicking for Goal or Touch? An Expected Points Framework for Penalty Decisions in Rugby Union (2025)
    - Authors: Kenny Watts, Jonathan Pipping-Gamón
    - Citation Key: `arxiv_2512_00312`

    **KaTeX Formula**:
    $$
    xLO = max{5, x-dtouch},
    $$

    Args:
        a (float): Input parameter `a`.
        m (float): Input parameter `m`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(m * (a * x))


def expr_x_l_o_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_l_o_form_d`."""
    return pl.col("m") * (pl.col("a") * pl.col("x"))


def calc_r_form_5(
    P: float,
    a: float,
    c: float,
    i: float,
    l: float,
    m: float,
    o: float,
    p: float,
    t: float,
    u: float,
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_00312.

    **Source**:
    - Title: Kicking for Goal or Touch? An Expected Points Framework for Penalty Decisions in Rugby Union (2025)
    - Authors: Kenny Watts, Jonathan Pipping-Gamón
    - Citation Key: `arxiv_2512_00312`

    **KaTeX Formula**:
    $$
    R = EPoptimal - EPactual,
    $$

    Args:
        P (float): Input parameter `P`.
        a (float): Input parameter `a`.
        c (float): Input parameter `c`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.
        o (float): Input parameter `o`.
        p (float): Input parameter `p`.
        t (float): Input parameter `t`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(-math.e * P * a**2 * c * l * t * u + math.e * P * a * i * l * m * o * p * t)


def expr_r_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_form_5`."""
    return -math.e * pl.col("P") * pl.col("a") ** 2 * pl.col("c") * pl.col("l") * pl.col(
        "t"
    ) * pl.col("u") + math.e * pl.col("P") * pl.col("a") * pl.col("i") * pl.col("l") * pl.col(
        "m"
    ) * pl.col("o") * pl.col("p") * pl.col("t")


def calc_p_r_i_w_i_n_s_o_v_e_j_r_form_f(i: float, j: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2508_19848.

    **Source**:
    - Title: Hierarchy and ranking in pairwise sports contests (2025)
    - Authors: Bogdán Asztalos, Boldizsár Balázs, Gergely Palla et al.
    - Citation Key: `arxiv_2508_19848`

    **KaTeX Formula**:
    $$
    Pr(i wins over j) = 1 1+10(s j-si)/400 ,
    $$

    Args:
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(-1 / 40 * i * s + (1 / 40) * j * s + 11)


def expr_p_r_i_w_i_n_s_o_v_e_j_r_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_r_i_w_i_n_s_o_v_e_j_r_form_f`."""
    return -1 / 40 * pl.col("i") * pl.col("s") + (1 / 40) * pl.col("j") * pl.col("s") + 11


def calc_r_w_c_i_form_4(a: float, i: float, p: float, s: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2508_19848.

    **Source**:
    - Title: Hierarchy and ranking in pairwise sports contests (2025)
    - Authors: Bogdán Asztalos, Boldizsár Balázs, Gergely Palla et al.
    - Citation Key: `arxiv_2508_19848`

    **KaTeX Formula**:
    $$
    RWC(i) = (p stat )i .
    $$

    Args:
        a (float): Input parameter `a`.
        i (float): Input parameter `i`.
        p (float): Input parameter `p`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * i * p * s * t**2)


def expr_r_w_c_i_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_w_c_i_form_4`."""
    return pl.col("a") * pl.col("i") * pl.col("p") * pl.col("s") * pl.col("t") ** 2


def calc_g_x_form_9(e: float, t: float, w: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2506_05866.

    **Source**:
    - Title: Analysis of points outcome in ATP Grand Slam Tennis using big data and machine learning (2025)
    - Authors: Martin Illum, Hans Christian Bechsøfft Mikkelsen, Emil Hovad
    - Citation Key: `arxiv_2506_05866`

    **KaTeX Formula**:
    $$
    G(x) = 1 1 + e-wt x
    $$

    Args:
        e (float): Input parameter `e`.
        t (float): Input parameter `t`.
        w (float): Input parameter `w`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(e - t * w * x + 11)


def expr_g_x_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_x_form_9`."""
    return pl.col("e") - pl.col("t") * pl.col("w") * pl.col("x") + 11


def calc_val_2506_05866_form_5(j: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2506_05866.

    **Source**:
    - Title: Analysis of points outcome in ATP Grand Slam Tennis using big data and machine learning (2025)
    - Authors: Martin Illum, Hans Christian Bechsøfft Mikkelsen, Emil Hovad
    - Citation Key: `arxiv_2506_05866`

    **KaTeX Formula**:
    $$
    wj,n+1 = wj,n -α ∂ ∂wj L(x)
    $$

    Args:
        j (float): Input parameter `j`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(j * w)


def expr_val_2506_05866_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2506_05866_form_5`."""
    return pl.col("j") * pl.col("w")


def calc_val_2503_11669_form_5(m: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2503_11669.

    **Source**:
    - Title: Fast Algorithm for Calculating Probability of Chess Winning Streaks (2025)
    - Authors: Guoqing Diao
    - Citation Key: `arxiv_2503_11669`

    **KaTeX Formula**:
    $$
    pm,k = 1, m= 1, ..., k - 1, pk,k = 1 - k∏ i=1 (1 - qi), pk,k-1 = 1 - k-1 ∏ i=1 (1 - qi) - k∏ i=2 (1 - qi) - k∏ i=1
    $$

    Args:
        m (float): Input parameter `m`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(m * p)


def expr_val_2503_11669_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2503_11669_form_5`."""
    return pl.col("m") * pl.col("p")


def calc_val_2503_11669_form_3(i: float, q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2503_11669.

    **Source**:
    - Title: Fast Algorithm for Calculating Probability of Chess Winning Streaks (2025)
    - Authors: Guoqing Diao
    - Citation Key: `arxiv_2503_11669`

    **KaTeX Formula**:
    $$
    (1 - qi).
    $$

    Args:
        i (float): Input parameter `i`.
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float(-i * q + 1)


def expr_val_2503_11669_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2503_11669_form_3`."""
    return -pl.col("i") * pl.col("q") + 1


def calc_val_2503_11669_form_9(m: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2503_11669.

    **Source**:
    - Title: Fast Algorithm for Calculating Probability of Chess Winning Streaks (2025)
    - Authors: Guoqing Diao
    - Citation Key: `arxiv_2503_11669`

    **KaTeX Formula**:
    $$
    pm+1,k = qm+1pm,k + (1 - qm+1) pm,k - qm-(k-1)pm-k,k m∏ j=m-(k-1)+1(1 - qj )  .
    $$

    Args:
        m (float): Input parameter `m`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(m * p + 1)


def expr_val_2503_11669_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2503_11669_form_9`."""
    return pl.col("m") * pl.col("p") + 1


def calc_val_2503_11669_form_c(g: float, k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2503_11669.

    **Source**:
    - Title: Fast Algorithm for Calculating Probability of Chess Winning Streaks (2025)
    - Authors: Guoqing Diao
    - Citation Key: `arxiv_2503_11669`

    **KaTeX Formula**:
    $$
    gk+1,k+1/2 = 1 - k+1 ∏ i=1 qi,3 - k+1∑ i=1 qi,2 ( k+1 ∏ j=1,j̸=i qj,3) .
    $$

    Args:
        g (float): Input parameter `g`.
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(g * k + 1)


def expr_val_2503_11669_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2503_11669_form_c`."""
    return pl.col("g") * pl.col("k") + 1


def calc_val_2503_11669_form_8(g: float, k: float, m: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2503_11669.

    **Source**:
    - Title: Fast Algorithm for Calculating Probability of Chess Winning Streaks (2025)
    - Authors: Guoqing Diao
    - Citation Key: `arxiv_2503_11669`

    **KaTeX Formula**:
    $$
    gm-k-1,k+1/2 - hm-2k-1,m-k-1,k,
    $$

    Args:
        g (float): Input parameter `g`.
        k (float): Input parameter `k`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(g * m - k - 1)


def expr_val_2503_11669_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2503_11669_form_8`."""
    return pl.col("g") * pl.col("m") - pl.col("k") - 1


def calc_val_2503_11669_form_b(a: float, h: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2503_11669.

    **Source**:
    - Title: Fast Algorithm for Calculating Probability of Chess Winning Streaks (2025)
    - Authors: Guoqing Diao
    - Citation Key: `arxiv_2503_11669`

    **KaTeX Formula**:
    $$
    ha,b,k  = ∏bj=a+1 qj,3 a = 0 = (qa,1 + qa,2) ∏bj=a+1 qj,3 a = 1 ≈ ga-1,k+1/2(qa,1 + qa,2) ∏bj=a+1 qj,3 a > 1 .
    $$

    Args:
        a (float): Input parameter `a`.
        h (float): Input parameter `h`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * h)


def expr_val_2503_11669_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2503_11669_form_b`."""
    return pl.col("a") * pl.col("h")


def calc_val_2610_18417_form_a(r: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_18417.

    **Source**:
    - Title: Resource-Efficient 3D Shape and Orientation Estimation of Road Users using Roadside RGB Camera and 3D Radar (2026)
    - Authors: Shiva Agrawal, Savankumar Bhanderi, Gordon Elger
    - Citation Key: `arxiv_2610_18417`

    **KaTeX Formula**:
    $$
    vr,i = 1Ki Ki∑ k=1 v(k) r
    $$

    Args:
        r (float): Input parameter `r`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(r * v)


def expr_val_2610_18417_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_18417_form_a`."""
    return pl.col("r") * pl.col("v")


def calc_val_2610_18417_form_6(X: float, g: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_18417.

    **Source**:
    - Title: Resource-Efficient 3D Shape and Orientation Estimation of Road Users using Roadside RGB Camera and 3D Radar (2026)
    - Authors: Shiva Agrawal, Savankumar Bhanderi, Gordon Elger
    - Citation Key: `arxiv_2610_18417`

    **KaTeX Formula**:
    $$
    Xg,m = TLG \cdot  TRL \cdot  ˜P-1 \cdot  s \cdot   um vm 1 1/s  
    $$

    Args:
        X (float): Input parameter `X`.
        g (float): Input parameter `g`.

    Returns:
        float: Calculated metric value.
    """
    return float(X * g)


def expr_val_2610_18417_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_18417_form_6`."""
    return pl.col("X") * pl.col("g")


def calc_val_2610_18417_form_5(b: float, c: float, i: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_18417.

    **Source**:
    - Title: Resource-Efficient 3D Shape and Orientation Estimation of Road Users using Roadside RGB Camera and 3D Radar (2026)
    - Authors: Shiva Agrawal, Savankumar Bhanderi, Gordon Elger
    - Citation Key: `arxiv_2610_18417`

    **KaTeX Formula**:
    $$
    wbic,i =  wbic,min, if ∆ybic,i < wbic,min ∆ybic,i, if wbic,min \le  ∆ybic,i \le  wbic,max wbic,max, if ∆ybic,i > wbic,max
    $$

    Args:
        b (float): Input parameter `b`.
        c (float): Input parameter `c`.
        i (float): Input parameter `i`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(b * c * i * w)


def expr_val_2610_18417_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_18417_form_5`."""
    return pl.col("b") * pl.col("c") * pl.col("i") * pl.col("w")


def calc_val_2609_10498_form_d(c: float, i: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10498.

    **Source**:
    - Title: Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts (2026)
    - Authors: Simon Khan, Laurent Gajny, Jennyfer Lecompte et al.
    - Citation Key: `arxiv_2609_10498`

    **KaTeX Formula**:
    $$
    xci,t,j = Rtxwi,t,j + tt,
    $$

    Args:
        c (float): Input parameter `c`.
        i (float): Input parameter `i`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(c * i * x)


def expr_val_2609_10498_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_10498_form_d`."""
    return pl.col("c") * pl.col("i") * pl.col("x")


def calc_val_2609_10498_form_e(i: float, w: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10498.

    **Source**:
    - Title: Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts (2026)
    - Authors: Simon Khan, Laurent Gajny, Jennyfer Lecompte et al.
    - Citation Key: `arxiv_2609_10498`

    **KaTeX Formula**:
    $$
    xwi,t,j =R⊤t (xci,t,j - tt ) .
    $$

    Args:
        i (float): Input parameter `i`.
        w (float): Input parameter `w`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(i * w * x)


def expr_val_2609_10498_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_10498_form_e`."""
    return pl.col("i") * pl.col("w") * pl.col("x")


def calc_val_2609_10498_form_1(c: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10498.

    **Source**:
    - Title: Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts (2026)
    - Authors: Simon Khan, Laurent Gajny, Jennyfer Lecompte et al.
    - Citation Key: `arxiv_2609_10498`

    **KaTeX Formula**:
    $$
    rc,gt i,t = 12 (xc,gt i,t,jL + xc,gt i,t,jR ) .
    $$

    Args:
        c (float): Input parameter `c`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(c * r)


def expr_val_2609_10498_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_10498_form_1`."""
    return pl.col("c") * pl.col("r")


def calc_val_2609_10498_form_b(e: float, l: float, r: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10498.

    **Source**:
    - Title: Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts (2026)
    - Authors: Simon Khan, Laurent Gajny, Jennyfer Lecompte et al.
    - Citation Key: `arxiv_2609_10498`

    **KaTeX Formula**:
    $$
    xrel,gt i,t,j = xc,gt i,t,j - rc,gt i,t , j = 1, . . . , J.
    $$

    Args:
        e (float): Input parameter `e`.
        l (float): Input parameter `l`.
        r (float): Input parameter `r`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(e * l * r * x)


def expr_val_2609_10498_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_10498_form_b`."""
    return pl.col("e") * pl.col("l") * pl.col("r") * pl.col("x")


def calc_val_2609_10498_form_c(dw: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10498.

    **Source**:
    - Title: Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts (2026)
    - Authors: Simon Khan, Laurent Gajny, Jennyfer Lecompte et al.
    - Citation Key: `arxiv_2609_10498`

    **KaTeX Formula**:
    $$
    dwi,t =R⊤t dci,t .
    $$

    Args:
        dw (float): Input parameter `dw`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(dw * i)


def expr_val_2609_10498_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_10498_form_c`."""
    return pl.col("dw") * pl.col("i")


def calc_val_2609_10498_form_8(i: float, q: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10498.

    **Source**:
    - Title: Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts (2026)
    - Authors: Simon Khan, Laurent Gajny, Jennyfer Lecompte et al.
    - Citation Key: `arxiv_2609_10498`

    **KaTeX Formula**:
    $$
    qwi,t = Ct + λ∗i,tdwi,t .
    $$

    Args:
        i (float): Input parameter `i`.
        q (float): Input parameter `q`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(i * q * w)


def expr_val_2609_10498_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_10498_form_8`."""
    return pl.col("i") * pl.col("q") * pl.col("w")


def calc_val_2609_10498_form_5(f: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10498.

    **Source**:
    - Title: Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts (2026)
    - Authors: Simon Khan, Laurent Gajny, Jennyfer Lecompte et al.
    - Citation Key: `arxiv_2609_10498`

    **KaTeX Formula**:
    $$
    fi,t = [f 3D i,t , f 2D i,t , f box i,t , f cam t , qwi,t , mi,t ] .
    $$

    Args:
        f (float): Input parameter `f`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(f * i)


def expr_val_2609_10498_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_10498_form_5`."""
    return pl.col("f") * pl.col("i")


def calc_val_2609_10498_form_a(b: float, i: float, o: float, p: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10498.

    **Source**:
    - Title: Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts (2026)
    - Authors: Simon Khan, Laurent Gajny, Jennyfer Lecompte et al.
    - Citation Key: `arxiv_2609_10498`

    **KaTeX Formula**:
    $$
    pbox i,t,j = [ ui,t,j - cxi,t wi,t , vi,t,j - cyi,t hi,t ] .
    $$

    Args:
        b (float): Input parameter `b`.
        i (float): Input parameter `i`.
        o (float): Input parameter `o`.
        p (float): Input parameter `p`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(b * i * o * p * x)


def expr_val_2609_10498_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_10498_form_a`."""
    return pl.col("b") * pl.col("i") * pl.col("o") * pl.col("p") * pl.col("x")


def calc_val_2609_10498_form_f(D: float, f: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10498.

    **Source**:
    - Title: Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts (2026)
    - Authors: Simon Khan, Laurent Gajny, Jennyfer Lecompte et al.
    - Citation Key: `arxiv_2609_10498`

    **KaTeX Formula**:
    $$
    f 2D i,t = vec ([pimg i,t,j , pbox i,t,j ]J j=1 ) .
    $$

    Args:
        D (float): Input parameter `D`.
        f (float): Input parameter `f`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(2 * D * f * i)


def expr_val_2609_10498_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_10498_form_f`."""
    return 2 * pl.col("D") * pl.col("f") * pl.col("i")


def calc_val_2609_10498_form_0(b: float, f: float, i: float, o: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10498.

    **Source**:
    - Title: Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts (2026)
    - Authors: Simon Khan, Laurent Gajny, Jennyfer Lecompte et al.
    - Citation Key: `arxiv_2609_10498`

    **KaTeX Formula**:
    $$
    f box i,t = [ cxi,t W , cyi,t H , wi,t W , hi,t H , log wi,t hi,t ] .
    $$

    Args:
        b (float): Input parameter `b`.
        f (float): Input parameter `f`.
        i (float): Input parameter `i`.
        o (float): Input parameter `o`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(b * f * i * o * x)


def expr_val_2609_10498_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_10498_form_0`."""
    return pl.col("b") * pl.col("f") * pl.col("i") * pl.col("o") * pl.col("x")


def calc_c_p_q_form_c(g: float, l: float, o: float, p: float, q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_25621.

    **Source**:
    - Title: Dissonance Spectrum explicitly models perceptual frequency interactions for better music understanding (2026)
    - Authors: Tianle Wang, Xinyi Tong, Liangke Zhao et al.
    - Citation Key: `arxiv_2608_25621`

    **KaTeX Formula**:
    $$
    C ( pq ) = log2(pq),
    $$

    Args:
        g (float): Input parameter `g`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.
        p (float): Input parameter `p`.
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float(2 * g * l * o * p * q)


def expr_c_p_q_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_p_q_form_c`."""
    return 2 * pl.col("g") * pl.col("l") * pl.col("o") * pl.col("p") * pl.col("q")


def calc_f_r_e_q_p_i_t_c_h_form_1(c: float, h: float, i: float, p: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_25621.

    **Source**:
    - Title: Dissonance Spectrum explicitly models perceptual frequency interactions for better music understanding (2026)
    - Authors: Tianle Wang, Xinyi Tong, Liangke Zhao et al.
    - Citation Key: `arxiv_2608_25621`

    **KaTeX Formula**:
    $$
    freq(pitch) = 440 \cdot  2 pitch-69 12
    $$

    Args:
        c (float): Input parameter `c`.
        h (float): Input parameter `h`.
        i (float): Input parameter `i`.
        p (float): Input parameter `p`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(880 * c * h * i * p * t - 6912)


def expr_f_r_e_q_p_i_t_c_h_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_r_e_q_p_i_t_c_h_form_1`."""
    return 880 * pl.col("c") * pl.col("h") * pl.col("i") * pl.col("p") * pl.col("t") - 6912


def calc_val_2608_25621_form_6(D: float, i: float, n: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_25621.

    **Source**:
    - Title: Dissonance Spectrum explicitly models perceptual frequency interactions for better music understanding (2026)
    - Authors: Tianle Wang, Xinyi Tong, Liangke Zhao et al.
    - Citation Key: `arxiv_2608_25621`

    **KaTeX Formula**:
    $$
    Dint,max = max ∆p∈[0,12) Dinterval(∆p),
    $$

    Args:
        D (float): Input parameter `D`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(D * i * n * t)


def expr_val_2608_25621_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2608_25621_form_6`."""
    return pl.col("D") * pl.col("i") * pl.col("n") * pl.col("t")


def calc_m_t_form_d(a: float, k: float, m: float, t: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_25621.

    **Source**:
    - Title: Dissonance Spectrum explicitly models perceptual frequency interactions for better music understanding (2026)
    - Authors: Tianle Wang, Xinyi Tong, Liangke Zhao et al.
    - Citation Key: `arxiv_2608_25621`

    **KaTeX Formula**:
    $$
    m(t) = max k x t k , ⃗x t frame = ⃗x t/m(t), m = max k,t x t k , Xglobal =X/m.
    $$

    Args:
        a (float): Input parameter `a`.
        k (float): Input parameter `k`.
        m (float): Input parameter `m`.
        t (float): Input parameter `t`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(a * k**2 * m * t * x**2)


def expr_m_t_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_t_form_d`."""
    return pl.col("a") * pl.col("k") ** 2 * pl.col("m") * pl.col("t") * pl.col("x") ** 2


def calc_k_p_form_8(
    B: float, c: float, h: float, i: float, k: float, m: float, n: float, p: float, t: float
) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_25621.

    **Source**:
    - Title: Dissonance Spectrum explicitly models perceptual frequency interactions for better music understanding (2026)
    - Authors: Tianle Wang, Xinyi Tong, Liangke Zhao et al.
    - Citation Key: `arxiv_2608_25621`

    **KaTeX Formula**:
    $$
    pk = pitchmin + 12k B , k = 0, . . . ,K - 1,
    $$

    Args:
        B (float): Input parameter `B`.
        c (float): Input parameter `c`.
        h (float): Input parameter `h`.
        i (float): Input parameter `i`.
        k (float): Input parameter `k`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(12 * B * k + c * h * i**2 * m * n * p * t)


def expr_k_p_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_p_form_8`."""
    return 12 * pl.col("B") * pl.col("k") + pl.col("c") * pl.col("h") * pl.col("i") ** 2 * pl.col(
        "m"
    ) * pl.col("n") * pl.col("p") * pl.col("t")


def calc_c_l_form_b(x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_14819.

    **Source**:
    - Title: What Makes a Good Layer? Assessing the Layer-Wise Intrinsic Properties of Music Foundation Models (2026)
    - Authors: Angelos-Nikolaos Kanatas, Yuexuan Kong, Pablo Alonso-Jiménez et al.
    - Citation Key: `arxiv_2608_14819`

    **KaTeX Formula**:
    $$
    C (l) = Ex, t [ arccos( ˆv(l) t+1 \cdot  ˆv(l) t ) ] ∈ [0, π],
    $$

    Args:
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e * x)


def expr_c_l_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_l_form_b`."""
    return math.e * pl.col("x")


def calc_c_a_b_form_0(C: float, a: float, n: float, o: float, s: float, t: float) -> float:
    r"""Compute mathematical metric extracted from openalex_meyer2008_w1992303757.

    **Source**:
    - Title: Influence of a humidor on the aerodynamics of baseballs (2008)
    - Authors: Edmund Meyer, John L. Bohn
    - Citation Key: `openalex_meyer2008_w1992303757`

    **KaTeX Formula**:
    $$
    a + b - c = Constant
    $$

    Args:
        C (float): Input parameter `C`.
        a (float): Input parameter `a`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(C * a * n**2 * o * s * t**2)


def expr_c_a_b_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_a_b_form_0`."""
    return (
        pl.col("C") * pl.col("a") * pl.col("n") ** 2 * pl.col("o") * pl.col("s") * pl.col("t") ** 2
    )


def calc_s_form_1(b: float, omega: float, r: float, v: float) -> float:
    r"""Compute mathematical metric extracted from openalex_meyer2008_w1992303757.

    **Source**:
    - Title: Influence of a humidor on the aerodynamics of baseballs (2008)
    - Authors: Edmund Meyer, John L. Bohn
    - Citation Key: `openalex_meyer2008_w1992303757`

    **KaTeX Formula**:
    $$
    S = r\omega b v
    $$

    Args:
        b (float): Input parameter `b`.
        omega (float): Input parameter `omega`.
        r (float): Input parameter `r`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(r * (omega * (b * v)))


def expr_s_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_form_1`."""
    return pl.col("r") * (pl.col("omega") * (pl.col("b") * pl.col("v")))


def calc_c_l_form_3(S: float) -> float:
    r"""Compute mathematical metric extracted from openalex_meyer2008_w1992303757.

    **Source**:
    - Title: Influence of a humidor on the aerodynamics of baseballs (2008)
    - Authors: Edmund Meyer, John L. Bohn
    - Citation Key: `openalex_meyer2008_w1992303757`

    **KaTeX Formula**:
    $$
    CL =  1.5S, S < 0.1 0.09 + 0.6S, S > 0.1
    $$

    Args:
        S (float): Input parameter `S`.

    Returns:
        float: Calculated metric value.
    """
    return float(1.5 * S)


def expr_c_l_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_l_form_3`."""
    return 1.5 * pl.col("S")


def calc_openalex_saavedra2009_w2041165548_form_6(C: float) -> float:
    r"""Compute mathematical metric extracted from openalex_saavedra2009_w2041165548.

    **Source**:
    - Title: Mutually-antagonistic interactions in baseball networks (2009)
    - Authors: Serguei Saavedra, Scott Powers, Trent McCotter et al.
    - Citation Key: `openalex_saavedra2009_w2041165548`

    **KaTeX Formula**:
    $$
    C4,mn(i) = qimn (km - ηimn) + (kn - ηimn) + qimn , (A1)
    $$

    Args:
        C (float): Input parameter `C`.

    Returns:
        float: Calculated metric value.
    """
    return float(4 * C)


def expr_openalex_saavedra2009_w2041165548_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_openalex_saavedra2009_w2041165548_form_6`."""
    return 4 * pl.col("C")


def calc_q_i_j_form_9(B: float, P: float, i: float, j: float, k: float) -> float:
    r"""Compute mathematical metric extracted from openalex_saavedra2009_w2041165548.

    **Source**:
    - Title: Mutually-antagonistic interactions in baseball networks (2009)
    - Authors: Serguei Saavedra, Scott Powers, Trent McCotter et al.
    - Citation Key: `openalex_saavedra2009_w2041165548`

    **KaTeX Formula**:
    $$
    q(i, j) = ki 2B + kj 2P , (A5)
    $$

    Args:
        B (float): Input parameter `B`.
        P (float): Input parameter `P`.
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(2 * B * i * k + 2 * P * j * k)


def expr_q_i_j_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_i_j_form_9`."""
    return 2 * pl.col("B") * pl.col("i") * pl.col("k") + 2 * pl.col("P") * pl.col("j") * pl.col("k")
