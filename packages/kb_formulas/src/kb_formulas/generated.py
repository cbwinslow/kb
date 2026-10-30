# ruff: noqa
# pyright: off
"""Auto-generated standalone scientific formula library.

Compiled directly from peer-reviewed research preprints in the Knowledge Base.
Each formula provides typed Python scalar execution and vectorized Polars expressions.
"""

from __future__ import annotations

import math

import polars as pl

__all__ = [
    "calc_sigma_g_form_1",
    "expr_sigma_g_form_1",
    "calc_c_t_form_f",
    "expr_c_t_form_f",
    "calc_a_form_4",
    "expr_a_form_4",
    "calc_gamma_form_9",
    "expr_gamma_form_9",
    "calc_r_m_e_s_form_d",
    "expr_r_m_e_s_form_d",
    "calc_m_a_e_form_3",
    "expr_m_a_e_form_3",
    "calc_m_a_e_p_form_d",
    "expr_m_a_e_p_form_d",
    "calc_delta_e_r_form_0",
    "expr_delta_e_r_form_0",
    "calc_s_i_form_a",
    "expr_s_i_form_a",
    "calc_l_a_c_c_form_b",
    "expr_l_a_c_c_form_b",
    "calc_p_z_form_7",
    "expr_p_z_form_7",
    "calc_i_y_form_9",
    "expr_i_y_form_9",
    "calc_y_form_3",
    "expr_y_form_3",
    "calc_p_2_form_4",
    "expr_p_2_form_4",
    "calc_y_form_4",
    "expr_y_form_4",
    "calc_a_s_t_form_0",
    "expr_a_s_t_form_0",
    "calc_f_2_form_9",
    "expr_f_2_form_9",
    "calc_beta_l_a_s_o_s_form_d",
    "expr_beta_l_a_s_o_s_form_d",
    "calc_sigma_u_form_e",
    "expr_sigma_u_form_e",
    "calc_l_form_f",
    "expr_l_form_f",
    "calc_b_form_4",
    "expr_b_form_4",
    "calc_a_p_form_6",
    "expr_a_p_form_6",
    "calc_eta_i_form_f",
    "expr_eta_i_form_f",
    "calc_delta_rho_1312_7",
    "expr_delta_rho_1312_7",
    "calc_b_r_s_form_6",
    "expr_b_r_s_form_6",
    "calc_t_log_e_t_e_form_f",
    "expr_t_log_e_t_e_form_f",
    "calc_h_lambda_i_j_lambda_1712_0",
    "expr_h_lambda_i_j_lambda_1712_0",
    "calc_val_1712_05879_1712_0",
    "expr_val_1712_05879_1712_0",
    "calc_r_i_j_brown_",
    "expr_r_i_j_brown_",
    "calc_v_a_r_x_1_i_x_2_i_brown_",
    "expr_v_a_r_x_1_i_x_2_i_brown_",
    "calc_g_tau_c_nu_m_nu_form_3",
    "expr_g_tau_c_nu_m_nu_form_3",
    "calc_r_e_p_l_a_c_e_m_e_n_t_r_u_n_s_form_a",
    "expr_r_e_p_l_a_c_e_m_e_n_t_r_u_n_s_form_a",
    "calc_p_x_form_5",
    "expr_p_x_form_5",
    "calc_d_c_p_l_s_u_r_form_a",
    "expr_d_c_p_l_s_u_r_form_a",
    "calc_n_v_s_form_b",
    "expr_n_v_s_form_b",
    "calc_e_r_o_t_form_c",
    "expr_e_r_o_t_form_c",
    "calc_f_m_x_form_1",
    "expr_f_m_x_form_1",
    "calc_v_n_t_k_x_form_4",
    "expr_v_n_t_k_x_form_4",
    "calc_a_p_m_efron_",
    "expr_a_p_m_efron_",
    "calc_d_k_p_l_p_form_9",
    "expr_d_k_p_l_p_form_9",
    "calc_q_form_4",
    "expr_q_form_4",
    "calc_b_a_t_t_i_n_g_r_u_n_s_form_f",
    "expr_b_a_t_t_i_n_g_r_u_n_s_form_f",
    "calc_d_a_h_1603_0",
    "expr_d_a_h_1603_0",
    "calc_q_form_e",
    "expr_q_form_e",
    "calc_rho_form_8",
    "expr_rho_form_8",
    "calc_theta_i_j_brown_",
    "expr_theta_i_j_brown_",
    "calc_t_m_g_i_form_0",
    "expr_t_m_g_i_form_0",
    "calc_n_form_0",
    "expr_n_form_0",
    "calc_sim_t_v_form_1",
    "expr_sim_t_v_form_1",
    "calc_a_l_r_3_form_9",
    "expr_a_l_r_3_form_9",
    "calc_theta_d_t_form_d",
    "expr_theta_d_t_form_d",
    "calc_r_t_form_d",
    "expr_r_t_form_d",
    "calc_b_p_k_form_0",
    "expr_b_p_k_form_0",
    "calc_val_30_form_1",
    "expr_val_30_form_1",
    "calc_log_m_e_form_e",
    "expr_log_m_e_form_e",
    "calc_k_z_form_2",
    "expr_k_z_form_2",
    "calc_z_i_j_form_2",
    "expr_z_i_j_form_2",
    "calc_j_i_t_t_e_r_form_2",
    "expr_j_i_t_t_e_r_form_2",
    "calc_f_h_y_form_2",
    "expr_f_h_y_form_2",
    "calc_r_t_form_2",
    "expr_r_t_form_2",
    "calc_v_phi_r_form_3",
    "expr_v_phi_r_form_3",
    "calc_theta_m_a_x_form_3",
    "expr_theta_m_a_x_form_3",
    "calc_s_a_t_u_form_8",
    "expr_s_a_t_u_form_8",
    "calc_n_form_6",
    "expr_n_form_6",
    "calc_a_r_form_4",
    "expr_a_r_form_4",
    "calc_t_form_c",
    "expr_t_form_c",
    "calc_t_form_f",
    "expr_t_form_f",
    "calc_t_form_7",
    "expr_t_form_7",
    "calc_d_form_4",
    "expr_d_form_4",
    "calc_c_l_p_form_1",
    "expr_c_l_p_form_1",
    "calc_j_z_form_9",
    "expr_j_z_form_9",
    "calc_t_form_9",
    "expr_t_form_9",
    "calc_f_p_form_9",
    "expr_f_p_form_9",
    "calc_v_n_1_form_a",
    "expr_v_n_1_form_a",
    "calc_delta_form_a",
    "expr_delta_form_a",
    "calc_p_x_a_p_e_x_form_f",
    "expr_p_x_a_p_e_x_form_f",
    "calc_m_a_c_c_form_d",
    "expr_m_a_c_c_form_d",
    "calc_i_s_form_f",
    "expr_i_s_form_f",
    "calc_f_s_p_y_2005_0",
    "expr_f_s_p_y_2005_0",
    "calc_t_b_form_5",
    "expr_t_b_form_5",
    "calc_eta_form_5",
    "expr_eta_form_5",
    "calc_w_e_v_e_n_t_form_5",
    "expr_w_e_v_e_n_t_form_5",
    "calc_p_i_i_theta_form_0",
    "expr_p_i_i_theta_form_0",
    "calc_c_a_b_form_0",
    "expr_c_a_b_form_0",
    "calc_c_form_6",
    "expr_c_form_6",
    "calc_sim_beta_0_form_3",
    "expr_sim_beta_0_form_3",
    "calc_val_2511_17733_2511_1",
    "expr_val_2511_17733_2511_1",
    "calc_alpha_f_delta_e_gamma_x_form_b",
    "expr_alpha_f_delta_e_gamma_x_form_b",
    "calc_w_1_2511_1",
    "expr_w_1_2511_1",
    "calc_l_x_2511_1",
    "expr_l_x_2511_1",
    "calc_r_x_2511_1",
    "expr_r_x_2511_1",
    "calc_eta_1_form_6",
    "expr_eta_1_form_6",
    "calc_s_di_f_f_i_c_u_l_t_form_6",
    "expr_s_di_f_f_i_c_u_l_t_form_6",
    "calc_miller2005_99c4eb",
    "expr_miller2005_99c4eb",
    "calc_g_m_i_l_form_7",
    "expr_g_m_i_l_form_7",
    "calc_val_2610_31153_form_7",
    "expr_val_2610_31153_form_7",
    "calc_psi_b_w_form_0",
    "expr_psi_b_w_form_0",
    "calc_l_v_a_l_form_4",
    "expr_l_v_a_l_form_4",
    "calc_e_b_a_e_s_form_3",
    "expr_e_b_a_e_s_form_3",
    "calc_f_l_x_2511_1",
    "expr_f_l_x_2511_1",
    "calc_val_1205_2071_form_2",
    "expr_val_1205_2071_form_2",
    "calc_f_r_x_2511_1",
    "expr_f_r_x_2511_1",
    "calc_log_theta_c_j_theta_j_c_1_e_beyond",
    "expr_log_theta_c_j_theta_j_c_1_e_beyond",
    "calc_f_s_p_y_form_0",
    "expr_f_s_p_y_form_0",
    "calc_a_t_w_o_w_a_o_form_9",
    "expr_a_t_w_o_w_a_o_form_9",
    "calc_u_l_s_o_form_4",
    "expr_u_l_s_o_form_4",
    "calc_i_b_a_l_l_omega_form_3",
    "expr_i_b_a_l_l_omega_form_3",
    "calc_phi_form_1",
    "expr_phi_form_1",
    "calc_alpha_s_form_3",
    "expr_alpha_s_form_3",
    "calc_c_m_s_l_form_3",
    "expr_c_m_s_l_form_3",
    "calc_rho_c_o_u_n_t_form_4",
    "expr_rho_c_o_u_n_t_form_4",
    "calc_e_t_i_z_form_4",
    "expr_e_t_i_z_form_4",
    "calc_j_i_t_t_e_r_form_9",
    "expr_j_i_t_t_e_r_form_9",
    "calc_w_b_y_form_5",
    "expr_w_b_y_form_5",
    "calc_f_k_z_form_5",
    "expr_f_k_z_form_5",
    "calc_a_form_a",
    "expr_a_form_a",
    "calc_w_t_z_form_6",
    "expr_w_t_z_form_6",
    "calc_dv_dt_theta_v_r_v_r_theta_form_b",
    "expr_dv_dt_theta_v_r_v_r_theta_form_b",
    "calc_val_0_k_nu_form_6",
    "expr_val_0_k_nu_form_6",
    "calc_u_2_form_7",
    "expr_u_2_form_7",
    "calc_i_l_form_9",
    "expr_i_l_form_9",
    "calc_beta_j_n_n_a_form_1",
    "expr_beta_j_n_n_a_form_1",
    "calc_c_a_f_e_a_c_form_6",
    "expr_c_a_f_e_a_c_form_6",
    "calc_z_l_form_7",
    "expr_z_l_form_7",
    "calc_z_l_y_u_c_c_u_x_i_k_2_j_r_maher_",
    "expr_z_l_y_u_c_c_u_x_i_k_2_j_r_maher_",
    "calc_rho_form_7",
    "expr_rho_form_7",
    "calc_f_s_b_y_form_7",
    "expr_f_s_b_y_form_7",
    "calc_n_l_2_q_h_e_a_t_form_8",
    "expr_n_l_2_q_h_e_a_t_form_8",
    "calc_e_p_o_s_form_8",
    "expr_e_p_o_s_form_8",
    "calc_partial_t_u_2_sim_l_u_2_form_7",
    "expr_partial_t_u_2_sim_l_u_2_form_7",
    "calc_val_1_diebol",
    "expr_val_1_diebol",
    "calc_m_t_form_d",
    "expr_m_t_form_d",
    "calc_m_a_e_t_form_d",
    "expr_m_a_e_t_form_d",
    "calc_partial_z_c_k_epsilon_partial_form_1",
    "expr_partial_z_c_k_epsilon_partial_form_1",
    "calc_j_m_e_r_form_3",
    "expr_j_m_e_r_form_3",
    "calc_y_d_p_form_a",
    "expr_y_d_p_form_a",
    "calc_h_da_a_t_form_2",
    "expr_h_da_a_t_form_2",
    "calc_l_r_k_l_theta_form_2",
    "expr_l_r_k_l_theta_form_2",
    "calc_val_0_t_n_q_form_a",
    "expr_val_0_t_n_q_form_a",
    "calc_rho_c_o_u_n_t_1704_0",
    "expr_rho_c_o_u_n_t_1704_0",
    "calc_m_tau_form_b",
    "expr_m_tau_form_b",
    "calc_c_a_f_e_a_c_1704_0",
    "expr_c_a_f_e_a_c_1704_0",
    "calc_w_c_r_form_b",
    "expr_w_c_r_form_b",
    "calc_r_e_t_form_3",
    "expr_r_e_t_form_3",
    "calc_eq_y_d_p_1_n_p_dsum_i_p_i_form_c",
    "expr_eq_y_d_p_1_n_p_dsum_i_p_i_form_c",
    "calc_u_form_d",
    "expr_u_form_d",
    "calc_theta_form_d",
    "expr_theta_form_d",
    "calc_delta_p_form_e",
    "expr_delta_p_form_e",
    "calc_a_x_y_form_e",
    "expr_a_x_y_form_e",
    "calc_val_2610_01307_form_e",
    "expr_val_2610_01307_form_e",
    "calc_v_n_1_form_e",
    "expr_v_n_1_form_e",
    "calc_i_n_de_x_2603_2",
    "expr_i_n_de_x_2603_2",
    "calc_m_o_e_x_form_b",
    "expr_m_o_e_x_form_b",
    "calc_i_l_form_b",
    "expr_i_l_form_b",
    "calc_d_omega_2_pi_v_form_4",
    "expr_d_omega_2_pi_v_form_4",
    "calc_p_brier_",
    "expr_p_brier_",
    "calc_p_t_brier_",
    "expr_p_t_brier_",
    "calc_log_c_theta_theta_c_1_e_beyond",
    "expr_log_c_theta_theta_c_1_e_beyond",
    "calc_p_i_brown_",
    "expr_p_i_brown_",
    "calc_m_q_q_form_5",
    "expr_m_q_q_form_5",
    "calc_gamma_form_b",
    "expr_gamma_form_b",
    "calc_bt_secondary_many_routes_2023_bt_sec",
    "expr_bt_secondary_many_routes_2023_bt_sec",
    "calc_sigma_a_a_sigma_form_7",
    "expr_sigma_a_a_sigma_form_7",
    "calc_f_x_bt_sec",
    "expr_f_x_bt_sec",
    "calc_p_i_j_bt_sec",
    "expr_p_i_j_bt_sec",
    "calc_l_m_e_l_form_0",
    "expr_l_m_e_l_form_0",
    "calc_y_n_w_form_0",
    "expr_y_n_w_form_0",
    "calc_p_n_1_form_0",
    "expr_p_n_1_form_0",
    "calc_d_n_form_0",
    "expr_d_n_form_0",
    "calc_c_f_m_theta_l_o_t_form_0",
    "expr_c_f_m_theta_l_o_t_form_0",
    "calc_sigma_2_theta_form_2",
    "expr_sigma_2_theta_form_2",
    "calc_m_a_u_di_o_form_2",
    "expr_m_a_u_di_o_form_2",
    "calc_i_k_p_i_2103_1",
    "expr_i_k_p_i_2103_1",
    "calc_r_b_n_form_2",
    "expr_r_b_n_form_2",
    "calc_l_p_c_c_form_3",
    "expr_l_p_c_c_form_3",
    "calc_m_a_u_di_o_form_3",
    "expr_m_a_u_di_o_form_3",
    "calc_t_t_form_3",
    "expr_t_t_form_3",
    "calc_delta_t_0_form_4",
    "expr_delta_t_0_form_4",
    "calc_omega_i_form_4",
    "expr_omega_i_form_4",
    "calc_partial_l_mu_partial_2209_0",
    "expr_partial_l_mu_partial_2209_0",
    "calc_partial_l_partial_2_p_sigma_2209_0",
    "expr_partial_l_partial_2_p_sigma_2209_0",
    "calc_i_x_form_5",
    "expr_i_x_form_5",
    "calc_f_x_form_5",
    "expr_f_x_form_5",
    "calc_n_omega_form_5",
    "expr_n_omega_form_5",
    "calc_lambda_o_v_e_r_a_l_l_2501_0",
    "expr_lambda_o_v_e_r_a_l_l_2501_0",
    "calc_l_w_o_k_r_form_4",
    "expr_l_w_o_k_r_form_4",
    "calc_l_m_e_s_form_8",
    "expr_l_m_e_s_form_8",
    "calc_l_du_r_form_8",
    "expr_l_du_r_form_8",
    "calc_a_t_c_p_form_b",
    "expr_a_t_c_p_form_b",
    "calc_p_b_form_b",
    "expr_p_b_form_b",
    "calc_p_form_c",
    "expr_p_form_c",
    "calc_n_omega_form_d",
    "expr_n_omega_form_d",
    "calc_k_d_d_x_x_r_e_f_d_d_dv_m_d_dv_form_d",
    "expr_k_d_d_x_x_r_e_f_d_d_dv_m_d_dv_form_d",
    "calc_w_c_r_form_1",
    "expr_w_c_r_form_1",
    "calc_p_n_1_form_e",
    "expr_p_n_1_form_e",
    "calc_f_s_p_y_form_e",
    "expr_f_s_p_y_form_e",
    "calc_a_form_b",
    "expr_a_form_b",
    "calc_e_p_z_d_f_e_p_d_z_p_f_2602_2",
    "expr_e_p_z_d_f_e_p_d_z_p_f_2602_2",
    "calc_u_form_9",
    "expr_u_form_9",
    "calc_w_b_z_form_e",
    "expr_w_b_z_form_e",
    "calc_h_x_form_4",
    "expr_h_x_form_4",
    "calc_v_form_a",
    "expr_v_form_a",
    "calc_r_e_form_a",
    "expr_r_e_form_a",
    "calc_b_v_form_a",
    "expr_b_v_form_a",
    "calc_f_h_y_form_f",
    "expr_f_h_y_form_f",
    "calc_tau_w_form_f",
    "expr_tau_w_form_f",
    "calc_p_i_j_p_i_j_p_j_k_p_j_k_bt_sec",
    "expr_p_i_j_p_i_j_p_j_k_p_j_k_bt_sec",
    "calc_w_i_n_p_c_t_form_c",
    "expr_w_i_n_p_c_t_form_c",
    "calc_beta_form_c",
    "expr_beta_form_c",
    "calc_p_m_g_o_d_o_form_6",
    "expr_p_m_g_o_d_o_form_6",
    "calc_psi_r_a_da_n_psi_r_a_n_p_da_2602_2",
    "expr_psi_r_a_da_n_psi_r_a_n_p_da_2602_2",
    "calc_partial_y_c_k_epsilon_partial_form_7",
    "expr_partial_y_c_k_epsilon_partial_form_7",
    "calc_val_2_alpha_e_form_4",
    "expr_val_2_alpha_e_form_4",
    "calc_r_s_r_s_m_i_x_form_a",
    "expr_r_s_r_s_m_i_x_form_a",
    "calc_delta_r_beta_form_7",
    "expr_delta_r_beta_form_7",
    "calc_a_l_r_2_form_b",
    "expr_a_l_r_2_form_b",
    "calc_u_p_e_a_k_form_3",
    "expr_u_p_e_a_k_form_3",
    "calc_c_i_j_bt_sec",
    "expr_c_i_j_bt_sec",
    "calc_c_bt_sec",
    "expr_c_bt_sec",
    "calc_o_f_buchda",
    "expr_o_f_buchda",
    "calc_v_i_theta_alpha_0_form_e",
    "expr_v_i_theta_alpha_0_form_e",
    "calc_p_i_form_e",
    "expr_p_i_form_e",
    "calc_l_form_0",
    "expr_l_form_0",
    "calc_e_form_0",
    "expr_e_form_0",
    "calc_l_f_o_r_c_e_form_0",
    "expr_l_f_o_r_c_e_form_0",
    "calc_l_f_s_form_1",
    "expr_l_f_s_form_1",
    "calc_l_s_m_o_o_h_t_form_2",
    "expr_l_s_m_o_o_h_t_form_2",
    "calc_delta_i_x_form_2",
    "expr_delta_i_x_form_2",
    "calc_delta_e_k_p_form_7",
    "expr_delta_e_k_p_form_7",
    "calc_f_o_r_a_c_l_e_s_257_form_3",
    "expr_f_o_r_a_c_l_e_s_257_form_3",
    "calc_l_f_d_w_form_4",
    "expr_l_f_d_w_form_4",
    "calc_e_a_n_form_4",
    "expr_e_a_n_form_4",
    "calc_c_g_form_4",
    "expr_c_g_form_4",
    "calc_tau_form_4",
    "expr_tau_form_4",
    "calc_t_12_form_4",
    "expr_t_12_form_4",
    "calc_g_r_form_f",
    "expr_g_r_form_f",
    "calc_b_theta_form_5",
    "expr_b_theta_form_5",
    "calc_b_phi_form_7",
    "expr_b_phi_form_7",
    "calc_d_u_p_p_e_n_r_form_5",
    "expr_d_u_p_p_e_n_r_form_5",
    "calc_l_k_i_n_form_5",
    "expr_l_k_i_n_form_5",
    "calc_psi_form_1",
    "expr_psi_form_1",
    "calc_v_m_a_x_form_6",
    "expr_v_m_a_x_form_6",
    "calc_v_r_form_6",
    "expr_v_r_form_6",
    "calc_u_form_8",
    "expr_u_form_8",
    "calc_j_q_form_7",
    "expr_j_q_form_7",
    "calc_i_y_form_7",
    "expr_i_y_form_7",
    "calc_m_e_s_form_7",
    "expr_m_e_s_form_7",
    "calc_f_s_257_form_8",
    "expr_f_s_257_form_8",
    "calc_j_a_o_p_d_theta_form_9",
    "expr_j_a_o_p_d_theta_form_9",
    "calc_l_f_c_l_s_1_form_9",
    "expr_l_f_c_l_s_1_form_9",
    "calc_l_k_l_t_form_c",
    "expr_l_k_l_t_form_c",
    "calc_delta_x_1_brown_",
    "expr_delta_x_1_brown_",
    "calc_sim_r_i_brown_",
    "expr_sim_r_i_brown_",
    "calc_c_o_s_g_b_a_l_g_n_a_v_form_8",
    "expr_c_o_s_g_b_a_l_g_n_a_v_form_8",
    "calc_l_k_l_t_form_f",
    "expr_l_k_l_t_form_f",
    "calc_x_form_b",
    "expr_x_form_b",
    "calc_l_r_e_s_form_d",
    "expr_l_r_e_s_form_d",
    "calc_l_m_a_e_form_e",
    "expr_l_m_a_e_form_e",
    "calc_z_form_2",
    "expr_z_form_2",
    "calc_l_m_e_s_form_e",
    "expr_l_m_e_s_form_e",
    "calc_t_23_form_e",
    "expr_t_23_form_e",
    "calc_f_diebol",
    "expr_f_diebol",
    "calc_p_i_j_j_pi_bt_sec",
    "expr_p_i_j_j_pi_bt_sec",
    "calc_l_p_eta_bt_sec",
    "expr_l_p_eta_bt_sec",
    "calc_r_diebol",
    "expr_r_diebol",
    "calc_w_form_1",
    "expr_w_form_1",
    "calc_partial_partial_p_i_j_s_p_bt_sec",
    "expr_partial_partial_p_i_j_s_p_bt_sec",
    "calc_val_3_m_s_e_y_y_form_5",
    "expr_val_3_m_s_e_y_y_form_5",
    "calc_d_form_8",
    "expr_d_form_8",
    "calc_log_p_i_j_e_log_1_p_i_j_e_bt_sec",
    "expr_log_p_i_j_e_log_1_p_i_j_e_bt_sec",
    "calc_r_p_w_form_d",
    "expr_r_p_w_form_d",
    "calc_delta_alpha_alpha_form_e",
    "expr_delta_alpha_alpha_form_e",
    "calc_x_t_0_form_e",
    "expr_x_t_0_form_e",
    "calc_b_p_egidi_",
    "expr_b_p_egidi_",
    "calc_q_s_m_y_form_1",
    "expr_q_s_m_y_form_1",
    "calc_r_w_c_i_form_4",
    "expr_r_w_c_i_form_4",
    "calc_n_f_d_f_a_i_l_form_2",
    "expr_n_f_d_f_a_i_l_form_2",
    "calc_alpha_c_form_2",
    "expr_alpha_c_form_2",
    "calc_psi_form_3",
    "expr_psi_form_3",
    "calc_omega_form_4",
    "expr_omega_form_4",
    "calc_f_s_form_4",
    "expr_f_s_form_4",
    "calc_val_2609_05500_form_f",
    "expr_val_2609_05500_form_f",
    "calc_a_0_form_5",
    "expr_a_0_form_5",
    "calc_r_f_e_e_t_k_delta_q_form_5",
    "expr_r_f_e_e_t_k_delta_q_form_5",
    "calc_r_t_form_6",
    "expr_r_t_form_6",
    "calc_e_0_y_4_theta_form_6",
    "expr_e_0_y_4_theta_form_6",
    "calc_v_mu_form_d",
    "expr_v_mu_form_d",
    "calc_v_x_t_form_f",
    "expr_v_x_t_form_f",
    "calc_e_0_y_theta_4_form_8",
    "expr_e_0_y_theta_4_form_8",
    "calc_phi_form_e",
    "expr_phi_form_e",
    "calc_e_z_h_t_form_f",
    "expr_e_z_h_t_form_f",
    "calc_w_z_form_f",
    "expr_w_z_form_f",
    "calc_n_w_s_form_f",
    "expr_n_w_s_form_f",
    "calc_eta_m_form_8",
    "expr_eta_m_form_8",
    "calc_g_r_form_b",
    "expr_g_r_form_b",
    "calc_o_t_form_c",
    "expr_o_t_form_c",
    "calc_e_c_e_guo_20",
    "expr_e_c_e_guo_20",
    "calc_miller2005_82322c",
    "expr_miller2005_82322c",
    "calc_k_p_form_0",
    "expr_k_p_form_0",
    "calc_s_p_x_gneiti",
    "expr_s_p_x_gneiti",
    "calc_t_k_form_7",
    "expr_t_k_form_7",
    "calc_f_alpha_s_form_d",
    "expr_f_alpha_s_form_d",
    "calc_l_guo_20",
    "expr_l_guo_20",
    "calc_i_m_i_n_n_i_u_form_4",
    "expr_i_m_i_n_n_i_u_form_4",
    "calc_k_m_i_n_n_k_u_form_4",
    "expr_k_m_i_n_n_k_u_form_4",
    "calc_f_q_s_form_4",
    "expr_f_q_s_form_4",
    "calc_w_delta_form_5",
    "expr_w_delta_form_5",
    "calc_phi_v_i_r_t_form_5",
    "expr_phi_v_i_r_t_form_5",
    "calc_e_a_m_form_6",
    "expr_e_a_m_form_6",
    "calc_theta_form_7",
    "expr_theta_form_7",
    "calc_d_form_9",
    "expr_d_form_9",
    "calc_db_tau_form_9",
    "expr_db_tau_form_9",
    "calc_l_y_k_u_form_1",
    "expr_l_y_k_u_form_1",
    "calc_partial_x_c_k_epsilon_partial_form_a",
    "expr_partial_x_c_k_epsilon_partial_form_a",
    "calc_e_t_form_b",
    "expr_e_t_form_b",
    "calc_a_s_h_0_di_f_f_i_c_u_l_t_form_b",
    "expr_a_s_h_0_di_f_f_i_c_u_l_t_form_b",
    "calc_i_b_a_l_l_form_e",
    "expr_i_b_a_l_l_form_e",
    "calc_s_s_k_i_l_l_n_gneiti",
    "expr_s_s_k_i_l_l_n_gneiti",
    "calc_r_u_form_2",
    "expr_r_u_form_2",
    "calc_val_2610_27057_form_2",
    "expr_val_2610_27057_form_2",
    "calc_val_2609_24299_form_2",
    "expr_val_2609_24299_form_2",
    "calc_s_c_p_1_gneiti",
    "expr_s_c_p_1_gneiti",
    "calc_g_p_gneiti",
    "expr_g_p_gneiti",
    "calc_val_2609_04690_form_2",
    "expr_val_2609_04690_form_2",
    "calc_b_gneiti",
    "expr_b_gneiti",
    "calc_l_o_b_g_gneiti",
    "expr_l_o_b_g_gneiti",
    "calc_val_2609_24299_form_4",
    "expr_val_2609_24299_form_4",
    "calc_a_l_r_1_form_5",
    "expr_a_l_r_1_form_5",
    "calc_u_form_4",
    "expr_u_form_4",
    "calc_s_2_harvey",
    "expr_s_2_harvey",
    "calc_l_s_h_a_r_e_d_i_form_d",
    "expr_l_s_h_a_r_e_d_i_form_d",
    "calc_c_v_a_r_alpha_x_c_form_3",
    "expr_c_v_a_r_alpha_x_c_form_3",
    "calc_j_f_k_l_s_j_f_k_l_pi_form_a",
    "expr_j_f_k_l_s_j_f_k_l_pi_form_a",
    "calc_val_1_12_2_harvey",
    "expr_val_1_12_2_harvey",
    "calc_c_i_maher_",
    "expr_c_i_maher_",
    "calc_f_s_b_y_2005_0",
    "expr_f_s_b_y_2005_0",
    "calc_u_form_0",
    "expr_u_form_0",
    "calc_w_form_0",
    "expr_w_form_0",
    "calc_v_form_0",
    "expr_v_form_0",
    "calc_p_w_i_g_n_form_1",
    "expr_p_w_i_g_n_form_1",
    "calc_v_a_l_m_psi_x_form_2",
    "expr_v_a_l_m_psi_x_form_2",
    "calc_c_e_b_c_w_e_i_j_form_2",
    "expr_c_e_b_c_w_e_i_j_form_2",
    "calc_v_form_2",
    "expr_v_form_2",
    "calc_l_e_q_u_2333_c_1_form_3",
    "expr_l_e_q_u_2333_c_1_form_3",
    "calc_l_w_i_g_n_form_3",
    "expr_l_w_i_g_n_form_3",
    "calc_p_form_4",
    "expr_p_form_4",
    "calc_r_form_4",
    "expr_r_form_4",
    "calc_h_p_form_6",
    "expr_h_p_form_6",
    "calc_delta_1_form_6",
    "expr_delta_1_form_6",
    "calc_m_e_r_e_g_g_3_form_3",
    "expr_m_e_r_e_g_g_3_form_3",
    "calc_d_form_7",
    "expr_d_form_7",
    "calc_h_t_form_7",
    "expr_h_t_form_7",
    "calc_openalex_sutton1988_w2100677568_form_0",
    "expr_openalex_sutton1988_w2100677568_form_0",
    "calc_i_f_w_form_7",
    "expr_i_f_w_form_7",
    "calc_r_e_form_7",
    "expr_r_e_form_7",
    "calc_n_e_v_x_form_7",
    "expr_n_e_v_x_form_7",
    "calc_k_t_form_9",
    "expr_k_t_form_9",
    "calc_e_c_o_n_t_a_c_t_form_9",
    "expr_e_c_o_n_t_a_c_t_form_9",
    "calc_sim_h_dagger_n_form_1",
    "expr_sim_h_dagger_n_form_1",
    "calc_d_xi_xi_form_2",
    "expr_d_xi_xi_form_2",
    "calc_a_v_g_t_i_e_m_form_3",
    "expr_a_v_g_t_i_e_m_form_3",
    "calc_t_form_8",
    "expr_t_form_8",
    "calc_theta_w_form_1",
    "expr_theta_w_form_1",
    "calc_abs_n_r_n_t_a_r_g_e_t_22_form_0",
    "expr_abs_n_r_n_t_a_r_g_e_t_22_form_0",
    "calc_q_form_1",
    "expr_q_form_1",
    "calc_val_0_form_5",
    "expr_val_0_form_5",
    "calc_s_form_e",
    "expr_s_form_e",
    "calc_sigma_form_2",
    "expr_sigma_form_2",
    "calc_f_a_e_o_r_form_3",
    "expr_f_a_e_o_r_form_3",
    "calc_c_tau_form_4",
    "expr_c_tau_form_4",
    "calc_tau_e_t_x_form_4",
    "expr_tau_e_t_x_form_4",
    "calc_theta_l_r_t_form_5",
    "expr_theta_l_r_t_form_5",
    "calc_p_a_form_5",
    "expr_p_a_form_5",
    "calc_u_h_i_n_form_e",
    "expr_u_h_i_n_form_e",
    "calc_i_d_s_form_8",
    "expr_i_d_s_form_8",
    "calc_psi_form_f",
    "expr_psi_form_f",
    "calc_q_s_form_9",
    "expr_q_s_form_9",
    "calc_w_e_s_form_9",
    "expr_w_e_s_form_9",
    "calc_r_t_theta_form_9",
    "expr_r_t_theta_form_9",
    "calc_f_i_form_9",
    "expr_f_i_form_9",
    "calc_v_form_9",
    "expr_v_form_9",
    "calc_h_d_form_a",
    "expr_h_d_form_a",
    "calc_r_c_l_e_a_r_form_c",
    "expr_r_c_l_e_a_r_form_c",
    "calc_r_e_form_d",
    "expr_r_e_form_d",
    "calc_h_l_i_j_c_1_form_d",
    "expr_h_l_i_j_c_1_form_d",
    "calc_false_form_e",
    "expr_false_form_e",
    "calc_p_r_form_e",
    "expr_p_r_form_e",
    "calc_r_i_t_form_c",
    "expr_r_i_t_form_c",
    "calc_q_l_y_t_form_7",
    "expr_q_l_y_t_form_7",
    "calc_q_l_y_t_form_a",
    "expr_q_l_y_t_form_a",
    "calc_q_l_y_t_form_c",
    "expr_q_l_y_t_form_c",
    "calc_p_i_i_l_form_5",
    "expr_p_i_i_l_form_5",
    "calc_p_o_s_t_p_a_r_i_t_y_z_form_d",
    "expr_p_o_s_t_p_a_r_i_t_y_z_form_d",
    "calc_w_i_j_form_a",
    "expr_w_i_j_form_a",
    "calc_i_m_form_0",
    "expr_i_m_form_0",
    "calc_epsilon_i_1312_7",
    "expr_epsilon_i_1312_7",
    "calc_i_y_2209_0",
    "expr_i_y_2209_0",
    "calc_u_s_form_c",
    "expr_u_s_form_c",
    "calc_m_p_j_p_b_e_form_e",
    "expr_m_p_j_p_b_e_form_e",
    "calc_m_omega_v_v_form_9",
    "expr_m_omega_v_v_form_9",
    "calc_m_form_1",
    "expr_m_form_1",
    "calc_tau_t_form_f",
    "expr_tau_t_form_f",
    "calc_b_f_form_2",
    "expr_b_f_form_2",
    "calc_r_beta_form_4",
    "expr_r_beta_form_4",
    "calc_begin_x_k_a_l_i_g_n_d_e_form_4",
    "expr_begin_x_k_a_l_i_g_n_d_e_form_4",
    "calc_r_m_d_i_form_5",
    "expr_r_m_d_i_form_5",
    "calc_p_i_j_form_6",
    "expr_p_i_j_form_6",
    "calc_eq_e_x_e_f_y_form_8",
    "expr_eq_e_x_e_f_y_form_8",
    "calc_f_tau_form_c",
    "expr_f_tau_form_c",
    "calc_x_form_c",
    "expr_x_form_c",
    "calc_l_z_form_a",
    "expr_l_z_form_a",
    "calc_p_a_form_b",
    "expr_p_a_form_b",
    "calc_v_f_f_form_c",
    "expr_v_f_f_form_c",
    "calc_l_k_x_k_u_form_c",
    "expr_l_k_x_k_u_form_c",
    "calc_u_i_brown_",
    "expr_u_i_brown_",
    "calc_i_n_de_x_form_0",
    "expr_i_n_de_x_form_0",
    "calc_c_v_z_form_0",
    "expr_c_v_z_form_0",
    "calc_m_p_p_form_4",
    "expr_m_p_p_form_4",
    "calc_m_n_p_form_5",
    "expr_m_n_p_form_5",
    "calc_m_p_j_e_p_form_5",
    "expr_m_p_j_e_p_form_5",
    "calc_c_e_form_5",
    "expr_c_e_form_5",
    "calc_c_e_form_6",
    "expr_c_e_form_6",
    "calc_delta_e_alpha_t_2_2_form_6",
    "expr_delta_e_alpha_t_2_2_form_6",
    "calc_mu_h_i_form_7",
    "expr_mu_h_i_form_7",
    "calc_theta_3_form_8",
    "expr_theta_3_form_8",
    "calc_a_j_u_form_9",
    "expr_a_j_u_form_9",
    "calc_w_a_p_form_9",
    "expr_w_a_p_form_9",
    "calc_val_1205_2071_form_9",
    "expr_val_1205_2071_form_9",
    "calc_e_form_a",
    "expr_e_form_a",
    "calc_d_i_v_form_c",
    "expr_d_i_v_form_c",
    "calc_c_g_f_r_form_c",
    "expr_c_g_f_r_form_c",
    "calc_g_rho_form_d",
    "expr_g_rho_form_d",
    "calc_n_alpha_form_d",
    "expr_n_alpha_form_d",
    "calc_tan_0_psi_psi_form_d",
    "expr_tan_0_psi_psi_form_d",
    "calc_v_v_1_form_e",
    "expr_v_v_1_form_e",
    "calc_lambda_2_form_e",
    "expr_lambda_2_form_e",
    "calc_r_beta_form_e",
    "expr_r_beta_form_e",
    "calc_s_w_form_0",
    "expr_s_w_form_0",
    "calc_j_a_o_p_d_theta_form_1",
    "expr_j_a_o_p_d_theta_form_1",
    "calc_y_r_s_h_s_y_p_s_form_1",
    "expr_y_r_s_h_s_y_p_s_form_1",
    "calc_j_0_form_2",
    "expr_j_0_form_2",
    "calc_j_i_form_3",
    "expr_j_i_form_3",
    "calc_d_m_s_w_form_3",
    "expr_d_m_s_w_form_3",
    "calc_z_form_4",
    "expr_z_form_4",
    "calc_w_c_y_form_6",
    "expr_w_c_y_form_6",
    "calc_l_a_a_i_form_6",
    "expr_l_a_a_i_form_6",
    "calc_h_e_f_f_form_7",
    "expr_h_e_f_f_form_7",
    "calc_omega_o_b_s_form_7",
    "expr_omega_o_b_s_form_7",
    "calc_k_theta_l_form_7",
    "expr_k_theta_l_form_7",
    "calc_e_u_p_p_e_r_form_a",
    "expr_e_u_p_p_e_r_form_a",
    "calc_e_s_m_o_o_h_t_form_b",
    "expr_e_s_m_o_o_h_t_form_b",
    "calc_g_theta_form_b",
    "expr_g_theta_form_b",
    "calc_k_l_l_s_form_c",
    "expr_k_l_l_s_form_c",
    "calc_e_p_e_n_form_d",
    "expr_e_p_e_n_form_d",
    "calc_q_form_f",
    "expr_q_form_f",
    "calc_d_d_form_f",
    "expr_d_d_form_f",
    "calc_r_c_o_m_p_l_y_form_f",
    "expr_r_c_o_m_p_l_y_form_f",
    "calc_l_0_p_w_form_0",
    "expr_l_0_p_w_form_0",
    "calc_r_s_r_s_m_i_x_form_0",
    "expr_r_s_r_s_m_i_x_form_0",
    "calc_e_a_sim_t_a_s_h_0_a_form_0",
    "expr_e_a_sim_t_a_s_h_0_a_form_0",
    "calc_t_di_f_f_i_c_u_l_t_form_0",
    "expr_t_di_f_f_i_c_u_l_t_form_0",
    "calc_h_y_form_2",
    "expr_h_y_form_2",
    "calc_l_b_a_e_s_form_a",
    "expr_l_b_a_e_s_form_a",
    "calc_l_f_k_l_theta_form_a",
    "expr_l_f_k_l_theta_form_a",
    "calc_w_form_4",
    "expr_w_form_4",
    "calc_r_s_r_pi_form_4",
    "expr_r_s_r_pi_form_4",
    "calc_p_u_form_5",
    "expr_p_u_form_5",
    "calc_g_s_p_e_c_t_r_a_l_form_5",
    "expr_g_s_p_e_c_t_r_a_l_form_5",
    "calc_e_r_e_c_n_o_form_c",
    "expr_e_r_e_c_n_o_form_c",
    "calc_f_form_5",
    "expr_f_form_5",
    "calc_sim_j_a_o_p_d_theta_form_d",
    "expr_sim_j_a_o_p_d_theta_form_d",
    "calc_tau_form_d",
    "expr_tau_form_d",
    "calc_j_4_form_7",
    "expr_j_4_form_7",
    "calc_j_u_delta_u_form_7",
    "expr_j_u_delta_u_form_7",
    "calc_g_k_form_7",
    "expr_g_k_form_7",
    "calc_l_f_m_form_8",
    "expr_l_f_m_form_8",
    "calc_i_x_form_9",
    "expr_i_x_form_9",
    "calc_j_5_form_9",
    "expr_j_5_form_9",
    "calc_p_x_z_form_c",
    "expr_p_x_z_form_c",
    "calc_sim_t_w_form_c",
    "expr_sim_t_w_form_c",
    "calc_l_r_e_c_n_o_form_d",
    "expr_l_r_e_c_n_o_form_d",
    "calc_e_f_i_n_a_l_form_e",
    "expr_e_f_i_n_a_l_form_e",
    "calc_j_f_k_l_theta_form_e",
    "expr_j_f_k_l_theta_form_e",
    "calc_n_q_form_0",
    "expr_n_q_form_0",
    "calc_c_t_form_0",
    "expr_c_t_form_0",
    "calc_e_0_a_4_i_form_2",
    "expr_e_0_a_4_i_form_2",
    "calc_l_omega_b_form_3",
    "expr_l_omega_b_form_3",
    "calc_log_z_e_form_4",
    "expr_log_z_e_form_4",
    "calc_f_k_l_s_form_5",
    "expr_f_k_l_s_form_5",
    "calc_r_s_form_6",
    "expr_r_s_form_6",
    "calc_n_pi_form_6",
    "expr_n_pi_form_6",
    "calc_val_1_h_r_s_r_pi_form_8",
    "expr_val_1_h_r_s_r_pi_form_8",
    "calc_l_g_a_p_w_form_8",
    "expr_l_g_a_p_w_form_8",
    "calc_e_u_s_t_form_9",
    "expr_e_u_s_t_form_9",
    "calc_p_b_a_s_e_l_i_e_n_form_9",
    "expr_p_b_a_s_e_l_i_e_n_form_9",
    "calc_g_a_form_9",
    "expr_g_a_form_9",
    "calc_l_p_m_form_a",
    "expr_l_p_m_form_a",
    "calc_o_b_k_s_form_9",
    "expr_o_b_k_s_form_9",
    "calc_c_p_form_a",
    "expr_c_p_form_a",
    "calc_val_2610_31563_form_b",
    "expr_val_2610_31563_form_b",
    "calc_f_r_form_4",
    "expr_f_r_form_4",
    "calc_q_s_h_0_di_f_f_i_c_u_l_t_form_c",
    "expr_q_s_h_0_di_f_f_i_c_u_l_t_form_c",
    "calc_j_form_5",
    "expr_j_form_5",
    "calc_p_s_form_5",
    "expr_p_s_form_5",
    "calc_e_m_d_n_o_r_m_p_q_form_d",
    "expr_e_m_d_n_o_r_m_p_q_form_d",
    "calc_e_a_s_sim_c_a_s_h_a_form_f",
    "expr_e_a_s_sim_c_a_s_h_a_form_f",
    "calc_phi_x_form_0",
    "expr_phi_x_form_0",
    "calc_m_r_s_form_1",
    "expr_m_r_s_form_1",
    "calc_h_g_form_1",
    "expr_h_g_form_1",
    "calc_val_2610_28223_form_1",
    "expr_val_2610_28223_form_1",
    "calc_sigma_a_a_sigma_form_4",
    "expr_sigma_a_a_sigma_form_4",
    "calc_n_q_1_form_4",
    "expr_n_q_1_form_4",
    "calc_log_b_e_form_5",
    "expr_log_b_e_form_5",
    "calc_w_sigma_a_a_sigma_form_5",
    "expr_w_sigma_a_a_sigma_form_5",
    "calc_lambda_v_form_5",
    "expr_lambda_v_form_5",
    "calc_val_0_form_6",
    "expr_val_0_form_6",
    "calc_l_form_9",
    "expr_l_form_9",
    "calc_p_s_form_b",
    "expr_p_s_form_b",
    "calc_val_2_a_sigma_form_b",
    "expr_val_2_a_sigma_form_b",
    "calc_l_form_c",
    "expr_l_form_c",
    "calc_d_form_d",
    "expr_d_form_d",
    "calc_val_2_a_sigma_form_e",
    "expr_val_2_a_sigma_form_e",
    "calc_i_theta_form_f",
    "expr_i_theta_form_f",
    "calc_l_s_k_k_l_form_1",
    "expr_l_s_k_k_l_form_1",
    "calc_val_2610_26568_form_2",
    "expr_val_2610_26568_form_2",
    "calc_g_eta_form_2",
    "expr_g_eta_form_2",
    "calc_a_form_2",
    "expr_a_form_2",
    "calc_pi_beta_w_form_3",
    "expr_pi_beta_w_form_3",
    "calc_a_w_form_3",
    "expr_a_w_form_3",
    "calc_d_f_form_4",
    "expr_d_f_form_4",
    "calc_f_form_4",
    "expr_f_form_4",
    "calc_h_form_6",
    "expr_h_form_6",
    "calc_e_y_form_6",
    "expr_e_y_form_6",
    "calc_z_m_i_x_form_e",
    "expr_z_m_i_x_form_e",
    "calc_r_m_a_x_r_m_i_n_form_7",
    "expr_r_m_a_x_r_m_i_n_form_7",
    "calc_sim_j_m_form_8",
    "expr_sim_j_m_form_8",
    "calc_r_h_form_a",
    "expr_r_h_form_a",
    "calc_a_l_r_form_a",
    "expr_a_l_r_form_a",
    "calc_l_e_gamma_i_j_form_a",
    "expr_l_e_gamma_i_j_form_a",
    "calc_w_form_a",
    "expr_w_form_a",
    "calc_h_m_form_b",
    "expr_h_m_form_b",
    "calc_o_v_x_y_e_e_i_j_k_l_form_b",
    "expr_o_v_x_y_e_e_i_j_k_l_form_b",
    "calc_l_o_t_v_form_c",
    "expr_l_o_t_v_form_c",
    "calc_l_e_gamma_i_j_h_m_form_c",
    "expr_l_e_gamma_i_j_h_m_form_c",
    "calc_p_w_t_form_2",
    "expr_p_w_t_form_2",
    "calc_ds_dw_form_d",
    "expr_ds_dw_form_d",
    "calc_h_form_f",
    "expr_h_form_f",
    "calc_dt_dw_form_f",
    "expr_dt_dw_form_f",
    "calc_z_i_de_a_l_form_0",
    "expr_z_i_de_a_l_form_0",
    "calc_rho_t_x_p_d_2_form_0",
    "expr_rho_t_x_p_d_2_form_0",
    "calc_w_k_s_form_1",
    "expr_w_k_s_form_1",
    "calc_p_r_i_s_m_i_l_s_form_1",
    "expr_p_r_i_s_m_i_l_s_form_1",
    "calc_rho_r_x_form_1",
    "expr_rho_r_x_form_1",
    "calc_k_1_form_3",
    "expr_k_1_form_3",
    "calc_e_v_form_3",
    "expr_e_v_form_3",
    "calc_l_p_r_i_s_m_i_form_3",
    "expr_l_p_r_i_s_m_i_form_3",
    "calc_psi_t_form_4",
    "expr_psi_t_form_4",
    "calc_n_g_n_l_s_form_5",
    "expr_n_g_n_l_s_form_5",
    "calc_phi_eta_form_5",
    "expr_phi_eta_form_5",
    "calc_d_form_6",
    "expr_d_form_6",
    "calc_p_i_t_form_6",
    "expr_p_i_t_form_6",
    "calc_c_p_form_f",
    "expr_c_p_form_f",
    "calc_y_form_f",
    "expr_y_form_f",
    "calc_l_s_h_a_r_e_d_i_form_7",
    "expr_l_s_h_a_r_e_d_i_form_7",
    "calc_val_2610_25605_form_8",
    "expr_val_2610_25605_form_8",
    "calc_p_m_form_9",
    "expr_p_m_form_9",
    "calc_true_form_9",
    "expr_true_form_9",
    "calc_beta_c_v_a_r_alpha_v_p_form_9",
    "expr_beta_c_v_a_r_alpha_v_p_form_9",
    "calc_e_s_k_n_y_form_b",
    "expr_e_s_k_n_y_form_b",
    "calc_f_p_b_form_d",
    "expr_f_p_b_form_d",
    "calc_g_eta_form_e",
    "expr_g_eta_form_e",
    "calc_w_b_r_form_0",
    "expr_w_b_r_form_0",
    "calc_e_form_1",
    "expr_e_form_1",
    "calc_w_b_x_form_1",
    "expr_w_b_x_form_1",
    "calc_l_form_2",
    "expr_l_form_2",
    "calc_p_r_dk_e_form_3",
    "expr_p_r_dk_e_form_3",
    "calc_e_p_form_3",
    "expr_e_p_form_3",
    "calc_w_b_r_form_3",
    "expr_w_b_r_form_3",
    "calc_a_p_form_5",
    "expr_a_p_form_5",
    "calc_a_j_h_form_8",
    "expr_a_j_h_form_8",
    "calc_i_z_form_8",
    "expr_i_z_form_8",
    "calc_s_w_form_8",
    "expr_s_w_form_8",
    "calc_z_m_i_x_form_8",
    "expr_z_m_i_x_form_8",
    "calc_l_r_o_l_l_j_o_i_n_form_9",
    "expr_l_r_o_l_l_j_o_i_n_form_9",
    "calc_rho_t_x_p_d_1_form_9",
    "expr_rho_t_x_p_d_1_form_9",
    "calc_f_m_a_x_form_9",
    "expr_f_m_a_x_form_9",
    "calc_p_c_i_j_form_9",
    "expr_p_c_i_j_form_9",
    "calc_z_m_i_x_form_9",
    "expr_z_m_i_x_form_9",
    "calc_a_v_e_phi_t_form_a",
    "expr_a_v_e_phi_t_form_a",
    "calc_l_r_o_l_l_e_x_c_e_s_s_form_c",
    "expr_l_r_o_l_l_e_x_c_e_s_s_form_c",
    "calc_o_form_c",
    "expr_o_form_c",
    "calc_l_s_h_a_r_e_d_i_form_c",
    "expr_l_s_h_a_r_e_d_i_form_c",
    "calc_i_z_form_f",
    "expr_i_z_form_f",
    "calc_e_p_form_1",
    "expr_e_p_form_1",
    "calc_v_infty_t_x_form_1",
    "expr_v_infty_t_x_form_1",
    "calc_t_p_x_p_y_p_z_1_form_5",
    "expr_t_p_x_p_y_p_z_1_form_5",
    "calc_v_t_t_x_form_5",
    "expr_v_t_t_x_form_5",
    "calc_w_c_x_form_9",
    "expr_w_c_x_form_9",
    "calc_i_w_form_a",
    "expr_i_w_form_a",
    "calc_f_c_d_m_form_a",
    "expr_f_c_d_m_form_a",
    "calc_theta_form_b",
    "expr_theta_form_b",
    "calc_q_dt_p_form_c",
    "expr_q_dt_p_form_c",
    "calc_val_2_r_phi_form_d",
    "expr_val_2_r_phi_form_d",
    "calc_tau_t_l_form_0",
    "expr_tau_t_l_form_0",
    "calc_v_infty_t_x_v_infty_t_y_form_1",
    "expr_v_infty_t_x_v_infty_t_y_form_1",
    "calc_sigma_j_l_form_6",
    "expr_sigma_j_l_form_6",
    "calc_h_a_p_e_x_form_b",
    "expr_h_a_p_e_x_form_b",
    "calc_s_form_c",
    "expr_s_form_c",
    "calc_v_beta_t_t_x_form_f",
    "expr_v_beta_t_t_x_form_f",
    "calc_y_s_form_0",
    "expr_y_s_form_0",
    "calc_sim_s_t_form_0",
    "expr_sim_s_t_form_0",
    "calc_u_t_x_form_1",
    "expr_u_t_x_form_1",
    "calc_t_s_s_k_form_3",
    "expr_t_s_s_k_form_3",
    "calc_pi_i_j_form_7",
    "expr_pi_i_j_form_7",
    "calc_omega_s_form_6",
    "expr_omega_s_form_6",
    "calc_sigma_a_x_form_7",
    "expr_sigma_a_x_form_7",
    "calc_partial_p_w_t_partial_s_i_form_8",
    "expr_partial_p_w_t_partial_s_i_form_8",
    "calc_kappa_form_8",
    "expr_kappa_form_8",
    "calc_t_k_form_8",
    "expr_t_k_form_8",
    "calc_k_epsilon_s_l_l_s_form_8",
    "expr_k_epsilon_s_l_l_s_form_8",
    "calc_j_p_form_d",
    "expr_j_p_form_d",
    "calc_g_i_form_1",
    "expr_g_i_form_1",
    "calc_e_l_form_2",
    "expr_e_l_form_2",
    "calc_i_pi_form_3",
    "expr_i_pi_form_3",
    "calc_i_p_form_4",
    "expr_i_p_form_4",
    "calc_f_h_form_4",
    "expr_f_h_form_4",
    "calc_i_l_form_5",
    "expr_i_l_form_5",
    "calc_e_i_p_form_5",
    "expr_e_i_p_form_5",
    "calc_i_y_form_5",
    "expr_i_y_form_5",
    "calc_delta_p_w_t_form_5",
    "expr_delta_p_w_t_form_5",
    "calc_n_i_form_6",
    "expr_n_i_form_6",
    "calc_e_s_form_6",
    "expr_e_s_form_6",
    "calc_h_x_form_6",
    "expr_h_x_form_6",
    "calc_f_m_lambda_x_form_7",
    "expr_f_m_lambda_x_form_7",
    "calc_t_a_b_form_9",
    "expr_t_a_b_form_9",
    "calc_f_m_lambda_x_form_9",
    "expr_f_m_lambda_x_form_9",
    "calc_t_a_b_form_a",
    "expr_t_a_b_form_a",
    "calc_l_c_x_form_b",
    "expr_l_c_x_form_b",
    "calc_v_form_c",
    "expr_v_form_c",
    "calc_t_a_b_form_c",
    "expr_t_a_b_form_c",
    "calc_pi_s_form_d",
    "expr_pi_s_form_d",
    "calc_t_k_form_d",
    "expr_t_k_form_d",
    "calc_v_b_t_r_b_w_form_e",
    "expr_v_b_t_r_b_w_form_e",
    "calc_c_e_x_a_c_t_form_f",
    "expr_c_e_x_a_c_t_form_f",
    "calc_e_a_g_v_form_0",
    "expr_e_a_g_v_form_0",
    "calc_i_z_form_1",
    "expr_i_z_form_1",
    "calc_s_form_1",
    "expr_s_form_1",
    "calc_dt_k_form_1",
    "expr_dt_k_form_1",
    "calc_d_a_form_1",
    "expr_d_a_form_1",
    "calc_ds_h_o_e_r_form_2",
    "expr_ds_h_o_e_r_form_2",
    "calc_eta_i_form_4",
    "expr_eta_i_form_4",
    "calc_dt_k_form_4",
    "expr_dt_k_form_4",
    "calc_g_sigma_form_5",
    "expr_g_sigma_form_5",
    "calc_a_c_u_form_5",
    "expr_a_c_u_form_5",
    "calc_log_y_i_e_form_6",
    "expr_log_y_i_e_form_6",
    "calc_s_form_6",
    "expr_s_form_6",
    "calc_l_c_a_3_d_m_form_7",
    "expr_l_c_a_3_d_m_form_7",
    "calc_g_c_r_form_8",
    "expr_g_c_r_form_8",
    "calc_a_s_t_form_1",
    "expr_a_s_t_form_1",
    "calc_t_k_form_9",
    "expr_t_k_form_9",
    "calc_eta_i_form_9",
    "expr_eta_i_form_9",
    "calc_r_p_r_i_form_a",
    "expr_r_p_r_i_form_a",
    "calc_d_form_a",
    "expr_d_form_a",
    "calc_x_i_t_form_b",
    "expr_x_i_t_form_b",
    "calc_p_0_form_c",
    "expr_p_0_form_c",
    "calc_e_b_t_form_c",
    "expr_e_b_t_form_c",
    "calc_u_o_t_v_form_c",
    "expr_u_o_t_v_form_c",
    "calc_r_form_c",
    "expr_r_form_c",
    "calc_g_i_form_d",
    "expr_g_i_form_d",
    "calc_i_x_form_f",
    "expr_i_x_form_f",
    "calc_i_w_form_f",
    "expr_i_w_form_f",
    "calc_l_x_form_f",
    "expr_l_x_form_f",
    "calc_t_x_1_form_f",
    "expr_t_x_1_form_f",
    "calc_l_o_s_s_2206_0",
    "expr_l_o_s_s_2206_0",
    "calc_delta_r_e_e_v_e_n_t_2208_0",
    "expr_delta_r_e_e_v_e_n_t_2208_0",
    "calc_w_k_form_0",
    "expr_w_k_form_0",
    "calc_l_i_m_i_n_f_n_b_n_form_0",
    "expr_l_i_m_i_n_f_n_b_n_form_0",
    "calc_b_r_s_form_1",
    "expr_b_r_s_form_1",
    "calc_r_i_j_form_1",
    "expr_r_i_j_form_1",
    "calc_lambda_s_form_2",
    "expr_lambda_s_form_2",
    "calc_delta_h_form_2",
    "expr_delta_h_form_2",
    "calc_delta_h_k_form_2",
    "expr_delta_h_k_form_2",
    "calc_i_y_i_y_form_2",
    "expr_i_y_i_y_form_2",
    "calc_c_t_form_3",
    "expr_c_t_form_3",
    "calc_omega_b_w_form_4",
    "expr_omega_b_w_form_4",
    "calc_l_a_form_8",
    "expr_l_a_form_8",
    "calc_e_pi_s_form_8",
    "expr_e_pi_s_form_8",
    "calc_l_v_e_l_form_8",
    "expr_l_v_e_l_form_8",
    "calc_n_form_9",
    "expr_n_form_9",
    "calc_dt_k_form_a",
    "expr_dt_k_form_a",
    "calc_v_z_form_b",
    "expr_v_z_form_b",
    "calc_r_form_b",
    "expr_r_form_b",
    "calc_alpha_form_c",
    "expr_alpha_form_c",
    "calc_sim_r_t_o_b_p_form_c",
    "expr_sim_r_t_o_b_p_form_c",
    "calc_df_o_r_w_a_dt_r_form_d",
    "expr_df_o_r_w_a_dt_r_form_d",
    "calc_y_i_form_d",
    "expr_y_i_form_d",
    "calc_rho_beta_e_form_d",
    "expr_rho_beta_e_form_d",
    "calc_delta_1312_7",
    "expr_delta_1312_7",
    "calc_eta_i_1312_7",
    "expr_eta_i_1312_7",
    "calc_kappa_i_j_1312_7",
    "expr_kappa_i_j_1312_7",
    "calc_alpha_t_1_1706_1",
    "expr_alpha_t_1_1706_1",
    "calc_b_t_1_1706_1",
    "expr_b_t_1_1706_1",
    "calc_h_sigma_sigma_1712_0",
    "expr_h_sigma_sigma_1712_0",
    "calc_v_mu_form_2",
    "expr_v_mu_form_2",
    "calc_p_form_2",
    "expr_p_form_2",
    "calc_u_2_s_3_form_2",
    "expr_u_2_s_3_form_2",
    "calc_c_form_2",
    "expr_c_form_2",
    "calc_p_k_form_5",
    "expr_p_k_form_5",
    "calc_delta_h_form_6",
    "expr_delta_h_form_6",
    "calc_l_v_r_r_e_e_2223_form_7",
    "expr_l_v_r_r_e_e_2223_form_7",
    "calc_c_r_r_form_7",
    "expr_c_r_r_form_7",
    "calc_lambda_i_phi_form_7",
    "expr_lambda_i_phi_form_7",
    "calc_val_2507_16328_form_7",
    "expr_val_2507_16328_form_7",
    "calc_val_2507_16328_form_9",
    "expr_val_2507_16328_form_9",
    "calc_l_r_o_o_t_form_9",
    "expr_l_r_o_o_t_form_9",
    "calc_i_y_form_a",
    "expr_i_y_form_a",
    "calc_c_b_r_form_f",
    "expr_c_b_r_form_f",
    "calc_val_2506_22350_2506_2",
    "expr_val_2506_22350_2506_2",
    "calc_theta_1_2510_2",
    "expr_theta_1_2510_2",
    "calc_beta_p_a_r_k_p_2603_2",
    "expr_beta_p_a_r_k_p_2603_2",
    "calc_sim_beta_0_2603_2",
    "expr_sim_beta_0_2603_2",
    "calc_z_2603_2",
    "expr_z_2603_2",
    "calc_i_z_2609_0",
    "expr_i_z_2609_0",
    "calc_t_s_e_delta_brown_",
    "expr_t_s_e_delta_brown_",
    "calc_delta_t_e_s_brown_",
    "expr_delta_t_e_s_brown_",
    "calc_p_egidi_",
    "expr_p_egidi_",
    "calc_k_tau_form_0",
    "expr_k_tau_form_0",
    "calc_eta_g_form_2",
    "expr_eta_g_form_2",
    "calc_p_z_l_o_form_3",
    "expr_p_z_l_o_form_3",
    "calc_a_q_form_6",
    "expr_a_q_form_6",
    "calc_e_j_form_6",
    "expr_e_j_form_6",
    "calc_l_v_form_6",
    "expr_l_v_form_6",
    "calc_u_2_s_4_form_7",
    "expr_u_2_s_4_form_7",
    "calc_z_m_i_x_form_7",
    "expr_z_m_i_x_form_7",
    "calc_r_p_o_s_form_9",
    "expr_r_p_o_s_form_9",
    "calc_u_2_s_1_form_f",
    "expr_u_2_s_1_form_f",
    "calc_a_x_1_x_2_form_f",
    "expr_a_x_1_x_2_form_f",
    "calc_v_r_form_f",
    "expr_v_r_form_f",
    "calc_val_1205_4750_1205_4",
    "expr_val_1205_4750_1205_4",
    "calc_w_a_r_q_1312_7",
    "expr_w_a_r_q_1312_7",
    "calc_w_p_c_t_p_r_s_r_a_1312_7",
    "expr_w_p_c_t_p_r_s_r_a_1312_7",
    "calc_sim_omega_l_l_r_form_3",
    "expr_sim_omega_l_l_r_form_3",
    "calc_p_form_5",
    "expr_p_form_5",
    "calc_sigma_a_c_form_5",
    "expr_sigma_a_c_form_5",
    "calc_j_l_v_form_5",
    "expr_j_l_v_form_5",
    "calc_y_form_6",
    "expr_y_form_6",
    "calc_partial_v_tau_form_6",
    "expr_partial_v_tau_form_6",
    "calc_r_form_9",
    "expr_r_form_9",
    "calc_lambda_a_e_form_a",
    "expr_lambda_a_e_form_a",
    "calc_psi_v_form_a",
    "expr_psi_v_form_a",
    "calc_e_psi_form_d",
    "expr_e_psi_form_d",
    "calc_eq_a_p_b_p_form_e",
    "expr_eq_a_p_b_p_form_e",
    "calc_theta_form_e",
    "expr_theta_form_e",
    "calc_dd_t_m_r_2_theta_form_e",
    "expr_dd_t_m_r_2_theta_form_e",
    "calc_delta_glickm",
    "expr_delta_glickm",
    "calc_val_1406_3402_1406_3",
    "expr_val_1406_3402_1406_3",
    "calc_f_s_form_0",
    "expr_f_s_form_0",
    "calc_t_a_b_form_0",
    "expr_t_a_b_form_0",
    "calc_t_x_x_form_2",
    "expr_t_x_x_form_2",
    "calc_p_g_i_form_3",
    "expr_p_g_i_form_3",
    "calc_r_l_i_i_form_3",
    "expr_r_l_i_i_form_3",
    "calc_p_t_form_4",
    "expr_p_t_form_4",
    "calc_val_2603_08746_form_4",
    "expr_val_2603_08746_form_4",
    "calc_p_0_x_form_5",
    "expr_p_0_x_form_5",
    "calc_t_a_b_form_6",
    "expr_t_a_b_form_6",
    "calc_p_w_t_form_9",
    "expr_p_w_t_form_9",
    "calc_xi_e_form_a",
    "expr_xi_e_form_a",
    "calc_c_t_form_b",
    "expr_c_t_form_b",
    "calc_omega_l_l_r_sim_j_l_c_form_e",
    "expr_omega_l_l_r_sim_j_l_c_form_e",
    "calc_f_r_e_q_p_i_t_c_h_form_1",
    "expr_f_r_e_q_p_i_t_c_h_form_1",
    "calc_o_n_e_t_h_i_r_df_o_m_r_form_1",
    "expr_o_n_e_t_h_i_r_df_o_m_r_form_1",
    "calc_r_form_5",
    "expr_r_form_5",
    "calc_f_x_form_6",
    "expr_f_x_form_6",
    "calc_k_form_6",
    "expr_k_form_6",
    "calc_e_pi_l_e_v_i_t_t_form_6",
    "expr_e_pi_l_e_v_i_t_t_form_6",
    "calc_d_k_p_l_p_form_8",
    "expr_d_k_p_l_p_form_8",
    "calc_k_p_form_8",
    "expr_k_p_form_8",
    "calc_g_x_form_9",
    "expr_g_x_form_9",
    "calc_phi_form_a",
    "expr_phi_form_a",
    "calc_omega_l_l_r_form_a",
    "expr_omega_l_l_r_form_a",
    "calc_t_a_b_form_b",
    "expr_t_a_b_form_b",
    "calc_k_p_form_c",
    "expr_k_p_form_c",
    "calc_t_a_b_form_d",
    "expr_t_a_b_form_d",
    "calc_f_form_e",
    "expr_f_form_e",
    "calc_y_i_x_form_e",
    "expr_y_i_x_form_e",
    "calc_sim_j_l_c_form_f",
    "expr_sim_j_l_c_form_f",
    "calc_delta_i_1312_7",
    "expr_delta_i_1312_7",
    "calc_r_a_a_b_r_i_j_1312_7",
    "expr_r_a_a_b_r_i_j_1312_7",
    "calc_i_mu_1312_7",
    "expr_i_mu_1312_7",
    "calc_j_sigma_1603_0",
    "expr_j_sigma_1603_0",
    "calc_r_t_o_t_x_y_v_46e930",
    "expr_r_t_o_t_x_y_v_46e930",
    "calc_p_j_l_m_beyond",
    "expr_p_j_l_m_beyond",
    "calc_c_theta_beyond",
    "expr_c_theta_beyond",
    "calc_v_di_r_form_1",
    "expr_v_di_r_form_1",
    "calc_c_l_form_3",
    "expr_c_l_form_3",
    "calc_delta_a_d_a_d_s_form_3",
    "expr_delta_a_d_a_d_s_form_3",
    "calc_delta_a_l_a_l_s_form_3",
    "expr_delta_a_l_a_l_s_form_3",
    "calc_q_i_j_form_9",
    "expr_q_i_j_form_9",
    "calc_c_l_form_b",
    "expr_c_l_form_b",
    "calc_delta_s_form_c",
    "expr_delta_s_form_c",
    "calc_p_o_i_form_c",
    "expr_p_o_i_form_c",
    "calc_z_form_c",
    "expr_z_form_c",
    "calc_c_p_q_form_c",
    "expr_c_p_q_form_c",
    "calc_y_form_c",
    "expr_y_form_c",
    "calc_x_l_o_form_d",
    "expr_x_l_o_form_d",
    "calc_delta_a_l_a_l_s_form_d",
    "expr_delta_a_l_a_l_s_form_d",
    "calc_delta_o_w_n_s_form_d",
    "expr_delta_o_w_n_s_form_d",
    "calc_t_w_o_t_h_i_r_df_o_m_r_form_e",
    "expr_t_w_o_t_h_i_r_df_o_m_r_form_e",
    "calc_p_r_i_w_i_n_s_o_v_e_j_r_form_f",
    "expr_p_r_i_w_i_n_s_o_v_e_j_r_form_f",
    "calc_val_1003_0134_formul",
    "expr_val_1003_0134_formul",
    "calc_l_o_g_i_t_p_i_l_1312_7",
    "expr_l_o_g_i_t_p_i_l_1312_7",
    "calc_s_i_l_1312_7",
    "expr_s_i_l_1312_7",
    "calc_delta_f_i_s_i_l_1312_7",
    "expr_delta_f_i_s_i_l_1312_7",
    "calc_delta_i_p_1312_7",
    "expr_delta_i_p_1312_7",
    "calc_p_x_1603_0",
    "expr_p_x_1603_0",
    "calc_k_x_1603_0",
    "expr_k_x_1603_0",
    "calc_partial_l_partial_sigma_1712_0",
    "expr_partial_l_partial_sigma_1712_0",
    "calc_e_r_r_o_r_b_a_y_e_s_1712_0",
    "expr_e_r_r_o_r_b_a_y_e_s_1712_0",
    "calc_m_i_n_l_i_m_1811_0",
    "expr_m_i_n_l_i_m_1811_0",
    "calc_x_d_i_2004_0",
    "expr_x_d_i_2004_0",
    "calc_f_h_y_2005_0",
    "expr_f_h_y_2005_0",
    "calc_l_o_g_i_t_i_j_p_g_2103_1",
    "expr_l_o_g_i_t_i_j_p_g_2103_1",
    "calc_x_gamma_sigma_formul",
    "expr_x_gamma_sigma_formul",
    "calc_alpha_m_e_l_formul",
    "expr_alpha_m_e_l_formul",
    "calc_r_t_o_t_x_y_v_formul",
    "expr_r_t_o_t_x_y_v_formul",
    "calc_a_c_c_b_m_guo_20",
    "expr_a_c_c_b_m_guo_20",
    "calc_p_i_k_2103_1",
    "expr_p_i_k_2103_1",
    "calc_sim_f_y_t_2207_1",
    "expr_sim_f_y_t_2207_1",
    "calc_sim_f_y_i_y_i_i_n_2207_1",
    "expr_sim_f_y_i_y_i_i_n_2207_1",
    "calc_delta_e_r_2208_0",
    "expr_delta_e_r_2208_0",
    "calc_x_p_2209_0",
    "expr_x_p_2209_0",
    "calc_q_2210_0",
    "expr_q_2210_0",
    "calc_u_2210_0",
    "expr_u_2210_0",
    "calc_x_w_o_b_a_t_x_2210_0",
    "expr_x_w_o_b_a_t_x_2210_0",
    "calc_theta_b_j_2210_0",
    "expr_theta_b_j_2210_0",
    "calc_f_x_y_2310_0",
    "expr_f_x_y_2310_0",
    "calc_theta_2402_0",
    "expr_theta_2402_0",
    "calc_a_k_2511_1",
    "expr_a_k_2511_1",
    "calc_mu_p_a_x_2602_2",
    "expr_mu_p_a_x_2602_2",
    "calc_psi_p_2602_2",
    "expr_psi_p_2602_2",
    "calc_psi_r_a_da_n_2602_2",
    "expr_psi_r_a_da_n_2602_2",
    "calc_psi_r_a_da_n_psi_r_a_da_n_2602_2",
    "expr_psi_r_a_da_n_psi_r_a_da_n_2602_2",
    "calc_eq_y_d_p_1_n_p_dsum_i_p_i_2603_2",
    "expr_eq_y_d_p_1_n_p_dsum_i_p_i_2603_2",
    "calc_y_d_p_2603_2",
    "expr_y_d_p_2603_2",
    "calc_h_x_beyond",
    "expr_h_x_beyond",
    "calc_theta_i_j_beyond",
    "expr_theta_i_j_beyond",
    "calc_theta_m_l_j_beyond",
    "expr_theta_m_l_j_beyond",
    "calc_c_theta_theta_c_1_beyond",
    "expr_c_theta_theta_c_1_beyond",
    "calc_beta_m_l_j_beyond",
    "expr_beta_m_l_j_beyond",
    "calc_beyond_runs_expectancy_jsm2014_beyond",
    "expr_beyond_runs_expectancy_jsm2014_beyond",
    "calc_delta_0_x_1_i_brown_",
    "expr_delta_0_x_1_i_brown_",
    "calc_z_i_brown_",
    "expr_z_i_brown_",
    "calc_p_s_i_bt_sec",
    "expr_p_s_i_bt_sec",
    "calc_p_i_j_p_i_j_bt_sec",
    "expr_p_i_j_p_i_j_bt_sec",
    "calc_f_i_x_bt_sec",
    "expr_f_i_x_bt_sec",
    "calc_mu_i_j_bt_sec",
    "expr_mu_i_j_bt_sec",
    "calc_alpha_p_r_bt_sec",
    "expr_alpha_p_r_bt_sec",
    "calc_i_p_form_9",
    "expr_i_p_form_9",
    "calc_pi_form_c",
    "expr_pi_form_c",
    "calc_k_alpha_k_w_bt_sec",
    "expr_k_alpha_k_w_bt_sec",
    "calc_alpha_k_w_bt_sec",
    "expr_alpha_k_w_bt_sec",
    "calc_pi_bt_sec",
    "expr_pi_bt_sec",
    "calc_r_i_p_bt_sec",
    "expr_r_i_p_bt_sec",
    "calc_alpha_1_bt_sec",
    "expr_alpha_1_bt_sec",
    "calc_theta_bt_sec",
    "expr_theta_bt_sec",
    "calc_v_buchda",
    "expr_v_buchda",
    "calc_m_i_buchda",
    "expr_m_i_buchda",
    "calc_h_m_buchda",
    "expr_h_m_buchda",
    "calc_d_m_buchda",
    "expr_d_m_buchda",
    "calc_a_m_buchda",
    "expr_a_m_buchda",
    "calc_x_buchda",
    "expr_x_buchda",
    "calc_y_buchda",
    "expr_y_buchda",
    "calc_p_buchda",
    "expr_p_buchda",
    "calc_glickman_1999_applstat_parameter_estimation_form_9",
    "expr_glickman_1999_applstat_parameter_estimation_form_9",
    "calc_q_buchda",
    "expr_q_buchda",
    "calc_false_buchda",
    "expr_false_buchda",
    "calc_i_pi_egidi_",
    "expr_i_pi_egidi_",
    "calc_d_r_glickm",
    "expr_d_r_glickm",
    "calc_math_0509698_form_9",
    "expr_math_0509698_form_9",
    "calc_e_glickm",
    "expr_e_glickm",
    "calc_s_n_theta_gneiti",
    "expr_s_n_theta_gneiti",
    "calc_s_n_gneiti",
    "expr_s_n_gneiti",
    "calc_s_p_i_gneiti",
    "expr_s_p_i_gneiti",
    "calc_s_p_1_gneiti",
    "expr_s_p_1_gneiti",
    "calc_c_r_p_s_n_mu_sigma_2_x_gneiti",
    "expr_c_r_p_s_n_mu_sigma_2_x_gneiti",
    "calc_e_s_p_x_gneiti",
    "expr_e_s_p_x_gneiti",
    "calc_math_0509698_form_3",
    "expr_math_0509698_form_3",
    "calc_miller_2007_pythag_weibull_form_5",
    "expr_miller_2007_pythag_weibull_form_5",
    "calc_miller_2007_pythag_weibull_form_c",
    "expr_miller_2007_pythag_weibull_form_c",
    "calc_miller_2005_pythag_derivation_form_c",
    "expr_miller_2005_pythag_derivation_form_c",
    "calc_p_m_c_c_gneiti",
    "expr_p_m_c_c_gneiti",
    "calc_x_t_1_gneiti",
    "expr_x_t_1_gneiti",
    "calc_e_p_pi_form_0",
    "expr_e_p_pi_form_0",
    "calc_p_n_e_n_w_form_0",
    "expr_p_n_e_n_w_form_0",
    "calc_delta_p_c_e_l_l_form_1",
    "expr_delta_p_c_e_l_l_form_1",
    "calc_r_p_s_form_1",
    "expr_r_p_s_form_1",
    "calc_p_form_1",
    "expr_p_form_1",
    "calc_h_p_form_1",
    "expr_h_p_form_1",
    "calc_m_f_form_2",
    "expr_m_f_form_2",
    "calc_l_k_form_2",
    "expr_l_k_form_2",
    "calc_m_z_1_form_2",
    "expr_m_z_1_form_2",
    "calc_b_s_form_2",
    "expr_b_s_form_2",
    "calc_f_x_form_2",
    "expr_f_x_form_2",
    "calc_i_p_form_3",
    "expr_i_p_form_3",
    "calc_h_form_3",
    "expr_h_form_3",
    "calc_e_c_e_form_5",
    "expr_e_c_e_form_5",
    "calc_l_dr_y_o_t_u_form_5",
    "expr_l_dr_y_o_t_u_form_5",
    "calc_t_pi_form_5",
    "expr_t_pi_form_5",
    "calc_i_p_form_6",
    "expr_i_p_form_6",
    "calc_dt_dv_form_6",
    "expr_dt_dv_form_6",
    "calc_l_c_e_form_6",
    "expr_l_c_e_form_6",
    "calc_q_h_e_a_t_form_6",
    "expr_q_h_e_a_t_form_6",
    "calc_nabla_a_f_dagger_form_7",
    "expr_nabla_a_f_dagger_form_7",
    "calc_m_q_form_9",
    "expr_m_q_form_9",
    "calc_equiv_tan_gamma_u_q_u_form_9",
    "expr_equiv_tan_gamma_u_q_u_form_9",
    "calc_f_t_y_0_sigma_y_y_0_form_c",
    "expr_f_t_y_0_sigma_y_y_0_form_c",
    "calc_a_phi_z_form_e",
    "expr_a_phi_z_form_e",
    "calc_nabla_p_f_dagger_form_7",
    "expr_nabla_p_f_dagger_form_7",
    "calc_q_c_f_h_form_e",
    "expr_q_c_f_h_form_e",
    "calc_i_z_form_e",
    "expr_i_z_form_e",
    "calc_m_form_f",
    "expr_m_form_f",
    "calc_u_form_f",
    "expr_u_form_f",
    "calc_f_dagger_n_form_0",
    "expr_f_dagger_n_form_0",
    "calc_n_omega_form_0",
    "expr_n_omega_form_0",
    "calc_m_z_form_0",
    "expr_m_z_form_0",
    "calc_r_b_p_a_form_1",
    "expr_r_b_p_a_form_1",
    "calc_l_t_e_o_form_3",
    "expr_l_t_e_o_form_3",
    "calc_sim_a_sigma_form_4",
    "expr_sim_a_sigma_form_4",
    "calc_dmu_k_form_4",
    "expr_dmu_k_form_4",
    "calc_k_form_4",
    "expr_k_form_4",
    "calc_e_f_sim_form_4",
    "expr_e_f_sim_form_4",
    "calc_delta_n_p_form_4",
    "expr_delta_n_p_form_4",
    "calc_val_1_gamma_form_5",
    "expr_val_1_gamma_form_5",
    "calc_gamma_dagger_n_form_5",
    "expr_gamma_dagger_n_form_5",
    "calc_delta_m_form_6",
    "expr_delta_m_form_6",
    "calc_partial_t_u_3_sim_l_u_3_form_7",
    "expr_partial_t_u_3_sim_l_u_3_form_7",
    "calc_z_form_8",
    "expr_z_form_8",
    "calc_g_delta_form_8",
    "expr_g_delta_form_8",
    "calc_l_t_e_o_form_a",
    "expr_l_t_e_o_form_a",
    "calc_l_t_e_o_form_9",
    "expr_l_t_e_o_form_9",
    "calc_q_0_x_form_d",
    "expr_q_0_x_form_d",
    "calc_sim_a_lambda_form_d",
    "expr_sim_a_lambda_form_d",
    "calc_beta_p_a_r_k_p_form_e",
    "expr_beta_p_a_r_k_p_form_e",
    "calc_delta_t_form_0",
    "expr_delta_t_form_0",
    "calc_t_c_form_2",
    "expr_t_c_form_2",
    "calc_delta_m_s_e_e_form_3",
    "expr_delta_m_s_e_e_form_3",
    "calc_r_f_l_a_k_t_form_3",
    "expr_r_f_l_a_k_t_form_3",
    "calc_t_x_phi_form_4",
    "expr_t_x_phi_form_4",
    "calc_h_form_8",
    "expr_h_form_8",
    "calc_x_form_8",
    "expr_x_form_8",
    "calc_t_alpha_epsilon_rho_form_8",
    "expr_t_alpha_epsilon_rho_form_8",
    "calc_e_m_p_j_e_p_form_8",
    "expr_e_m_p_j_e_p_form_8",
    "calc_l_p_r_i_o_r_form_9",
    "expr_l_p_r_i_o_r_form_9",
    "calc_d_i_form_a",
    "expr_d_i_form_a",
    "calc_m_form_c",
    "expr_m_form_c",
    "calc_j_theta_form_d",
    "expr_j_theta_form_d",
    "calc_m_y_t_form_d",
    "expr_m_y_t_form_d",
    "calc_e_w_o_k_r_form_d",
    "expr_e_w_o_k_r_form_d",
    "calc_x_form_e",
    "expr_x_form_e",
    "calc_eta_k_t_form_e",
    "expr_eta_k_t_form_e",
    "calc_l_dagger_form_e",
    "expr_l_dagger_form_e",
    "calc_partial_z_c_k_alpha_partial_form_e",
    "expr_partial_z_c_k_alpha_partial_form_e",
    "calc_omega_t_a_alpha_form_f",
    "expr_omega_t_a_alpha_form_f",
    "calc_val_2609_24299_form_0",
    "expr_val_2609_24299_form_0",
    "calc_delta_0_form_0",
    "expr_delta_0_form_0",
    "calc_k_phi_c_form_1",
    "expr_k_phi_c_form_1",
    "calc_a_q_form_4",
    "expr_a_q_form_4",
    "calc_x_1_form_4",
    "expr_x_1_form_4",
    "calc_i_omega_omega_i_omega_form_8",
    "expr_i_omega_omega_i_omega_form_8",
    "calc_epsilon_n_form_9",
    "expr_epsilon_n_form_9",
    "calc_p_i_n_form_a",
    "expr_p_i_n_form_a",
    "calc_val_2609_24299_form_a",
    "expr_val_2609_24299_form_a",
    "calc_val_2609_24299_form_b",
    "expr_val_2609_24299_form_b",
    "calc_omega_form_e",
    "expr_omega_form_e",
    "calc_x_1_form_f",
    "expr_x_1_form_f",
    "calc_sim_b_lambda_form_f",
    "expr_sim_b_lambda_form_f",
    "calc_r_x_phi_form_f",
    "expr_r_x_phi_form_f",
    "calc_m_xi_form_f",
    "expr_m_xi_form_f",
]

def calc_sigma_g_form_1(q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1408_4306.

    **Source**:
    - Title: Effect of lift force on the aerodynamics of dust grains in the protoplanetary disk (2014)
    - Authors: Masaki S. Yamaguchi, Shigeo S. Kimura
    - Citation Key: `arxiv_1408_4306`

    **KaTeX Formula**:
    $$
    \Sigma g = \Sigma 0R-q 1
    $$

    Args:
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float(-q)


def expr_sigma_g_form_1(q: str = "q") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sigma_g_form_1`."""
    return (-pl.col(q))


def calc_c_t_form_f(k: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    c(t) = k1 + k2 \sin(2\pi t)
    $$

    Args:
        k (float): Input parameter `k`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*k*math.sin(2*math.pi*t) + k)


def expr_c_t_form_f(k: str = "k", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_t_form_f`."""
    return (2*pl.col(k)*math.sin(2*math.pi*pl.col(t)) + pl.col(k))


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
    return float(16*m**4*x**3*y**3)


def expr_a_form_4(m: str = "m", x: str = "x", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_form_4`."""
    return (16*pl.col(m)**4*pl.col(x)**3*pl.col(y)**3)


def calc_gamma_form_9(A: float, G: float, R: float, R_S: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_39088.

    **Source**:
    - Title: Comparing wins above replacement across baseball history (2026)
    - Authors: Michael Doane
    - Citation Key: `arxiv_2610_39088`

    **KaTeX Formula**:
    $$
    \gamma  =( R_{S}+R A G )0.285 , p PP = R_{S} \gamma  R_{S} \gamma  +R A \gamma  . (S15)
    $$

    Args:
        A (float): Input parameter `A`.
        G (float): Input parameter `G`.
        R (float): Input parameter `R`.
        R_S (float): Input parameter `R_S`.

    Returns:
        float: Calculated metric value.
    """
    return float(0.285*(R*(A*G) + R_S))


def expr_gamma_form_9(A: str = "A", G: str = "G", R: str = "R", R_S: str = "R_S") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_gamma_form_9`."""
    return (0.285*(pl.col(R)*(pl.col(A)*pl.col(G)) + pl.col(R_S)))


def calc_r_m_e_s_form_d(b: float, dr: float, m: float, n: float, o: float, p: float, r: float, t: float) -> float:
    r"""Compute mathematical metric extracted from openalex_lee2025_w4409781220.

    **Source**:
    - Title: Pitcher Performance Prediction Major League Baseball (MLB) by Temporal Fusion Transformer (2025)
    - Authors: Won Suk Lee, Jang Hyun Kim
    - Citation Key: `openalex_lee2025_w4409781220`

    **KaTeX Formula**:
    $$
    RMSE = roottoprootmodrootmodrootbot 1 n n\sum  i = 1(yi -  y i )2
    $$

    Args:
        b (float): Input parameter `b`.
        dr (float): Input parameter `dr`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(r*(o*(o*(t*(t*(o*(p*(r*(o*(o*(t*(m*(o*(dr*(o*(o*(t*(m*(o*(dr*(o*(o*(t*(b*(o*(t*(1*(n*n))))))))))))))))))))))))))))


def expr_r_m_e_s_form_d(b: str = "b", dr: str = "dr", m: str = "m", n: str = "n", o: str = "o", p: str = "p", r: str = "r", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_m_e_s_form_d`."""
    return (pl.col(r)*(pl.col(o)*(pl.col(o)*(pl.col(t)*(pl.col(t)*(pl.col(o)*(pl.col(p)*(pl.col(r)*(pl.col(o)*(pl.col(o)*(pl.col(t)*(pl.col(m)*(pl.col(o)*(pl.col(dr)*(pl.col(o)*(pl.col(o)*(pl.col(t)*(pl.col(m)*(pl.col(o)*(pl.col(dr)*(pl.col(o)*(pl.col(o)*(pl.col(t)*(pl.col(b)*(pl.col(o)*(pl.col(t)*(1*(pl.col(n)*pl.col(n)))))))))))))))))))))))))))))


def calc_m_a_e_form_3(n: float) -> float:
    r"""Compute mathematical metric extracted from openalex_lee2025_w4409781220.

    **Source**:
    - Title: Pitcher Performance Prediction Major League Baseball (MLB) by Temporal Fusion Transformer (2025)
    - Authors: Won Suk Lee, Jang Hyun Kim
    - Citation Key: `openalex_lee2025_w4409781220`

    **KaTeX Formula**:
    $$
    MAE = 1 n n\sum  i = 1 |yi -  yi |
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(n**2)


def expr_m_a_e_form_3(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_a_e_form_3`."""
    return (pl.col(n)**2)


def calc_m_a_e_p_form_d(n: float) -> float:
    r"""Compute mathematical metric extracted from openalex_lee2025_w4409781220.

    **Source**:
    - Title: Pitcher Performance Prediction Major League Baseball (MLB) by Temporal Fusion Transformer (2025)
    - Authors: Won Suk Lee, Jang Hyun Kim
    - Citation Key: `openalex_lee2025_w4409781220`

    **KaTeX Formula**:
    $$
    MAPE = 100 n n\sum  i = 1 | yi -  yi yi |
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(100*n**2)


def expr_m_a_e_p_form_d(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_a_e_p_form_d`."""
    return (100*pl.col(n)**2)


def calc_delta_e_r_form_0(E_e_d_n: float, E_s_t_a_r_t: float, R: float, R_p_l_a_y: float) -> float:
    r"""Compute mathematical metric extracted from tangotiger_re24_glossary.

    **Source**:
    - Title: Tom Tango: 24-State Run Expectancy Matrix (RE24) and Transition Values (2026)
    - Authors: Tom Tango, Mitchel Lichtman, Andrew Dolphin
    - Citation Key: `tangotiger_re24_glossary`

    **KaTeX Formula**:
    $$
    \Delta RE = RE_{end} - RE_{start} + R_{play}
    $$

    Args:
        E_e_d_n (float): Input parameter `E_e_d_n`.
        E_s_t_a_r_t (float): Input parameter `E_s_t_a_r_t`.
        R (float): Input parameter `R`.
        R_p_l_a_y (float): Input parameter `R_p_l_a_y`.

    Returns:
        float: Calculated metric value.
    """
    return float(R_p*(l*(a*y)) + (E_e*(d*n)*R - E_s*(t*(a*(r*t)))*R))


def expr_delta_e_r_form_0(E_e_d_n: str = "E_e_d_n", E_s_t_a_r_t: str = "E_s_t_a_r_t", R: str = "R", R_p_l_a_y: str = "R_p_l_a_y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_e_r_form_0`."""
    return (R_p*(l*(a*y)) + (E_e*(d*n)*pl.col(R) - E_s*(t*(a*(r*t)))*pl.col(R)))


def calc_s_i_form_a(M: float, epsilon: float, i: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_39452.

    **Source**:
    - Title: Challenge or Pass? A Dynamic Policy for MLB's Automated Ball-Strike System (2026)
    - Authors: Jonathan Pipping-Gamón, Zach Sissman, Lila Dodson et al.
    - Citation Key: `arxiv_2610_39452`

    **KaTeX Formula**:
    $$
    Si = Mi + \epsilon s,i, \epsilon s,i | Mi, r, c \sim  N(0, \sigma 2 s,r )
    $$

    Args:
        M (float): Input parameter `M`.
        epsilon (float): Input parameter `epsilon`.
        i (float): Input parameter `i`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(M*i + epsilon*s)


def expr_s_i_form_a(M: str = "M", epsilon: str = "epsilon", i: str = "i", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_i_form_a`."""
    return (pl.col(M)*pl.col(i) + pl.col(epsilon)*pl.col(s))


def calc_l_a_c_c_form_b(N: float, a: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10498.

    **Source**:
    - Title: Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts (2026)
    - Authors: Simon Khan, Laurent Gajny, Jennyfer Lecompte et al.
    - Citation Key: `arxiv_2609_10498`

    **KaTeX Formula**:
    $$
    Lacc = 1 3Na \sum  i,t mai,t \sum  a\in {x,y,z} \rho \beta  (̂ai,t,a - agt i,t,a )
    $$

    Args:
        N (float): Input parameter `N`.
        a (float): Input parameter `a`.

    Returns:
        float: Calculated metric value.
    """
    return float(13*(N*a))


def expr_l_a_c_c_form_b(N: str = "N", a: str = "a") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_a_c_c_form_b`."""
    return (13*(pl.col(N)*pl.col(a)))


def calc_p_z_form_7(P: float, a: float, e: float, l: float, o: float, omega: float, p: float, s: float, t: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_39452.

    **Source**:
    - Title: Challenge or Pass? A Dynamic Policy for MLB's Automated Ball-Strike System (2026)
    - Authors: Jonathan Pipping-Gamón, Zach Sissman, Lila Dodson et al.
    - Citation Key: `arxiv_2610_39452`

    **KaTeX Formula**:
    $$
    Pz = \omega z  P state z + (1 -\omega z)  P pool z , \omega z = nz nz + \lambda F
    $$

    Args:
        P (float): Input parameter `P`.
        a (float): Input parameter `a`.
        e (float): Input parameter `e`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.
        omega (float): Input parameter `omega`.
        p (float): Input parameter `p`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(P*a*e*omega*s*t**2*z**2 + P*l*o**2*p*z*(-omega*z + 1))


def expr_p_z_form_7(P: str = "P", a: str = "a", e: str = "e", l: str = "l", o: str = "o", omega: str = "omega", p: str = "p", s: str = "s", t: str = "t", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_z_form_7`."""
    return (pl.col(P)*pl.col(a)*pl.col(e)*pl.col(omega)*pl.col(s)*pl.col(t)**2*pl.col(z)**2 + pl.col(P)*pl.col(l)*pl.col(o)**2*pl.col(p)*pl.col(z)*(-pl.col(omega)*pl.col(z) + 1))


def calc_i_y_form_9(G: float, T: float, W: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_39088.

    **Source**:
    - Title: Comparing wins above replacement across baseball history (2026)
    - Authors: Michael Doane
    - Citation Key: `arxiv_2610_39088`

    **KaTeX Formula**:
    $$
    y i = W i +0 . 5T i G i
    $$

    Args:
        G (float): Input parameter `G`.
        T (float): Input parameter `T`.
        W (float): Input parameter `W`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(0.5*G*T*i**2 + W*i)


def expr_i_y_form_9(G: str = "G", T: str = "T", W: str = "W", i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_y_form_9`."""
    return (0.5*pl.col(G)*pl.col(T)*pl.col(i)**2 + pl.col(W)*pl.col(i))


def calc_y_form_3(G: float, T: float, W: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_39088.

    **Source**:
    - Title: Comparing wins above replacement across baseball history (2026)
    - Authors: Michael Doane
    - Citation Key: `arxiv_2610_39088`

    **KaTeX Formula**:
    $$
    y= W+T / 2 G . (S13)
    $$

    Args:
        G (float): Input parameter `G`.
        T (float): Input parameter `T`.
        W (float): Input parameter `W`.

    Returns:
        float: Calculated metric value.
    """
    return float(W + (1/2)*T/G)


def expr_y_form_3(G: str = "G", T: str = "T", W: str = "W") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_y_form_3`."""
    return (pl.col(W) + (1/2)*pl.col(T)/pl.col(G))


def calc_p_2_form_4(A: float, R: float, R_S: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_39088.

    **Source**:
    - Title: Comparing wins above replacement across baseball history (2026)
    - Authors: Michael Doane
    - Citation Key: `arxiv_2610_39088`

    **KaTeX Formula**:
    $$
    p 2 = R_{S} 2 R_{S} 2 +R A 2 . (S14)
    $$

    Args:
        A (float): Input parameter `A`.
        R (float): Input parameter `R`.
        R_S (float): Input parameter `R_S`.

    Returns:
        float: Calculated metric value.
    """
    return float(A*R + R_S*(2*(2*R_S)))


def expr_p_2_form_4(A: str = "A", R: str = "R", R_S: str = "R_S") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_2_form_4`."""
    return (pl.col(A)*pl.col(R) + pl.col(R_S)*(2*(2*pl.col(R_S))))


def calc_y_form_4(alpha: float, beta: float, epsilon: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_39088.

    **Source**:
    - Title: Comparing wins above replacement across baseball history (2026)
    - Authors: Michael Doane
    - Citation Key: `arxiv_2610_39088`

    **KaTeX Formula**:
    $$
    y=\alpha +\beta  x+\epsilon  . (S16)
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        beta (float): Input parameter `beta`.
        epsilon (float): Input parameter `epsilon`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(epsilon + (alpha + beta*x))


def expr_y_form_4(alpha: str = "alpha", beta: str = "beta", epsilon: str = "epsilon", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_y_form_4`."""
    return (pl.col(epsilon) + (pl.col(alpha) + pl.col(beta)*pl.col(x)))


def calc_a_s_t_form_0(n: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    As(t) = (ns 2 )-1 \sum  a<b Ns,ab \sum  l=1 ht(Us,abl),  Bs = (ns 2 )-1 \sum  a<b Ns,ab
    $$

    Args:
        n (float): Input parameter `n`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*n*s - 1)


def expr_a_s_t_form_0(n: str = "n", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_s_t_form_0`."""
    return (2*pl.col(n)*pl.col(s) - 1)


def calc_f_2_form_9(T: float, p: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_37732.

    **Source**:
    - Title: The Camera Inside the Editor: Reading the Implicit Camera of Image Editors with Painted Calibration Patterns (2026)
    - Authors: Sebastian Rückerl
    - Citation Key: `arxiv_2609_37732`

    **KaTeX Formula**:
    $$
    f 2 = -(v1 - p)^T(v2 - p), \theta  = \arctan yh - py f
    $$

    Args:
        T (float): Input parameter `T`.
        p (float): Input parameter `p`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(-(-p + v)**T*(-p + 2*v))


def expr_f_2_form_9(T: str = "T", p: str = "p", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_2_form_9`."""
    return (-(-pl.col(p) + pl.col(v))**pl.col(T)*(-pl.col(p) + 2*pl.col(v)))


def calc_beta_l_a_s_o_s_form_d(a: float, beta: float, g: float, i: float, m: float, n: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_0911_4503.

    **Source**:
    - Title: A Bayesian Variable Selection Approach to Major League Baseball Hitting Metrics (2009)
    - Authors: Blakeley B. McShane, Alexander Braunstein, James Piette et al.
    - Citation Key: `arxiv_0911_4503`

    **KaTeX Formula**:
    $$
    \beta Lasso = argmin  \beta  [\sum  i,j (yij -Xi  \beta )2 + \lambda  \sum  i |  \beta i|] , \lambda  \ge  0
    $$

    Args:
        a (float): Input parameter `a`.
        beta (float): Input parameter `beta`.
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*(r*(g*(m*(i*(beta*n))))))


def expr_beta_l_a_s_o_s_form_d(a: str = "a", beta: str = "beta", g: str = "g", i: str = "i", m: str = "m", n: str = "n", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_beta_l_a_s_o_s_form_d`."""
    return (pl.col(a)*(pl.col(r)*(pl.col(g)*(pl.col(m)*(pl.col(i)*(pl.col(beta)*pl.col(n)))))))


def calc_sigma_u_form_e(z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_02081.

    **Source**:
    - Title: Isotonic Bradley-Terry Model for Paired Comparison Data (2026)
    - Authors: Ryoya Yamasaki
    - Citation Key: `arxiv_2608_02081`

    **KaTeX Formula**:
    $$
    \sigma (u) =    z1
    $$

    Args:
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(z)


def expr_sigma_u_form_e(z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sigma_u_form_e`."""
    return (pl.col(z))


def calc_l_form_f(A: float, C: float, L: float, b: float, omega: float, rho: float, v: float) -> float:
    r"""Compute mathematical metric extracted from openalex_meyer2008_w1992303757.

    **Source**:
    - Title: Influence of a humidor on the aerodynamics of baseballs (2008)
    - Authors: Edmund Meyer, John L. Bohn
    - Citation Key: `openalex_meyer2008_w1992303757`

    **KaTeX Formula**:
    $$
    L = - 12 \rho CLAv2 v\times  \omega b
    $$

    Args:
        A (float): Input parameter `A`.
        C (float): Input parameter `C`.
        L (float): Input parameter `L`.
        b (float): Input parameter `b`.
        omega (float): Input parameter `omega`.
        rho (float): Input parameter `rho`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(-24*A*C*L*b*omega*rho*v**2)


def expr_l_form_f(A: str = "A", C: str = "C", L: str = "L", b: str = "b", omega: str = "omega", rho: str = "rho", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_form_f`."""
    return (-24*pl.col(A)*pl.col(C)*pl.col(L)*pl.col(b)*pl.col(omega)*pl.col(rho)*pl.col(v)**2)


def calc_b_form_4(B_B: float, H: float, H_R: float, T_B: float) -> float:
    r"""Compute mathematical metric extracted from tango_base_runs_glossary.

    **Source**:
    - Title: Base Runs (BsR) Offensive Estimator (2026)
    - Authors: David Smyth, Tom Tango
    - Citation Key: `tango_base_runs_glossary`

    **KaTeX Formula**:
    $$
    B = 1.4 \cdot T_{B} - 0.6 \cdot H - 3 \cdot H_{R} + 0.1 \cdot B_{B}
    $$

    Args:
        B_B (float): Input parameter `B_B`.
        H (float): Input parameter `H`.
        H_R (float): Input parameter `H_R`.
        T_B (float): Input parameter `T_B`.

    Returns:
        float: Calculated metric value.
    """
    return float(0.1*B_B + (-3*H_R + (-0.6*H + 1.4*T_B)))


def expr_b_form_4(B_B: str = "B_B", H: str = "H", H_R: str = "H_R", T_B: str = "T_B") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_b_form_4`."""
    return (0.1*pl.col(B_B) + (-3*pl.col(H_R) + (-0.6*pl.col(H) + 1.4*pl.col(T_B))))


def calc_a_p_form_6(A_B: float, B: float, B_B: float, F: float, H: float, P: float, S: float) -> float:
    r"""Compute mathematical metric extracted from fangraphs_woba_glossary.

    **Source**:
    - Title: FanGraphs Sabermetric Library: Weighted On-Base Average (wOBA) (2026)
    - Authors: FanGraphs
    - Citation Key: `fangraphs_woba_glossary`

    **KaTeX Formula**:
    $$
    PA = A_{B} + B_{B} + SF + HBP
    $$

    Args:
        A_B (float): Input parameter `A_B`.
        B (float): Input parameter `B`.
        B_B (float): Input parameter `B_B`.
        F (float): Input parameter `F`.
        H (float): Input parameter `H`.
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.

    Returns:
        float: Calculated metric value.
    """
    return float(H*(B*P) + (F*S + (A_B + B_B)))


def expr_a_p_form_6(A_B: str = "A_B", B: str = "B", B_B: str = "B_B", F: str = "F", H: str = "H", P: str = "P", S: str = "S") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_p_form_6`."""
    return (pl.col(H)*(pl.col(B)*pl.col(P)) + (pl.col(F)*pl.col(S) + (pl.col(A_B) + pl.col(B_B))))


def calc_eta_i_form_f(T: float, a: float, beta: float, c: float, dd: float, gamma: float, i: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_25525.

    **Source**:
    - Title: When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review (2026)
    - Authors: Kichang Lee, Gyeongmin Han, Sungmin Lee et al.
    - Citation Key: `arxiv_2609_25525`

    **KaTeX Formula**:
    $$
    \eta i = aci + \beta ddi + x ^T i \gamma  + \sum  m,v,s Am,v,s i  \tau m,v,s +\delta m,v,sdi
    $$

    Args:
        T (float): Input parameter `T`.
        a (float): Input parameter `a`.
        beta (float): Input parameter `beta`.
        c (float): Input parameter `c`.
        dd (float): Input parameter `dd`.
        gamma (float): Input parameter `gamma`.
        i (float): Input parameter `i`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(x**T*(gamma*i) + (a*(c*i) + beta*(dd*i)))


def expr_eta_i_form_f(T: str = "T", a: str = "a", beta: str = "beta", c: str = "c", dd: str = "dd", gamma: str = "gamma", i: str = "i", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_eta_i_form_f`."""
    return (pl.col(x)**pl.col(T)*(pl.col(gamma)*pl.col(i)) + (pl.col(a)*(pl.col(c)*pl.col(i)) + pl.col(beta)*(pl.col(dd)*pl.col(i))))


def calc_delta_rho_1312_7(S: float, a: float, dS: float, e: float, n: float, r: float, rho: float, s: float, t: float) -> float:
    r"""Compute mathematical metric extracted from 1312_7158.

    **Source**:
    - Title: openWAR: An Open Source System for Evaluating Overall Player Performance in Major League Baseball (2013)
    - Authors: Benjamin S. Baumer, Shane T. Jensen, Gregory J. Matthews
    - Citation Key: `1312_7158`

    **KaTeX Formula**:
    $$
    \Delta \rho  = \rho endState - \rho startState
    $$

    Args:
        S (float): Input parameter `S`.
        a (float): Input parameter `a`.
        dS (float): Input parameter `dS`.
        e (float): Input parameter `e`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.
        rho (float): Input parameter `rho`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(rho*(e*(n*(dS*(t*(a*(e*t)))))) - rho*s*(t*(a*(r*(t*(S*(t*(a*(e*t)))))))))


def expr_delta_rho_1312_7(S: str = "S", a: str = "a", dS: str = "dS", e: str = "e", n: str = "n", r: str = "r", rho: str = "rho", s: str = "s", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_rho_1312_7`."""
    return (pl.col(rho)*(pl.col(e)*(pl.col(n)*(pl.col(dS)*(pl.col(t)*(pl.col(a)*(pl.col(e)*pl.col(t))))))) - pl.col(rho)*pl.col(s)*(pl.col(t)*(pl.col(a)*(pl.col(r)*(pl.col(t)*(pl.col(S)*(pl.col(t)*(pl.col(a)*(pl.col(e)*pl.col(t))))))))))


def calc_b_r_s_form_6(A: float, B: float, C: float, D: float) -> float:
    r"""Compute mathematical metric extracted from tango_base_runs_glossary.

    **Source**:
    - Title: Base Runs (BsR) Offensive Estimator (2026)
    - Authors: David Smyth, Tom Tango
    - Citation Key: `tango_base_runs_glossary`

    **KaTeX Formula**:
    $$
    BsR = A \cdot \frac{B}{B + C} + D
    $$

    Args:
        A (float): Input parameter `A`.
        B (float): Input parameter `B`.
        C (float): Input parameter `C`.
        D (float): Input parameter `D`.

    Returns:
        float: Calculated metric value.
    """
    return float(A*B/(B + C) + D)


def expr_b_r_s_form_6(A: str = "A", B: str = "B", C: str = "C", D: str = "D") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_b_r_s_form_6`."""
    return (pl.col(A)*pl.col(B)/(pl.col(B) + pl.col(C)) + pl.col(D))


def calc_t_log_e_t_e_form_f(t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2604_21851.

    **Source**:
    - Title: Betting on Bets: Anytime-Valid Tests for Stochastic Dominance (2026)
    - Authors: Sebastian Arnold, Yo Joong Choe, Marco Scarsini et al.
    - Citation Key: `arxiv_2604_21851`

    **KaTeX Formula**:
    $$
    \log(Et ) t = 1t t\sum  l=1 \log(Sl) \ge  1t t\sum  l=1 \int  \log(Sl(z)) dψl(z) = It
    $$

    Args:
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(t**2)


def expr_t_log_e_t_e_form_f(t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_log_e_t_e_form_f`."""
    return (pl.col(t)**2)


def calc_h_lambda_i_j_lambda_1712_0(delta: float, i: float, j: float) -> float:
    r"""Compute mathematical metric extracted from 1712_05879.

    **Source**:
    - Title: Hierarchical Bayesian Bradley-Terry for Applications in Major League Baseball (2017)
    - Authors: Gabriel C. Phelan, John T. Whelan
    - Citation Key: `1712_05879`

    **KaTeX Formula**:
    $$
    H\lambda i\lambda j = \delta ij ( \sigma -2 + N\sum  k=1 nik e\lambda i+\lambda k e\lambda i + e\lambda k ) - nij e\lambda i+\lambda j e\lambda i + e\lambda j . (20c)
    $$

    Args:
        delta (float): Input parameter `delta`.
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.

    Returns:
        float: Calculated metric value.
    """
    return float(delta*(i*j))


def expr_h_lambda_i_j_lambda_1712_0(delta: str = "delta", i: str = "i", j: str = "j") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_lambda_i_j_lambda_1712_0`."""
    return (pl.col(delta)*(pl.col(i)*pl.col(j)))


def calc_val_1712_05879_1712_0(N: float, sigma: float) -> float:
    r"""Compute mathematical metric extracted from 1712_05879.

    **Source**:
    - Title: Hierarchical Bayesian Bradley-Terry for Applications in Major League Baseball (2017)
    - Authors: Gabriel C. Phelan, John T. Whelan
    - Citation Key: `1712_05879`

    **KaTeX Formula**:
    $$
    \varsigma  \approx  1 H\sigma \sigma  =  \sigma 2 2N
    $$

    Args:
        N (float): Input parameter `N`.
        sigma (float): Input parameter `sigma`.

    Returns:
        float: Calculated metric value.
    """
    return float((22*N)*sigma)


def expr_val_1712_05879_1712_0(N: str = "N", sigma: str = "sigma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1712_05879_1712_0`."""
    return ((22*pl.col(N))*pl.col(sigma))


def calc_r_i_j_brown_(H: float, N: float, i: float, j: float) -> float:
    r"""Compute mathematical metric extracted from brown_2008_arxiv.

    **Source**:
    - Title: In-season prediction of batting averages: a field test of empirical Bayes and Bayes methodologies (2008)
    - Authors: Brown, L. D.
    - Citation Key: `brown_2008_arxiv`

    **KaTeX Formula**:
    $$
    Rji = Hji Nji .
    $$

    Args:
        H (float): Input parameter `H`.
        N (float): Input parameter `N`.
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.

    Returns:
        float: Calculated metric value.
    """
    return float(H*(j*(i*(N*(i*j)))))


def expr_r_i_j_brown_(H: str = "H", N: str = "N", i: str = "i", j: str = "j") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_i_j_brown_`."""
    return (pl.col(H)*(pl.col(j)*(pl.col(i)*(pl.col(N)*(pl.col(i)*pl.col(j))))))


def calc_v_a_r_x_1_i_x_2_i_brown_(N: float, i: float) -> float:
    r"""Compute mathematical metric extracted from brown_2008_arxiv.

    **Source**:
    - Title: In-season prediction of batting averages: a field test of empirical Bayes and Bayes methodologies (2008)
    - Authors: Brown, L. D.
    - Citation Key: `brown_2008_arxiv`

    **KaTeX Formula**:
    $$
    Var(X2i -X1i) = 1 4N2i + 1 4N1i .
    $$

    Args:
        N (float): Input parameter `N`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(14*(N*(1*i)) + 14*(N*(2*i)))


def expr_v_a_r_x_1_i_x_2_i_brown_(N: str = "N", i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_a_r_x_1_i_x_2_i_brown_`."""
    return (14*(pl.col(N)*(1*pl.col(i))) + 14*(pl.col(N)*(2*pl.col(i))))


def calc_g_tau_c_nu_m_nu_form_3(J: float, T: float, c: float, f: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_13304.

    **Source**:
    - Title: Humanoid Robot Running Through Random Stepping Stones and Jumping Over Obstacles: Step Adaptation Using Spring-Mass Trajectories (2025)
    - Authors: Sait Sovukluk, Johannes Englsberger, Christian Ott
    - Citation Key: `arxiv_2512_13304`

    **KaTeX Formula**:
    $$
    M\nu  + C\nu  + \tau g =   0 \tau    + J ^T c fc + J ^T p fp, (38a)
    $$

    Args:
        J (float): Input parameter `J`.
        T (float): Input parameter `T`.
        c (float): Input parameter `c`.
        f (float): Input parameter `f`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(J**T*c**2*f + J**T*f*p**2)


def expr_g_tau_c_nu_m_nu_form_3(J: str = "J", T: str = "T", c: str = "c", f: str = "f", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_tau_c_nu_m_nu_form_3`."""
    return (pl.col(J)**pl.col(T)*pl.col(c)**2*pl.col(f) + pl.col(J)**pl.col(T)*pl.col(f)*pl.col(p)**2)


def calc_r_e_p_l_a_c_e_m_e_n_t_r_u_n_s_form_a(A: float, P: float) -> float:
    r"""Compute mathematical metric extracted from fangraphs_war_position_glossary.

    **Source**:
    - Title: FanGraphs Sabermetric Library: Wins Above Replacement (WAR) for Position Players (2026)
    - Authors: FanGraphs
    - Citation Key: `fangraphs_war_position_glossary`

    **KaTeX Formula**:
    $$
    ReplacementRuns = 57.0 \cdot \left(\frac{PA}{2430}\right)
    $$

    Args:
        A (float): Input parameter `A`.
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(0.0234567901234568*A*P)


def expr_r_e_p_l_a_c_e_m_e_n_t_r_u_n_s_form_a(A: str = "A", P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_e_p_l_a_c_e_m_e_n_t_r_u_n_s_form_a`."""
    return (0.0234567901234568*pl.col(A)*pl.col(P))


def calc_p_x_form_5(A: float, B: float, p: float, u: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_17701.

    **Source**:
    - Title: Barrier Functions Against Safety Drift in Shared Control (2026)
    - Authors: M. Yusuf Uzun, Yildiray Yildiz
    - Citation Key: `arxiv_2609_17701`

    **KaTeX Formula**:
    $$
    xp = Ap xp +Bp up, yp = Cp xp
    $$

    Args:
        A (float): Input parameter `A`.
        B (float): Input parameter `B`.
        p (float): Input parameter `p`.
        u (float): Input parameter `u`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(A*p**2*x + B*p**2*u)


def expr_p_x_form_5(A: str = "A", B: str = "B", p: str = "p", u: str = "u", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_x_form_5`."""
    return (pl.col(A)*pl.col(p)**2*pl.col(x) + pl.col(B)*pl.col(p)**2*pl.col(u))


def calc_d_c_p_l_s_u_r_form_a(C_A_P: float, D: float, R: float, g: float, l: float) -> float:
    r"""Compute mathematical metric extracted from bp_drc_plus_glossary.

    **Source**:
    - Title: Baseball Prospectus: Deserved Runs Created Plus (DRC+) and DRA (2026)
    - Authors: Jonathan Judge, Baseball Prospectus
    - Citation Key: `bp_drc_plus_glossary`

    **KaTeX Formula**:
    $$
    DRC_{plus} = 100 \cdot \left(\frac{DRC_{PA}}{lgDRC_{PA}}\right)
    $$

    Args:
        C_A_P (float): Input parameter `C_A_P`.
        D (float): Input parameter `D`.
        R (float): Input parameter `R`.
        g (float): Input parameter `g`.
        l (float): Input parameter `l`.

    Returns:
        float: Calculated metric value.
    """
    return float(100*((D*(C_A*P*R))/((l*(g*(D*(C_A*P*R)))))))


def expr_d_c_p_l_s_u_r_form_a(C_A_P: str = "C_A_P", D: str = "D", R: str = "R", g: str = "g", l: str = "l") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_c_p_l_s_u_r_form_a`."""
    return (100*((pl.col(D)*(C_A*P*pl.col(R)))/((pl.col(l)*(pl.col(g)*(pl.col(D)*(C_A*P*pl.col(R))))))))


def calc_n_v_s_form_b(n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    Nv(s) = n\sum  i=1 [H(s - (i - 1)l) - H(s - il) ]N (i) v (s)
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(n)


def expr_n_v_s_form_b(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_n_v_s_form_b`."""
    return (pl.col(n))


def calc_e_r_o_t_form_c(Omega: float, R: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    Erot = 180 \pi |\Omega R| \sum  (n,i,j)\in \Omega R \arccos(clip[ tr( RTnij Rnij ) - 1 2 , -1, 1])
    $$

    Args:
        Omega (float): Input parameter `Omega`.
        R (float): Input parameter `R`.

    Returns:
        float: Calculated metric value.
    """
    return float(180*math.pi*abs(Omega*R))


def expr_e_r_o_t_form_c(Omega: str = "Omega", R: str = "R") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_r_o_t_form_c`."""
    return (180*math.pi*abs(pl.col(Omega)*pl.col(R)))


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


def expr_f_m_x_form_1(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_m_x_form_1`."""
    return (pl.col(P))


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
    return float(i*m*n)


def expr_v_n_t_k_x_form_4(i: str = "i", m: str = "m", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_n_t_k_x_form_4`."""
    return (pl.col(i)*pl.col(m)*pl.col(n))


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


def expr_a_p_m_efron_(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_p_m_efron_`."""
    return (pl.col(P))


def calc_d_k_p_l_p_form_9(D: float, K: float, k: float, l: float, pm: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_25621.

    **Source**:
    - Title: Dissonance Spectrum explicitly models perceptual frequency interactions for better music understanding (2026)
    - Authors: Tianle Wang, Xinyi Tong, Liangke Zhao et al.
    - Citation Key: `arxiv_2608_25621`

    **KaTeX Formula**:
    $$
    D(pl -pk) =  D\pm K+l-k-1
    $$

    Args:
        D (float): Input parameter `D`.
        K (float): Input parameter `K`.
        k (float): Input parameter `k`.
        l (float): Input parameter `l`.
        pm (float): Input parameter `pm`.

    Returns:
        float: Calculated metric value.
    """
    return float(D*K*pm - k + l - 1)


def expr_d_k_p_l_p_form_9(D: str = "D", K: str = "K", k: str = "k", l: str = "l", pm: str = "pm") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_k_p_l_p_form_9`."""
    return (pl.col(D)*pl.col(K)*pl.col(pm) - pl.col(k) + pl.col(l) - 1)


def calc_q_form_4(L: float, R: float, phi: float, psi: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_08746.

    **Source**:
    - Title: Kinematics of Single-Winged Spinning Seeds: A Study on Mahogany and Buddha Coconut Samaras (2026)
    - Authors: Yogeshwaran G, Srisha M. V. Rao, Jagadeesh G
    - Citation Key: `arxiv_2603_08746`

    **KaTeX Formula**:
    $$
    q = \cos\phi LR \cdot   \theta LR + \sin\phi LR \cdot  \cos \theta LR \cdot  \psi LR
    $$

    Args:
        L (float): Input parameter `L`.
        R (float): Input parameter `R`.
        phi (float): Input parameter `phi`.
        psi (float): Input parameter `psi`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.sin(L*R*phi*math.cos(L**2*R**2*psi*theta)) + math.cos(L**2*R**2*phi*theta))


def expr_q_form_4(L: str = "L", R: str = "R", phi: str = "phi", psi: str = "psi", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_form_4`."""
    return (math.sin(pl.col(L)*pl.col(R)*pl.col(phi)*math.cos(pl.col(L)**2*pl.col(R)**2*pl.col(psi)*pl.col(theta))) + math.cos(pl.col(L)**2*pl.col(R)**2*pl.col(phi)*pl.col(theta)))


def calc_b_a_t_t_i_n_g_r_u_n_s_form_f(A: float, F: float, P: float, R: float, a: float, c: float, k: float, o: float, r: float, t: float, w: float) -> float:
    r"""Compute mathematical metric extracted from fangraphs_war_position_glossary.

    **Source**:
    - Title: FanGraphs Sabermetric Library: Wins Above Replacement (WAR) for Position Players (2026)
    - Authors: FanGraphs
    - Citation Key: `fangraphs_war_position_glossary`

    **KaTeX Formula**:
    $$
    BattingRuns = wRAA + \left(\frac{lgR}{lgPA} - ParkFactor \cdot \frac{lgR}{lgPA}\right) \cdot PA
    $$

    Args:
        A (float): Input parameter `A`.
        F (float): Input parameter `F`.
        P (float): Input parameter `P`.
        R (float): Input parameter `R`.
        a (float): Input parameter `a`.
        c (float): Input parameter `c`.
        k (float): Input parameter `k`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(A**2*R*w + A*P*(-F*R*a**2*c*k*o*r**2*t/A + R/(A*P)))


def expr_b_a_t_t_i_n_g_r_u_n_s_form_f(A: str = "A", F: str = "F", P: str = "P", R: str = "R", a: str = "a", c: str = "c", k: str = "k", o: str = "o", r: str = "r", t: str = "t", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_b_a_t_t_i_n_g_r_u_n_s_form_f`."""
    return (pl.col(A)**2*pl.col(R)*pl.col(w) + pl.col(A)*pl.col(P)*(-pl.col(F)*pl.col(R)*pl.col(a)**2*pl.col(c)*pl.col(k)*pl.col(o)*pl.col(r)**2*pl.col(t)/pl.col(A) + pl.col(R)/(pl.col(A)*pl.col(P))))


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
    return float(-A*D + D*H)


def expr_d_a_h_1603_0(A: str = "A", D: str = "D", H: str = "H") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_a_h_1603_0`."""
    return (-pl.col(A)*pl.col(D) + pl.col(D)*pl.col(H))


def calc_q_form_e(T: float, kappa: float, nabla: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_21639.

    **Source**:
    - Title: Liquid-Nitrogen Micropillar-Wick Cooling for Cryogenic Electronics: A Numerical Study of Thermal Performance and Capillary Dry-Out Limits (2026)
    - Authors: Felix Mende, Marcus Wislicenus, Dianping Jiang et al.
    - Citation Key: `arxiv_2609_21639`

    **KaTeX Formula**:
    $$
    q = -\kappa \nabla T
    $$

    Args:
        T (float): Input parameter `T`.
        kappa (float): Input parameter `kappa`.
        nabla (float): Input parameter `nabla`.

    Returns:
        float: Calculated metric value.
    """
    return float(-T*kappa*nabla)


def expr_q_form_e(T: str = "T", kappa: str = "kappa", nabla: str = "nabla") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_form_e`."""
    return (-pl.col(T)*pl.col(kappa)*pl.col(nabla))


def calc_rho_form_8(M: float, R: float, f: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2309_15318.

    **Source**:
    - Title: A Global 3-D Simulation of Magnetospheric Accretion: I. Magnetically Disrupted Disks and Surface Accretion (2023)
    - Authors: Zhaohuan Zhu, James M. Stone, Nuria Calvet
    - Citation Key: `arxiv_2309_15318`

    **KaTeX Formula**:
    $$
    \rho  = M 4\pi R2 vff
    $$

    Args:
        M (float): Input parameter `M`.
        R (float): Input parameter `R`.
        f (float): Input parameter `f`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(8*math.pi*M*R*f**2*v)


def expr_rho_form_8(M: str = "M", R: str = "R", f: str = "f", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_rho_form_8`."""
    return (8*math.pi*pl.col(M)*pl.col(R)*pl.col(f)**2*pl.col(v))


def calc_theta_i_j_brown_(i: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from brown_2008_arxiv.

    **Source**:
    - Title: In-season prediction of batting averages: a field test of empirical Bayes and Bayes methodologies (2008)
    - Authors: Brown, L. D.
    - Citation Key: `brown_2008_arxiv`

    **KaTeX Formula**:
    $$
    \theta ji = \theta i, j = 1, 2
    $$

    Args:
        i (float): Input parameter `i`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*theta)


def expr_theta_i_j_brown_(i: str = "i", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_theta_i_j_brown_`."""
    return (pl.col(i)*pl.col(theta))


def calc_t_m_g_i_form_0(Omega: float, h: float, q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2309_15318.

    **Source**:
    - Title: A Global 3-D Simulation of Magnetospheric Accretion: I. Magnetically Disrupted Disks and Surface Accretion (2023)
    - Authors: Zhaohuan Zhu, James M. Stone, Nuria Calvet
    - Citation Key: `arxiv_2309_15318`

    **KaTeX Formula**:
    $$
    tmig = \Omega -1h2 q-1 ( \Sigma R2 M* )-1 (1 + hK)
    $$

    Args:
        Omega (float): Input parameter `Omega`.
        h (float): Input parameter `h`.
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float(Omega - 2*h*q - 1)


def expr_t_m_g_i_form_0(Omega: str = "Omega", h: str = "h", q: str = "q") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_m_g_i_form_0`."""
    return (pl.col(Omega) - 2*pl.col(h)*pl.col(q) - 1)


def calc_n_form_0(B: float, omega: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1709_07969.

    **Source**:
    - Title: Optimal-power Configurations for Hover Solutions in Mono-spinners (2017)
    - Authors: Mojtaba Hedayatpour, Mehran Mehrandezh, Farrokh Janabi-Sharifi
    - Citation Key: `arxiv_1709_07969`

    **KaTeX Formula**:
    $$
    n = \omega B | \omega B|
    $$

    Args:
        B (float): Input parameter `B`.
        omega (float): Input parameter `omega`.

    Returns:
        float: Calculated metric value.
    """
    return float(B*omega*abs(B*omega))


def expr_n_form_0(B: str = "B", omega: str = "omega") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_n_form_0`."""
    return (pl.col(B)*pl.col(omega)*abs(pl.col(B)*pl.col(omega)))


def calc_sim_t_v_form_1(N: float, emptyset: float, gamma: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_06478.

    **Source**:
    - Title: Smorph: Playable Sound Morphing with Diffusion Models (2026)
    - Authors: Annie Chu, Hugo Flores García, Johannes Imort et al.
    - Citation Key: `arxiv_2610_06478`

    **KaTeX Formula**:
    $$
    \sim vt = v\emptyset  + \gamma  N\sum  i=1 wi (vi - v\emptyset )
    $$

    Args:
        N (float): Input parameter `N`.
        emptyset (float): Input parameter `emptyset`.
        gamma (float): Input parameter `gamma`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(N*gamma + emptyset*v)


def expr_sim_t_v_form_1(N: str = "N", emptyset: str = "emptyset", gamma: str = "gamma", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sim_t_v_form_1`."""
    return (pl.col(N)*pl.col(gamma) + pl.col(emptyset)*pl.col(v))


def calc_a_l_r_3_form_9(L: float, R: float, phi: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_08746.

    **Source**:
    - Title: Kinematics of Single-Winged Spinning Seeds: A Study on Mahogany and Buddha Coconut Samaras (2026)
    - Authors: Yogeshwaran G, Srisha M. V. Rao, Jagadeesh G
    - Citation Key: `arxiv_2603_08746`

    **KaTeX Formula**:
    $$
    aLR 3 =  - \sin \theta LR \sin \phi LR \cos \theta LR \cos \phi LR \cos \theta LR
    $$

    Args:
        L (float): Input parameter `L`.
        R (float): Input parameter `R`.
        phi (float): Input parameter `phi`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(-math.sin(L*R*phi)*math.sin(L*R*theta)*math.cos(L*R*phi)*math.cos(L*R*theta)**2)


def expr_a_l_r_3_form_9(L: str = "L", R: str = "R", phi: str = "phi", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_l_r_3_form_9`."""
    return (-math.sin(pl.col(L)*pl.col(R)*pl.col(phi))*math.sin(pl.col(L)*pl.col(R)*pl.col(theta))*math.cos(pl.col(L)*pl.col(R)*pl.col(phi))*math.cos(pl.col(L)*pl.col(R)*pl.col(theta))**2)


def calc_theta_d_t_form_d(e: float, l: float, o: float, omega: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    \theta td = -\theta * lo - \pi  \omega e(a* )
    $$

    Args:
        e (float): Input parameter `e`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.
        omega (float): Input parameter `omega`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(-math.pi*e*omega - l*o*theta)


def expr_theta_d_t_form_d(e: str = "e", l: str = "l", o: str = "o", omega: str = "omega", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_theta_d_t_form_d`."""
    return (-math.pi*pl.col(e)*pl.col(omega) - pl.col(l)*pl.col(o)*pl.col(theta))


def calc_r_t_form_d(Delta: float, P: float, alpha: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_03140.

    **Source**:
    - Title: Sample-Efficient Pareto Front Modeling for Energy-Aware Reinforcement Learning Using Bayesian Optimization (2026)
    - Authors: Georg Schäfer, Jakob Rehrl, Stefan Huber et al.
    - Citation Key: `arxiv_2607_03140`

    **KaTeX Formula**:
    $$
    Rt = -(1 - \alpha ) \cdot  |\Delta t| - \alpha  \cdot  Pt
    $$

    Args:
        Delta (float): Input parameter `Delta`.
        P (float): Input parameter `P`.
        alpha (float): Input parameter `alpha`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(-P*alpha*t + (alpha - 1)*abs(Delta*t))


def expr_r_t_form_d(Delta: str = "Delta", P: str = "P", alpha: str = "alpha", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_t_form_d`."""
    return (-pl.col(P)*pl.col(alpha)*pl.col(t) + (pl.col(alpha) - 1)*abs(pl.col(Delta)*pl.col(t)))


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
    return float(a*m*x)


def expr_b_p_k_form_0(a: str = "a", m: str = "m", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_b_p_k_form_0`."""
    return (pl.col(a)*pl.col(m)*pl.col(x))


def calc_val_30_form_1(L: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    (30) = L\sum  l=1 \int  f(yw[n, l]|H0) \ln f(yw[n, l]|H0) f(yw[n, l]|H1) dyw[n, l] (31) = L [\ln (1+\gamma w[n]) - \gamma w[n] 1 + \gamma w[n] ]
    $$

    Args:
        L (float): Input parameter `L`.

    Returns:
        float: Calculated metric value.
    """
    return float(L)


def expr_val_30_form_1(L: str = "L") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_30_form_1`."""
    return (pl.col(L))


def calc_log_m_e_form_e(A: float, O: float, T: float, alpha: float, c: float, dA: float, dB: float, dF: float, dt: float, s: float, sigma: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27416.

    **Source**:
    - Title: Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization (2026)
    - Authors: Koichi Miyamoto
    - Citation Key: `arxiv_2610_27416`

    **KaTeX Formula**:
    $$
    \log M = O \log  \alpha dA/dt + \sigma 2 T c2 \alpha dB/dt + ( \sigma 2 T c2 ) 1-s 2 \alpha dF/dt \alpha 2A \cdot  (\sqrt \sigma 2T +\sigma X)(\alpha AT + \sqrt N)  C \epsilon c(1 - c)
    $$

    Args:
        A (float): Input parameter `A`.
        O (float): Input parameter `O`.
        T (float): Input parameter `T`.
        alpha (float): Input parameter `alpha`.
        c (float): Input parameter `c`.
        dA (float): Input parameter `dA`.
        dB (float): Input parameter `dB`.
        dF (float): Input parameter `dF`.
        dt (float): Input parameter `dt`.
        s (float): Input parameter `s`.
        sigma (float): Input parameter `sigma`.

    Returns:
        float: Calculated metric value.
    """
    return float((1*(sigma*(2*(T*(2*c)))) + (O*math.log((alpha*dA)/dt, math.e) + (sigma*(2*(T*(c*(2*(alpha*dB))))))/dt)) - (s*(2*(alpha*dF)))/(dt*((2*A)*alpha)))


def expr_log_m_e_form_e(A: str = "A", O: str = "O", T: str = "T", alpha: str = "alpha", c: str = "c", dA: str = "dA", dB: str = "dB", dF: str = "dF", dt: str = "dt", s: str = "s", sigma: str = "sigma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_log_m_e_form_e`."""
    return ((1*(pl.col(sigma)*(2*(pl.col(T)*(2*pl.col(c))))) + (pl.col(O)*((pl.col(alpha).log()*pl.col(dA))/pl.col(dt), math.e) + (pl.col(sigma)*(2*(pl.col(T)*(pl.col(c)*(2*(pl.col(alpha)*pl.col(dB)))))))/pl.col(dt))) - (pl.col(s)*(2*(pl.col(alpha)*pl.col(dF))))/(pl.col(dt)*((2*pl.col(A))*pl.col(alpha))))


def calc_k_z_form_2(i: float, m: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_12629.

    **Source**:
    - Title: Bivariate Isotonic Regression by Dynamic Programming (2026)
    - Authors: Pedro Afonso Fernandes
    - Citation Key: `arxiv_2607_12629`

    **KaTeX Formula**:
    $$
    z* k = min{z* k+1, pk}
    $$

    Args:
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*m*n)


def expr_k_z_form_2(i: str = "i", m: str = "m", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_z_form_2`."""
    return (pl.col(i)*pl.col(m)*pl.col(n))


def calc_z_i_j_form_2(i: float, m: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_12629.

    **Source**:
    - Title: Bivariate Isotonic Regression by Dynamic Programming (2026)
    - Authors: Pedro Afonso Fernandes
    - Citation Key: `arxiv_2607_12629`

    **KaTeX Formula**:
    $$
    z* ij = min{z* i+1,j , z* i,j+1, pij }
    $$

    Args:
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*m*n)


def expr_z_i_j_form_2(i: str = "i", m: str = "m", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_i_j_form_2`."""
    return (pl.col(i)*pl.col(m)*pl.col(n))


def calc_j_i_t_t_e_r_form_2(Omega: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    Jitter = 1 |\Omega 3| \sum  (n,i,j)\in \Omega 3 |f 3\Delta 3 Jnij |2
    $$

    Args:
        Omega (float): Input parameter `Omega`.

    Returns:
        float: Calculated metric value.
    """
    return float(3*abs(Omega))


def expr_j_i_t_t_e_r_form_2(Omega: str = "Omega") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_i_t_t_e_r_form_2`."""
    return (3*abs(pl.col(Omega)))


def calc_f_h_y_form_2(h: float, n: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2005_07742.

    **Source**:
    - Title: SEAM methodology for context-rich player matchup evaluations (2020)
    - Authors: Julia Wapner, David Dalpiaz, Daniel J. Eck
    - Citation Key: `arxiv_2005_07742`

    **KaTeX Formula**:
    $$
    fh(y) = 1 nhy1 hy2 n\sum  i=1 \phi  ( y1 - y1i hy1 ) \phi  ( y2 - y2i hy2 )
    $$

    Args:
        h (float): Input parameter `h`.
        n (float): Input parameter `n`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*h**2*n**2*y**2)


def expr_f_h_y_form_2(h: str = "h", n: str = "n", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_h_y_form_2`."""
    return (2*pl.col(h)**2*pl.col(n)**2*pl.col(y)**2)


def calc_r_t_form_2(G: float, M: float, m: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2309_15318.

    **Source**:
    - Title: A Global 3-D Simulation of Magnetospheric Accretion: I. Magnetically Disrupted Disks and Surface Accretion (2023)
    - Authors: Zhaohuan Zhu, James M. Stone, Nuria Calvet
    - Citation Key: `arxiv_2309_15318`

    **KaTeX Formula**:
    $$
    RT = ( m4 (4\pi )2 2GM* M 2 )1/7
    $$

    Args:
        G (float): Input parameter `G`.
        M (float): Input parameter `M`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float((704/7)*math.pi*G*M**2*m)


def expr_r_t_form_2(G: str = "G", M: str = "M", m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_t_form_2`."""
    return ((704/7)*math.pi*pl.col(G)*pl.col(M)**2*pl.col(m))


def calc_v_phi_r_form_3(Omega: float, R: float, phi: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2309_15318.

    **Source**:
    - Title: A Global 3-D Simulation of Magnetospheric Accretion: I. Magnetically Disrupted Disks and Surface Accretion (2023)
    - Authors: Zhaohuan Zhu, James M. Stone, Nuria Calvet
    - Citation Key: `arxiv_2309_15318`

    **KaTeX Formula**:
    $$
    v\phi (r) = \Omega *R + v\phi ,de-(r-rmag)2 /r2 sm
    $$

    Args:
        Omega (float): Input parameter `Omega`.
        R (float): Input parameter `R`.
        phi (float): Input parameter `phi`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(Omega*R + phi*v)


def expr_v_phi_r_form_3(Omega: str = "Omega", R: str = "R", phi: str = "phi", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_phi_r_form_3`."""
    return (pl.col(Omega)*pl.col(R) + pl.col(phi)*pl.col(v))


def calc_theta_m_a_x_form_3(N: float, a: float, e: float, l: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29142.

    **Source**:
    - Title: State-Dependent Objective Coordination for End-to-End Balance and Navigation (2026)
    - Authors: Xuhao Huang, Xitao Xu, Yuxin Zheng et al.
    - Citation Key: `arxiv_2610_29142`

    **KaTeX Formula**:
    $$
    \theta max = 1 Neval Neval \sum  i=1 max 1\le t\le Hi |\theta i,t|
    $$

    Args:
        N (float): Input parameter `N`.
        a (float): Input parameter `a`.
        e (float): Input parameter `e`.
        l (float): Input parameter `l`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*(e*(v*(a*(l*(N*(e*(v*(a*l))))))))))


def expr_theta_m_a_x_form_3(N: str = "N", a: str = "a", e: str = "e", l: str = "l", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_theta_m_a_x_form_3`."""
    return (1*(pl.col(N)*(pl.col(e)*(pl.col(v)*(pl.col(a)*(pl.col(l)*(pl.col(N)*(pl.col(e)*(pl.col(v)*(pl.col(a)*pl.col(l)))))))))))


def calc_s_a_t_u_form_8(a: float, m: float, u: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_06439.

    **Source**:
    - Title: Deep Reinforcement Learning based Control Design for Aircraft Recovery from Loss-of-Control Scenario (2026)
    - Authors: Imran Sayyed, Aayush Konar, Nandan Kumar Sinha
    - Citation Key: `arxiv_2601_06439`

    **KaTeX Formula**:
    $$
    sat(u) =  umax
    $$

    Args:
        a (float): Input parameter `a`.
        m (float): Input parameter `m`.
        u (float): Input parameter `u`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*m*u*x)


def expr_s_a_t_u_form_8(a: str = "a", m: str = "m", u: str = "u", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_a_t_u_form_8`."""
    return (pl.col(a)*pl.col(m)*pl.col(u)*pl.col(x))


def calc_n_form_6(B: float, n: float, omega: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1709_07969.

    **Source**:
    - Title: Optimal-power Configurations for Hover Solutions in Mono-spinners (2017)
    - Authors: Mojtaba Hedayatpour, Mehran Mehrandezh, Farrokh Janabi-Sharifi
    - Citation Key: `arxiv_1709_07969`

    **KaTeX Formula**:
    $$
    n = -\omega  B \times n
    $$

    Args:
        B (float): Input parameter `B`.
        n (float): Input parameter `n`.
        omega (float): Input parameter `omega`.

    Returns:
        float: Calculated metric value.
    """
    return float(-B*n*omega)


def expr_n_form_6(B: str = "B", n: str = "n", omega: str = "omega") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_n_form_6`."""
    return (-pl.col(B)*pl.col(n)*pl.col(omega))


def calc_a_r_form_4(B: float, C: float, G: float, M: float, i: float, n: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2309_15318.

    **Source**:
    - Title: A Global 3-D Simulation of Magnetospheric Accretion: I. Magnetically Disrupted Disks and Surface Accretion (2023)
    - Authors: Zhaohuan Zhu, James M. Stone, Nuria Calvet
    - Citation Key: `arxiv_2309_15318`

    **KaTeX Formula**:
    $$
    rA = r* ( B4 * r5 * 2GM* M 2 )1/7 in C.G.S
    $$

    Args:
        B (float): Input parameter `B`.
        C (float): Input parameter `C`.
        G (float): Input parameter `G`.
        M (float): Input parameter `M`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float((80/7)*B*G*M**2*r**2/(C*i*n))


def expr_a_r_form_4(B: str = "B", C: str = "C", G: str = "G", M: str = "M", i: str = "i", n: str = "n", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_r_form_4`."""
    return ((80/7)*pl.col(B)*pl.col(G)*pl.col(M)**2*pl.col(r)**2/(pl.col(C)*pl.col(i)*pl.col(n)))


def calc_t_form_c(A: float, gamma: float, i: float, rho: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1905_04632.

    **Source**:
    - Title: Ceiling Effects for Hybrid Aerial-Surface Locomotion of Small Rotorcraft (2019)
    - Authors: Yi Hsuan Hsiao, Pakpong Chirarattananon
    - Citation Key: `arxiv_1905_04632`

    **KaTeX Formula**:
    $$
    T = 2\rho A\gamma  2 v2 i
    $$

    Args:
        A (float): Input parameter `A`.
        gamma (float): Input parameter `gamma`.
        i (float): Input parameter `i`.
        rho (float): Input parameter `rho`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*(rho*(A*(gamma*(2*((2*i)*v))))))


def expr_t_form_c(A: str = "A", gamma: str = "gamma", i: str = "i", rho: str = "rho", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_form_c`."""
    return (2*(pl.col(rho)*(pl.col(A)*(pl.col(gamma)*(2*((2*pl.col(i))*pl.col(v)))))))


def calc_t_form_f(A: float, Omega: float, R: float, c: float, delta: float, i: float, rho: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1905_04632.

    **Source**:
    - Title: Ceiling Effects for Hybrid Aerial-Surface Locomotion of Small Rotorcraft (2019)
    - Authors: Yi Hsuan Hsiao, Pakpong Chirarattananon
    - Citation Key: `arxiv_1905_04632`

    **KaTeX Formula**:
    $$
    T = 12 \rho AR2 (c0 - c1 vi \Omega R + c2 vi \Omega R \delta )\Omega 2
    $$

    Args:
        A (float): Input parameter `A`.
        Omega (float): Input parameter `Omega`.
        R (float): Input parameter `R`.
        c (float): Input parameter `c`.
        delta (float): Input parameter `delta`.
        i (float): Input parameter `i`.
        rho (float): Input parameter `rho`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(48*A*Omega*R*rho*(2*Omega*R*c*delta*i*v - Omega*R*c*i*v))


def expr_t_form_f(A: str = "A", Omega: str = "Omega", R: str = "R", c: str = "c", delta: str = "delta", i: str = "i", rho: str = "rho", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_form_f`."""
    return (48*pl.col(A)*pl.col(Omega)*pl.col(R)*pl.col(rho)*(2*pl.col(Omega)*pl.col(R)*pl.col(c)*pl.col(delta)*pl.col(i)*pl.col(v) - pl.col(Omega)*pl.col(R)*pl.col(c)*pl.col(i)*pl.col(v)))


def calc_t_form_7(A: float, Omega: float, R: float, c: float, delta: float, i: float, rho: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1905_04632.

    **Source**:
    - Title: Ceiling Effects for Hybrid Aerial-Surface Locomotion of Small Rotorcraft (2019)
    - Authors: Yi Hsuan Hsiao, Pakpong Chirarattananon
    - Citation Key: `arxiv_1905_04632`

    **KaTeX Formula**:
    $$
    T = 12 \rho AR2 (c0 - c1 vi \Omega R + c2 vi \Omega R \delta )\Omega 2
    $$

    Args:
        A (float): Input parameter `A`.
        Omega (float): Input parameter `Omega`.
        R (float): Input parameter `R`.
        c (float): Input parameter `c`.
        delta (float): Input parameter `delta`.
        i (float): Input parameter `i`.
        rho (float): Input parameter `rho`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(48*A*Omega*R*rho*(2*Omega*R*c*delta*i*v - Omega*R*c*i*v))


def expr_t_form_7(A: str = "A", Omega: str = "Omega", R: str = "R", c: str = "c", delta: str = "delta", i: str = "i", rho: str = "rho", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_form_7`."""
    return (48*pl.col(A)*pl.col(Omega)*pl.col(R)*pl.col(rho)*(2*pl.col(Omega)*pl.col(R)*pl.col(c)*pl.col(delta)*pl.col(i)*pl.col(v) - pl.col(Omega)*pl.col(R)*pl.col(c)*pl.col(i)*pl.col(v)))


def calc_d_form_4(H_R: float) -> float:
    r"""Compute mathematical metric extracted from tango_base_runs_glossary.

    **Source**:
    - Title: Base Runs (BsR) Offensive Estimator (2026)
    - Authors: David Smyth, Tom Tango
    - Citation Key: `tango_base_runs_glossary`

    **KaTeX Formula**:
    $$
    D = H_{R}
    $$

    Args:
        H_R (float): Input parameter `H_R`.

    Returns:
        float: Calculated metric value.
    """
    return float(H_R)


def expr_d_form_4(H_R: str = "H_R") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_form_4`."""
    return (pl.col(H_R))


def calc_c_l_p_form_1(alpha: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1709_07969.

    **Source**:
    - Title: Optimal-power Configurations for Hover Solutions in Mono-spinners (2017)
    - Authors: Mojtaba Hedayatpour, Mehran Mehrandezh, Farrokh Janabi-Sharifi
    - Citation Key: `arxiv_1709_07969`

    **KaTeX Formula**:
    $$
    CLp =0.1\alpha p+0.5 , CLB =0.1\alpha B+0.5 CDp =0.006\alpha p+0.04 , CDB =0.006\alpha B+0.04
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(0.1*alpha*p + 0.5)


def expr_c_l_p_form_1(alpha: str = "alpha", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_l_p_form_1`."""
    return (0.1*pl.col(alpha)*pl.col(p) + 0.5)


def calc_j_z_form_9(i: float, m: float, n: float, sim: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_12629.

    **Source**:
    - Title: Bivariate Isotonic Regression by Dynamic Programming (2026)
    - Authors: Pedro Afonso Fernandes
    - Citation Key: `arxiv_2607_12629`

    **KaTeX Formula**:
    $$
    J(z) = min\sim  z {L(z) + [J(\sim  z) : \sim  z \le  z]}
    $$

    Args:
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        sim (float): Input parameter `sim`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*m*n*sim*z)


def expr_j_z_form_9(i: str = "i", m: str = "m", n: str = "n", sim: str = "sim", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_z_form_9`."""
    return (pl.col(i)*pl.col(m)*pl.col(n)*pl.col(sim)*pl.col(z))


def calc_t_form_9(A: float, Omega: float, R: float, c: float, i: float, rho: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1905_04632.

    **Source**:
    - Title: Ceiling Effects for Hybrid Aerial-Surface Locomotion of Small Rotorcraft (2019)
    - Authors: Yi Hsuan Hsiao, Pakpong Chirarattananon
    - Citation Key: `arxiv_1905_04632`

    **KaTeX Formula**:
    $$
    T = 12 \rho AR2 (c0 - c1 vi \Omega R )\Omega 2
    $$

    Args:
        A (float): Input parameter `A`.
        Omega (float): Input parameter `Omega`.
        R (float): Input parameter `R`.
        c (float): Input parameter `c`.
        i (float): Input parameter `i`.
        rho (float): Input parameter `rho`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(-48*A*Omega**2*R**2*c*i*rho*v)


def expr_t_form_9(A: str = "A", Omega: str = "Omega", R: str = "R", c: str = "c", i: str = "i", rho: str = "rho", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_form_9`."""
    return (-48*pl.col(A)*pl.col(Omega)**2*pl.col(R)**2*pl.col(c)*pl.col(i)*pl.col(rho)*pl.col(v))


def calc_f_p_form_9(c: float, h: float, l: float, p: float, sigma: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_13304.

    **Source**:
    - Title: Humanoid Robot Running Through Random Stepping Stones and Jumping Over Obstacles: Step Adaptation Using Spring-Mass Trajectories (2025)
    - Authors: Sait Sovukluk, Johannes Englsberger, Christian Ott
    - Citation Key: `arxiv_2512_13304`

    **KaTeX Formula**:
    $$
    pf = pc +   0 \sigma yh 0   + lh   \sin \theta 1 \cos \theta 2 \sigma  \sin \theta 2 - \cos \theta 1 \cos \theta 2
    $$

    Args:
        c (float): Input parameter `c`.
        h (float): Input parameter `h`.
        l (float): Input parameter `l`.
        p (float): Input parameter `p`.
        sigma (float): Input parameter `sigma`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(c*p + h*l*math.sin(theta)*math.sin(2*theta)*math.cos(2*sigma*theta) - math.cos(theta)*math.cos(2*theta))


def expr_f_p_form_9(c: str = "c", h: str = "h", l: str = "l", p: str = "p", sigma: str = "sigma", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_p_form_9`."""
    return (pl.col(c)*pl.col(p) + pl.col(h)*pl.col(l)*math.sin(pl.col(theta))*math.sin(2*pl.col(theta))*math.cos(2*pl.col(sigma)*pl.col(theta)) - math.cos(pl.col(theta))*math.cos(2*pl.col(theta)))


def calc_v_n_1_form_a(a: float, delta: float, n: float, t: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    v[n+1] = v[n] +a[n]\delta t, \forall n \in  N \ {N}
    $$

    Args:
        a (float): Input parameter `a`.
        delta (float): Input parameter `delta`.
        n (float): Input parameter `n`.
        t (float): Input parameter `t`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*delta*n*t + n*v)


def expr_v_n_1_form_a(a: str = "a", delta: str = "delta", n: str = "n", t: str = "t", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_n_1_form_a`."""
    return (pl.col(a)*pl.col(delta)*pl.col(n)*pl.col(t) + pl.col(n)*pl.col(v))


def calc_delta_form_a(q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_03805.

    **Source**:
    - Title: Regularization in Paired Comparison Models via Pseudo-Games and Phantom Players (2026)
    - Authors: Mark E. Glickman
    - Citation Key: `arxiv_2606_03805`

    **KaTeX Formula**:
    $$
    \delta  = 1 - q 2q - 1
    $$

    Args:
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float(-2*q**2)


def expr_delta_form_a(q: str = "q") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_form_a`."""
    return (-2*pl.col(q)**2)


def calc_p_x_a_p_e_x_form_f(a: float, c: float, e: float, l: float, o: float, psi: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    pxapex = ae \sin(\theta lo + \psi e) (61c)
    $$

    Args:
        a (float): Input parameter `a`.
        c (float): Input parameter `c`.
        e (float): Input parameter `e`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.
        psi (float): Input parameter `psi`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(61*a*c*e*math.sin(e*psi + l*o*theta))


def expr_p_x_a_p_e_x_form_f(a: str = "a", c: str = "c", e: str = "e", l: str = "l", o: str = "o", psi: str = "psi", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_x_a_p_e_x_form_f`."""
    return (61*pl.col(a)*pl.col(c)*pl.col(e)*math.sin(pl.col(e)*pl.col(psi) + pl.col(l)*pl.col(o)*pl.col(theta)))


def calc_m_a_c_c_form_d(k: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2309_15318.

    **Source**:
    - Title: A Global 3-D Simulation of Magnetospheric Accretion: I. Magnetically Disrupted Disks and Surface Accretion (2023)
    - Authors: Zhaohuan Zhu, James M. Stone, Nuria Calvet
    - Citation Key: `arxiv_2309_15318`

    **KaTeX Formula**:
    $$
    Macc = - 2\pi  \partial Rvk/\partial R \times  ( \partial  \partial R (R2\alpha int\Sigma c2s ) + R2 (\langle \rho vz\delta v\phi \rangle  - \langle BzB\phi \rangle ) ||||zmax zmin )
    $$

    Args:
        k (float): Input parameter `k`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(-2*math.pi*k*v)


def expr_m_a_c_c_form_d(k: str = "k", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_a_c_c_form_d`."""
    return (-2*math.pi*pl.col(k)*pl.col(v))


def calc_i_s_form_f(N: float, e: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_26780.

    **Source**:
    - Title: Event-based Gaze Control System for Accurate Real-time Spin Estimation in Professional Ball Games (2026)
    - Authors: Yunpu Hu, Fabian Schilling, Valentina Cavinato et al.
    - Citation Key: `arxiv_2606_26780`

    **KaTeX Formula**:
    $$
    I[s] = Ne\sum  k=1 \delta (s - s'k )
    $$

    Args:
        N (float): Input parameter `N`.
        e (float): Input parameter `e`.

    Returns:
        float: Calculated metric value.
    """
    return float(N*e)


def expr_i_s_form_f(N: str = "N", e: str = "e") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_s_form_f`."""
    return (pl.col(N)*pl.col(e))


def calc_f_s_p_y_2005_0(e: float, n: float, p: float, t: float, y: float) -> float:
    r"""Compute mathematical metric extracted from 2005_07742.

    **Source**:
    - Title: SEAM methodology for context-rich player matchup evaluations (2020)
    - Authors: Julia Wapner, David Dalpiaz, Daniel J. Eck
    - Citation Key: `2005_07742`

    **KaTeX Formula**:
    $$
    fsp(y) = ntype \sum  t=1 \rho t  fsp,t(y|xb,t),  fsb(y) = ntype \sum  t=1 \rho t  fsb,t(y|xp,t)
    $$

    Args:
        e (float): Input parameter `e`.
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.
        t (float): Input parameter `t`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(e*n*p*t*y)


def expr_f_s_p_y_2005_0(e: str = "e", n: str = "n", p: str = "p", t: str = "t", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_s_p_y_2005_0`."""
    return (pl.col(e)*pl.col(n)*pl.col(p)*pl.col(t)*pl.col(y))


def calc_t_b_form_5(B: float, H_R: float) -> float:
    r"""Compute mathematical metric extracted from tango_base_runs_glossary.

    **Source**:
    - Title: Base Runs (BsR) Offensive Estimator (2026)
    - Authors: David Smyth, Tom Tango
    - Citation Key: `tango_base_runs_glossary`

    **KaTeX Formula**:
    $$
    T_{B} = 1B + 2 \cdot 2B + 3 \cdot 3B + 4 \cdot H_{R}
    $$

    Args:
        B (float): Input parameter `B`.
        H_R (float): Input parameter `H_R`.

    Returns:
        float: Calculated metric value.
    """
    return float(4*H_R + (3*(3*B) + (1*B + 2*(2*B))))


def expr_t_b_form_5(B: str = "B", H_R: str = "H_R") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_b_form_5`."""
    return (4*pl.col(H_R) + (3*(3*pl.col(B)) + (1*pl.col(B) + 2*(2*pl.col(B)))))


def calc_eta_form_5(dsigma: float, sigma: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2605_05487.

    **Source**:
    - Title: Cross-individual generalizability of machine learning models for ball speed prediction in baseball pitching (2026)
    - Authors: Ryota Takamido, Chiharu Suzuki, Hiroki Nakamoto
    - Citation Key: `arxiv_2605_05487`

    **KaTeX Formula**:
    $$
    \eta  = d   \sigma   + \sigma
    $$

    Args:
        dsigma (float): Input parameter `dsigma`.
        sigma (float): Input parameter `sigma`.

    Returns:
        float: Calculated metric value.
    """
    return float(dsigma + sigma)


def expr_eta_form_5(dsigma: str = "dsigma", sigma: str = "sigma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_eta_form_5`."""
    return (pl.col(dsigma) + pl.col(sigma))


def calc_w_e_v_e_n_t_form_5(Delta: float, E_k: float, N_e_v_e_n_t: float, R: float) -> float:
    r"""Compute mathematical metric extracted from tangotiger_re24_glossary.

    **Source**:
    - Title: Tom Tango: 24-State Run Expectancy Matrix (RE24) and Transition Values (2026)
    - Authors: Tom Tango, Mitchel Lichtman, Andrew Dolphin
    - Citation Key: `tangotiger_re24_glossary`

    **KaTeX Formula**:
    $$
    w_{event} = \frac{1}{N_{event}} \cdot \sum_{k=1}^{N_{event}} \Delta RE_k
    $$

    Args:
        Delta (float): Input parameter `Delta`.
        E_k (float): Input parameter `E_k`.
        N_e_v_e_n_t (float): Input parameter `N_e_v_e_n_t`.
        R (float): Input parameter `R`.

    Returns:
        float: Calculated metric value.
    """
    return float((builtins.sum(Delta*(E_k*R) for k in range(1, N_e*(v*(e*(n*t)))+1)))/N_e*(v*(e*(n*t))))


def expr_w_e_v_e_n_t_form_5(Delta: str = "Delta", E_k: str = "E_k", N_e_v_e_n_t: str = "N_e_v_e_n_t", R: str = "R") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_e_v_e_n_t_form_5`."""
    return ((builtins.sum(pl.col(Delta)*(pl.col(E_k)*pl.col(R)) for k in range(1, N_e*(v*(e*(n*t)))+1)))/N_e*(v*(e*(n*t))))


def calc_p_i_i_theta_form_0(beta: float, e: float, i: float, pi: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    Pi(\theta i) = 1 (2\pi /\beta i)1/2 e-\beta i\theta 2 i /2
    $$

    Args:
        beta (float): Input parameter `beta`.
        e (float): Input parameter `e`.
        i (float): Input parameter `i`.
        pi (float): Input parameter `pi`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(-(beta*(i*((2*i)*theta)))/2 + (1*(1*((2*pi)/((beta*i)))))/((2*e)))


def expr_p_i_i_theta_form_0(beta: str = "beta", e: str = "e", i: str = "i", pi: str = "pi", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_i_theta_form_0`."""
    return (-(pl.col(beta)*(pl.col(i)*((2*pl.col(i))*pl.col(theta))))/2 + (1*(1*((2*pl.col(pi))/((pl.col(beta)*pl.col(i))))))/((2*pl.col(e))))


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
    return float(C*a*n**2*o*s*t**2)


def expr_c_a_b_form_0(C: str = "C", a: str = "a", n: str = "n", o: str = "o", s: str = "s", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_a_b_form_0`."""
    return (pl.col(C)*pl.col(a)*pl.col(n)**2*pl.col(o)*pl.col(s)*pl.col(t)**2)


def calc_c_form_6(A_B: float, B_B: float, H: float, H_R: float) -> float:
    r"""Compute mathematical metric extracted from tango_base_runs_glossary.

    **Source**:
    - Title: Base Runs (BsR) Offensive Estimator (2026)
    - Authors: David Smyth, Tom Tango
    - Citation Key: `tango_base_runs_glossary`

    **KaTeX Formula**:
    $$
    C = 3 \cdot (A_{B} - H) + 0.9 \cdot (H + B_{B} - H_{R})
    $$

    Args:
        A_B (float): Input parameter `A_B`.
        B_B (float): Input parameter `B_B`.
        H (float): Input parameter `H`.
        H_R (float): Input parameter `H_R`.

    Returns:
        float: Calculated metric value.
    """
    return float(3*(A_B - H) + 0.9*(-H_R + (B_B + H)))


def expr_c_form_6(A_B: str = "A_B", B_B: str = "B_B", H: str = "H", H_R: str = "H_R") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_form_6`."""
    return (3*(pl.col(A_B) - pl.col(H)) + 0.9*(-pl.col(H_R) + (pl.col(B_B) + pl.col(H))))


def calc_sim_beta_0_form_3(a: float, beta: float, de: float, f: float, k: float, p: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_21163.

    **Source**:
    - Title: Simultaneous Estimation of Ballpark Effects and Team Defense Using Total Bases Residuals (2026)
    - Authors: Jhe-Jia Wu, Tian-Li Yan, Ting-Li Chen
    - Citation Key: `arxiv_2603_21163`

    **KaTeX Formula**:
    $$
    \sim  \beta 0 =  \beta 0 +  \beta park -  \beta def
    $$

    Args:
        a (float): Input parameter `a`.
        beta (float): Input parameter `beta`.
        de (float): Input parameter `de`.
        f (float): Input parameter `f`.
        k (float): Input parameter `k`.
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(-beta*de*f + (beta*(p*(a*(k*r))) + 0*beta))


def expr_sim_beta_0_form_3(a: str = "a", beta: str = "beta", de: str = "de", f: str = "f", k: str = "k", p: str = "p", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sim_beta_0_form_3`."""
    return (-pl.col(beta)*pl.col(de)*pl.col(f) + (pl.col(beta)*(pl.col(p)*(pl.col(a)*(pl.col(k)*pl.col(r)))) + 0*pl.col(beta)))


def calc_val_2511_17733_2511_1(alpha: float, beta: float, n: float, x: float) -> float:
    r"""Compute mathematical metric extracted from 2511_17733.

    **Source**:
    - Title: The Impacts of Increasingly Complex Matchup Models on Baseball Win Probability (2025)
    - Authors: Tristan Mott, Caleb Bradshaw, David Grimsman et al.
    - Citation Key: `2511_17733`

    **KaTeX Formula**:
    $$
    posterior predictive rate = \alpha +x \alpha  +\beta  +n
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        beta (float): Input parameter `beta`.
        n (float): Input parameter `n`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(n + (beta + (alpha*x + alpha)))


def expr_val_2511_17733_2511_1(alpha: str = "alpha", beta: str = "beta", n: str = "n", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2511_17733_2511_1`."""
    return (pl.col(n) + (pl.col(beta) + (pl.col(alpha)*pl.col(x) + pl.col(alpha))))


def calc_alpha_f_delta_e_gamma_x_form_b(a: float, alpha: float, b: float, delta: float, e: float, gamma: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_06635.

    **Source**:
    - Title: Modelling Athletic Ageing Relative to an Estimated Performance Envelope (2026)
    - Authors: Dae-Jin Lee
    - Citation Key: `arxiv_2608_06635`

    **KaTeX Formula**:
    $$
    \alpha  + f((x - \gamma )e-\delta  ) = (\alpha  + a - b\gamma e-\delta  ) + be-\delta  x
    $$

    Args:
        a (float): Input parameter `a`.
        alpha (float): Input parameter `alpha`.
        b (float): Input parameter `b`.
        delta (float): Input parameter `delta`.
        e (float): Input parameter `e`.
        gamma (float): Input parameter `gamma`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(-delta*x + (b*e + (-delta + (-b*e*gamma + (a + alpha)))))


def expr_alpha_f_delta_e_gamma_x_form_b(a: str = "a", alpha: str = "alpha", b: str = "b", delta: str = "delta", e: str = "e", gamma: str = "gamma", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_alpha_f_delta_e_gamma_x_form_b`."""
    return (-pl.col(delta)*pl.col(x) + (pl.col(b)*pl.col(e) + (-pl.col(delta) + (-pl.col(b)*pl.col(e)*pl.col(gamma) + (pl.col(a) + pl.col(alpha))))))


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
    return float(3*h*k - 1)


def expr_w_1_2511_1(h: str = "h", k: str = "k") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_1_2511_1`."""
    return (3*pl.col(h)*pl.col(k) - 1)


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


def expr_l_x_2511_1(x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_x_2511_1`."""
    return (pl.col(x))


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
    return float(n*x)


def expr_r_x_2511_1(n: str = "n", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_x_2511_1`."""
    return (pl.col(n)*pl.col(x))


def calc_eta_1_form_6(T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    1 + \eta  = T
    $$

    Args:
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(T)


def expr_eta_1_form_6(T: str = "T") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_eta_1_form_6`."""
    return (pl.col(T))


def calc_s_di_f_f_i_c_u_l_t_form_6(epsilon: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    S(difficult) = \epsilon , S(success | difficult) = \epsilon , S(success | safe) = 1- \epsilon
    $$

    Args:
        epsilon (float): Input parameter `epsilon`.

    Returns:
        float: Calculated metric value.
    """
    return float(epsilon)


def expr_s_di_f_f_i_c_u_l_t_form_6(epsilon: str = "epsilon") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_di_f_f_i_c_u_l_t_form_6`."""
    return (pl.col(epsilon))


def calc_miller2005_99c4eb(R_A: float, R_S: float, beta: float, gamma: float) -> float:
    r"""Compute mathematical metric extracted from miller2005.

    **Source**:
    - Title: A Derivation of the Pythagorean Expectation for Baseball (2005)
    - Authors: Steven J. Miller
    - Citation Key: `miller2005`

    **KaTeX Formula**:
    $$
    Won-Loss Percentage(R_{S},R_{A}, \beta , \gamma ) = (R_{S} - \beta )\gamma  (R_{S} - \beta )\gamma  + (R_{A} - \beta )\gamma
    $$

    Args:
        R_A (float): Input parameter `R_A`.
        R_S (float): Input parameter `R_S`.
        beta (float): Input parameter `beta`.
        gamma (float): Input parameter `gamma`.

    Returns:
        float: Calculated metric value.
    """
    return float(gamma*(R_A - beta) + (gamma*math.gamma(R_S - beta))*(R_S - beta))


def expr_miller2005_99c4eb(R_A: str = "R_A", R_S: str = "R_S", beta: str = "beta", gamma: str = "gamma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_miller2005_99c4eb`."""
    return (pl.col(gamma)*(pl.col(R_A) - pl.col(beta)) + (pl.col(gamma)*math.gamma(pl.col(R_S) - pl.col(beta)))*(pl.col(R_S) - pl.col(beta)))


def calc_g_m_i_l_form_7(I_j: float, L: float, M: float) -> float:
    r"""Compute mathematical metric extracted from tangotiger_leverage_index_glossary.

    **Source**:
    - Title: Tom Tango: Leverage Index (LI) and Win Probability Added (2026)
    - Authors: Tom Tango
    - Citation Key: `tangotiger_leverage_index_glossary`

    **KaTeX Formula**:
    $$
    gmLI = \frac{1}{M} \cdot \sum_{j=1}^{M} LI_j
    $$

    Args:
        I_j (float): Input parameter `I_j`.
        L (float): Input parameter `L`.
        M (float): Input parameter `M`.

    Returns:
        float: Calculated metric value.
    """
    return float((builtins.sum(I_j*L for j in range(1, M+1)))/M)


def expr_g_m_i_l_form_7(I_j: str = "I_j", L: str = "L", M: str = "M") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_m_i_l_form_7`."""
    return ((builtins.sum(pl.col(I_j)*pl.col(L) for j in range(1, pl.col(M)+1)))/pl.col(M))


def calc_val_2610_31153_form_7(epsilon: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31153.

    **Source**:
    - Title: Balanced Posted Prices in Stationary Two-Sided Markets (2026)
    - Authors: Ilan Reuven Cohen
    - Citation Key: `arxiv_2610_31153`

    **KaTeX Formula**:
    $$
    (u\epsilon j (p) + \epsilon )\pi \epsilon  j (l) = E\pi \epsilon p [(d\epsilon j (N, p) + \epsilon )1{Nj = l + 1}]
    $$

    Args:
        epsilon (float): Input parameter `epsilon`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e*math.pi*epsilon*p)


def expr_val_2610_31153_form_7(epsilon: str = "epsilon", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_31153_form_7`."""
    return (math.e*math.pi*pl.col(epsilon)*pl.col(p))


def calc_psi_b_w_form_0(B: float, R: float, W: float, omega: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    \psi wb = (W RB B \omega )[3]
    $$

    Args:
        B (float): Input parameter `B`.
        R (float): Input parameter `R`.
        W (float): Input parameter `W`.
        omega (float): Input parameter `omega`.

    Returns:
        float: Calculated metric value.
    """
    return float(3*B**2*R*W*omega)


def expr_psi_b_w_form_0(B: str = "B", R: str = "R", W: str = "W", omega: str = "omega") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_psi_b_w_form_0`."""
    return (3*pl.col(B)**2*pl.col(R)*pl.col(W)*pl.col(omega))


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
    return float(L*i*k*n)


def expr_l_v_a_l_form_4(L: str = "L", i: str = "i", k: str = "k", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_v_a_l_form_4`."""
    return (pl.col(L)*pl.col(i)*pl.col(k)*pl.col(n))


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
    return float(math.e*s)


def expr_e_b_a_e_s_form_3(s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_b_a_e_s_form_3`."""
    return (math.e*pl.col(s))


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
    return float(L*f)


def expr_f_l_x_2511_1(L: str = "L", f: str = "f") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_l_x_2511_1`."""
    return (pl.col(L)*pl.col(f))


def calc_val_1205_2071_form_2(D: float, m: float, omega: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    e*(2\pi *q*S*V/\omega 2)*CD\alpha  = m*(D*\omega 2)2
    $$

    Args:
        D (float): Input parameter `D`.
        m (float): Input parameter `m`.
        omega (float): Input parameter `omega`.

    Returns:
        float: Calculated metric value.
    """
    return float(m*(2*(D*(2*omega))))


def expr_val_1205_2071_form_2(D: str = "D", m: str = "m", omega: str = "omega") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1205_2071_form_2`."""
    return (pl.col(m)*(2*(pl.col(D)*(2*pl.col(omega)))))


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
    return float(R*f)


def expr_f_r_x_2511_1(R: str = "R", f: str = "f") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_r_x_2511_1`."""
    return (pl.col(R)*pl.col(f))


def calc_log_theta_c_j_theta_j_c_1_e_beyond(beta: float, c: float, gamma: float, j: float, x: float) -> float:
    r"""Compute mathematical metric extracted from beyond_runs_expectancy_jsm2014.

    **Source**:
    - Title: 311431_85069
    - Authors: Scientific Literature
    - Citation Key: `beyond_runs_expectancy_jsm2014`

    **KaTeX Formula**:
    $$
    \log ( \theta j c 1 - \theta j c ) = \gamma  j c + x\beta j
    $$

    Args:
        beta (float): Input parameter `beta`.
        c (float): Input parameter `c`.
        gamma (float): Input parameter `gamma`.
        j (float): Input parameter `j`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(gamma*(c*j) + x*(beta*j))


def expr_log_theta_c_j_theta_j_c_1_e_beyond(beta: str = "beta", c: str = "c", gamma: str = "gamma", j: str = "j", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_log_theta_c_j_theta_j_c_1_e_beyond`."""
    return (pl.col(gamma)*(pl.col(c)*pl.col(j)) + pl.col(x)*(pl.col(beta)*pl.col(j)))


def calc_f_s_p_y_form_0(e: float, n: float, p: float, t: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2005_07742.

    **Source**:
    - Title: SEAM methodology for context-rich player matchup evaluations (2020)
    - Authors: Julia Wapner, David Dalpiaz, Daniel J. Eck
    - Citation Key: `arxiv_2005_07742`

    **KaTeX Formula**:
    $$
    fsp(y) = ntype \sum  t=1 \rho tfsp,t(y|xb,t)
    $$

    Args:
        e (float): Input parameter `e`.
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.
        t (float): Input parameter `t`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(e*n*p*t*y)


def expr_f_s_p_y_form_0(e: str = "e", n: str = "n", p: str = "p", t: str = "t", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_s_p_y_form_0`."""
    return (pl.col(e)*pl.col(n)*pl.col(p)*pl.col(t)*pl.col(y))


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
    return float(-S*S*T)


def expr_a_t_w_o_w_a_o_form_9(S: str = "S", T: str = "T") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_t_w_o_w_a_o_form_9`."""
    return (-pl.col(S)*pl.col(S)*pl.col(T))


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
    return float(-a*p + p*s)


def expr_u_l_s_o_form_4(a: str = "a", p: str = "p", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_l_s_o_form_4`."""
    return (-pl.col(a)*pl.col(p) + pl.col(p)*pl.col(s))


def calc_i_b_a_l_l_omega_form_3(a: float, b: float, l: float, m: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1610_03464.

    **Source**:
    - Title: Oblique Collisions of Baseballs and Softballs with a Bat (2016)
    - Authors: Jeffrey R. Kensrud, Alan M. Nathan, Lloyd V. Smith
    - Citation Key: `arxiv_1610_03464`

    **KaTeX Formula**:
    $$
    Iball\omega  = mvball,tr = mvballr \sin(\psi  - \theta )
    $$

    Args:
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*b*l**2*m*v)


def expr_i_b_a_l_l_omega_form_3(a: str = "a", b: str = "b", l: str = "l", m: str = "m", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_b_a_l_l_omega_form_3`."""
    return (pl.col(a)*pl.col(b)*pl.col(l)**2*pl.col(m)*pl.col(v))


def calc_phi_form_1(T: float, c: float, m: float, x: float, y: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    \phi  = [m mc^T Ixx Ixy Ixz Iyy Iyz Izz ]^T
    $$

    Args:
        T (float): Input parameter `T`.
        c (float): Input parameter `c`.
        m (float): Input parameter `m`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float((-c**T*m**2*x**4*y**4*z**4)**T)


def expr_phi_form_1(T: str = "T", c: str = "c", m: str = "m", x: str = "x", y: str = "y", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_phi_form_1`."""
    return ((-pl.col(c)**pl.col(T)*pl.col(m)**2*pl.col(x)**4*pl.col(y)**4*pl.col(z)**4)**pl.col(T))


def calc_alpha_s_form_3(alpha: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_26548.

    **Source**:
    - Title: Camera Calibration Using Inaccurate and Asynchronous Discrete GPS Trajectory from Drones (2026)
    - Authors: R. Yang, Y. Bar-Shalom, H. A. J. Huang
    - Citation Key: `arxiv_2608_26548`

    **KaTeX Formula**:
    $$
    s\alpha  = \sin\alpha , s\epsilon  = \sin \epsilon , s\rho  = \sin\rho
    $$

    Args:
        alpha (float): Input parameter `alpha`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.sin(alpha))


def expr_alpha_s_form_3(alpha: str = "alpha") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_alpha_s_form_3`."""
    return (math.sin(pl.col(alpha)))


def calc_c_m_s_l_form_3(C: float, S: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    CMS[l] =  1 |CS | \sum  g\in CS \sum b,i \sum d\in g VbiSbidlbid \sum b,i \sum d\in g VbiSbid , |CS| > 0, 0, |CS| = 0
    $$

    Args:
        C (float): Input parameter `C`.
        S (float): Input parameter `S`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*abs(C*S))


def expr_c_m_s_l_form_3(C: str = "C", S: str = "S") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_m_s_l_form_3`."""
    return (1*abs(pl.col(C)*pl.col(S)))


def calc_rho_c_o_u_n_t_form_4(E: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1704_00823.

    **Source**:
    - Title: A Hierarchical Bayesian Model of Pitch Framing (2017)
    - Authors: Sameer K. Deshpande, Abraham J. Wyner
    - Citation Key: `arxiv_1704_00823`

    **KaTeX Formula**:
    $$
    \rho (COUNT ) = E[S|COUNT, TAKEN, Ball] - E[S|COUNT, TAKEN, Strike]
    $$

    Args:
        E (float): Input parameter `E`.

    Returns:
        float: Calculated metric value.
    """
    return float(E)


def expr_rho_c_o_u_n_t_form_4(E: str = "E") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_rho_c_o_u_n_t_form_4`."""
    return (pl.col(E))


def calc_e_t_i_z_form_4(t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2604_21851.

    **Source**:
    - Title: Betting on Bets: Anytime-Valid Tests for Stochastic Dominance (2026)
    - Authors: Sebastian Arnold, Yo Joong Choe, Marco Scarsini et al.
    - Citation Key: `arxiv_2604_21851`

    **KaTeX Formula**:
    $$
    Et(zi) = t\prod l=1 Sl(λl(zi), zi), t \in  ℕ
    $$

    Args:
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(t)


def expr_e_t_i_z_form_4(t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_t_i_z_form_4`."""
    return (pl.col(t))


def calc_j_i_t_t_e_r_form_9(Omega: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    Jitter = 1 |\Omega 3| \sum  (n,i,j)\in \Omega 3 |f 3\Delta 3Jnij |2
    $$

    Args:
        Omega (float): Input parameter `Omega`.

    Returns:
        float: Calculated metric value.
    """
    return float(3*abs(Omega))


def expr_j_i_t_t_e_r_form_9(Omega: str = "Omega") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_i_t_t_e_r_form_9`."""
    return (3*abs(pl.col(Omega)))


def calc_w_b_y_form_5(H: float, L: float, N: float, P: float, R: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    W yB = (  PRH -  PRN ) + (  PLH -  PLN ) |||(  PRH -  PRN ) + (  PLH -  PLN )|||
    $$

    Args:
        H (float): Input parameter `H`.
        L (float): Input parameter `L`.
        N (float): Input parameter `N`.
        P (float): Input parameter `P`.
        R (float): Input parameter `R`.

    Returns:
        float: Calculated metric value.
    """
    return float((P*(H*L) - P*L*N)*abs(abs(abs((P*(H*L) - P*L*N) + (P*(H*R) - P*N*R)))) + (P*(H*R) - P*N*R))


def expr_w_b_y_form_5(H: str = "H", L: str = "L", N: str = "N", P: str = "P", R: str = "R") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_b_y_form_5`."""
    return ((pl.col(P)*(pl.col(H)*pl.col(L)) - pl.col(P)*pl.col(L)*pl.col(N))*abs(abs(abs((pl.col(P)*(pl.col(H)*pl.col(L)) - pl.col(P)*pl.col(L)*pl.col(N)) + (pl.col(P)*(pl.col(H)*pl.col(R)) - pl.col(P)*pl.col(N)*pl.col(R))))) + (pl.col(P)*(pl.col(H)*pl.col(R)) - pl.col(P)*pl.col(N)*pl.col(R)))


def calc_f_k_z_form_5(k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2604_21851.

    **Source**:
    - Title: Betting on Bets: Anytime-Valid Tests for Stochastic Dominance (2026)
    - Authors: Sebastian Arnold, Yo Joong Choe, Marco Scarsini et al.
    - Citation Key: `arxiv_2604_21851`

    **KaTeX Formula**:
    $$
    F[k] (z) = 1 (k - 1)! E [(z - X)k-1 + ] , z \in  Z
    $$

    Args:
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e*math.factorial(k - 1))


def expr_f_k_z_form_5(k: str = "k") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_k_z_form_5`."""
    return (math.e*math.factorial(pl.col(k) - 1))


def calc_a_form_a(T: float, a: float, b: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    A = a1b^T1 , single selection, ∨Rr=1 arb^Tr , composition, F, correlated map
    $$

    Args:
        T (float): Input parameter `T`.
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*b**T)


def expr_a_form_a(T: str = "T", a: str = "a", b: str = "b") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_form_a`."""
    return (pl.col(a)*pl.col(b)**pl.col(T))


def calc_w_t_z_form_6(t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2604_21851.

    **Source**:
    - Title: Betting on Bets: Anytime-Valid Tests for Stochastic Dominance (2026)
    - Authors: Sebastian Arnold, Yo Joong Choe, Marco Scarsini et al.
    - Citation Key: `arxiv_2604_21851`

    **KaTeX Formula**:
    $$
    Wt(z) = t\prod l=1 [(1 - λl(z)) + λl(z)Sl(z)] , t \in  ℕ
    $$

    Args:
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(t)


def expr_w_t_z_form_6(t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_t_z_form_6`."""
    return (pl.col(t))


def calc_dv_dt_theta_v_r_v_r_theta_form_b(D: float, F: float, L: float, Omega: float, g: float, r: float, theta: float, u: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1408_4306.

    **Source**:
    - Title: Effect of lift force on the aerodynamics of dust grains in the protoplanetary disk (2014)
    - Authors: Masaki S. Yamaguchi, Shigeo S. Kimura
    - Citation Key: `arxiv_1408_4306`

    **KaTeX Formula**:
    $$
    dv\theta  dt + vrv\theta  r = -FD v\theta  - r\Omega g u +FL vr u
    $$

    Args:
        D (float): Input parameter `D`.
        F (float): Input parameter `F`.
        L (float): Input parameter `L`.
        Omega (float): Input parameter `Omega`.
        g (float): Input parameter `g`.
        r (float): Input parameter `r`.
        theta (float): Input parameter `theta`.
        u (float): Input parameter `u`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(-D*F*theta*v + F*L*r*u*v - Omega*g*r*u)


def expr_dv_dt_theta_v_r_v_r_theta_form_b(D: str = "D", F: str = "F", L: str = "L", Omega: str = "Omega", g: str = "g", r: str = "r", theta: str = "theta", u: str = "u", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_dv_dt_theta_v_r_v_r_theta_form_b`."""
    return (-pl.col(D)*pl.col(F)*pl.col(theta)*pl.col(v) + pl.col(F)*pl.col(L)*pl.col(r)*pl.col(u)*pl.col(v) - pl.col(Omega)*pl.col(g)*pl.col(r)*pl.col(u))


def calc_val_0_k_nu_form_6(k: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_0902_1360.

    **Source**:
    - Title: Hierarchical Bayesian Modeling of Hitting Performance in Baseball (2009)
    - Authors: Shane T. Jensen, Blake McShane, Abraham J. Wyner
    - Citation Key: `arxiv_0902_1360`

    **KaTeX Formula**:
    $$
    \nu 00k = nk\sum  i=1 \nu  i00 / nk and s20k = nk\sum  i=1 (\nu  i00 - \nu 00k)2 / nk
    $$

    Args:
        k (float): Input parameter `k`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(k*n)


def expr_val_0_k_nu_form_6(k: str = "k", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_0_k_nu_form_6`."""
    return (pl.col(k)*pl.col(n))


def calc_u_2_form_7(A: float, A_B: float, B: float, delta: float, nabla: float, sim: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_39364.

    **Source**:
    - Title: Imperfect bifurcations in a laminar 3D bluff body wake: effect of pitch and yaw (2026)
    - Authors: Atharva Lagwankar, Alessandro Chiarini, François Gallaire et al.
    - Citation Key: `arxiv_2609_39364`

    **KaTeX Formula**:
    $$
    u2 = - \sim  \delta \nabla  2 u \delta  2 - A 2 u A 2 2 + ABu A_{B} 2 - B 2 u B 2 2 , (A 12)
    $$

    Args:
        A (float): Input parameter `A`.
        A_B (float): Input parameter `A_B`.
        B (float): Input parameter `B`.
        delta (float): Input parameter `delta`.
        nabla (float): Input parameter `nabla`.
        sim (float): Input parameter `sim`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(-B*2*(u*(22*B)) + (A*(B*(u*(2*A_B))) + (-A*2*(u*(22*A)) - sim*delta*(nabla*(2*(u*(2*delta)))))))


def expr_u_2_form_7(A: str = "A", A_B: str = "A_B", B: str = "B", delta: str = "delta", nabla: str = "nabla", sim: str = "sim", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_2_form_7`."""
    return (-pl.col(B)*2*(pl.col(u)*(22*pl.col(B))) + (pl.col(A)*(pl.col(B)*(pl.col(u)*(2*pl.col(A_B)))) + (-pl.col(A)*2*(pl.col(u)*(22*pl.col(A))) - pl.col(sim)*pl.col(delta)*(pl.col(nabla)*(2*(pl.col(u)*(2*pl.col(delta))))))))


def calc_i_l_form_9(Delta: float, E_P_W: float, P_m_a_x: float, P_m_i_n: float, W: float) -> float:
    r"""Compute mathematical metric extracted from tangotiger_leverage_index_glossary.

    **Source**:
    - Title: Tom Tango: Leverage Index (LI) and Win Probability Added (2026)
    - Authors: Tom Tango
    - Citation Key: `tangotiger_leverage_index_glossary`

    **KaTeX Formula**:
    $$
    LI = \frac{\Delta WP_{max} - \Delta WP_{min}}{E_{WP}}
    $$

    Args:
        Delta (float): Input parameter `Delta`.
        E_P_W (float): Input parameter `E_P_W`.
        P_m_a_x (float): Input parameter `P_m_a_x`.
        P_m_i_n (float): Input parameter `P_m_i_n`.
        W (float): Input parameter `W`.

    Returns:
        float: Calculated metric value.
    """
    return float((Delta*(P_m*(a*x)*W) - Delta*P_m*(i*n)*W)/E_P*W)


def expr_i_l_form_9(Delta: str = "Delta", E_P_W: str = "E_P_W", P_m_a_x: str = "P_m_a_x", P_m_i_n: str = "P_m_i_n", W: str = "W") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_l_form_9`."""
    return ((pl.col(Delta)*(P_m*(a*x)*pl.col(W)) - pl.col(Delta)*P_m*(i*n)*pl.col(W))/E_P*pl.col(W))


def calc_beta_j_n_n_a_form_1(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_29041.

    **Source**:
    - Title: Baseball, An Extensive-Form Game-Theoretic Duel (2026)
    - Authors: Sebastian E. Ferrando, Eli Kohn
    - Citation Key: `arxiv_2607_29041`

    **KaTeX Formula**:
    $$
    \beta jN (aN) = P(AN = aN ||| AP = ajP , A_{B} = ajB ) , aN \in  AN
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_beta_j_n_n_a_form_1(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_beta_j_n_n_a_form_1`."""
    return (pl.col(P))


def calc_c_a_f_e_a_c_form_6(N: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1704_00823.

    **Source**:
    - Title: A Hierarchical Bayesian Model of Pitch Framing (2017)
    - Authors: Sameer K. Deshpande, Abraham J. Wyner
    - Citation Key: `arxiv_1704_00823`

    **KaTeX Formula**:
    $$
    CAFE(ca) = 4000 \times  1N \sum  \xi  f (ca, \xi )
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(4000*(1*N))


def expr_c_a_f_e_a_c_form_6(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_a_f_e_a_c_form_6`."""
    return (4000*(1*pl.col(N)))


def calc_z_l_form_7(F: float, L: float, Z: float, l: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_22876.

    **Source**:
    - Title: Full-Body Golf Swing Kinematic Reconstruction From a Smartwatch IMU (2026)
    - Authors: Yuanshuo Tan, Kezhe Zhu, Xiujie Sun et al.
    - Citation Key: `arxiv_2606_22876`

    **KaTeX Formula**:
    $$
    Zl = Zl + FFN (LN(Zl )) , (3a)
    $$

    Args:
        F (float): Input parameter `F`.
        L (float): Input parameter `L`.
        Z (float): Input parameter `Z`.
        l (float): Input parameter `l`.

    Returns:
        float: Calculated metric value.
    """
    return float(F**2*L*Z*l + Z*l)


def expr_z_l_form_7(F: str = "F", L: str = "L", Z: str = "Z", l: str = "l") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_l_form_7`."""
    return (pl.col(F)**2*pl.col(L)*pl.col(Z)*pl.col(l) + pl.col(Z)*pl.col(l))


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
    return float(-i**2*j)


def expr_z_l_y_u_c_c_u_x_i_k_2_j_r_maher_(i: str = "i", j: str = "j") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_l_y_u_c_c_u_x_i_k_2_j_r_maher_`."""
    return (-pl.col(i)**2*pl.col(j))


def calc_rho_form_7(A: float, B: float, F: float, Omega: float, T: float, cup: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    \rho  = |\Omega F \cup \Omega B \cup \Omega A| T \cdot  21 \cdot  3
    $$

    Args:
        A (float): Input parameter `A`.
        B (float): Input parameter `B`.
        F (float): Input parameter `F`.
        Omega (float): Input parameter `Omega`.
        T (float): Input parameter `T`.
        cup (float): Input parameter `cup`.

    Returns:
        float: Calculated metric value.
    """
    return float(63*T*abs(A*B*F*Omega**3*cup**2))


def expr_rho_form_7(A: str = "A", B: str = "B", F: str = "F", Omega: str = "Omega", T: str = "T", cup: str = "cup") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_rho_form_7`."""
    return (63*pl.col(T)*abs(pl.col(A)*pl.col(B)*pl.col(F)*pl.col(Omega)**3*pl.col(cup)**2))


def calc_f_s_b_y_form_7(e: float, n: float, p: float, t: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2005_07742.

    **Source**:
    - Title: SEAM methodology for context-rich player matchup evaluations (2020)
    - Authors: Julia Wapner, David Dalpiaz, Daniel J. Eck
    - Citation Key: `arxiv_2005_07742`

    **KaTeX Formula**:
    $$
    fsb(y) = ntype \sum  t=1 \rho tfsb,t(y|xp,t)
    $$

    Args:
        e (float): Input parameter `e`.
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.
        t (float): Input parameter `t`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(e*n*p*t*y)


def expr_f_s_b_y_form_7(e: str = "e", n: str = "n", p: str = "p", t: str = "t", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_s_b_y_form_7`."""
    return (pl.col(e)*pl.col(n)*pl.col(p)*pl.col(t)*pl.col(y))


def calc_n_l_2_q_h_e_a_t_form_8(N: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_21639.

    **Source**:
    - Title: Liquid-Nitrogen Micropillar-Wick Cooling for Cryogenic Electronics: A Numerical Study of Thermal Performance and Capillary Dry-Out Limits (2026)
    - Authors: Felix Mende, Marcus Wislicenus, Dianping Jiang et al.
    - Citation Key: `arxiv_2609_21639`

    **KaTeX Formula**:
    $$
    Nl2 qheat = N\sum  n=1 Qn
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(N)


def expr_n_l_2_q_h_e_a_t_form_8(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_n_l_2_q_h_e_a_t_form_8`."""
    return (pl.col(N))


def calc_e_p_o_s_form_8(Omega: float, P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    Epos = 1 |\Omega P | \sum  (n,i,j,A)\in \Omega P |PA(Jnij - Jnij )|2
    $$

    Args:
        Omega (float): Input parameter `Omega`.
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(abs(Omega*P))


def expr_e_p_o_s_form_8(Omega: str = "Omega", P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_p_o_s_form_8`."""
    return (abs(pl.col(Omega)*pl.col(P)))


def calc_partial_t_u_2_sim_l_u_2_form_7(F: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_39364.

    **Source**:
    - Title: Imperfect bifurcations in a laminar 3D bluff body wake: effect of pitch and yaw (2026)
    - Authors: Atharva Lagwankar, Alessandro Chiarini, François Gallaire et al.
    - Citation Key: `arxiv_2609_39364`

    **KaTeX Formula**:
    $$
    \partial tu2 + \sim Lu2 = F2, (A 10)
    $$

    Args:
        F (float): Input parameter `F`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*F)


def expr_partial_t_u_2_sim_l_u_2_form_7(F: str = "F") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_partial_t_u_2_sim_l_u_2_form_7`."""
    return (2*pl.col(F))


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


def expr_val_1_diebol(T: str = "T") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1_diebol`."""
    return (pl.col(T))


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
    return float(a*k**2*m*t*x**2)


def expr_m_t_form_d(a: str = "a", k: str = "k", m: str = "m", t: str = "t", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_t_form_d`."""
    return (pl.col(a)*pl.col(k)**2*pl.col(m)*pl.col(t)*pl.col(x)**2)


def calc_m_a_e_t_form_d(N: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_36769.

    **Source**:
    - Title: Externalizing Hand Grip Pressure Through Real-Time Visual Feedback (2026)
    - Authors: Andrew L. Huard, Avinash Ajit Nargund, Misha Sra
    - Citation Key: `arxiv_2610_36769`

    **KaTeX Formula**:
    $$
    MAE(t) = 1N N\sum i=1 |Puser,i(t) - Pideal,i(t)|
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*N))


def expr_m_a_e_t_form_d(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_a_e_t_form_d`."""
    return (1*(pl.col(N)*pl.col(N)))


def calc_partial_z_c_k_epsilon_partial_form_1(Delta: float, alpha: float, c: float, epsilon: float, k: float, s: float, x: float, y: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_26548.

    **Source**:
    - Title: Camera Calibration Using Inaccurate and Asynchronous Discrete GPS Trajectory from Drones (2026)
    - Authors: R. Yang, Y. Bar-Shalom, H. A. J. Huang
    - Citation Key: `arxiv_2608_26548`

    **KaTeX Formula**:
    $$
    \partial zC k \partial \epsilon  = -\Delta xks\alpha s\epsilon  -\Delta ykc\alpha s\epsilon  +\Delta zkc\epsilon
    $$

    Args:
        Delta (float): Input parameter `Delta`.
        alpha (float): Input parameter `alpha`.
        c (float): Input parameter `c`.
        epsilon (float): Input parameter `epsilon`.
        k (float): Input parameter `k`.
        s (float): Input parameter `s`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(-Delta*alpha*c*epsilon*k*s*y - Delta*alpha*epsilon*k*s**2*x + Delta*c*epsilon*k*z)


def expr_partial_z_c_k_epsilon_partial_form_1(Delta: str = "Delta", alpha: str = "alpha", c: str = "c", epsilon: str = "epsilon", k: str = "k", s: str = "s", x: str = "x", y: str = "y", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_partial_z_c_k_epsilon_partial_form_1`."""
    return (-pl.col(Delta)*pl.col(alpha)*pl.col(c)*pl.col(epsilon)*pl.col(k)*pl.col(s)*pl.col(y) - pl.col(Delta)*pl.col(alpha)*pl.col(epsilon)*pl.col(k)*pl.col(s)**2*pl.col(x) + pl.col(Delta)*pl.col(c)*pl.col(epsilon)*pl.col(k)*pl.col(z))


def calc_j_m_e_r_form_3(D: float, M: float, N: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_02991.

    **Source**:
    - Title: Subject-Specific Predictive Musculoskeletal Simulations of Lower-Limb Exoskeleton Assistance: Metabolic and Biomechanical Effects of Joint Assistance Strategies (2026)
    - Authors: Neethan Ratnakumar, Mariya Tohfafarosh, Xianlian Zhou
    - Citation Key: `arxiv_2610_02991`

    **KaTeX Formula**:
    $$
    JMER = 1 M \times D N\sum  i=1 ˙Ei(t)
    $$

    Args:
        D (float): Input parameter `D`.
        M (float): Input parameter `M`.
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float((1*M)*(D*N))


def expr_j_m_e_r_form_3(D: str = "D", M: str = "M", N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_m_e_r_form_3`."""
    return ((1*pl.col(M))*(pl.col(D)*pl.col(N)))


def calc_y_d_p_form_a(a: float, beta: float, d: float, de: float, epsilon: float, f: float, k: float, p: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_21163.

    **Source**:
    - Title: Simultaneous Estimation of Ballpark Effects and Team Defense Using Total Bases Residuals (2026)
    - Authors: Jhe-Jia Wu, Tian-Li Yan, Ting-Li Chen
    - Citation Key: `arxiv_2603_21163`

    **KaTeX Formula**:
    $$
    ypd = \beta 0 + \beta park p -\beta def d + \epsilon pd
    $$

    Args:
        a (float): Input parameter `a`.
        beta (float): Input parameter `beta`.
        d (float): Input parameter `d`.
        de (float): Input parameter `de`.
        epsilon (float): Input parameter `epsilon`.
        f (float): Input parameter `f`.
        k (float): Input parameter `k`.
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(epsilon*(d*p) + (-beta*de*(d*f) + (beta*(p*(a*(r*(k*p)))) + 0*beta)))


def expr_y_d_p_form_a(a: str = "a", beta: str = "beta", d: str = "d", de: str = "de", epsilon: str = "epsilon", f: str = "f", k: str = "k", p: str = "p", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_y_d_p_form_a`."""
    return (pl.col(epsilon)*(pl.col(d)*pl.col(p)) + (-pl.col(beta)*pl.col(de)*(pl.col(d)*pl.col(f)) + (pl.col(beta)*(pl.col(p)*(pl.col(a)*(pl.col(r)*(pl.col(k)*pl.col(p))))) + 0*pl.col(beta))))


def calc_h_da_a_t_form_2(J: float, T: float, a: float, da: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_02306.

    **Source**:
    - Title: Contact-Constrained Lower-Limb Joint-Offset Calibration for Humanoid Robots (2026)
    - Authors: Kaixiang Lu, Haiyu Lan, Chunxiao Qiao et al.
    - Citation Key: `arxiv_2609_02306`

    **KaTeX Formula**:
    $$
    Hdata = J ^T dataJdata, Hreg = Hdata + \lambda q diag(W 2 q ) +Hmech
    $$

    Args:
        J (float): Input parameter `J`.
        T (float): Input parameter `T`.
        a (float): Input parameter `a`.
        da (float): Input parameter `da`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(J*J**T*a**2*da**2*t**2)


def expr_h_da_a_t_form_2(J: str = "J", T: str = "T", a: str = "a", da: str = "da", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_da_a_t_form_2`."""
    return (pl.col(J)*pl.col(J)**pl.col(T)*pl.col(a)**2*pl.col(da)**2*pl.col(t)**2)


def calc_l_r_k_l_theta_form_2(H: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    LRKL(\theta ) = 1 H H-1 \sum  t=0 Eht\sim S(.) [KL(S\theta (\cdot  | ht)|T(\cdot  | ht))]
    $$

    Args:
        H (float): Input parameter `H`.

    Returns:
        float: Calculated metric value.
    """
    return float(H**2 - 1)


def expr_l_r_k_l_theta_form_2(H: str = "H") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_r_k_l_theta_form_2`."""
    return (pl.col(H)**2 - 1)


def calc_val_0_t_n_q_form_a(n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29565.

    **Source**:
    - Title: Preserving Operator Intent Under Actuation Constraints: Teleoperation of Manipulators with Coupled Transmissions (2026)
    - Authors: Xuhan Miao, Zijin Han, Yutong Shen et al.
    - Citation Key: `arxiv_2610_29565`

    **KaTeX Formula**:
    $$
    0Tn(q) = n\prod  i=1 [Rz(qi)Tz(di)Tx(ai)Rx(\alpha i)] = [R(q) p(q) 0 1 ]
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(n)


def expr_val_0_t_n_q_form_a(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_0_t_n_q_form_a`."""
    return (pl.col(n))


def calc_rho_c_o_u_n_t_1704_0(E: float) -> float:
    r"""Compute mathematical metric extracted from 1704_00823.

    **Source**:
    - Title: A Hierarchical Bayesian Model of Pitch Framing (2017)
    - Authors: Sameer K. Deshpande, Abraham J. Wyner
    - Citation Key: `1704_00823`

    **KaTeX Formula**:
    $$
    \rho (COUNT ) = E[S|COUNT, TAKEN, Ball] - E[S|COUNT, TAKEN, Strike]
    $$

    Args:
        E (float): Input parameter `E`.

    Returns:
        float: Calculated metric value.
    """
    return float(E)


def expr_rho_c_o_u_n_t_1704_0(E: str = "E") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_rho_c_o_u_n_t_1704_0`."""
    return (pl.col(E))


def calc_m_tau_form_b(B: float, T: float, g: float, tau: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29565.

    **Source**:
    - Title: Preserving Operator Intent Under Actuation Constraints: Teleoperation of Manipulators with Coupled Transmissions (2026)
    - Authors: Xuhan Miao, Zijin Han, Yutong Shen et al.
    - Citation Key: `arxiv_2610_29565`

    **KaTeX Formula**:
    $$
    \tau m = B-T\tau w + \tau g,m(q), im = K-1 t \tau m
    $$

    Args:
        B (float): Input parameter `B`.
        T (float): Input parameter `T`.
        g (float): Input parameter `g`.
        tau (float): Input parameter `tau`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(B - T*tau*w + g*tau)


def expr_m_tau_form_b(B: str = "B", T: str = "T", g: str = "g", tau: str = "tau", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_tau_form_b`."""
    return (pl.col(B) - pl.col(T)*pl.col(tau)*pl.col(w) + pl.col(g)*pl.col(tau))


def calc_c_a_f_e_a_c_1704_0(N: float) -> float:
    r"""Compute mathematical metric extracted from 1704_00823.

    **Source**:
    - Title: A Hierarchical Bayesian Model of Pitch Framing (2017)
    - Authors: Sameer K. Deshpande, Abraham J. Wyner
    - Citation Key: `1704_00823`

    **KaTeX Formula**:
    $$
    CAFE(ca) = 4000 \times  1N \sum  \xi  f (ca, \xi )
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(4000*(1*N))


def expr_c_a_f_e_a_c_1704_0(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_a_f_e_a_c_1704_0`."""
    return (4000*(1*pl.col(N)))


def calc_w_c_r_form_b(A: float, R: float, w: float) -> float:
    r"""Compute mathematical metric extracted from fangraphs_wrc_glossary.

    **Source**:
    - Title: FanGraphs Sabermetric Library: Weighted Runs Created (wRC and wRC+) (2026)
    - Authors: FanGraphs
    - Citation Key: `fangraphs_wrc_glossary`

    **KaTeX Formula**:
    $$
    wRC = wRAA + \frac{lgR}{lgPA} \cdot PA
    $$

    Args:
        A (float): Input parameter `A`.
        R (float): Input parameter `R`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(A**2*R*w + R)


def expr_w_c_r_form_b(A: str = "A", R: str = "R", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_c_r_form_b`."""
    return (pl.col(A)**2*pl.col(R)*pl.col(w) + pl.col(R))


def calc_r_e_t_form_3(N: float, T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    RTE = 1 NT \sum  n,i |rni - rni|2
    $$

    Args:
        N (float): Input parameter `N`.
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*T))


def expr_r_e_t_form_3(N: str = "N", T: str = "T") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_e_t_form_3`."""
    return (1*(pl.col(N)*pl.col(T)))


def calc_eq_y_d_p_1_n_p_dsum_i_p_i_form_c(p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_21163.

    **Source**:
    - Title: Simultaneous Estimation of Ballpark Effects and Team Defense Using Total Bases Residuals (2026)
    - Authors: Jhe-Jia Wu, Tian-Li Yan, Ting-Li Chen
    - Citation Key: `arxiv_2603_21163`

    **KaTeX Formula**:
    $$
    ypd = 1 npd \sum  i: p(i)=p, d(i)=d Ri
    $$

    Args:
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(p)


def expr_eq_y_d_p_1_n_p_dsum_i_p_i_form_c(p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_eq_y_d_p_1_n_p_dsum_i_p_i_form_c`."""
    return (pl.col(p))


def calc_u_form_d(alpha: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27416.

    **Source**:
    - Title: Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization (2026)
    - Authors: Koichi Miyamoto
    - Citation Key: `arxiv_2610_27416`

    **KaTeX Formula**:
    $$
    U =  1\alpha  (A1 * * *) . . . 1\alpha  (An * * * ) I(2⌈lg n⌉-n)2d
    $$

    Args:
        alpha (float): Input parameter `alpha`.

    Returns:
        float: Calculated metric value.
    """
    return float(alpha)


def expr_u_form_d(alpha: str = "alpha") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_form_d`."""
    return (pl.col(alpha))


def calc_theta_form_d(T: float, alpha: float, d: float, s: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    \theta  = [\alpha  d1 d2 d3 s12 s23 s13 t1 t2 t3 ]^T
    $$

    Args:
        T (float): Input parameter `T`.
        alpha (float): Input parameter `alpha`.
        d (float): Input parameter `d`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float((129168*alpha*d**3*s**3*t**3)**T)


def expr_theta_form_d(T: str = "T", alpha: str = "alpha", d: str = "d", s: str = "s", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_theta_form_d`."""
    return ((129168*pl.col(alpha)*pl.col(d)**3*pl.col(s)**3*pl.col(t)**3)**pl.col(T))


def calc_delta_p_form_e(N: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_21639.

    **Source**:
    - Title: Liquid-Nitrogen Micropillar-Wick Cooling for Cryogenic Electronics: A Numerical Study of Thermal Performance and Capillary Dry-Out Limits (2026)
    - Authors: Felix Mende, Marcus Wislicenus, Dianping Jiang et al.
    - Citation Key: `arxiv_2609_21639`

    **KaTeX Formula**:
    $$
    \Delta p = N\sum  n=1 \Delta pn = μlqheat l2 ρlℎlvℎkd,l,ℎ N(N + 1) 2
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(N)


def expr_delta_p_form_e(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_p_form_e`."""
    return (pl.col(N))


def calc_a_x_y_form_e(k: float, omega: float, s: float, theta: float, w: float, x: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_05895.

    **Source**:
    - Title: Residual Reinforcement Learning for Waste-Container Lifting Using Large-Scale Cranes with Underactuated Tools (2026)
    - Authors: Qi Li, Karsten Berns
    - Citation Key: `arxiv_2602_05895`

    **KaTeX Formula**:
    $$
    axy = ws k\theta   \theta x + k\omega   \theta x k\theta   \theta y + k\omega   \theta y 0  ,  \theta k+1 xy = (1-\alpha ) \theta kxy +\alpha \theta kxy ,  \theta k+1 xy = (1-\alpha )  \theta kxy + \alpha   \theta kxy
    $$

    Args:
        k (float): Input parameter `k`.
        omega (float): Input parameter `omega`.
        s (float): Input parameter `s`.
        theta (float): Input parameter `theta`.
        w (float): Input parameter `w`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(k**2*omega*theta**3*x*y + k*s*theta**2*w*x)


def expr_a_x_y_form_e(k: str = "k", omega: str = "omega", s: str = "s", theta: str = "theta", w: str = "w", x: str = "x", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_x_y_form_e`."""
    return (pl.col(k)**2*pl.col(omega)*pl.col(theta)**3*pl.col(x)*pl.col(y) + pl.col(k)*pl.col(s)*pl.col(theta)**2*pl.col(w)*pl.col(x))


def calc_val_2610_01307_form_e(E: float, S: float, alpha: float, d: float, dagger: float, n: float, sim: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    ES\dagger [n]{|||\sim h\dagger [n]|||2} =d-\sim \alpha  \dagger  [n] ES\dagger [n] [ M\sum  m=1 I\sum  i=1 q\dagger ,m,i[n]] (17) =d-\sim \alpha  \dagger  [n] ES\dagger [n][ M\sum  m=1 I\sum  i=1 \beta \dagger ,m,i[n] \times G( \sim  \theta tx,\dagger ,m,i[n])G( \sim  \theta rx,\dagger ,m,i[n])]
    $$

    Args:
        E (float): Input parameter `E`.
        S (float): Input parameter `S`.
        alpha (float): Input parameter `alpha`.
        d (float): Input parameter `d`.
        dagger (float): Input parameter `dagger`.
        n (float): Input parameter `n`.
        sim (float): Input parameter `sim`.

    Returns:
        float: Calculated metric value.
    """
    return float(d - sim*alpha*(dagger*(n*(E*(S*(dagger*n))))))


def expr_val_2610_01307_form_e(E: str = "E", S: str = "S", alpha: str = "alpha", d: str = "d", dagger: str = "dagger", n: str = "n", sim: str = "sim") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_01307_form_e`."""
    return (pl.col(d) - pl.col(sim)*pl.col(alpha)*(pl.col(dagger)*(pl.col(n)*(pl.col(E)*(pl.col(S)*(pl.col(dagger)*pl.col(n)))))))


def calc_v_n_1_form_e(a: float, delta: float, n: float, t: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    v[n+1]=v[n]+a[n]\delta t, \forall n \in  N \{N}, (40e)
    $$

    Args:
        a (float): Input parameter `a`.
        delta (float): Input parameter `delta`.
        n (float): Input parameter `n`.
        t (float): Input parameter `t`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*delta*n*t + n*v)


def expr_v_n_1_form_e(a: str = "a", delta: str = "delta", n: str = "n", t: str = "t", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_n_1_form_e`."""
    return (pl.col(a)*pl.col(delta)*pl.col(n)*pl.col(t) + pl.col(n)*pl.col(v))


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
    return float(20*z + 100)


def expr_i_n_de_x_2603_2(z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_n_de_x_2603_2`."""
    return (20*pl.col(z) + 100)


def calc_m_o_e_x_form_b(n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_28223.

    **Source**:
    - Title: Local Inference of LLMs on Long Contexts: A Data Systems Perspective (2026)
    - Authors: Mattias Dürrmeier, Alberto Lerner
    - Citation Key: `arxiv_2610_28223`

    **KaTeX Formula**:
    $$
    MoE(x) = n\sum  i G(x)iEi (x) G(x) = softmax(TopK(xWg), k)
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(n)


def expr_m_o_e_x_form_b(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_o_e_x_form_b`."""
    return (pl.col(n))


def calc_i_l_form_b(L: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_28993.

    **Source**:
    - Title: Digital Quantum Simulation of Dynamics in Interacting Fields (2026)
    - Authors: Zhiyao Li
    - Citation Key: `arxiv_2610_28993`

    **KaTeX Formula**:
    $$
    IL = 1L (1- |\langle \psi var|\psi target\rangle |2)
    $$

    Args:
        L (float): Input parameter `L`.

    Returns:
        float: Calculated metric value.
    """
    return float(L)


def expr_i_l_form_b(L: str = "L") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_l_form_b`."""
    return (pl.col(L))


def calc_d_omega_2_pi_v_form_4(C: float, D: float, L: float, M: float, alpha: float, e: float, k: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    (\omega /2\pi )*d/V = e*kx-2 *CM\alpha *CD\alpha /(CL\alpha  + CD0)2
    $$

    Args:
        C (float): Input parameter `C`.
        D (float): Input parameter `D`.
        L (float): Input parameter `L`.
        M (float): Input parameter `M`.
        alpha (float): Input parameter `alpha`.
        e (float): Input parameter `e`.
        k (float): Input parameter `k`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(-C*D*M*alpha/L + e*k*x)


def expr_d_omega_2_pi_v_form_4(C: str = "C", D: str = "D", L: str = "L", M: str = "M", alpha: str = "alpha", e: str = "e", k: str = "k", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_omega_2_pi_v_form_4`."""
    return (-pl.col(C)*pl.col(D)*pl.col(M)*pl.col(alpha)/pl.col(L) + pl.col(e)*pl.col(k)*pl.col(x))


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
    return float(-B*c*f*t*z)


def expr_p_brier_(B: str = "B", c: str = "c", f: str = "f", t: str = "t", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_brier_`."""
    return (-pl.col(B)*pl.col(c)*pl.col(f)*pl.col(t)*pl.col(z))


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
    return float(-i*p + l)


def expr_p_t_brier_(i: str = "i", l: str = "l", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_t_brier_`."""
    return (-pl.col(i)*pl.col(p) + pl.col(l))


def calc_log_c_theta_theta_c_1_e_beyond(P: float, S: float, beta: float, c: float, gamma: float) -> float:
    r"""Compute mathematical metric extracted from beyond_runs_expectancy_jsm2014.

    **Source**:
    - Title: 311431_85069
    - Authors: Scientific Literature
    - Citation Key: `beyond_runs_expectancy_jsm2014`

    **KaTeX Formula**:
    $$
    \log ( \theta c 1 - \theta c ) = \gamma c + SP \times  \beta
    $$

    Args:
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.
        beta (float): Input parameter `beta`.
        c (float): Input parameter `c`.
        gamma (float): Input parameter `gamma`.

    Returns:
        float: Calculated metric value.
    """
    return float(beta*(P*S) + c*gamma)


def expr_log_c_theta_theta_c_1_e_beyond(P: str = "P", S: str = "S", beta: str = "beta", c: str = "c", gamma: str = "gamma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_log_c_theta_theta_c_1_e_beyond`."""
    return (pl.col(beta)*(pl.col(P)*pl.col(S)) + pl.col(c)*pl.col(gamma))


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
    return float(-U*i + 1)


def expr_p_i_brown_(U: str = "U", i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_brown_`."""
    return (-pl.col(U)*pl.col(i) + 1)


def calc_m_q_q_form_5(M: float, N: float, T: float, c: float, m: float, u: float, v: float, w: float) -> float:
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
    return float(m*(u*(N*(T*(w*(N*w))))) + (M*c + m*(u*(N*(T*(v*(N*v)))))))


def expr_m_q_q_form_5(M: str = "M", N: str = "N", T: str = "T", c: str = "c", m: str = "m", u: str = "u", v: str = "v", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_q_q_form_5`."""
    return (pl.col(m)*(pl.col(u)*(pl.col(N)*(pl.col(T)*(pl.col(w)*(pl.col(N)*pl.col(w)))))) + (pl.col(M)*pl.col(c) + pl.col(m)*(pl.col(u)*(pl.col(N)*(pl.col(T)*(pl.col(v)*(pl.col(N)*pl.col(v))))))))


def calc_gamma_form_b(R_A: float, R_S: float) -> float:
    r"""Compute mathematical metric extracted from tango_pythagenpat_glossary.

    **Source**:
    - Title: Tom Tango: Pythagenpat Win Expectancy (2026)
    - Authors: Tom Tango
    - Citation Key: `tango_pythagenpat_glossary`

    **KaTeX Formula**:
    $$
    \gamma = (R_{S} + R_{A})^{0.285}
    $$

    Args:
        R_A (float): Input parameter `R_A`.
        R_S (float): Input parameter `R_S`.

    Returns:
        float: Calculated metric value.
    """
    return float((R_A + R_S)**0.285)


def expr_gamma_form_b(R_A: str = "R_A", R_S: str = "R_S") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_gamma_form_b`."""
    return ((pl.col(R_A) + pl.col(R_S))**0.285)


def calc_bt_secondary_many_routes_2023_bt_sec(g: float, i: float, k: float, l: float, o: float, p: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    log pij pji + log pjk pkj = log pik pki .
    $$

    Args:
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        k (float): Input parameter `k`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(g*i**2*k**2*l*o*p**2)


def expr_bt_secondary_many_routes_2023_bt_sec(g: str = "g", i: str = "i", k: str = "k", l: str = "l", o: str = "o", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_bt_secondary_many_routes_2023_bt_sec`."""
    return (pl.col(g)*pl.col(i)**2*pl.col(k)**2*pl.col(l)*pl.col(o)*pl.col(p)**2)


def calc_sigma_a_a_sigma_form_7(A: float, B: float, N: float, a: float, b: float, i: float, n: float, r: float, sigma: float, t: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    \sigma A\sigma A = Ntrain 1 \sigma 2A - 3 \sigma 4A yaB-1 ab yb, (59) W -1 \sigma A\Lambda  = -1 \Lambda 3\sigma 3A ya (B-1B'B-1 )ab yb, W -1 \Lambda \Lambda  = 1 2 d2 d\Lambda 2 \ln(|B|) + 1 2\sigma 2A\Lambda 6 ya (2B-1B'B-1B'B-1 - B-1B''B-1 )ab yb + 3 2\sigma 2A\Lambda 4 ya (B-1B'B-1 )ab yb
    $$

    Args:
        A (float): Input parameter `A`.
        B (float): Input parameter `B`.
        N (float): Input parameter `N`.
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.
        sigma (float): Input parameter `sigma`.
        t (float): Input parameter `t`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(-1*a*(b*(b*y)) + (N*(t*(r*(a*(i*(n*(1*((2*A)*sigma))))))) - 3*sigma*(4*(A*(y*(B*a))))))


def expr_sigma_a_a_sigma_form_7(A: str = "A", B: str = "B", N: str = "N", a: str = "a", b: str = "b", i: str = "i", n: str = "n", r: str = "r", sigma: str = "sigma", t: str = "t", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sigma_a_a_sigma_form_7`."""
    return (-1*pl.col(a)*(pl.col(b)*(pl.col(b)*pl.col(y))) + (pl.col(N)*(pl.col(t)*(pl.col(r)*(pl.col(a)*(pl.col(i)*(pl.col(n)*(1*((2*pl.col(A))*pl.col(sigma)))))))) - 3*pl.col(sigma)*(4*(pl.col(A)*(pl.col(y)*(pl.col(B)*pl.col(a)))))))


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
    return float(2*x)


def expr_f_x_bt_sec(x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_x_bt_sec`."""
    return (2*pl.col(x))


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


def expr_p_i_j_bt_sec(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_j_bt_sec`."""
    return (pl.col(P))


def calc_l_m_e_l_form_0(F: float, M: float, T: float, a: float, di: float, o: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_00735.

    **Source**:
    - Title: Articulatory Source-Filter TTS: Physically Grounded Control through Vocal Tract Kinematics (2026)
    - Authors: Jesuraj Bandekar, Shinji Watanabe, Prasanta Kumar Ghosh
    - Citation Key: `arxiv_2610_00735`

    **KaTeX Formula**:
    $$
    Lmel = 1 T |M- Maudio|2F
    $$

    Args:
        F (float): Input parameter `F`.
        M (float): Input parameter `M`.
        T (float): Input parameter `T`.
        a (float): Input parameter `a`.
        di (float): Input parameter `di`.
        o (float): Input parameter `o`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*F*T*abs(M*a*di*o*u - M))


def expr_l_m_e_l_form_0(F: str = "F", M: str = "M", T: str = "T", a: str = "a", di: str = "di", o: str = "o", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_m_e_l_form_0`."""
    return (2*pl.col(F)*pl.col(T)*abs(pl.col(M)*pl.col(a)*pl.col(di)*pl.col(o)*pl.col(u) - pl.col(M)))


def calc_y_n_w_form_0(n: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    yw[n] = nw[n], H0, \sqrt PtG20  Fw[n] ( \lambda  4\pi  )2 x[n] +nw[n], H1
    $$

    Args:
        n (float): Input parameter `n`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(n**2*w)


def expr_y_n_w_form_0(n: str = "n", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_y_n_w_form_0`."""
    return (pl.col(n)**2*pl.col(w))


def calc_p_n_1_form_0(a: float, delta: float, n: float, p: float, t: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    p[n + 1] = p[n] + v[n]\delta t + 12 a[n]\delta 2 t , \forall n \in  N \ {N}
    $$

    Args:
        a (float): Input parameter `a`.
        delta (float): Input parameter `delta`.
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.
        t (float): Input parameter `t`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(24*a*delta*n*t + delta*n*t*v + n*p)


def expr_p_n_1_form_0(a: str = "a", delta: str = "delta", n: str = "n", p: str = "p", t: str = "t", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_n_1_form_0`."""
    return (24*pl.col(a)*pl.col(delta)*pl.col(n)*pl.col(t) + pl.col(delta)*pl.col(n)*pl.col(t)*pl.col(v) + pl.col(n)*pl.col(p))


def calc_d_n_form_0(L: float, gamma: float, n: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    D[n] = L [\ln (1+\gamma w[n]) - \gamma w[n] 1 + \gamma w[n] ]
    $$

    Args:
        L (float): Input parameter `L`.
        gamma (float): Input parameter `gamma`.
        n (float): Input parameter `n`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(L*(gamma*(n*w) + (-gamma*w*(1*n) + math.log(gamma*(n*w) + 1, math.e))))


def expr_d_n_form_0(L: str = "L", gamma: str = "gamma", n: str = "n", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_n_form_0`."""
    return (pl.col(L)*(pl.col(gamma)*(pl.col(n)*pl.col(w)) + (-pl.col(gamma)*pl.col(w)*(1*pl.col(n)) + (pl.col(gamma).log()*(pl.col(n)*pl.col(w)) + 1, math.e))))


def calc_c_f_m_theta_l_o_t_form_0(E: float, tau: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_00735.

    **Source**:
    - Title: Articulatory Source-Filter TTS: Physically Grounded Control through Vocal Tract Kinematics (2026)
    - Authors: Jesuraj Bandekar, Shinji Watanabe, Prasanta Kumar Ghosh
    - Citation Key: `arxiv_2610_00735`

    **KaTeX Formula**:
    $$
    LOT-CFM(\theta ) = E\tau ,x0,x1 [ |(x1 - x0) - v\tau  (\phi \tau  (x); \theta , c)|2 ]
    $$

    Args:
        E (float): Input parameter `E`.
        tau (float): Input parameter `tau`.

    Returns:
        float: Calculated metric value.
    """
    return float(E*tau)


def expr_c_f_m_theta_l_o_t_form_0(E: str = "E", tau: str = "tau") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_f_m_theta_l_o_t_form_0`."""
    return (pl.col(E)*pl.col(tau))


def calc_sigma_2_theta_form_2(Omega: float, R: float, kappa: float, sigma: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18161.

    **Source**:
    - Title: In-depth analysis of bar formation mechanisms of disk galaxies in halos of different concentrations (2026)
    - Authors: T. Worrakitpoonpon
    - Citation Key: `arxiv_2601_18161`

    **KaTeX Formula**:
    $$
    \sigma 2 \theta  = \kappa 2 4\Omega 2 \sigma 2R
    $$

    Args:
        Omega (float): Input parameter `Omega`.
        R (float): Input parameter `R`.
        kappa (float): Input parameter `kappa`.
        sigma (float): Input parameter `sigma`.

    Returns:
        float: Calculated metric value.
    """
    return float(96*Omega*R*kappa*sigma)


def expr_sigma_2_theta_form_2(Omega: str = "Omega", R: str = "R", kappa: str = "kappa", sigma: str = "sigma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sigma_2_theta_form_2`."""
    return (96*pl.col(Omega)*pl.col(R)*pl.col(kappa)*pl.col(sigma))


def calc_m_a_u_di_o_form_2(M: float, c: float, e: float, f: float, l: float, r: float, s: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_00735.

    **Source**:
    - Title: Articulatory Source-Filter TTS: Physically Grounded Control through Vocal Tract Kinematics (2026)
    - Authors: Jesuraj Bandekar, Shinji Watanabe, Prasanta Kumar Ghosh
    - Citation Key: `arxiv_2610_00735`

    **KaTeX Formula**:
    $$
    Maudio = Mres src + Mflt
    $$

    Args:
        M (float): Input parameter `M`.
        c (float): Input parameter `c`.
        e (float): Input parameter `e`.
        f (float): Input parameter `f`.
        l (float): Input parameter `l`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(M*c*e*r**2*s**2 + M*f*l*t)


def expr_m_a_u_di_o_form_2(M: str = "M", c: str = "c", e: str = "e", f: str = "f", l: str = "l", r: str = "r", s: str = "s", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_a_u_di_o_form_2`."""
    return (pl.col(M)*pl.col(c)*pl.col(e)*pl.col(r)**2*pl.col(s)**2 + pl.col(M)*pl.col(f)*pl.col(l)*pl.col(t))


def calc_i_k_p_i_2103_1(gamma: float, i: float, k: float, r: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from 2103_12094.

    **Source**:
    - Title: Modelling intransitivity in pairwise comparisons with application to baseball data (2021)
    - Authors: Jess Spearing, Jonathan Tawn, David Irons et al.
    - Citation Key: `2103_12094`

    **KaTeX Formula**:
    $$
    p(i) ik = 1 1+ \exp[-(\theta ik +\gamma  + ri - rk)] , and p(i) ki = 1-p(i) ik \forall i ̸= k \in  I
    $$

    Args:
        gamma (float): Input parameter `gamma`.
        i (float): Input parameter `i`.
        k (float): Input parameter `k`.
        r (float): Input parameter `r`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.exp(-gamma - i*r + k*r - theta*i*k) + 11)


def expr_i_k_p_i_2103_1(gamma: str = "gamma", i: str = "i", k: str = "k", r: str = "r", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_k_p_i_2103_1`."""
    return ((-pl.col(gamma).exp() - pl.col(i)*pl.col(r) + pl.col(k)*pl.col(r) - pl.col(theta)*pl.col(i)*pl.col(k)) + 11)


def calc_r_b_n_form_2(g: float, l: float, o: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    Rb[n] = log2 (1 + \rho 0  Fb[n])
    $$

    Args:
        g (float): Input parameter `g`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*g*l*o)


def expr_r_b_n_form_2(g: str = "g", l: str = "l", o: str = "o") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_b_n_form_2`."""
    return (2*pl.col(g)*pl.col(l)*pl.col(o))


def calc_l_p_c_c_form_3(K: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_00735.

    **Source**:
    - Title: Articulatory Source-Filter TTS: Physically Grounded Control through Vocal Tract Kinematics (2026)
    - Authors: Jesuraj Bandekar, Shinji Watanabe, Prasanta Kumar Ghosh
    - Citation Key: `arxiv_2610_00735`

    **KaTeX Formula**:
    $$
    LPCC = 1K K\sum  k=1 (1 - \rho (ak, \sim ak))
    $$

    Args:
        K (float): Input parameter `K`.

    Returns:
        float: Calculated metric value.
    """
    return float(K**2)


def expr_l_p_c_c_form_3(K: str = "K") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_p_c_c_form_3`."""
    return (pl.col(K)**2)


def calc_m_a_u_di_o_form_3(M: float, c: float, f: float, l: float, r: float, s: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_00735.

    **Source**:
    - Title: Articulatory Source-Filter TTS: Physically Grounded Control through Vocal Tract Kinematics (2026)
    - Authors: Jesuraj Bandekar, Shinji Watanabe, Prasanta Kumar Ghosh
    - Citation Key: `arxiv_2610_00735`

    **KaTeX Formula**:
    $$
    Maudio = Msrc + Mflt
    $$

    Args:
        M (float): Input parameter `M`.
        c (float): Input parameter `c`.
        f (float): Input parameter `f`.
        l (float): Input parameter `l`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(M*c*r*s + M*f*l*t)


def expr_m_a_u_di_o_form_3(M: str = "M", c: str = "c", f: str = "f", l: str = "l", r: str = "r", s: str = "s", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_a_u_di_o_form_3`."""
    return (pl.col(M)*pl.col(c)*pl.col(r)*pl.col(s) + pl.col(M)*pl.col(f)*pl.col(l)*pl.col(t))


def calc_t_t_form_3(T: float, w: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_04871.

    **Source**:
    - Title: A Multidimensional Model for Quantifying Tonal Strength: A Continuous Framework of Analyzing Tonal Evolution Beyond Tonal-Atonal Binary Classification (2026)
    - Authors: Yuliang Li, Nan Nan, Meilian Gu et al.
    - Citation Key: `arxiv_2610_04871`

    **KaTeX Formula**:
    $$
    TT = wwTTzz, ww = ΣΣ -1λλ
    $$

    Args:
        T (float): Input parameter `T`.
        w (float): Input parameter `w`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(T**2*w**2*z**2)


def expr_t_t_form_3(T: str = "T", w: str = "w", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_t_form_3`."""
    return (pl.col(T)**2*pl.col(w)**2*pl.col(z)**2)


def calc_delta_t_0_form_4(Delta: float, P: float, b: float, phi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2604_25278.

    **Source**:
    - Title: The GMRT High-Resolution Southern Sky Survey for pulsars and transients -- VIII: Orbital Variability and the Evolution of a 1-Day He-WD Millisecond Pulsar J2101-4802 (2026)
    - Authors: Ankita Ghosh, Bhaswati Bhattacharyya, David L. Kaplan et al.
    - Citation Key: `arxiv_2604_25278`

    **KaTeX Formula**:
    $$
    \Delta T0 = \Delta \phi  \times  Pb
    $$

    Args:
        Delta (float): Input parameter `Delta`.
        P (float): Input parameter `P`.
        b (float): Input parameter `b`.
        phi (float): Input parameter `phi`.

    Returns:
        float: Calculated metric value.
    """
    return float(Delta*P*b*phi)


def expr_delta_t_0_form_4(Delta: str = "Delta", P: str = "P", b: str = "b", phi: str = "phi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_t_0_form_4`."""
    return (pl.col(Delta)*pl.col(P)*pl.col(b)*pl.col(phi))


def calc_omega_i_form_4(Omega: float, kappa: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18161.

    **Source**:
    - Title: In-depth analysis of bar formation mechanisms of disk galaxies in halos of different concentrations (2026)
    - Authors: T. Worrakitpoonpon
    - Citation Key: `arxiv_2601_18161`

    **KaTeX Formula**:
    $$
    \Omega i = \Omega  - \kappa 2
    $$

    Args:
        Omega (float): Input parameter `Omega`.
        kappa (float): Input parameter `kappa`.

    Returns:
        float: Calculated metric value.
    """
    return float(Omega - 2*kappa)


def expr_omega_i_form_4(Omega: str = "Omega", kappa: str = "kappa") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_omega_i_form_4`."""
    return (pl.col(Omega) - 2*pl.col(kappa))


def calc_partial_l_mu_partial_2209_0(P: float) -> float:
    r"""Compute mathematical metric extracted from 2209_07274.

    **Source**:
    - Title: Introducing Grid WAR: Rethinking WAR for Starting Pitchers (2022)
    - Authors: Ryan S. Brill, Abraham J. Wyner
    - Citation Key: `2209_07274`

    **KaTeX Formula**:
    $$
    \partial  l \partial \mu  =- P\sum  p=1 1 2(\tau  2 + \sigma  2 p) Np\sum  g=1 2(Xpg - \mu ) = 0
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(-P)


def expr_partial_l_mu_partial_2209_0(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_partial_l_mu_partial_2209_0`."""
    return (-pl.col(P))


def calc_partial_l_partial_2_p_sigma_2209_0(N: float, p: float) -> float:
    r"""Compute mathematical metric extracted from 2209_07274.

    **Source**:
    - Title: Introducing Grid WAR: Rethinking WAR for Starting Pitchers (2022)
    - Authors: Ryan S. Brill, Abraham J. Wyner
    - Citation Key: `2209_07274`

    **KaTeX Formula**:
    $$
    \partial  l \partial \sigma  2 p = - 1 2 Np\sum  g=1 1 \tau  2 +\sigma  2 p + 1 2 Np\sum  g=1 (Xpg - \mu )2 (\tau  2 + \sigma  2 p)2
    $$

    Args:
        N (float): Input parameter `N`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(-12*N*p)


def expr_partial_l_partial_2_p_sigma_2209_0(N: str = "N", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_partial_l_partial_2_p_sigma_2209_0`."""
    return (-12*pl.col(N)*pl.col(p))


def calc_i_x_form_5(J: float, i: float, nu: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_13304.

    **Source**:
    - Title: Humanoid Robot Running Through Random Stepping Stones and Jumping Over Obstacles: Step Adaptation Using Spring-Mass Trajectories (2025)
    - Authors: Sait Sovukluk, Johannes Englsberger, Christian Ott
    - Citation Key: `arxiv_2512_13304`

    **KaTeX Formula**:
    $$
    xi = Ji\nu
    $$

    Args:
        J (float): Input parameter `J`.
        i (float): Input parameter `i`.
        nu (float): Input parameter `nu`.

    Returns:
        float: Calculated metric value.
    """
    return float(J*i*nu)


def expr_i_x_form_5(J: str = "J", i: str = "i", nu: str = "nu") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_x_form_5`."""
    return (pl.col(J)*pl.col(i)*pl.col(nu))


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
    return float(12*P*g*l*o)


def expr_f_x_form_5(P: str = "P", g: str = "g", l: str = "l", o: str = "o") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_x_form_5`."""
    return (12*pl.col(P)*pl.col(g)*pl.col(l)*pl.col(o))


def calc_n_omega_form_5(a: float, g: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    \omega [n] = a[n] +g |a[n] +g| , \forall n \in  N, (40i)
    $$

    Args:
        a (float): Input parameter `a`.
        g (float): Input parameter `g`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*n + g*abs(a*n + g))


def expr_n_omega_form_5(a: str = "a", g: str = "g", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_n_omega_form_5`."""
    return (pl.col(a)*pl.col(n) + pl.col(g)*abs(pl.col(a)*pl.col(n) + pl.col(g)))


def calc_lambda_o_v_e_r_a_l_l_2501_0(L: float) -> float:
    r"""Compute mathematical metric extracted from 2501_09153.

    **Source**:
    - Title: Layered Dirichlet Modeling to Assess the Changing Contributions of MLB Players as they Age (2025)
    - Authors: Monnie McGee, Jacob Turner, Bianca Luedeker
    - Citation Key: `2501_09153`

    **KaTeX Formula**:
    $$
    \Lambda overall = L\sum  l=1 \Lambda l \sim  \chi 2v
    $$

    Args:
        L (float): Input parameter `L`.

    Returns:
        float: Calculated metric value.
    """
    return float(L)


def expr_lambda_o_v_e_r_a_l_l_2501_0(L: str = "L") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_lambda_o_v_e_r_a_l_l_2501_0`."""
    return (pl.col(L))


def calc_l_w_o_k_r_form_4(T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_20558.

    **Source**:
    - Title: Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction (2026)
    - Authors: Songyang Liu, Shuai Li
    - Citation Key: `arxiv_2609_20558`

    **KaTeX Formula**:
    $$
    Lwork = T\sum  t=1 c work t      pℎ   qt , p r t   - p * ℎ,t       2 2
    $$

    Args:
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(T)


def expr_l_w_o_k_r_form_4(T: str = "T") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_w_o_k_r_form_4`."""
    return (pl.col(T))


def calc_l_m_e_s_form_8(K: float, T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_00735.

    **Source**:
    - Title: Articulatory Source-Filter TTS: Physically Grounded Control through Vocal Tract Kinematics (2026)
    - Authors: Jesuraj Bandekar, Shinji Watanabe, Prasanta Kumar Ghosh
    - Citation Key: `arxiv_2610_00735`

    **KaTeX Formula**:
    $$
    LMSE = 1 TK T\sum  t=1 K\sum  k=1 (at,k - \sim at,k)2
    $$

    Args:
        K (float): Input parameter `K`.
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(T*(K*T)))


def expr_l_m_e_s_form_8(K: str = "K", T: str = "T") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_m_e_s_form_8`."""
    return (1*(pl.col(T)*(pl.col(K)*pl.col(T))))


def calc_l_du_r_form_8(L: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_00735.

    **Source**:
    - Title: Articulatory Source-Filter TTS: Physically Grounded Control through Vocal Tract Kinematics (2026)
    - Authors: Jesuraj Bandekar, Shinji Watanabe, Prasanta Kumar Ghosh
    - Citation Key: `arxiv_2610_00735`

    **KaTeX Formula**:
    $$
    Ldur = 1L L\sum  i=1 (\log di - \log  di)2
    $$

    Args:
        L (float): Input parameter `L`.

    Returns:
        float: Calculated metric value.
    """
    return float(L**2)


def expr_l_du_r_form_8(L: str = "L") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_du_r_form_8`."""
    return (pl.col(L)**2)


def calc_a_t_c_p_form_b(k: float, omega: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_05895.

    **Source**:
    - Title: Residual Reinforcement Learning for Waste-Container Lifting Using Large-Scale Cranes with Underactuated Tools (2026)
    - Authors: Qi Li, Karsten Berns
    - Citation Key: `arxiv_2602_05895`

    **KaTeX Formula**:
    $$
    aTCP = k\theta \theta  + k\omega   \theta
    $$

    Args:
        k (float): Input parameter `k`.
        omega (float): Input parameter `omega`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(k*omega*theta + k*theta**2)


def expr_a_t_c_p_form_b(k: str = "k", omega: str = "omega", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_t_c_p_form_b`."""
    return (pl.col(k)*pl.col(omega)*pl.col(theta) + pl.col(k)*pl.col(theta)**2)


def calc_p_b_form_b(D: float, G: float, P: float, T: float, W: float, b: float, m: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2604_25278.

    **Source**:
    - Title: The GMRT High-Resolution Southern Sky Survey for pulsars and transients -- VIII: Orbital Variability and the Evolution of a 1-Day He-WD Millisecond Pulsar J2101-4802 (2026)
    - Authors: Ankita Ghosh, Bhaswati Bhattacharyya, David L. Kaplan et al.
    - Citation Key: `arxiv_2604_25278`

    **KaTeX Formula**:
    $$
    Pb = P m b + P T b + P D b + P GW b
    $$

    Args:
        D (float): Input parameter `D`.
        G (float): Input parameter `G`.
        P (float): Input parameter `P`.
        T (float): Input parameter `T`.
        W (float): Input parameter `W`.
        b (float): Input parameter `b`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(D*P*b + G*P*W*b + P*T*b + P*b*m)


def expr_p_b_form_b(D: str = "D", G: str = "G", P: str = "P", T: str = "T", W: str = "W", b: str = "b", m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_b_form_b`."""
    return (pl.col(D)*pl.col(P)*pl.col(b) + pl.col(G)*pl.col(P)*pl.col(W)*pl.col(b) + pl.col(P)*pl.col(T)*pl.col(b) + pl.col(P)*pl.col(b)*pl.col(m))


def calc_p_form_c(p: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_04813.

    **Source**:
    - Title: A Markov Chain Approach to Modeling Rugby Union (2026)
    - Authors: Kenny Watts, Jonathan Pipping-Gamón
    - Citation Key: `arxiv_2610_04813`

    **KaTeX Formula**:
    $$
    P =  ps1,s1 ps1,s2 \cdot  \cdot  \cdot  ps1, PC ps1, S3 ps1, S5 \cdot  \cdot  \cdot  ps2,s1 ps2,s2 \cdot  \cdot  \cdot  ps2, PC ps2, S3 ps2, S5 \cdot  \cdot  \cdot  . . . . . . . . . . . . . . . . . . . . . psn,s1 psn,s2 \cdot  \cdot  \cdot  psn, PC psn, S3 psn, S5 \cdot  \cdot  \cdot
    $$

    Args:
        p (float): Input parameter `p`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(p*s)


def expr_p_form_c(p: str = "p", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_form_c`."""
    return (pl.col(p)*pl.col(s))


def calc_n_omega_form_d(a: float, g: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    \omega [n] = a[n] +g |a[n] + g|
    $$

    Args:
        a (float): Input parameter `a`.
        g (float): Input parameter `g`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*n + g*abs(a*n + g))


def expr_n_omega_form_d(a: str = "a", g: str = "g", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_n_omega_form_d`."""
    return (pl.col(a)*pl.col(n) + pl.col(g)*abs(pl.col(a)*pl.col(n) + pl.col(g)))


def calc_k_d_d_x_x_r_e_f_d_d_dv_m_d_dv_form_d(F: float, c: float, d: float, m: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_05895.

    **Source**:
    - Title: Residual Reinforcement Learning for Waste-Container Lifting Using Large-Scale Cranes with Underactuated Tools (2026)
    - Authors: Qi Li, Karsten Berns
    - Citation Key: `arxiv_2602_05895`

    **KaTeX Formula**:
    $$
    Md vd + Ddvd + Kd(xd - xref ) = Fcmd, vk+1 d = satvmax (vk d +\Delta t vk d )
    $$

    Args:
        F (float): Input parameter `F`.
        c (float): Input parameter `c`.
        d (float): Input parameter `d`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(F*c*d*m)


def expr_k_d_d_x_x_r_e_f_d_d_dv_m_d_dv_form_d(F: str = "F", c: str = "c", d: str = "d", m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_d_d_x_x_r_e_f_d_d_dv_m_d_dv_form_d`."""
    return (pl.col(F)*pl.col(c)*pl.col(d)*pl.col(m))


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
    return float(C**3*W**3*x*y*z)


def expr_w_c_r_form_1(C: str = "C", W: str = "W", x: str = "x", y: str = "y", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_c_r_form_1`."""
    return (pl.col(C)**3*pl.col(W)**3*pl.col(x)*pl.col(y)*pl.col(z))


def calc_p_n_1_form_e(a: float, delta: float, n: float, p: float, t: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    p[n+1]=p[n]+v[n]\delta t+12 a[n]\delta 2 t ,\forall n\in N\{N},(40d)
    $$

    Args:
        a (float): Input parameter `a`.
        delta (float): Input parameter `delta`.
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.
        t (float): Input parameter `t`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(24*a*delta*n*t + delta*n*t*v + n*p)


def expr_p_n_1_form_e(a: str = "a", delta: str = "delta", n: str = "n", p: str = "p", t: str = "t", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_n_1_form_e`."""
    return (24*pl.col(a)*pl.col(delta)*pl.col(n)*pl.col(t) + pl.col(delta)*pl.col(n)*pl.col(t)*pl.col(v) + pl.col(n)*pl.col(p))


def calc_f_s_p_y_form_e(e: float, n: float, p: float, t: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2005_07742.

    **Source**:
    - Title: SEAM methodology for context-rich player matchup evaluations (2020)
    - Authors: Julia Wapner, David Dalpiaz, Daniel J. Eck
    - Citation Key: `arxiv_2005_07742`

    **KaTeX Formula**:
    $$
    fsp(y) = ntype \sum  t=1 \rho t  fsp,t(y|xb,t),  fsb(y) = ntype \sum  t=1 \rho t  fsb,t(y|xp,t)
    $$

    Args:
        e (float): Input parameter `e`.
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.
        t (float): Input parameter `t`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(e*n*p*t*y)


def expr_f_s_p_y_form_e(e: str = "e", n: str = "n", p: str = "p", t: str = "t", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_s_p_y_form_e`."""
    return (pl.col(e)*pl.col(n)*pl.col(p)*pl.col(t)*pl.col(y))


def calc_a_form_b(B_B: float, H: float, H_R: float) -> float:
    r"""Compute mathematical metric extracted from tango_base_runs_glossary.

    **Source**:
    - Title: Base Runs (BsR) Offensive Estimator (2026)
    - Authors: David Smyth, Tom Tango
    - Citation Key: `tango_base_runs_glossary`

    **KaTeX Formula**:
    $$
    A = H + B_{B} - H_{R}
    $$

    Args:
        B_B (float): Input parameter `B_B`.
        H (float): Input parameter `H`.
        H_R (float): Input parameter `H_R`.

    Returns:
        float: Calculated metric value.
    """
    return float(-H_R + (B_B + H))


def expr_a_form_b(B_B: str = "B_B", H: str = "H", H_R: str = "H_R") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_form_b`."""
    return (-pl.col(H_R) + (pl.col(B_B) + pl.col(H)))


def calc_e_p_z_d_f_e_p_d_z_p_f_2602_2(P: float) -> float:
    r"""Compute mathematical metric extracted from 2602_23233.

    **Source**:
    - Title: The Counterfactual Combine: A Causal Framework for Player Evaluation (2026)
    - Authors: Herbert P. Susmann, Antonio D'Alessandro
    - Citation Key: `2602_23233`

    **KaTeX Formula**:
    $$
    EP {D(F)(Z)} - EP {DP(F)(Z)} = EP [ 1(X \in  X ' ) F(X \in  X ' ) 1(A = a) F(a) {\theta F - \theta P}] = EP [{ P(X \in  X ' ) F(X \in  X ' ) P(a) F(a) - 1} {\theta F - \theta P}] + \theta P - \theta F
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e*P)


def expr_e_p_z_d_f_e_p_d_z_p_f_2602_2(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_p_z_d_f_e_p_d_z_p_f_2602_2`."""
    return (math.e*pl.col(P))


def calc_u_form_9(x: float, y: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_27423.

    **Source**:
    - Title: High-order stabilized matrix-free simulation of rotating mixing devices using the Mortar Element Method (2026)
    - Authors: B. Campos, P. Munch, V. O. Ferreira et al.
    - Citation Key: `arxiv_2608_27423`

    **KaTeX Formula**:
    $$
    u = 2\pi 2 [-3 \cos(2\pi x) + 2] \sin(\pi y) \sin(\pi z) \cos(\pi y) \cos(\pi z) +\pi [2 \cos(\pi y)2 - \cos(\pi z)2 ] \sin(\pi x)3 \sin(\pi y)2 \sin(\pi z)2 \cos(\pi x)
    $$

    Args:
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(4*math.pi*(2 - 3*math.cos(2*math.pi*x))*math.sin(math.pi*y)*math.sin(math.pi*z)*math.cos(math.pi*y)*math.cos(math.pi*z) + 12*math.pi*(4*math.cos(math.pi*y) - 2*math.cos(math.pi*z))*math.sin(math.pi*x)*math.sin(math.pi*y)*math.sin(math.pi*z)*math.cos(math.pi*x))


def expr_u_form_9(x: str = "x", y: str = "y", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_form_9`."""
    return (4*math.pi*(2 - 3*math.cos(2*math.pi*pl.col(x)))*math.sin(math.pi*pl.col(y))*math.sin(math.pi*pl.col(z))*math.cos(math.pi*pl.col(y))*math.cos(math.pi*pl.col(z)) + 12*math.pi*(4*math.cos(math.pi*pl.col(y)) - 2*math.cos(math.pi*pl.col(z)))*math.sin(math.pi*pl.col(x))*math.sin(math.pi*pl.col(y))*math.sin(math.pi*pl.col(z))*math.cos(math.pi*pl.col(x)))


def calc_w_b_z_form_e(A: float, L: float, P: float, R: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    W zB =  PLA -  PRA |  PLA -  PRA|
    $$

    Args:
        A (float): Input parameter `A`.
        L (float): Input parameter `L`.
        P (float): Input parameter `P`.
        R (float): Input parameter `R`.

    Returns:
        float: Calculated metric value.
    """
    return float(A*L*P - A*P*R*abs(A*L*P - A*P*R))


def expr_w_b_z_form_e(A: str = "A", L: str = "L", P: str = "P", R: str = "R") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_b_z_form_e`."""
    return (pl.col(A)*pl.col(L)*pl.col(P) - pl.col(A)*pl.col(P)*pl.col(R)*abs(pl.col(A)*pl.col(L)*pl.col(P) - pl.col(A)*pl.col(P)*pl.col(R)))


def calc_h_x_form_4(kappa: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    h(x) = \kappa x (\kappa  > 0, x \in  [0, 1])
    $$

    Args:
        kappa (float): Input parameter `kappa`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(kappa*x)


def expr_h_x_form_4(kappa: str = "kappa", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_x_form_4`."""
    return (pl.col(kappa)*pl.col(x))


def calc_v_form_a(x: float, y: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_27423.

    **Source**:
    - Title: High-order stabilized matrix-free simulation of rotating mixing devices using the Mortar Element Method (2026)
    - Authors: B. Campos, P. Munch, V. O. Ferreira et al.
    - Citation Key: `arxiv_2608_27423`

    **KaTeX Formula**:
    $$
    v = 2\pi 2 [-3 \cos(2\pi y) + 2] \sin(\pi x) \sin(\pi z) \cos(\pi x) \cos(\pi z)
    $$

    Args:
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(4*math.pi*(2 - 3*math.cos(2*math.pi*y))*math.sin(math.pi*x)*math.sin(math.pi*z)*math.cos(math.pi*x)*math.cos(math.pi*z))


def expr_v_form_a(x: str = "x", y: str = "y", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_form_a`."""
    return (4*math.pi*(2 - 3*math.cos(2*math.pi*pl.col(y)))*math.sin(math.pi*pl.col(x))*math.sin(math.pi*pl.col(z))*math.cos(math.pi*pl.col(x))*math.cos(math.pi*pl.col(z)))


def calc_r_e_form_a(d: float, i: float, nu: float, omega: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_27423.

    **Source**:
    - Title: High-order stabilized matrix-free simulation of rotating mixing devices using the Mortar Element Method (2026)
    - Authors: B. Campos, P. Munch, V. O. Ferreira et al.
    - Citation Key: `arxiv_2608_27423`

    **KaTeX Formula**:
    $$
    Re = \omega d2i 2\pi \nu
    $$

    Args:
        d (float): Input parameter `d`.
        i (float): Input parameter `i`.
        nu (float): Input parameter `nu`.
        omega (float): Input parameter `omega`.

    Returns:
        float: Calculated metric value.
    """
    return float(4*math.pi*d*i*nu*omega)


def expr_r_e_form_a(d: str = "d", i: str = "i", nu: str = "nu", omega: str = "omega") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_e_form_a`."""
    return (4*math.pi*pl.col(d)*pl.col(i)*pl.col(nu)*pl.col(omega))


def calc_b_v_form_a(a: float, t: float, v: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_26568.

    **Source**:
    - Title: Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games (2026)
    - Authors: Durgam Latha, Dion Reji, Dorde Zikelic et al.
    - Citation Key: `arxiv_2610_26568`

    **KaTeX Formula**:
    $$
    vb = v a xt,1 b1 y1 ⊥y2 b2 \cdot  \cdot  \cdot  yk-1 ⊥xk bk s'
    $$

    Args:
        a (float): Input parameter `a`.
        t (float): Input parameter `t`.
        v (float): Input parameter `v`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*t*v*x)


def expr_b_v_form_a(a: str = "a", t: str = "t", v: str = "v", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_b_v_form_a`."""
    return (pl.col(a)*pl.col(t)*pl.col(v)*pl.col(x))


def calc_f_h_y_form_f(H: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2005_07742.

    **Source**:
    - Title: SEAM methodology for context-rich player matchup evaluations (2020)
    - Authors: Julia Wapner, David Dalpiaz, Daniel J. Eck
    - Citation Key: `arxiv_2005_07742`

    **KaTeX Formula**:
    $$
    fH(y) = 1 n|H| n\sum  i=1 K (H-1 (yi -y)) , y \in  Y
    $$

    Args:
        H (float): Input parameter `H`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(n**2*abs(H))


def expr_f_h_y_form_f(H: str = "H", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_h_y_form_f`."""
    return (pl.col(n)**2*abs(pl.col(H)))


def calc_tau_w_form_f(p: float, r: float, tau: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29565.

    **Source**:
    - Title: Preserving Operator Intent Under Actuation Constraints: Teleoperation of Manipulators with Coupled Transmissions (2026)
    - Authors: Xuhan Miao, Zijin Han, Yutong Shen et al.
    - Citation Key: `arxiv_2610_29565`

    **KaTeX Formula**:
    $$
    \tau w = [\tau p \tau r ]
    $$

    Args:
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.
        tau (float): Input parameter `tau`.

    Returns:
        float: Calculated metric value.
    """
    return float(p*r*tau**2)


def expr_tau_w_form_f(p: str = "p", r: str = "r", tau: str = "tau") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_tau_w_form_f`."""
    return (pl.col(p)*pl.col(r)*pl.col(tau)**2)


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
    return float(i**2*k**2*p**2)


def expr_p_i_j_p_i_j_p_j_k_p_j_k_bt_sec(i: str = "i", k: str = "k", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_j_p_i_j_p_j_k_p_j_k_bt_sec`."""
    return (pl.col(i)**2*pl.col(k)**2*pl.col(p)**2)


def calc_w_i_n_p_c_t_form_c(R_A: float, R_S: float, gamma: float) -> float:
    r"""Compute mathematical metric extracted from tango_pythagenpat_glossary.

    **Source**:
    - Title: Tom Tango: Pythagenpat Win Expectancy (2026)
    - Authors: Tom Tango
    - Citation Key: `tango_pythagenpat_glossary`

    **KaTeX Formula**:
    $$
    WinPct = \frac{R_{S}^\gamma}{R_{S}^\gamma + R_{A}^\gamma}
    $$

    Args:
        R_A (float): Input parameter `R_A`.
        R_S (float): Input parameter `R_S`.
        gamma (float): Input parameter `gamma`.

    Returns:
        float: Calculated metric value.
    """
    return float(R_S**gamma/(R_A**gamma + R_S**gamma))


def expr_w_i_n_p_c_t_form_c(R_A: str = "R_A", R_S: str = "R_S", gamma: str = "gamma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_i_n_p_c_t_form_c`."""
    return (pl.col(R_S)**pl.col(gamma)/(pl.col(R_A)**pl.col(gamma) + pl.col(R_S)**pl.col(gamma)))


def calc_beta_form_c(i: float, l: float, m: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1810_06655.

    **Source**:
    - Title: Rank Dynamics for Functional Data (2018)
    - Authors: Yaqing Chen, Matthew Dawson, Hans-Georg Müller
    - Citation Key: `arxiv_1810_06655`

    **KaTeX Formula**:
    $$
    \beta  = lim n\to \infty  \sqrt n ⎡⎢⎢⎣ ⎛⎜⎜⎝q1q4/q2 2 q3/q2 q5/q2 ⎞⎟⎟⎠ - ⎛⎜⎜⎝ Ft(y)\theta '' (t)/\theta ' (t) \partial  \partial t [Ft(y)\theta ' (t)]/\theta ' (t) ft(y) ⎞⎟⎟⎠ ⎤⎥⎥⎦
    $$

    Args:
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(l*(i*(m*n)))


def expr_beta_form_c(i: str = "i", l: str = "l", m: str = "m", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_beta_form_c`."""
    return (pl.col(l)*(pl.col(i)*(pl.col(m)*pl.col(n))))


def calc_p_m_g_o_d_o_form_6(A: float, M: float, N: float, U: float, alpha: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_26031.

    **Source**:
    - Title: AuDQ: Auditable Data Quality through Agentic Rule Discovery (2026)
    - Authors: Jacopo Biggiogera, Nicolas Colombo, Krati Saxena et al.
    - Citation Key: `arxiv_2610_26031`

    **KaTeX Formula**:
    $$
    pMgood = AM + \alpha  UM NM , \alpha  = 0.5
    $$

    Args:
        A (float): Input parameter `A`.
        M (float): Input parameter `M`.
        N (float): Input parameter `N`.
        U (float): Input parameter `U`.
        alpha (float): Input parameter `alpha`.

    Returns:
        float: Calculated metric value.
    """
    return float(A*M + alpha*(U*(M*(M*N))))


def expr_p_m_g_o_d_o_form_6(A: str = "A", M: str = "M", N: str = "N", U: str = "U", alpha: str = "alpha") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_m_g_o_d_o_form_6`."""
    return (pl.col(A)*pl.col(M) + pl.col(alpha)*(pl.col(U)*(pl.col(M)*(pl.col(M)*pl.col(N)))))


def calc_psi_r_a_da_n_psi_r_a_n_p_da_2602_2(P: float, n: float) -> float:
    r"""Compute mathematical metric extracted from 2602_23233.

    **Source**:
    - Title: The Counterfactual Combine: A Causal Framework for Player Evaluation (2026)
    - Authors: Herbert P. Susmann, Antonio D'Alessandro
    - Citation Key: `2602_23233`

    **KaTeX Formula**:
    $$
    \psi rand a -\psi rand a (P) =-Pn [DP*] + (Pn - P) [DP] + (Pn - P) [DP* - DP] + R(P, P* )
    $$

    Args:
        P (float): Input parameter `P`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(-P*n)


def expr_psi_r_a_da_n_psi_r_a_n_p_da_2602_2(P: str = "P", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_psi_r_a_da_n_psi_r_a_n_p_da_2602_2`."""
    return (-pl.col(P)*pl.col(n))


def calc_partial_y_c_k_epsilon_partial_form_7(Delta: float, alpha: float, c: float, epsilon: float, k: float, rho: float, s: float, x: float, y: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_26548.

    **Source**:
    - Title: Camera Calibration Using Inaccurate and Asynchronous Discrete GPS Trajectory from Drones (2026)
    - Authors: R. Yang, Y. Bar-Shalom, H. A. J. Huang
    - Citation Key: `arxiv_2608_26548`

    **KaTeX Formula**:
    $$
    \partial yC k \partial \epsilon  = \Delta xks\alpha c\epsilon c\rho  +\Delta ykc\alpha c\epsilon c\rho  +\Delta zks\epsilon c\rho
    $$

    Args:
        Delta (float): Input parameter `Delta`.
        alpha (float): Input parameter `alpha`.
        c (float): Input parameter `c`.
        epsilon (float): Input parameter `epsilon`.
        k (float): Input parameter `k`.
        rho (float): Input parameter `rho`.
        s (float): Input parameter `s`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(Delta*alpha*c**3*epsilon*k*rho*y + Delta*alpha*c**2*epsilon*k*rho*s*x + Delta*c*epsilon*k*rho*s*z)


def expr_partial_y_c_k_epsilon_partial_form_7(Delta: str = "Delta", alpha: str = "alpha", c: str = "c", epsilon: str = "epsilon", k: str = "k", rho: str = "rho", s: str = "s", x: str = "x", y: str = "y", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_partial_y_c_k_epsilon_partial_form_7`."""
    return (pl.col(Delta)*pl.col(alpha)*pl.col(c)**3*pl.col(epsilon)*pl.col(k)*pl.col(rho)*pl.col(y) + pl.col(Delta)*pl.col(alpha)*pl.col(c)**2*pl.col(epsilon)*pl.col(k)*pl.col(rho)*pl.col(s)*pl.col(x) + pl.col(Delta)*pl.col(c)*pl.col(epsilon)*pl.col(k)*pl.col(rho)*pl.col(s)*pl.col(z))


def calc_val_2_alpha_e_form_4(k: float, m: float, n: float, o: float, t: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    e2\alpha  = mknown t21 + t22 + t23 + 1
    $$

    Args:
        k (float): Input parameter `k`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        t (float): Input parameter `t`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(21*k*m*n**2*o*t*w + 45*t + 1)


def expr_val_2_alpha_e_form_4(k: str = "k", m: str = "m", n: str = "n", o: str = "o", t: str = "t", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2_alpha_e_form_4`."""
    return (21*pl.col(k)*pl.col(m)*pl.col(n)**2*pl.col(o)*pl.col(t)*pl.col(w) + 45*pl.col(t) + 1)


def calc_r_s_r_s_m_i_x_form_a(eta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    R(S+mix ) - R(S) = \eta  \sum t Eht\sim S(\cdot ) [Ea\sim S[A S (ht, a)2 ] + \lambda Ea\sim T[A S (ht, a)]] +O(\eta 2 )
    $$

    Args:
        eta (float): Input parameter `eta`.

    Returns:
        float: Calculated metric value.
    """
    return float(eta)


def expr_r_s_r_s_m_i_x_form_a(eta: str = "eta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_s_r_s_m_i_x_form_a`."""
    return (pl.col(eta))


def calc_delta_r_beta_form_7(g: float, pi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    \Delta \beta R = \pi *g*/[\omega 2(t)*V(t)] = g/[2*f2(t)*V(t)] = g*T2/[2*V(t)] = -\Delta \Phi
    $$

    Args:
        g (float): Input parameter `g`.
        pi (float): Input parameter `pi`.

    Returns:
        float: Calculated metric value.
    """
    return float(g*pi)


def expr_delta_r_beta_form_7(g: str = "g", pi: str = "pi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_r_beta_form_7`."""
    return (pl.col(g)*pl.col(pi))


def calc_a_l_r_2_form_b(L: float, R: float, phi: float, psi: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_08746.

    **Source**:
    - Title: Kinematics of Single-Winged Spinning Seeds: A Study on Mahogany and Buddha Coconut Samaras (2026)
    - Authors: Yogeshwaran G, Srisha M. V. Rao, Jagadeesh G
    - Citation Key: `arxiv_2603_08746`

    **KaTeX Formula**:
    $$
    aLR 2 =  \cos \theta LR \sin \psi LR \sin \phi LR \sin \theta LR \sin \psi LR + \cos \phi LR \cos \psi LR \cos \phi LR \sin \theta LR \sin \psi LR - \sin \phi LR \cos \psi LR
    $$

    Args:
        L (float): Input parameter `L`.
        R (float): Input parameter `R`.
        phi (float): Input parameter `phi`.
        psi (float): Input parameter `psi`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.sin(L*R*phi)*math.sin(L*R*psi)**2*math.sin(L*R*theta)*math.cos(L*R*theta) - math.sin(L*R*phi)*math.cos(L*R*psi) + math.sin(L*R*psi)*math.sin(L*R*theta)*math.cos(L*R*phi)**2*math.cos(L*R*psi))


def expr_a_l_r_2_form_b(L: str = "L", R: str = "R", phi: str = "phi", psi: str = "psi", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_l_r_2_form_b`."""
    return (math.sin(pl.col(L)*pl.col(R)*pl.col(phi))*math.sin(pl.col(L)*pl.col(R)*pl.col(psi))**2*math.sin(pl.col(L)*pl.col(R)*pl.col(theta))*math.cos(pl.col(L)*pl.col(R)*pl.col(theta)) - math.sin(pl.col(L)*pl.col(R)*pl.col(phi))*math.cos(pl.col(L)*pl.col(R)*pl.col(psi)) + math.sin(pl.col(L)*pl.col(R)*pl.col(psi))*math.sin(pl.col(L)*pl.col(R)*pl.col(theta))*math.cos(pl.col(L)*pl.col(R)*pl.col(phi))**2*math.cos(pl.col(L)*pl.col(R)*pl.col(psi)))


def calc_u_p_e_a_k_form_3(a: float, e: float, f: float, l: float, p: float, x: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_20645.

    **Source**:
    - Title: TACT-ful: Multi-Channel Terrain Affordance and Compliance Training for Payload-Robust Perceptive Humanoid Locomotion (2026)
    - Authors: Thanh Ly, Truong-Duy Dang, Chien Le et al.
    - Citation Key: `arxiv_2606_20645`

    **KaTeX Formula**:
    $$
    upeak = zl - zapex zl - 2zapex + z* f
    $$

    Args:
        a (float): Input parameter `a`.
        e (float): Input parameter `e`.
        f (float): Input parameter `f`.
        l (float): Input parameter `l`.
        p (float): Input parameter `p`.
        x (float): Input parameter `x`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(-a*e*l*p*x*z**2 - 2*a*e*p*x*z + f*z + l*z)


def expr_u_p_e_a_k_form_3(a: str = "a", e: str = "e", f: str = "f", l: str = "l", p: str = "p", x: str = "x", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_p_e_a_k_form_3`."""
    return (-pl.col(a)*pl.col(e)*pl.col(l)*pl.col(p)*pl.col(x)*pl.col(z)**2 - 2*pl.col(a)*pl.col(e)*pl.col(p)*pl.col(x)*pl.col(z) + pl.col(f)*pl.col(z) + pl.col(l)*pl.col(z))


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
    return float(a*i**2*j*s)


def expr_c_i_j_bt_sec(a: str = "a", i: str = "i", j: str = "j", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_i_j_bt_sec`."""
    return (pl.col(a)*pl.col(i)**2*pl.col(j)*pl.col(s))


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
    return float(A*S)


def expr_c_bt_sec(A: str = "A", S: str = "S") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_bt_sec`."""
    return (pl.col(A)*pl.col(S))


def calc_o_f_buchda(M: float, O: float) -> float:
    r"""Compute mathematical metric extracted from buchdahl_wisdom_of_the_crowd.

    **Source**:
    - Title: wisdom_of_the_crowd_updated
    - Authors: Scientific Literature
    - Citation Key: `buchdahl_wisdom_of_the_crowd`

    **KaTeX Formula**:
    $$
    Of = 3O 3 -MO
    $$

    Args:
        M (float): Input parameter `M`.
        O (float): Input parameter `O`.

    Returns:
        float: Calculated metric value.
    """
    return float(-M*O + 3*(3*O))


def expr_o_f_buchda(M: str = "M", O: str = "O") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_o_f_buchda`."""
    return (-pl.col(M)*pl.col(O) + 3*(3*pl.col(O)))


def calc_v_i_theta_alpha_0_form_e(i: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1905_04632.

    **Source**:
    - Title: Ceiling Effects for Hybrid Aerial-Surface Locomotion of Small Rotorcraft (2019)
    - Authors: Yi Hsuan Hsiao, Pakpong Chirarattananon
    - Citation Key: `arxiv_1905_04632`

    **KaTeX Formula**:
    $$
    vi (\theta , \alpha 0) = vi (1 + \sqrt 2 (\alpha 0 - 1) \cos \theta )
    $$

    Args:
        i (float): Input parameter `i`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*v)


def expr_v_i_theta_alpha_0_form_e(i: str = "i", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_i_theta_alpha_0_form_e`."""
    return (pl.col(i)*pl.col(v))


def calc_p_i_form_e(P: float, R: float, c: float, i: float, k: float, m: float, tau: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1905_04632.

    **Source**:
    - Title: Ceiling Effects for Hybrid Aerial-Surface Locomotion of Small Rotorcraft (2019)
    - Authors: Yi Hsuan Hsiao, Pakpong Chirarattananon
    - Citation Key: `arxiv_1905_04632`

    **KaTeX Formula**:
    $$
    Pi = c2/3 \tau  k-2Ri \cdot  P 4/3 m +Pm
    $$

    Args:
        P (float): Input parameter `P`.
        R (float): Input parameter `R`.
        c (float): Input parameter `c`.
        i (float): Input parameter `i`.
        k (float): Input parameter `k`.
        m (float): Input parameter `m`.
        tau (float): Input parameter `tau`.

    Returns:
        float: Calculated metric value.
    """
    return float(-8/3*P*R*i/m + P*m + (2/3)*c/(k*tau))


def expr_p_i_form_e(P: str = "P", R: str = "R", c: str = "c", i: str = "i", k: str = "k", m: str = "m", tau: str = "tau") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_form_e`."""
    return (-8/3*pl.col(P)*pl.col(R)*pl.col(i)/pl.col(m) + pl.col(P)*pl.col(m) + (2/3)*pl.col(c)/(pl.col(k)*pl.col(tau)))


def calc_l_form_0(C: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_39364.

    **Source**:
    - Title: Imperfect bifurcations in a laminar 3D bluff body wake: effect of pitch and yaw (2026)
    - Authors: Atharva Lagwankar, Alessandro Chiarini, François Gallaire et al.
    - Citation Key: `arxiv_2609_39364`

    **KaTeX Formula**:
    $$
    L =   C(u0, \cdot ) - Re -1 ∇ 2 (\cdot ) ∇(\cdot ) ∇ \cdot  (\cdot ) 0   , B =   I 0 0 0
    $$

    Args:
        C (float): Input parameter `C`.

    Returns:
        float: Calculated metric value.
    """
    return float(C)


def expr_l_form_0(C: str = "C") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_form_0`."""
    return (pl.col(C))


def calc_e_form_0(a: float, cup: float, e: float, i: float, l: float, n: float, r: float, s: float, t: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    E = Etrain \cup  Eval \cup  Etest
    $$

    Args:
        a (float): Input parameter `a`.
        cup (float): Input parameter `cup`.
        e (float): Input parameter `e`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(a**2*cup**2*e*i*l*n*r*s*t**3*v*math.exp(3))


def expr_e_form_0(a: str = "a", cup: str = "cup", e: str = "e", i: str = "i", l: str = "l", n: str = "n", r: str = "r", s: str = "s", t: str = "t", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_form_0`."""
    return (pl.col(a)**2*pl.col(cup)**2*pl.col(e)*pl.col(i)*pl.col(l)*pl.col(n)*pl.col(r)*pl.col(s)*pl.col(t)**3*pl.col(v)*math.exp(3))


def calc_l_f_o_r_c_e_form_0(B: float, df: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    Lforce = 1 Bdf B\sum  i=1 |||f cl i - f target i |||2 2
    $$

    Args:
        B (float): Input parameter `B`.
        df (float): Input parameter `df`.

    Returns:
        float: Calculated metric value.
    """
    return float(B**2*df)


def expr_l_f_o_r_c_e_form_0(B: str = "B", df: str = "df") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_f_o_r_c_e_form_0`."""
    return (pl.col(B)**2*pl.col(df))


def calc_l_f_s_form_1(L: float, U: float, dphi: float, f: float, sim: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    fs+L = f fwd \phi  ( \sim Us:s+L)
    $$

    Args:
        L (float): Input parameter `L`.
        U (float): Input parameter `U`.
        dphi (float): Input parameter `dphi`.
        f (float): Input parameter `f`.
        sim (float): Input parameter `sim`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(dphi*f**2*w*(L + U*sim))


def expr_l_f_s_form_1(L: str = "L", U: str = "U", dphi: str = "dphi", f: str = "f", sim: str = "sim", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_f_s_form_1`."""
    return (pl.col(dphi)*pl.col(f)**2*pl.col(w)*(pl.col(L) + pl.col(U)*pl.col(sim)))


def calc_l_s_m_o_o_h_t_form_2(B: float, du: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    Lsmooth = 1 Bdu B\sum  i=1 |||| ui,s+L - ui,s+L-1 \sigma train u ||||2 2
    $$

    Args:
        B (float): Input parameter `B`.
        du (float): Input parameter `du`.

    Returns:
        float: Calculated metric value.
    """
    return float(B**2*du)


def expr_l_s_m_o_o_h_t_form_2(B: str = "B", du: str = "du") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_s_m_o_o_h_t_form_2`."""
    return (pl.col(B)**2*pl.col(du))


def calc_delta_i_x_form_2(D: float, di: float, i: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_26548.

    **Source**:
    - Title: Camera Calibration Using Inaccurate and Asynchronous Discrete GPS Trajectory from Drones (2026)
    - Authors: R. Yang, Y. Bar-Shalom, H. A. J. Huang
    - Citation Key: `arxiv_2608_26548`

    **KaTeX Formula**:
    $$
    \Delta ix = Didix
    $$

    Args:
        D (float): Input parameter `D`.
        di (float): Input parameter `di`.
        i (float): Input parameter `i`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(D*di*i*x)


def expr_delta_i_x_form_2(D: str = "D", di: str = "di", i: str = "i", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_i_x_form_2`."""
    return (pl.col(D)*pl.col(di)*pl.col(i)*pl.col(x))


def calc_delta_e_k_p_form_7(E: float, S: float, f: float, k: float, s: float, y: float) -> float:
    r"""Compute mathematical metric extracted from openalex_selim2024_w4398201786.

    **Source**:
    - Title: Advances in polymer/inorganic nanocomposite fabrics for lightweight and high-strength armor and ballistic-proof materials (2024)
    - Authors: Mohamed Sayed Selim, Sherif A. El‐Safty, Mohamed A. Shenashen et al.
    - Citation Key: `openalex_selim2024_w4398201786`

    **KaTeX Formula**:
    $$
    \Delta Epk=Eys + Syk+Ef
    $$

    Args:
        E (float): Input parameter `E`.
        S (float): Input parameter `S`.
        f (float): Input parameter `f`.
        k (float): Input parameter `k`.
        s (float): Input parameter `s`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(E*f + (E*(s*y) + S*(k*y)))


def expr_delta_e_k_p_form_7(E: str = "E", S: str = "S", f: str = "f", k: str = "k", s: str = "s", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_e_k_p_form_7`."""
    return (pl.col(E)*pl.col(f) + (pl.col(E)*(pl.col(s)*pl.col(y)) + pl.col(S)*(pl.col(k)*pl.col(y))))


def calc_f_o_r_a_c_l_e_s_257_form_3(U: float, a: float, c: float, dphi: float, e: float, f: float, l: float, o: float, r: float, s: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    f oracle s+257 = f fwd \phi  (Uoracle s+1:s+257 )
    $$

    Args:
        U (float): Input parameter `U`.
        a (float): Input parameter `a`.
        c (float): Input parameter `c`.
        dphi (float): Input parameter `dphi`.
        e (float): Input parameter `e`.
        f (float): Input parameter `f`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(dphi*f**2*w*(U*a*c*e*l*o*r*s + 257 + 1/s))


def expr_f_o_r_a_c_l_e_s_257_form_3(U: str = "U", a: str = "a", c: str = "c", dphi: str = "dphi", e: str = "e", f: str = "f", l: str = "l", o: str = "o", r: str = "r", s: str = "s", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_o_r_a_c_l_e_s_257_form_3`."""
    return (pl.col(dphi)*pl.col(f)**2*pl.col(w)*(pl.col(U)*pl.col(a)*pl.col(c)*pl.col(e)*pl.col(l)*pl.col(o)*pl.col(r)*pl.col(s) + 257 + 1/pl.col(s)))


def calc_l_f_d_w_form_4(B: float, df: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    Lfwd = 1 Bdf B\sum  i=1 |||fi - fi|||2 2
    $$

    Args:
        B (float): Input parameter `B`.
        df (float): Input parameter `df`.

    Returns:
        float: Calculated metric value.
    """
    return float(B**2*df)


def expr_l_f_d_w_form_4(B: str = "B", df: str = "df") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_f_d_w_form_4`."""
    return (pl.col(B)**2*pl.col(df))


def calc_e_a_n_form_4(Z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    E(An) = Z -1 \int  \prod  i dAi \sqrt 2\pi \sigma 2A  \exp - \sum  j A2 j 2\sigma 2A  An (34) \int  (\prod  a dka 2\pi  ) \exp i \sum  b kb(yb - \sum  l AlTl ( \theta b)) - \sigma 2A 2 \sum  ab ka\Delta abkb  , Cov(Am,An) = Z -1 \int  \prod  i dAi \sqrt 2\pi \sigma 2A  \exp - \sum  j A2 j 2\sigma 2A - \sigma 2A 2 \sum  ab ka\Delta abkb  AmAn \int  \prod  a dka 2\pi  \exp i \sum  b kb(yb - \sum  l AlTl ( \theta b))
    $$

    Args:
        Z (float): Input parameter `Z`.

    Returns:
        float: Calculated metric value.
    """
    return float(Z - 1)


def expr_e_a_n_form_4(Z: str = "Z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_a_n_form_4`."""
    return (pl.col(Z) - 1)


def calc_c_g_form_4(C: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31153.

    **Source**:
    - Title: Balanced Posted Prices in Stationary Two-Sided Markets (2026)
    - Authors: Ilan Reuven Cohen
    - Citation Key: `arxiv_2610_31153`

    **KaTeX Formula**:
    $$
    GC = C C + 1 \sum  j \beta j\gamma jbj - \sum  i \alpha i\lambda iai  = C C + 1 \sum  j \gamma j (bj - \tau  ) + + \sum  i \lambda i(\tau  - ai) +
    $$

    Args:
        C (float): Input parameter `C`.

    Returns:
        float: Calculated metric value.
    """
    return float(C**2 + 1)


def expr_c_g_form_4(C: str = "C") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_g_form_4`."""
    return (pl.col(C)**2 + 1)


def calc_tau_form_4(F: float, dcos: float, phi: float, s: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    \tau  = d \cos(\theta  - \phi )Fs
    $$

    Args:
        F (float): Input parameter `F`.
        dcos (float): Input parameter `dcos`.
        phi (float): Input parameter `phi`.
        s (float): Input parameter `s`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(F*dcos*s*(-phi + theta))


def expr_tau_form_4(F: str = "F", dcos: str = "dcos", phi: str = "phi", s: str = "s", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_tau_form_4`."""
    return (pl.col(F)*pl.col(dcos)*pl.col(s)*(-pl.col(phi) + pl.col(theta)))


def calc_t_12_form_4(l: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2507_16328.

    **Source**:
    - Title: Design and Dimensional Optimization of Legged Structures for Construction Robots (2025)
    - Authors: Xiao Liu, Xianlong Yang, Weijun Wang et al.
    - Citation Key: `arxiv_2507_16328`

    **KaTeX Formula**:
    $$
    T 1 2 =  \cos\theta 2 -\sin\theta 2 0 l2 \cos\theta 2 \sin\theta 2 \cos\theta 2 0 l2 \sin\theta 2 0 0 1 0 0 0 0 1
    $$

    Args:
        l (float): Input parameter `l`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(-math.sin(2*theta)*math.sin(200100001*theta)*math.sin(40*l*theta)*math.cos(2*theta)*math.cos(40*l*theta) + math.cos(2*theta))


def expr_t_12_form_4(l: str = "l", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_12_form_4`."""
    return (-math.sin(2*pl.col(theta))*math.sin(200100001*pl.col(theta))*math.sin(40*pl.col(l)*pl.col(theta))*math.cos(2*pl.col(theta))*math.cos(40*pl.col(l)*pl.col(theta)) + math.cos(2*pl.col(theta)))


def calc_g_r_form_f(G: float, dm: float, r: float, rho: float, s: float) -> float:
    r"""Compute mathematical metric extracted from openalex_oneill2010_w2081091143.

    **Source**:
    - Title: THREE-DIMENSIONAL SIMULATIONS OF BI-DIRECTED MAGNETOHYDRODYNAMIC JETS INTERACTING WITH CLUSTER ENVIRONMENTS (2010)
    - Authors: S. M. O'Neill, T. W. Jones
    - Citation Key: `openalex_oneill2010_w2081091143`

    **KaTeX Formula**:
    $$
    g(r) = - 4\pi Gr 3 dm \rho s r 2 [ \ln ( 1 + r rdm ) - r r + rdm ]
    $$

    Args:
        G (float): Input parameter `G`.
        dm (float): Input parameter `dm`.
        r (float): Input parameter `r`.
        rho (float): Input parameter `rho`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(-12*math.pi*G*dm*r**2*rho*s*(2*dm*r - 2*r**2 + 2*math.log(dm*r**2 + 1)))


def expr_g_r_form_f(G: str = "G", dm: str = "dm", r: str = "r", rho: str = "rho", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_r_form_f`."""
    return (-12*math.pi*pl.col(G)*pl.col(dm)*pl.col(r)**2*pl.col(rho)*pl.col(s)*(2*pl.col(dm)*pl.col(r) - 2*pl.col(r)**2 + 2*(pl.col(dm).log()*pl.col(r)**2 + 1)))


def calc_b_theta_form_5(F: float, m: float, phi: float, r: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from openalex_oneill2010_w2081091143.

    **Source**:
    - Title: THREE-DIMENSIONAL SIMULATIONS OF BI-DIRECTED MAGNETOHYDRODYNAMIC JETS INTERACTING WITH CLUSTER ENVIRONMENTS (2010)
    - Authors: S. M. O'Neill, T. W. Jones
    - Citation Key: `openalex_oneill2010_w2081091143`

    **KaTeX Formula**:
    $$
    B\theta  = F1(r) \cdot  m r \sin \theta  \cos(m\phi )
    $$

    Args:
        F (float): Input parameter `F`.
        m (float): Input parameter `m`.
        phi (float): Input parameter `phi`.
        r (float): Input parameter `r`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(F*m*r**2*math.sin(theta)*math.cos(m*phi))


def expr_b_theta_form_5(F: str = "F", m: str = "m", phi: str = "phi", r: str = "r", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_b_theta_form_5`."""
    return (pl.col(F)*pl.col(m)*pl.col(r)**2*math.sin(pl.col(theta))*math.cos(pl.col(m)*pl.col(phi)))


def calc_b_phi_form_7(F: float, m: float, n: float, phi: float, r: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from openalex_oneill2010_w2081091143.

    **Source**:
    - Title: THREE-DIMENSIONAL SIMULATIONS OF BI-DIRECTED MAGNETOHYDRODYNAMIC JETS INTERACTING WITH CLUSTER ENVIRONMENTS (2010)
    - Authors: S. M. O'Neill, T. W. Jones
    - Citation Key: `openalex_oneill2010_w2081091143`

    **KaTeX Formula**:
    $$
    B\phi  = F2(r) \cdot  n r \sin(n\theta  ) - F1(r ) r \sin(m\phi ) \sin(2\theta )
    $$

    Args:
        F (float): Input parameter `F`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        phi (float): Input parameter `phi`.
        r (float): Input parameter `r`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*F*n*r**2*math.sin(n*theta) - F*r**2*math.sin(2*theta)*math.sin(m*phi))


def expr_b_phi_form_7(F: str = "F", m: str = "m", n: str = "n", phi: str = "phi", r: str = "r", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_b_phi_form_7`."""
    return (2*pl.col(F)*pl.col(n)*pl.col(r)**2*math.sin(pl.col(n)*pl.col(theta)) - pl.col(F)*pl.col(r)**2*math.sin(2*pl.col(theta))*math.sin(pl.col(m)*pl.col(phi)))


def calc_d_u_p_p_e_n_r_form_5(p: float, s: float, t: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    Dupper n = sup t {t -  F (t-)}
    $$

    Args:
        p (float): Input parameter `p`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(p*s*t*u)


def expr_d_u_p_p_e_n_r_form_5(p: str = "p", s: str = "s", t: str = "t", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_u_p_p_e_n_r_form_5`."""
    return (pl.col(p)*pl.col(s)*pl.col(t)*pl.col(u))


def calc_l_k_i_n_form_5(B: float, du: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    Lkin = 1 Bdu B\sum  i=1 |ui -ui|22
    $$

    Args:
        B (float): Input parameter `B`.
        du (float): Input parameter `du`.

    Returns:
        float: Calculated metric value.
    """
    return float(B**2*du)


def expr_l_k_i_n_form_5(B: str = "B", du: str = "du") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_k_i_n_form_5`."""
    return (pl.col(B)**2*pl.col(du))


def calc_psi_form_1(a: float, rho: float) -> float:
    r"""Compute mathematical metric extracted from openalex_oneill2010_w2081091143.

    **Source**:
    - Title: THREE-DIMENSIONAL SIMULATIONS OF BI-DIRECTED MAGNETOHYDRODYNAMIC JETS INTERACTING WITH CLUSTER ENVIRONMENTS (2010)
    - Authors: S. M. O'Neill, T. W. Jones
    - Citation Key: `openalex_oneill2010_w2081091143`

    **KaTeX Formula**:
    $$
    \Psi  = -\pi \rho a,off r 2 off x (\kappa -2\kappa /3\gamma  ) off /mre = constant
    $$

    Args:
        a (float): Input parameter `a`.
        rho (float): Input parameter `rho`.

    Returns:
        float: Calculated metric value.
    """
    return float(-math.pi*a*rho)


def expr_psi_form_1(a: str = "a", rho: str = "rho") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_psi_form_1`."""
    return (-math.pi*pl.col(a)*pl.col(rho))


def calc_v_m_a_x_form_6(approx: float, l: float, m: float, omega: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_23163.

    **Source**:
    - Title: Spinning Quadrotor: Hover Thrust Augmentation with Passive Lifting Surfaces (2026)
    - Authors: Aniketh Parkala, Harikumar Kandath
    - Citation Key: `arxiv_2608_23163`

    **KaTeX Formula**:
    $$
    Vmax = \omega l \approx  6.5 m/s
    $$

    Args:
        approx (float): Input parameter `approx`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.
        omega (float): Input parameter `omega`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(6.5*approx*l*m*omega/s)


def expr_v_m_a_x_form_6(approx: str = "approx", l: str = "l", m: str = "m", omega: str = "omega", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_m_a_x_form_6`."""
    return (6.5*pl.col(approx)*pl.col(l)*pl.col(m)*pl.col(omega)/pl.col(s))


def calc_v_r_form_6(omega: float, r: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_23163.

    **Source**:
    - Title: Spinning Quadrotor: Hover Thrust Augmentation with Passive Lifting Surfaces (2026)
    - Authors: Aniketh Parkala, Harikumar Kandath
    - Citation Key: `arxiv_2608_23163`

    **KaTeX Formula**:
    $$
    V (r) = \omega zr
    $$

    Args:
        omega (float): Input parameter `omega`.
        r (float): Input parameter `r`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(omega*r*z)


def expr_v_r_form_6(omega: str = "omega", r: str = "r", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_r_form_6`."""
    return (pl.col(omega)*pl.col(r)*pl.col(z))


def calc_u_form_8(epsilon: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_39364.

    **Source**:
    - Title: Imperfect bifurcations in a laminar 3D bluff body wake: effect of pitch and yaw (2026)
    - Authors: Atharva Lagwankar, Alessandro Chiarini, François Gallaire et al.
    - Citation Key: `arxiv_2609_39364`

    **KaTeX Formula**:
    $$
    u = u0 + \epsilon u1 + \epsilon  2 u2 + \epsilon  3 u3 . . . (A 6)
    $$

    Args:
        epsilon (float): Input parameter `epsilon`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(8*epsilon*u)


def expr_u_form_8(epsilon: str = "epsilon", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_form_8`."""
    return (8*pl.col(epsilon)*pl.col(u))


def calc_j_q_form_7(p: float, partial: float, theta: float, x: float, y: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2507_16328.

    **Source**:
    - Title: Design and Dimensional Optimization of Legged Structures for Construction Robots (2025)
    - Authors: Xiao Liu, Xianlong Yang, Weijun Wang et al.
    - Citation Key: `arxiv_2507_16328`

    **KaTeX Formula**:
    $$
    J (q) =  \partial  px \partial  \theta 1 \partial  px \partial  \theta 2 \partial  px \partial  \theta 3 \partial  py \partial  \theta 1 \partial  py \partial  \theta 2 \partial  py \partial  \theta 3 \partial  pz \partial  \theta 1 \partial  pz \partial  \theta 2 \partial  pz \partial  \theta 3
    $$

    Args:
        p (float): Input parameter `p`.
        partial (float): Input parameter `partial`.
        theta (float): Input parameter `theta`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(216*p**9*partial**18*theta**9*x**3*y**3*z**3)


def expr_j_q_form_7(p: str = "p", partial: str = "partial", theta: str = "theta", x: str = "x", y: str = "y", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_q_form_7`."""
    return (216*pl.col(p)**9*pl.col(partial)**18*pl.col(theta)**9*pl.col(x)**3*pl.col(y)**3*pl.col(z)**3)


def calc_i_y_form_7(W: float, i: float, mu: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_28906.

    **Source**:
    - Title: ReaFlow-TTS: Realization-Conditioned Flow Matching for High-Quality and Controllable Speech Synthesis (2026)
    - Authors: Junyi Zhao, Yihao Qin, Changsheng Ma
    - Citation Key: `arxiv_2609_28906`

    **KaTeX Formula**:
    $$
    yi = W\mu i
    $$

    Args:
        W (float): Input parameter `W`.
        i (float): Input parameter `i`.
        mu (float): Input parameter `mu`.

    Returns:
        float: Calculated metric value.
    """
    return float(W*i*mu)


def expr_i_y_form_7(W: str = "W", i: str = "i", mu: str = "mu") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_y_form_7`."""
    return (pl.col(W)*pl.col(i)*pl.col(mu))


def calc_m_e_s_form_7(N: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    MSE = 1N N\sum  i=1 ( yi - yi)2 , MAE = 1N N\sum  i=1 | yi - yi|, P95 = Q0.95 ({| yi - yi|}Ni=1 )
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*N))


def expr_m_e_s_form_7(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_e_s_form_7`."""
    return (1*(pl.col(N)*pl.col(N)))


def calc_f_s_257_form_8(U: float, c: float, dphi: float, f: float, s: float, t: float, w: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    fs+257 = f fwd \phi  ( Uctx s )
    $$

    Args:
        U (float): Input parameter `U`.
        c (float): Input parameter `c`.
        dphi (float): Input parameter `dphi`.
        f (float): Input parameter `f`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.
        w (float): Input parameter `w`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(U*c*dphi*f**2*s*t*w*x)


def expr_f_s_257_form_8(U: str = "U", c: str = "c", dphi: str = "dphi", f: str = "f", s: str = "s", t: str = "t", w: str = "w", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_s_257_form_8`."""
    return (pl.col(U)*pl.col(c)*pl.col(dphi)*pl.col(f)**2*pl.col(s)*pl.col(t)*pl.col(w)*pl.col(x))


def calc_j_a_o_p_d_theta_form_9(H: float, R: float, S: float, sim: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    JAOPD(\theta ) = \sim R S H H-1 \sum  t=0 [wt logS\theta (at | ht) -Ea\sim T [ logS\theta (a | ht)]], wt := T(at | ht) S(at | ht)
    $$

    Args:
        H (float): Input parameter `H`.
        R (float): Input parameter `R`.
        S (float): Input parameter `S`.
        sim (float): Input parameter `sim`.

    Returns:
        float: Calculated metric value.
    """
    return float(sim*(R*(S*(H*H))) - 1)


def expr_j_a_o_p_d_theta_form_9(H: str = "H", R: str = "R", S: str = "S", sim: str = "sim") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_a_o_p_d_theta_form_9`."""
    return (pl.col(sim)*(pl.col(R)*(pl.col(S)*(pl.col(H)*pl.col(H)))) - 1)


def calc_l_f_c_l_s_1_form_9(L: float, U: float, c: float, dphi: float, f: float, l: float, s: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    f cl s+L+1 = f fwd \phi  ( Ucl s+1:s+L+1)
    $$

    Args:
        L (float): Input parameter `L`.
        U (float): Input parameter `U`.
        c (float): Input parameter `c`.
        dphi (float): Input parameter `dphi`.
        f (float): Input parameter `f`.
        l (float): Input parameter `l`.
        s (float): Input parameter `s`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(dphi*f**2*w*(L + U*c*l*s + 1 + 1/s))


def expr_l_f_c_l_s_1_form_9(L: str = "L", U: str = "U", c: str = "c", dphi: str = "dphi", f: str = "f", l: str = "l", s: str = "s", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_f_c_l_s_1_form_9`."""
    return (pl.col(dphi)*pl.col(f)**2*pl.col(w)*(pl.col(L) + pl.col(U)*pl.col(c)*pl.col(l)*pl.col(s) + 1 + 1/pl.col(s)))


def calc_l_k_l_t_form_c(gamma: float, j: float, rho: float) -> float:
    r"""Compute mathematical metric extracted from openalex_oneill2010_w2081091143.

    **Source**:
    - Title: THREE-DIMENSIONAL SIMULATIONS OF BI-DIRECTED MAGNETOHYDRODYNAMIC JETS INTERACTING WITH CLUSTER ENVIRONMENTS (2010)
    - Authors: S. M. O'Neill, T. W. Jones
    - Citation Key: `openalex_oneill2010_w2081091143`

    **KaTeX Formula**:
    $$
    Lk Lt = 3(\gamma  - 1)\rho j,0v 2 j,0 (\mu  2 + 3\mu  + 6) 20\gamma pj,0(\mu  2 + \mu  + 1) . (A6)
    $$

    Args:
        gamma (float): Input parameter `gamma`.
        j (float): Input parameter `j`.
        rho (float): Input parameter `rho`.

    Returns:
        float: Calculated metric value.
    """
    return float(3*((j*rho)*(gamma - 1)))


def expr_l_k_l_t_form_c(gamma: str = "gamma", j: str = "j", rho: str = "rho") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_k_l_t_form_c`."""
    return (3*((pl.col(j)*pl.col(rho))*(pl.col(gamma) - 1)))


def calc_delta_x_1_brown_(mu: float) -> float:
    r"""Compute mathematical metric extracted from brown_2008_arxiv.

    **Source**:
    - Title: In-season prediction of batting averages: a field test of empirical Bayes and Bayes methodologies (2008)
    - Authors: Brown, L. D.
    - Citation Key: `brown_2008_arxiv`

    **KaTeX Formula**:
    $$
    \delta (X1) = \mu 1 + (1- P1 -3 \sum (X1i - \mu 1)2 /\sigma 2 1i ) +(X1 - \mu 1)
    $$

    Args:
        mu (float): Input parameter `mu`.

    Returns:
        float: Calculated metric value.
    """
    return float(mu)


def expr_delta_x_1_brown_(mu: str = "mu") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_x_1_brown_`."""
    return (pl.col(mu))


def calc_sim_r_i_brown_(i: float, n: float, s: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from brown_2008_arxiv.

    **Source**:
    - Title: In-season prediction of batting averages: a field test of empirical Bayes and Bayes methodologies (2008)
    - Authors: Brown, L. D.
    - Citation Key: `brown_2008_arxiv`

    **KaTeX Formula**:
    $$
    \sim Ri = sin2  \theta i
    $$

    Args:
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        s (float): Input parameter `s`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*i**2*n*s*theta)


def expr_sim_r_i_brown_(i: str = "i", n: str = "n", s: str = "s", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sim_r_i_brown_`."""
    return (2*pl.col(i)**2*pl.col(n)*pl.col(s)*pl.col(theta))


def calc_c_o_s_g_b_a_l_g_n_a_v_form_8(T: float, a: float, b: float, epsilon: float, g: float, l: float, n: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29142.

    **Source**:
    - Title: State-Dependent Objective Coordination for End-to-End Balance and Navigation (2026)
    - Authors: Xuhao Huang, Xitao Xu, Yuxin Zheng et al.
    - Citation Key: `arxiv_2610_29142`

    **KaTeX Formula**:
    $$
    Cos(gbal , gnav) = g^T bal gnav |gbal ||gnav | + \epsilon
    $$

    Args:
        T (float): Input parameter `T`.
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        epsilon (float): Input parameter `epsilon`.
        g (float): Input parameter `g`.
        l (float): Input parameter `l`.
        n (float): Input parameter `n`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(a**2*b*g*g**T*l*n*v*abs(a*b*g*l)*abs(a*g*n*v) + epsilon)


def expr_c_o_s_g_b_a_l_g_n_a_v_form_8(T: str = "T", a: str = "a", b: str = "b", epsilon: str = "epsilon", g: str = "g", l: str = "l", n: str = "n", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_o_s_g_b_a_l_g_n_a_v_form_8`."""
    return (pl.col(a)**2*pl.col(b)*pl.col(g)*pl.col(g)**pl.col(T)*pl.col(l)*pl.col(n)*pl.col(v)*abs(pl.col(a)*pl.col(b)*pl.col(g)*pl.col(l))*abs(pl.col(a)*pl.col(g)*pl.col(n)*pl.col(v)) + pl.col(epsilon))


def calc_l_k_l_t_form_f(mu: float) -> float:
    r"""Compute mathematical metric extracted from openalex_oneill2010_w2081091143.

    **Source**:
    - Title: THREE-DIMENSIONAL SIMULATIONS OF BI-DIRECTED MAGNETOHYDRODYNAMIC JETS INTERACTING WITH CLUSTER ENVIRONMENTS (2010)
    - Authors: S. M. O'Neill, T. W. Jones
    - Citation Key: `openalex_oneill2010_w2081091143`

    **KaTeX Formula**:
    $$
    Lk Lt = 0.904 ( \mu  2 + 3\mu  + 6 \mu  2 + \mu  + 1 ) . (A7)
    $$

    Args:
        mu (float): Input parameter `mu`.

    Returns:
        float: Calculated metric value.
    """
    return float(16.272*mu + 0.904)


def expr_l_k_l_t_form_f(mu: str = "mu") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_k_l_t_form_f`."""
    return (16.272*pl.col(mu) + 0.904)


def calc_x_form_b(A: float, B: float, a: float, r: float, x: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_17701.

    **Source**:
    - Title: Barrier Functions Against Safety Drift in Shared Control (2026)
    - Authors: M. Yusuf Uzun, Yildiray Yildiz
    - Citation Key: `arxiv_2609_17701`

    **KaTeX Formula**:
    $$
    x = A x + Bya ya + Br r
    $$

    Args:
        A (float): Input parameter `A`.
        B (float): Input parameter `B`.
        a (float): Input parameter `a`.
        r (float): Input parameter `r`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(A*x + B*a**2*y**2 + B*r**2)


def expr_x_form_b(A: str = "A", B: str = "B", a: str = "a", r: str = "r", x: str = "x", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_form_b`."""
    return (pl.col(A)*pl.col(x) + pl.col(B)*pl.col(a)**2*pl.col(y)**2 + pl.col(B)*pl.col(r)**2)


def calc_l_r_e_s_form_d(B: float, H: float, du: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    Lres = 1 BHdu B\sum  i=1 |||∆ Ui|||2 F
    $$

    Args:
        B (float): Input parameter `B`.
        H (float): Input parameter `H`.
        du (float): Input parameter `du`.

    Returns:
        float: Calculated metric value.
    """
    return float(B**2*H*du)


def expr_l_r_e_s_form_d(B: str = "B", H: str = "H", du: str = "du") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_r_e_s_form_d`."""
    return (pl.col(B)**2*pl.col(H)*pl.col(du))


def calc_l_m_a_e_form_e(B: float, H: float, du: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    LMAE = 1 BHdu B\sum  i=1 ||| Ui - Ui|||1
    $$

    Args:
        B (float): Input parameter `B`.
        H (float): Input parameter `H`.
        du (float): Input parameter `du`.

    Returns:
        float: Calculated metric value.
    """
    return float(B**2*H*du)


def expr_l_m_a_e_form_e(B: str = "B", H: str = "H", du: str = "du") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_m_a_e_form_e`."""
    return (pl.col(B)**2*pl.col(H)*pl.col(du))


def calc_z_form_2(beta: float, j: float) -> float:
    r"""Compute mathematical metric extracted from openalex_bendtsen2017_w2617761836.

    **Source**:
    - Title: Regimes in baseball players’ career data (2017)
    - Authors: Marcus Bendtsen
    - Citation Key: `openalex_bendtsen2017_w2617761836`

    **KaTeX Formula**:
    $$
    Z = \beta  j\sum  i=lb(\beta  * j ) (1+ i -\beta j + \kappa ) + ub(\beta  * j ) \sum  i =\beta  j +1 (1- i +\beta j +\kappa )
    $$

    Args:
        beta (float): Input parameter `beta`.
        j (float): Input parameter `j`.

    Returns:
        float: Calculated metric value.
    """
    return float(beta*j)


def expr_z_form_2(beta: str = "beta", j: str = "j") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_form_2`."""
    return (pl.col(beta)*pl.col(j))


def calc_l_m_e_s_form_e(B: float, H: float, du: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    LMSE = 1 BHdu B\sum  i=1 ||| Ui - Ui|||2 F
    $$

    Args:
        B (float): Input parameter `B`.
        H (float): Input parameter `H`.
        du (float): Input parameter `du`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(B*(H*(B*du))))


def expr_l_m_e_s_form_e(B: str = "B", H: str = "H", du: str = "du") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_m_e_s_form_e`."""
    return (1*(pl.col(B)*(pl.col(H)*(pl.col(B)*pl.col(du)))))


def calc_t_23_form_e(l: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2507_16328.

    **Source**:
    - Title: Design and Dimensional Optimization of Legged Structures for Construction Robots (2025)
    - Authors: Xiao Liu, Xianlong Yang, Weijun Wang et al.
    - Citation Key: `arxiv_2507_16328`

    **KaTeX Formula**:
    $$
    T 2 3 =  \cos\theta 3 -\sin\theta 3 0 l3 \cos\theta 3 \sin\theta 3 \cos\theta 3 0 l3 \sin\theta 3 0 0 1 0 0 0 0 1
    $$

    Args:
        l (float): Input parameter `l`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(-math.sin(3*theta)*math.sin(300100001*theta)*math.sin(90*l*theta)*math.cos(3*theta)*math.cos(90*l*theta) + math.cos(3*theta))


def expr_t_23_form_e(l: str = "l", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_23_form_e`."""
    return (-math.sin(3*pl.col(theta))*math.sin(300100001*pl.col(theta))*math.sin(90*pl.col(l)*pl.col(theta))*math.cos(3*pl.col(theta))*math.cos(90*pl.col(l)*pl.col(theta)) + math.cos(3*pl.col(theta)))


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
    return float(T*e**2*i**2*j**2)


def expr_f_diebol(T: str = "T", e: str = "e", i: str = "i", j: str = "j") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_diebol`."""
    return (pl.col(T)*pl.col(e)**2*pl.col(i)**2*pl.col(j)**2)


def calc_p_i_j_j_pi_bt_sec(a: float, f: float, i: float, j: float, l: float, o: float, p: float, r: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    pij\pi j =pji\pi i for all i, j
    $$

    Args:
        a (float): Input parameter `a`.
        f (float): Input parameter `f`.
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.pi*a*f*i**3*j*l**2*o*p*r)


def expr_p_i_j_j_pi_bt_sec(a: str = "a", f: str = "f", i: str = "i", j: str = "j", l: str = "l", o: str = "o", p: str = "p", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_j_j_pi_bt_sec`."""
    return (math.pi*pl.col(a)*pl.col(f)*pl.col(i)**3*pl.col(j)*pl.col(l)**2*pl.col(o)*pl.col(p)*pl.col(r))


def calc_l_p_eta_bt_sec(n: float, p: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    L(p, \eta ) = S(p) - n\sum  i=1 \eta i( n\sum  j=1 (mij pij - cij ))
    $$

    Args:
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(-n + p)


def expr_l_p_eta_bt_sec(n: str = "n", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_p_eta_bt_sec`."""
    return (-pl.col(n) + pl.col(p))


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
    return float(math.e*P*p)


def expr_r_diebol(P: str = "P", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_diebol`."""
    return (math.e*pl.col(P)*pl.col(p))


def calc_w_form_1(A: float, phi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    w = A\phi
    $$

    Args:
        A (float): Input parameter `A`.
        phi (float): Input parameter `phi`.

    Returns:
        float: Calculated metric value.
    """
    return float(A*phi)


def expr_w_form_1(A: str = "A", phi: str = "phi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_form_1`."""
    return (pl.col(A)*pl.col(phi))


def calc_partial_partial_p_i_j_s_p_bt_sec(i: float, j: float, n: float, p: float, partial: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    \partial S(p) \partial pij = \partial  \partial pij n\sum  r=1 \eta r( n\sum  s=1 (mrsprs - crs)) for all i, j
    $$

    Args:
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.
        partial (float): Input parameter `partial`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*j*n*p*partial**2)


def expr_partial_partial_p_i_j_s_p_bt_sec(i: str = "i", j: str = "j", n: str = "n", p: str = "p", partial: str = "partial") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_partial_partial_p_i_j_s_p_bt_sec`."""
    return (pl.col(i)*pl.col(j)*pl.col(n)*pl.col(p)*pl.col(partial)**2)


def calc_val_3_m_s_e_y_y_form_5(N: float) -> float:
    r"""Compute mathematical metric extracted from openalex_kang2025_w4409349184.

    **Source**:
    - Title: Data-driven approaches for predicting Tommy John Surgery risk in major league baseball pitchers (2025)
    - Authors: Bosuk Kang, Minsu Park, Angel Pasqual del Pobil et al.
    - Citation Key: `openalex_kang2025_w4409349184`

    **KaTeX Formula**:
    $$
    (3) MSE(y, y) = 1 N N\sum  i=1 (yi - yi) 2
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*N))


def expr_val_3_m_s_e_y_y_form_5(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_3_m_s_e_y_y_form_5`."""
    return (1*(pl.col(N)*pl.col(N)))


def calc_d_form_8(K: float, d: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    D = \cos \theta d -K1 +K4 \cos \theta d +K5, E = -2 \sin\theta d F = K1 + (K4 - 1) \cos \theta d + K5
    $$

    Args:
        K (float): Input parameter `K`.
        d (float): Input parameter `d`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(4*K*math.cos(d*theta) + 4*K + math.cos(d*theta))


def expr_d_form_8(K: str = "K", d: str = "d", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_form_8`."""
    return (4*pl.col(K)*math.cos(pl.col(d)*pl.col(theta)) + 4*pl.col(K) + math.cos(pl.col(d)*pl.col(theta)))


def calc_log_p_i_j_e_log_1_p_i_j_e_bt_sec(eta: float, i: float, j: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    - \log pij + \log(1 - pij ) = \eta i - \eta j
    $$

    Args:
        eta (float): Input parameter `eta`.
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.

    Returns:
        float: Calculated metric value.
    """
    return float(eta*i - eta*j)


def expr_log_p_i_j_e_log_1_p_i_j_e_bt_sec(eta: str = "eta", i: str = "i", j: str = "j") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_log_p_i_j_e_log_1_p_i_j_e_bt_sec`."""
    return (pl.col(eta)*pl.col(i) - pl.col(eta)*pl.col(j))


def calc_r_p_w_form_d(G: float, R_A: float, R_S: float) -> float:
    r"""Compute mathematical metric extracted from fangraphs_war_position_glossary.

    **Source**:
    - Title: FanGraphs Sabermetric Library: Wins Above Replacement (WAR) for Position Players (2026)
    - Authors: FanGraphs
    - Citation Key: `fangraphs_war_position_glossary`

    **KaTeX Formula**:
    $$
    RPW = 10 \cdot \sqrt{\frac{R_{S} + R_{A}}{G}}
    $$

    Args:
        G (float): Input parameter `G`.
        R_A (float): Input parameter `R_A`.
        R_S (float): Input parameter `R_S`.

    Returns:
        float: Calculated metric value.
    """
    return float(10*math.sqrt((R_A + R_S)/G))


def expr_r_p_w_form_d(G: str = "G", R_A: str = "R_A", R_S: str = "R_S") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_p_w_form_d`."""
    return (10*((pl.col(R_A).sqrt() + pl.col(R_S))/pl.col(G)))


def calc_delta_alpha_alpha_form_e(C: float, D: float, S: float, T: float, V: float, alpha: float, e: float, m: float, omega: float, q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    (\Delta \alpha )/\alpha  = T2*[q*S*V*e*CD\alpha ]/[2*m*(D*\omega 2)2]
    $$

    Args:
        C (float): Input parameter `C`.
        D (float): Input parameter `D`.
        S (float): Input parameter `S`.
        T (float): Input parameter `T`.
        V (float): Input parameter `V`.
        alpha (float): Input parameter `alpha`.
        e (float): Input parameter `e`.
        m (float): Input parameter `m`.
        omega (float): Input parameter `omega`.
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float(((2*T)*((C*(D*alpha))*(e*(V*(S*q)))))/(((2*m)*(2*(D*(2*omega))))))


def expr_delta_alpha_alpha_form_e(C: str = "C", D: str = "D", S: str = "S", T: str = "T", V: str = "V", alpha: str = "alpha", e: str = "e", m: str = "m", omega: str = "omega", q: str = "q") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_alpha_alpha_form_e`."""
    return (((2*pl.col(T))*((pl.col(C)*(pl.col(D)*pl.col(alpha)))*(pl.col(e)*(pl.col(V)*(pl.col(S)*pl.col(q))))))/(((2*pl.col(m))*(2*(pl.col(D)*(2*pl.col(omega)))))))


def calc_x_t_0_form_e(c: float, de: float, t: float, tau: float, x: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    xt0 = \tau detz + (1 - \tau det)xc , \tau det = 0.3
    $$

    Args:
        c (float): Input parameter `c`.
        de (float): Input parameter `de`.
        t (float): Input parameter `t`.
        tau (float): Input parameter `tau`.
        x (float): Input parameter `x`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(c*x*(-de*t*tau + 1) + de*t*tau*z)


def expr_x_t_0_form_e(c: str = "c", de: str = "de", t: str = "t", tau: str = "tau", x: str = "x", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_t_0_form_e`."""
    return (pl.col(c)*pl.col(x)*(-pl.col(de)*pl.col(t)*pl.col(tau) + 1) + pl.col(de)*pl.col(t)*pl.col(tau)*pl.col(z))


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


def expr_b_p_egidi_(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_b_p_egidi_`."""
    return (pl.col(P))


def calc_q_s_m_y_form_1(T: float, gamma: float, h: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_17701.

    **Source**:
    - Title: Barrier Functions Against Safety Drift in Shared Control (2026)
    - Authors: M. Yusuf Uzun, Yildiray Yildiz
    - Citation Key: `arxiv_2609_17701`

    **KaTeX Formula**:
    $$
    Qsym = \gamma  h0hT 0 +h0hT 1 +h1hT 0 + \gamma  h1hT 1 +h1hT 2 +h2hT 1
    $$

    Args:
        T (float): Input parameter `T`.
        gamma (float): Input parameter `gamma`.
        h (float): Input parameter `h`.

    Returns:
        float: Calculated metric value.
    """
    return float(h*(2*(h*(1*T))) + (h*(1*(h*(2*T))) + (gamma*(h*(1*(h*(1*T)))) + (h*(1*(h*(0*T))) + (gamma*(h*(0*(h*(0*T)))) + h*(0*(h*(1*T))))))))


def expr_q_s_m_y_form_1(T: str = "T", gamma: str = "gamma", h: str = "h") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_s_m_y_form_1`."""
    return (pl.col(h)*(2*(pl.col(h)*(1*pl.col(T)))) + (pl.col(h)*(1*(pl.col(h)*(2*pl.col(T)))) + (pl.col(gamma)*(pl.col(h)*(1*(pl.col(h)*(1*pl.col(T))))) + (pl.col(h)*(1*(pl.col(h)*(0*pl.col(T)))) + (pl.col(gamma)*(pl.col(h)*(0*(pl.col(h)*(0*pl.col(T))))) + pl.col(h)*(0*(pl.col(h)*(1*pl.col(T)))))))))


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
    return float(a*i*p*s*t**2)


def expr_r_w_c_i_form_4(a: str = "a", i: str = "i", p: str = "p", s: str = "s", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_w_c_i_form_4`."""
    return (pl.col(a)*pl.col(i)*pl.col(p)*pl.col(s)*pl.col(t)**2)


def calc_n_f_d_f_a_i_l_form_2(N: float, a: float, f: float, i: float, l: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29142.

    **Source**:
    - Title: State-Dependent Objective Coordination for End-to-End Balance and Navigation (2026)
    - Authors: Xuhao Huang, Xitao Xu, Yuxin Zheng et al.
    - Citation Key: `arxiv_2610_29142`

    **KaTeX Formula**:
    $$
    NFDfail = 1 Nfail \sum  i\in Efail max(dT,i - dgoal , 0) max(d0,i - dgoal , \epsilon )
    $$

    Args:
        N (float): Input parameter `N`.
        a (float): Input parameter `a`.
        f (float): Input parameter `f`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*(f*(a*(i*l)))))


def expr_n_f_d_f_a_i_l_form_2(N: str = "N", a: str = "a", f: str = "f", i: str = "i", l: str = "l") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_n_f_d_f_a_i_l_form_2`."""
    return (1*(pl.col(N)*(pl.col(f)*(pl.col(a)*(pl.col(i)*pl.col(l))))))


def calc_alpha_c_form_2(alpha: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_26548.

    **Source**:
    - Title: Camera Calibration Using Inaccurate and Asynchronous Discrete GPS Trajectory from Drones (2026)
    - Authors: R. Yang, Y. Bar-Shalom, H. A. J. Huang
    - Citation Key: `arxiv_2608_26548`

    **KaTeX Formula**:
    $$
    c\alpha  = \cos\alpha , c\epsilon  = \cos \epsilon , c\rho  = \cos \rho
    $$

    Args:
        alpha (float): Input parameter `alpha`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.cos(alpha))


def expr_alpha_c_form_2(alpha: str = "alpha") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_alpha_c_form_2`."""
    return (math.cos(pl.col(alpha)))


def calc_psi_form_3(c: float, p: float, s: float, t: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_20558.

    **Source**:
    - Title: Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction (2026)
    - Authors: Songyang Liu, Shuai Li
    - Citation Key: `arxiv_2609_20558`

    **KaTeX Formula**:
    $$
    \Psi  =   c sup t,k , c work t , c knee t,k , dw  T t=1
    $$

    Args:
        c (float): Input parameter `c`.
        p (float): Input parameter `p`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(c*p*s*t*u)


def expr_psi_form_3(c: str = "c", p: str = "p", s: str = "s", t: str = "t", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_psi_form_3`."""
    return (pl.col(c)*pl.col(p)*pl.col(s)*pl.col(t)*pl.col(u))


def calc_omega_form_4(a: float, alpha: float, b: float, e: float, psi: float, r: float, t: float, v: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1610_03464.

    **Source**:
    - Title: Oblique Collisions of Baseballs and Softballs with a Bat (2016)
    - Authors: Jeffrey R. Kensrud, Alan M. Nathan, Lloyd V. Smith
    - Citation Key: `arxiv_1610_03464`

    **KaTeX Formula**:
    $$
    \omega  = (1 + ex) [ vbat \sin\psi  r(1 + rx)(1 + \alpha ) ]
    $$

    Args:
        a (float): Input parameter `a`.
        alpha (float): Input parameter `alpha`.
        b (float): Input parameter `b`.
        e (float): Input parameter `e`.
        psi (float): Input parameter `psi`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.
        v (float): Input parameter `v`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*b*t*v*(e*x + 1)*math.sin(psi*r*(alpha + 1)*(r*x + 1)))


def expr_omega_form_4(a: str = "a", alpha: str = "alpha", b: str = "b", e: str = "e", psi: str = "psi", r: str = "r", t: str = "t", v: str = "v", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_omega_form_4`."""
    return (pl.col(a)*pl.col(b)*pl.col(t)*pl.col(v)*(pl.col(e)*pl.col(x) + 1)*math.sin(pl.col(psi)*pl.col(r)*(pl.col(alpha) + 1)*(pl.col(r)*pl.col(x) + 1)))


def calc_f_s_form_4(b: float, tau: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_06739.

    **Source**:
    - Title: The profit-bias identity in sports betting: bookmaker profit as the public's prediction error (2026)
    - Authors: Jacek P. Dmochowski
    - Citation Key: `arxiv_2609_06739`

    **KaTeX Formula**:
    $$
    F * (s) = \tau  - bv,L(s) bh,L(s) - bv,L(s) \in  [0, 1]
    $$

    Args:
        b (float): Input parameter `b`.
        tau (float): Input parameter `tau`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(-b*v + tau)


def expr_f_s_form_4(b: str = "b", tau: str = "tau", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_s_form_4`."""
    return (-pl.col(b)*pl.col(v) + pl.col(tau))


def calc_val_2609_05500_form_f(p: float, partial: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_05500.

    **Source**:
    - Title: Performance comparison of tethered and self-propelled models of fish locomotion using unsteady thin airfoil theory (2026)
    - Authors: Anshul Nayak, Emad Masroor, Hodjat Pendar
    - Citation Key: `arxiv_2609_05500`

    **KaTeX Formula**:
    $$
    \partial  \partial t \gamma (s, t) + \partial  \partial s (vrel\gamma (s, t)) = \partial  \partial s [p](s, t), 0 < s < 1
    $$

    Args:
        p (float): Input parameter `p`.
        partial (float): Input parameter `partial`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(partial*(partial*(p*s)))


def expr_val_2609_05500_form_f(p: str = "p", partial: str = "partial", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_05500_form_f`."""
    return (pl.col(partial)*(pl.col(partial)*(pl.col(p)*pl.col(s))))


def calc_a_0_form_5(gamma: float, h: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_17701.

    **Source**:
    - Title: Barrier Functions Against Safety Drift in Shared Control (2026)
    - Authors: M. Yusuf Uzun, Yildiray Yildiz
    - Citation Key: `arxiv_2609_17701`

    **KaTeX Formula**:
    $$
    a0 = h1 +\gamma  h0, a1 = h0 +h2 +\gamma  h1, a2 = h1 \in  Rn, (31b)
    $$

    Args:
        gamma (float): Input parameter `gamma`.
        h (float): Input parameter `h`.

    Returns:
        float: Calculated metric value.
    """
    return float(gamma*(0*h) + 1*h)


def expr_a_0_form_5(gamma: str = "gamma", h: str = "h") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_0_form_5`."""
    return (pl.col(gamma)*(0*pl.col(h)) + 1*pl.col(h))


def calc_r_f_e_e_t_k_delta_q_form_5(L: float, g: float, o: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_02306.

    **Source**:
    - Title: Contact-Constrained Lower-Limb Joint-Offset Calibration for Humanoid Robots (2026)
    - Authors: Kaixiang Lu, Haiyu Lan, Chunxiao Qiao et al.
    - Citation Key: `arxiv_2609_02306`

    **KaTeX Formula**:
    $$
    rfeet k (\delta q) = Log((C * )-1Ck(\delta q)) \in  R6
    $$

    Args:
        L (float): Input parameter `L`.
        g (float): Input parameter `g`.
        o (float): Input parameter `o`.

    Returns:
        float: Calculated metric value.
    """
    return float(L*g*o)


def expr_r_f_e_e_t_k_delta_q_form_5(L: str = "L", g: str = "g", o: str = "o") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_f_e_e_t_k_delta_q_form_5`."""
    return (pl.col(L)*pl.col(g)*pl.col(o))


def calc_r_t_form_6(a: float, b: float, e: float, f: float, l: float, n: float, r: float, s: float, t: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29142.

    **Source**:
    - Title: State-Dependent Objective Coordination for End-to-End Balance and Navigation (2026)
    - Authors: Xuhao Huang, Xitao Xu, Yuxin Zheng et al.
    - Citation Key: `arxiv_2610_29142`

    **KaTeX Formula**:
    $$
    rt = \beta (st) rbal + (1 - \beta (st)) rnav + rsafe
    $$

    Args:
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        e (float): Input parameter `e`.
        f (float): Input parameter `f`.
        l (float): Input parameter `l`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*b*l*r*(math.gamma(s*t)**2/math.gamma(2*s*t)) + a*e*f*r*s + a*n*r*v*(1 - (math.gamma(s*t)**2/math.gamma(2*s*t))))


def expr_r_t_form_6(a: str = "a", b: str = "b", e: str = "e", f: str = "f", l: str = "l", n: str = "n", r: str = "r", s: str = "s", t: str = "t", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_t_form_6`."""
    return (pl.col(a)*pl.col(b)*pl.col(l)*pl.col(r)*(math.gamma(pl.col(s)*pl.col(t))**2/math.gamma(2*pl.col(s)*pl.col(t))) + pl.col(a)*pl.col(e)*pl.col(f)*pl.col(r)*pl.col(s) + pl.col(a)*pl.col(n)*pl.col(r)*pl.col(v)*(1 - (math.gamma(pl.col(s)*pl.col(t))**2/math.gamma(2*pl.col(s)*pl.col(t)))))


def calc_e_0_y_4_theta_form_6(A: float, sigma: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    E0(Y 4 ( \theta )) = 3\sigma 4A
    $$

    Args:
        A (float): Input parameter `A`.
        sigma (float): Input parameter `sigma`.

    Returns:
        float: Calculated metric value.
    """
    return float(12*A*sigma)


def expr_e_0_y_4_theta_form_6(A: str = "A", sigma: str = "sigma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_0_y_4_theta_form_6`."""
    return (12*pl.col(A)*pl.col(sigma))


def calc_v_mu_form_d(mu: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_06635.

    **Source**:
    - Title: Modelling Athletic Ageing Relative to an Estimated Performance Envelope (2026)
    - Authors: Dae-Jin Lee
    - Citation Key: `arxiv_2608_06635`

    **KaTeX Formula**:
    $$
    V (\mu ) = \mu 3 (1 - \mu )3
    $$

    Args:
        mu (float): Input parameter `mu`.

    Returns:
        float: Calculated metric value.
    """
    return float(mu*(9 - 9*mu))


def expr_v_mu_form_d(mu: str = "mu") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_mu_form_d`."""
    return (pl.col(mu)*(9 - 9*pl.col(mu)))


def calc_v_x_t_form_f(i: float, v: float, xi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    v(x, t) = (1 - \xi )vi + \xi vi+1, w(x, t) = (1 - \xi )wi + \xi wi+1
    $$

    Args:
        i (float): Input parameter `i`.
        v (float): Input parameter `v`.
        xi (float): Input parameter `xi`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*v*xi + i*v*(1 - xi) + 1)


def expr_v_x_t_form_f(i: str = "i", v: str = "v", xi: str = "xi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_x_t_form_f`."""
    return (pl.col(i)*pl.col(v)*pl.col(xi) + pl.col(i)*pl.col(v)*(1 - pl.col(xi)) + 1)


def calc_e_0_y_theta_4_form_8(A: float, e: float, kappa: float, sigma: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    E0(Y ( \theta )4 ) = 3\sigma 2A +\kappa e-2\theta 2 1 |2 /\Lambda 2 \sum  n 1 (n!)2 \theta 4n 1
    $$

    Args:
        A (float): Input parameter `A`.
        e (float): Input parameter `e`.
        kappa (float): Input parameter `kappa`.
        sigma (float): Input parameter `sigma`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(6*A*sigma + e*kappa - 42*theta)


def expr_e_0_y_theta_4_form_8(A: str = "A", e: str = "e", kappa: str = "kappa", sigma: str = "sigma", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_0_y_theta_4_form_8`."""
    return (6*pl.col(A)*pl.col(sigma) + pl.col(e)*pl.col(kappa) - 42*pl.col(theta))


def calc_phi_form_e(v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_06739.

    **Source**:
    - Title: The profit-bias identity in sports betting: bookmaker profit as the public's prediction error (2026)
    - Authors: Jacek P. Dmochowski
    - Citation Key: `arxiv_2609_06739`

    **KaTeX Formula**:
    $$
    \phi  = 1 1 + v . (S7)
    $$

    Args:
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(v + 11)


def expr_phi_form_e(v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_phi_form_e`."""
    return (pl.col(v) + 11)


def calc_e_z_h_t_form_f(N: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    ez(th) = 1 N + 1 N\sum  i=0 |zfr(i; th) - znf (i; th)|
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*N + 1*N)


def expr_e_z_h_t_form_f(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_z_h_t_form_f`."""
    return (1*pl.col(N) + 1*pl.col(N))


def calc_w_z_form_f(N: float, U: float, i: float, pi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_05500.

    **Source**:
    - Title: Performance comparison of tethered and self-propelled models of fish locomotion using unsteady thin airfoil theory (2026)
    - Authors: Anshul Nayak, Emad Masroor, Hodjat Pendar
    - Citation Key: `arxiv_2609_05500`

    **KaTeX Formula**:
    $$
    w(z) = U0 + 1 2\pi i N\sum  j=1 \Gamma j z - zj
    $$

    Args:
        N (float): Input parameter `N`.
        U (float): Input parameter `U`.
        i (float): Input parameter `i`.
        pi (float): Input parameter `pi`.

    Returns:
        float: Calculated metric value.
    """
    return float(0*U + 12*(pi*(N*i)))


def expr_w_z_form_f(N: str = "N", U: str = "U", i: str = "i", pi: str = "pi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_z_form_f`."""
    return (0*pl.col(U) + 12*(pl.col(pi)*(pl.col(N)*pl.col(i))))


def calc_n_w_s_form_f(n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    Nw(s) = n\sum  i=1 [H(s - (i - 1)l) - H(s - il) ]N (i) w (s)
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(n)


def expr_n_w_s_form_f(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_n_w_s_form_f`."""
    return (pl.col(n))


def calc_eta_m_form_8(C: float, k: float, m: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_11476.

    **Source**:
    - Title: 3D Euler-Angle Orientation Control for Two-Ray Fading Mitigation in Maritime Air-to-Sea Communications (2026)
    - Authors: Mohammed Bajja, Abdoul Karim A. H. Saliah, Hajar El Hammouti et al.
    - Citation Key: `arxiv_2609_11476`

    **KaTeX Formula**:
    $$
    \eta m = Cm |k|2 k
    $$

    Args:
        C (float): Input parameter `C`.
        k (float): Input parameter `k`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*C*k*m*abs(k))


def expr_eta_m_form_8(C: str = "C", k: str = "k", m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_eta_m_form_8`."""
    return (2*pl.col(C)*pl.col(k)*pl.col(m)*abs(pl.col(k)))


def calc_g_r_form_b(n: float, t: float, u: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_20558.

    **Source**:
    - Title: Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction (2026)
    - Authors: Songyang Liu, Shuai Li
    - Citation Key: `arxiv_2609_20558`

    **KaTeX Formula**:
    $$
    RG =   tu tv n
    $$

    Args:
        n (float): Input parameter `n`.
        t (float): Input parameter `t`.
        u (float): Input parameter `u`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(n*t**2*u*v)


def expr_g_r_form_b(n: str = "n", t: str = "t", u: str = "u", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_r_form_b`."""
    return (pl.col(n)*pl.col(t)**2*pl.col(u)*pl.col(v))


def calc_o_t_form_c(c: float, e: float, f: float, r: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_20558.

    **Source**:
    - Title: Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction (2026)
    - Authors: Songyang Liu, Shuai Li
    - Citation Key: `arxiv_2609_20558`

    **KaTeX Formula**:
    $$
    ot =   c ref t , R ref,b t , ω b t , qt - q0,  qt , at-1
    $$

    Args:
        c (float): Input parameter `c`.
        e (float): Input parameter `e`.
        f (float): Input parameter `f`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(c*e*f*r*t)


def expr_o_t_form_c(c: str = "c", e: str = "e", f: str = "f", r: str = "r", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_o_t_form_c`."""
    return (pl.col(c)*pl.col(e)*pl.col(f)*pl.col(r)*pl.col(t))


def calc_e_c_e_guo_20(M: float) -> float:
    r"""Compute mathematical metric extracted from guo_2017_calibration.

    **Source**:
    - Title: arxiv1706.04599
    - Authors: Scientific Literature
    - Citation Key: `guo_2017_calibration`

    **KaTeX Formula**:
    $$
    ECE = M\sum  m=1 |Bm| n |||| acc(Bm) - conf (Bm)||||
    $$

    Args:
        M (float): Input parameter `M`.

    Returns:
        float: Calculated metric value.
    """
    return float(M)


def expr_e_c_e_guo_20(M: str = "M") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_c_e_guo_20`."""
    return (pl.col(M))


def calc_miller2005_82322c(R_A: float, R_S: float, beta: float, gamma: float) -> float:
    r"""Compute mathematical metric extracted from miller2005.

    **Source**:
    - Title: A Derivation of the Pythagorean Expectation for Baseball (2005)
    - Authors: Steven J. Miller
    - Citation Key: `miller2005`

    **KaTeX Formula**:
    $$
    Won-Loss Percentage(R_{S},R_{A}, \beta , \gamma ) = (R_{S} - \beta )\gamma  (R_{S} - \beta )\gamma  + (R_{A} - \beta )\gamma
    $$

    Args:
        R_A (float): Input parameter `R_A`.
        R_S (float): Input parameter `R_S`.
        beta (float): Input parameter `beta`.
        gamma (float): Input parameter `gamma`.

    Returns:
        float: Calculated metric value.
    """
    return float(gamma*(R_A - beta) + (gamma*math.gamma(R_S - beta))*(R_S - beta))


def expr_miller2005_82322c(R_A: str = "R_A", R_S: str = "R_S", beta: str = "beta", gamma: str = "gamma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_miller2005_82322c`."""
    return (pl.col(gamma)*(pl.col(R_A) - pl.col(beta)) + (pl.col(gamma)*math.gamma(pl.col(R_S) - pl.col(beta)))*(pl.col(R_S) - pl.col(beta)))


def calc_k_p_form_0(k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_05500.

    **Source**:
    - Title: Performance comparison of tethered and self-propelled models of fish locomotion using unsteady thin airfoil theory (2026)
    - Authors: Anshul Nayak, Emad Masroor, Hodjat Pendar
    - Citation Key: `arxiv_2609_05500`

    **KaTeX Formula**:
    $$
    [p]k = k\sum  j=1 \Gamma j + vrel,k\Gamma k lk + c
    $$

    Args:
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(k)


def expr_k_p_form_0(k: str = "k") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_p_form_0`."""
    return (pl.col(k))


def calc_s_p_x_gneiti(P: float, S: float, a: float, de: float, g: float, i: float, m: float, mu: float, t: float, x: float) -> float:
    r"""Compute mathematical metric extracted from gneiting_raftery_2007_jasa.

    **Source**:
    - Title: gneiting2007jasa
    - Authors: Scientific Literature
    - Citation Key: `gneiting_raftery_2007_jasa`

    **KaTeX Formula**:
    $$
    S(P, x) = - \log det Sigma1P - (x - \mu P) ' Sigma1 -1 P (x-\mu P)
    $$

    Args:
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.
        a (float): Input parameter `a`.
        de (float): Input parameter `de`.
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        mu (float): Input parameter `mu`.
        t (float): Input parameter `t`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(-(-P*mu + x) - math.log(de*(t*(S*(i*(g*(m*((1*P)*a)))))), math.e))


def expr_s_p_x_gneiti(P: str = "P", S: str = "S", a: str = "a", de: str = "de", g: str = "g", i: str = "i", m: str = "m", mu: str = "mu", t: str = "t", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_p_x_gneiti`."""
    return (-(-pl.col(P)*pl.col(mu) + pl.col(x)) - (pl.col(de).log()*(pl.col(t)*(pl.col(S)*(pl.col(i)*(pl.col(g)*(pl.col(m)*((1*pl.col(P))*pl.col(a))))))), math.e))


def calc_t_k_form_7(S: float, alpha: float, k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    T k = \alpha 0 + \alpha 1Sk 1 + \cdot  \cdot  \cdot  +\alpha 8Sk 8 + \epsilon k
    $$

    Args:
        S (float): Input parameter `S`.
        alpha (float): Input parameter `alpha`.
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(alpha*(1*(S*(1*k))) + 0*alpha)


def expr_t_k_form_7(S: str = "S", alpha: str = "alpha", k: str = "k") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_k_form_7`."""
    return (pl.col(alpha)*(1*(pl.col(S)*(1*pl.col(k)))) + 0*pl.col(alpha))


def calc_f_alpha_s_form_d(alpha: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    F\alpha (s) = \alpha 1s1 + \cdot  \cdot  \cdot  + \alpha dsd
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(alpha*s)


def expr_f_alpha_s_form_d(alpha: str = "alpha", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_alpha_s_form_d`."""
    return (pl.col(alpha)*pl.col(s))


def calc_l_guo_20(n: float) -> float:
    r"""Compute mathematical metric extracted from guo_2017_calibration.

    **Source**:
    - Title: arxiv1706.04599
    - Authors: Scientific Literature
    - Citation Key: `guo_2017_calibration`

    **KaTeX Formula**:
    $$
    L =- n\sum  i=1 K\sum  k=1 q(zi)(k) \log q(zi)(k) + \lambda  n\sum  i=1 [ K\sum  k=1 z(k) i q(zi)(k) - z(yi) i ] + n\sum  i=1 \beta i K\sum  k=1(q(zi)(k) - 1)
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(-n)


def expr_l_guo_20(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_guo_20`."""
    return (-pl.col(n))


def calc_i_m_i_n_n_i_u_form_4(N: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    min {ui}N-1 i=0 N-1 \sum  i=0 l(xi, ui) + lf (xN )
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(0*N - 1)


def expr_i_m_i_n_n_i_u_form_4(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_m_i_n_n_i_u_form_4`."""
    return (0*pl.col(N) - 1)


def calc_k_m_i_n_n_k_u_form_4(N: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    min {uk}N-1 k=0 N-1 \sum  k=0 l(xk, uk) + lf (xN ) s.t. xk+1 = fd(xk, uk), x0 = x(tk), uk \in  U, xk \in  X
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(0*N - 1)


def expr_k_m_i_n_n_k_u_form_4(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_m_i_n_n_k_u_form_4`."""
    return (0*pl.col(N) - 1)


def calc_f_q_s_form_4(D: float, K: float, L: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_28203.

    **Source**:
    - Title: JAXbounce: A Continuous-Control Pong-Like Benchmark for Active Inference Beyond Low Dimensional Environments (2026)
    - Authors: Chaitanya Kaul, Markus Klar, Sebastian Stein et al.
    - Citation Key: `arxiv_2610_28203`

    **KaTeX Formula**:
    $$
    F(Qs ) =DKL(Qs | Qst+1 ) +EQsQk[-\log p(ot+1 | x,\sigma o)]
    $$

    Args:
        D (float): Input parameter `D`.
        K (float): Input parameter `K`.
        L (float): Input parameter `L`.

    Returns:
        float: Calculated metric value.
    """
    return float(D*(K*L))


def expr_f_q_s_form_4(D: str = "D", K: str = "K", L: str = "L") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_q_s_form_4`."""
    return (pl.col(D)*(pl.col(K)*pl.col(L)))


def calc_w_delta_form_5(a: float, delta: float, gamma: float, psi: float, tau: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    \delta W = \tau w \delta \psi  + \tau a \delta \gamma , \psi  = s r + \theta
    $$

    Args:
        a (float): Input parameter `a`.
        delta (float): Input parameter `delta`.
        gamma (float): Input parameter `gamma`.
        psi (float): Input parameter `psi`.
        tau (float): Input parameter `tau`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(tau*(a*(delta*gamma)) + tau*(w*(delta*psi)))


def expr_w_delta_form_5(a: str = "a", delta: str = "delta", gamma: str = "gamma", psi: str = "psi", tau: str = "tau", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_delta_form_5`."""
    return (pl.col(tau)*(pl.col(a)*(pl.col(delta)*pl.col(gamma))) + pl.col(tau)*(pl.col(w)*(pl.col(delta)*pl.col(psi))))


def calc_phi_v_i_r_t_form_5(alpha: float, k: float, o: float, phi: float, r: float, t: float, tau: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_20645.

    **Source**:
    - Title: TACT-ful: Multi-Channel Terrain Affordance and Compliance Training for Payload-Robust Perceptive Humanoid Locomotion (2026)
    - Authors: Thanh Ly, Truong-Duy Dang, Chien Le et al.
    - Citation Key: `arxiv_2606_20645`

    **KaTeX Formula**:
    $$
    \phi *virt = \alpha \phi  \tau y krot , \psi * virt = \alpha \psi  \tau x krot
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        k (float): Input parameter `k`.
        o (float): Input parameter `o`.
        phi (float): Input parameter `phi`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.
        tau (float): Input parameter `tau`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(alpha*k*o*phi*r*t*tau*y)


def expr_phi_v_i_r_t_form_5(alpha: str = "alpha", k: str = "k", o: str = "o", phi: str = "phi", r: str = "r", t: str = "t", tau: str = "tau", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_phi_v_i_r_t_form_5`."""
    return (pl.col(alpha)*pl.col(k)*pl.col(o)*pl.col(phi)*pl.col(r)*pl.col(t)*pl.col(tau)*pl.col(y))


def calc_e_a_m_form_6(Z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    E(Am) = -Z -1 \int  (\prod  a dka 2\pi  ) \exp [- \sum  b \sigma 2A 2 (Tm( \theta b)kb)2 + i \sum  b kbyb - \sigma 2A 2 \sum  ab ka\Delta abkb] (36) \int  \prod  i dAi \sqrt 2\pi \sigma 2A  i\sigma 2A (\sum  c T m( \theta c)kc) \exp - \sum  l A2l 2\sigma 2A
    $$

    Args:
        Z (float): Input parameter `Z`.

    Returns:
        float: Calculated metric value.
    """
    return float(-Z - 1)


def expr_e_a_m_form_6(Z: str = "Z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_a_m_form_6`."""
    return (-pl.col(Z) - 1)


def calc_theta_form_7(m: float, o: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_26548.

    **Source**:
    - Title: Camera Calibration Using Inaccurate and Asynchronous Discrete GPS Trajectory from Drones (2026)
    - Authors: R. Yang, Y. Bar-Shalom, H. A. J. Huang
    - Citation Key: `arxiv_2608_26548`

    **KaTeX Formula**:
    $$
    \theta  = [32o 4.1o 2.3o 10m 1.35s]'
    $$

    Args:
        m (float): Input parameter `m`.
        o (float): Input parameter `o`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(4073.76*m*o**3*s)


def expr_theta_form_7(m: str = "m", o: str = "o", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_theta_form_7`."""
    return (4073.76*pl.col(m)*pl.col(o)**3*pl.col(s))


def calc_d_form_9(R: float, psi: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1610_03464.

    **Source**:
    - Title: Oblique Collisions of Baseballs and Softballs with a Bat (2016)
    - Authors: Jeffrey R. Kensrud, Alan M. Nathan, Lloyd V. Smith
    - Citation Key: `arxiv_1610_03464`

    **KaTeX Formula**:
    $$
    D = (r +R) \sin\psi
    $$

    Args:
        R (float): Input parameter `R`.
        psi (float): Input parameter `psi`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float((R + r)*math.sin(psi))


def expr_d_form_9(R: str = "R", psi: str = "psi", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_form_9`."""
    return ((pl.col(R) + pl.col(r))*math.sin(pl.col(psi)))


def calc_db_tau_form_9(B: float, C: float, D: float, R: float, c: float, dB: float, e: float, gamma: float, r: float, rho: float, tau: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1709_07969.

    **Source**:
    - Title: Optimal-power Configurations for Hover Solutions in Mono-spinners (2017)
    - Authors: Mojtaba Hedayatpour, Mehran Mehrandezh, Farrokh Janabi-Sharifi
    - Citation Key: `arxiv_1709_07969`

    **KaTeX Formula**:
    $$
    \tau  dB = ( 1 4 \rho  cBCDB R 4 Br 2 - \gamma  r)e\tau dB
    $$

    Args:
        B (float): Input parameter `B`.
        C (float): Input parameter `C`.
        D (float): Input parameter `D`.
        R (float): Input parameter `R`.
        c (float): Input parameter `c`.
        dB (float): Input parameter `dB`.
        e (float): Input parameter `e`.
        gamma (float): Input parameter `gamma`.
        r (float): Input parameter `r`.
        rho (float): Input parameter `rho`.
        tau (float): Input parameter `tau`.

    Returns:
        float: Calculated metric value.
    """
    return float((e*(dB*tau))*(-gamma*r + 14*(rho*(c*(B*(C*(D*(B*(R*(4*(B*(2*r))))))))))))


def expr_db_tau_form_9(B: str = "B", C: str = "C", D: str = "D", R: str = "R", c: str = "c", dB: str = "dB", e: str = "e", gamma: str = "gamma", r: str = "r", rho: str = "rho", tau: str = "tau") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_db_tau_form_9`."""
    return ((pl.col(e)*(pl.col(dB)*pl.col(tau)))*(-pl.col(gamma)*pl.col(r) + 14*(pl.col(rho)*(pl.col(c)*(pl.col(B)*(pl.col(C)*(pl.col(D)*(pl.col(B)*(pl.col(R)*(4*(pl.col(B)*(2*pl.col(r)))))))))))))


def calc_l_y_k_u_form_1(H: float, Y: float, d: float, dq: float, e: float, h: float, l: float, q: float, sim: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27057.

    **Source**:
    - Title: Probing Lepton Flavor Violation at FCC-ee (2026)
    - Authors: L. Allwicher, R. Bartocci, M. Cepeda et al.
    - Citation Key: `arxiv_2610_27057`

    **KaTeX Formula**:
    $$
    LYuk = -Yu  q \sim Hu - Yd  qHd - Ye lHe + h.c. , (A1)
    $$

    Args:
        H (float): Input parameter `H`.
        Y (float): Input parameter `Y`.
        d (float): Input parameter `d`.
        dq (float): Input parameter `dq`.
        e (float): Input parameter `e`.
        h (float): Input parameter `h`.
        l (float): Input parameter `l`.
        q (float): Input parameter `q`.
        sim (float): Input parameter `sim`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(-H*Y*d*dq - H*Y*e**2*l - H*Y*q*sim*u**2 + h)


def expr_l_y_k_u_form_1(H: str = "H", Y: str = "Y", d: str = "d", dq: str = "dq", e: str = "e", h: str = "h", l: str = "l", q: str = "q", sim: str = "sim", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_y_k_u_form_1`."""
    return (-pl.col(H)*pl.col(Y)*pl.col(d)*pl.col(dq) - pl.col(H)*pl.col(Y)*pl.col(e)**2*pl.col(l) - pl.col(H)*pl.col(Y)*pl.col(q)*pl.col(sim)*pl.col(u)**2 + pl.col(h))


def calc_partial_x_c_k_epsilon_partial_form_a(Delta: float, alpha: float, c: float, epsilon: float, k: float, rho: float, s: float, x: float, y: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_26548.

    **Source**:
    - Title: Camera Calibration Using Inaccurate and Asynchronous Discrete GPS Trajectory from Drones (2026)
    - Authors: R. Yang, Y. Bar-Shalom, H. A. J. Huang
    - Citation Key: `arxiv_2608_26548`

    **KaTeX Formula**:
    $$
    \partial xCk \partial \epsilon  = \Delta xks\alpha c\epsilon s\rho  +\Delta ykc\alpha c\epsilon s\rho  +\Delta zks\epsilon c\rho
    $$

    Args:
        Delta (float): Input parameter `Delta`.
        alpha (float): Input parameter `alpha`.
        c (float): Input parameter `c`.
        epsilon (float): Input parameter `epsilon`.
        k (float): Input parameter `k`.
        rho (float): Input parameter `rho`.
        s (float): Input parameter `s`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(Delta*alpha*c**2*epsilon*k*rho*s*y + Delta*alpha*c*epsilon*k*rho*s**2*x + Delta*c*epsilon*k*rho*s*z)


def expr_partial_x_c_k_epsilon_partial_form_a(Delta: str = "Delta", alpha: str = "alpha", c: str = "c", epsilon: str = "epsilon", k: str = "k", rho: str = "rho", s: str = "s", x: str = "x", y: str = "y", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_partial_x_c_k_epsilon_partial_form_a`."""
    return (pl.col(Delta)*pl.col(alpha)*pl.col(c)**2*pl.col(epsilon)*pl.col(k)*pl.col(rho)*pl.col(s)*pl.col(y) + pl.col(Delta)*pl.col(alpha)*pl.col(c)*pl.col(epsilon)*pl.col(k)*pl.col(rho)*pl.col(s)**2*pl.col(x) + pl.col(Delta)*pl.col(c)*pl.col(epsilon)*pl.col(k)*pl.col(rho)*pl.col(s)*pl.col(z))


def calc_e_t_form_b(J: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_20558.

    **Source**:
    - Title: Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction (2026)
    - Authors: Songyang Liu, Shuai Li
    - Citation Key: `arxiv_2609_20558`

    **KaTeX Formula**:
    $$
    et = 1 J J\sum  j =1      p B t, j - p B,ref t, j       2 , J = 14
    $$

    Args:
        J (float): Input parameter `J`.

    Returns:
        float: Calculated metric value.
    """
    return float(J**2)


def expr_e_t_form_b(J: str = "J") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_t_form_b`."""
    return (pl.col(J)**2)


def calc_a_s_h_0_di_f_f_i_c_u_l_t_form_b(epsilon: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    A S (h0, difficult) = -(1- \epsilon )(1-2\epsilon ), A S (h0, safe) = \epsilon (1-2\epsilon )
    $$

    Args:
        epsilon (float): Input parameter `epsilon`.

    Returns:
        float: Calculated metric value.
    """
    return float((1 - 2*epsilon)*(epsilon - 1))


def expr_a_s_h_0_di_f_f_i_c_u_l_t_form_b(epsilon: str = "epsilon") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_s_h_0_di_f_f_i_c_u_l_t_form_b`."""
    return ((1 - 2*pl.col(epsilon))*(pl.col(epsilon) - 1))


def calc_i_b_a_l_l_form_e(alpha: float, m: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1610_03464.

    **Source**:
    - Title: Oblique Collisions of Baseballs and Softballs with a Bat (2016)
    - Authors: Jeffrey R. Kensrud, Alan M. Nathan, Lloyd V. Smith
    - Citation Key: `arxiv_1610_03464`

    **KaTeX Formula**:
    $$
    Iball = \alpha mr2
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        m (float): Input parameter `m`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*alpha*m*r)


def expr_i_b_a_l_l_form_e(alpha: str = "alpha", m: str = "m", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_b_a_l_l_form_e`."""
    return (2*pl.col(alpha)*pl.col(m)*pl.col(r))


def calc_s_s_k_i_l_l_n_gneiti(S: float, c: float, e: float, f: float, n: float, o: float, p: float, r: float, s: float, t: float) -> float:
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
    return float(-S*r*(e*(f*n)) + (S*(f*(c*(s*(n*t)))) - S*r*(e*(f*(n*(S*(o*(p*(n*t)))))))))


def expr_s_s_k_i_l_l_n_gneiti(S: str = "S", c: str = "c", e: str = "e", f: str = "f", n: str = "n", o: str = "o", p: str = "p", r: str = "r", s: str = "s", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_s_k_i_l_l_n_gneiti`."""
    return (-pl.col(S)*pl.col(r)*(pl.col(e)*(pl.col(f)*pl.col(n))) + (pl.col(S)*(pl.col(f)*(pl.col(c)*(pl.col(s)*(pl.col(n)*pl.col(t))))) - pl.col(S)*pl.col(r)*(pl.col(e)*(pl.col(f)*(pl.col(n)*(pl.col(S)*(pl.col(o)*(pl.col(p)*(pl.col(n)*pl.col(t))))))))))


def calc_r_u_form_2(A: float, L: float, f: float, nabla: float, nu: float, p: float, partial: float, t: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_27423.

    **Source**:
    - Title: High-order stabilized matrix-free simulation of rotating mixing devices using the Mortar Element Method (2026)
    - Authors: B. Campos, P. Munch, V. O. Ferreira et al.
    - Citation Key: `arxiv_2608_27423`

    **KaTeX Formula**:
    $$
    Ru = \partial tu + (u \cdot  \nabla )u - (uALE \cdot  \nabla )u + \nabla p* - \nu \nabla 2u - f
    $$

    Args:
        A (float): Input parameter `A`.
        L (float): Input parameter `L`.
        f (float): Input parameter `f`.
        nabla (float): Input parameter `nabla`.
        nu (float): Input parameter `nu`.
        p (float): Input parameter `p`.
        partial (float): Input parameter `partial`.
        t (float): Input parameter `t`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(-math.e*A*L*nabla*u**2 - f - 2*nabla**2*nu*p*u + nabla*u**2 + partial*t*u)


def expr_r_u_form_2(A: str = "A", L: str = "L", f: str = "f", nabla: str = "nabla", nu: str = "nu", p: str = "p", partial: str = "partial", t: str = "t", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_u_form_2`."""
    return (-math.e*pl.col(A)*pl.col(L)*pl.col(nabla)*pl.col(u)**2 - pl.col(f) - 2*pl.col(nabla)**2*pl.col(nu)*pl.col(p)*pl.col(u) + pl.col(nabla)*pl.col(u)**2 + pl.col(partial)*pl.col(t)*pl.col(u))


def calc_val_2610_27057_form_2(C: float, g: float, i: float, j: float, k: float, l: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27057.

    **Source**:
    - Title: Probing Lepton Flavor Violation at FCC-ee (2026)
    - Authors: L. Allwicher, R. Bartocci, M. Cepeda et al.
    - Citation Key: `arxiv_2610_27057`

    **KaTeX Formula**:
    $$
    +C ll kjik +2C ll kkij  C (3) Hl ij = + g2 2 48\pi 2 (C ll ikkj +C ll kjik ) + \cdot  \cdot  \cdot  , (B6)  CHe ij = - g2 1 24\pi 2 (C ee ijkk +C ee ikkj +C ee kjik
    $$

    Args:
        C (float): Input parameter `C`.
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.
        k (float): Input parameter `k`.
        l (float): Input parameter `l`.

    Returns:
        float: Calculated metric value.
    """
    return float(8992*math.pi*C*g*i*j*k**2*l**2)


def expr_val_2610_27057_form_2(C: str = "C", g: str = "g", i: str = "i", j: str = "j", k: str = "k", l: str = "l") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_27057_form_2`."""
    return (8992*math.pi*pl.col(C)*pl.col(g)*pl.col(i)*pl.col(j)*pl.col(k)**2*pl.col(l)**2)


def calc_val_2609_24299_form_2(Q: float, q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    d dt ( \partial L \partial  q ) - \partial L \partial q +Cc q =Qq
    $$

    Args:
        Q (float): Input parameter `Q`.
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float(Q*q)


def expr_val_2609_24299_form_2(Q: str = "Q", q: str = "q") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_24299_form_2`."""
    return (pl.col(Q)*pl.col(q))


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
    return float(1*(1 - c))


def expr_s_c_p_1_gneiti(c: str = "c") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_c_p_1_gneiti`."""
    return (1*(1 - pl.col(c)))


def calc_g_p_gneiti(P: float, S: float, a: float, de: float, g: float, i: float, m: float, t: float) -> float:
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
        m (float): Input parameter `m`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(-m - math.log(de*(t*(S*(i*(g*(m*((1*P)*a)))))), math.e))


def expr_g_p_gneiti(P: str = "P", S: str = "S", a: str = "a", de: str = "de", g: str = "g", i: str = "i", m: str = "m", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_p_gneiti`."""
    return (-pl.col(m) - (pl.col(de).log()*(pl.col(t)*(pl.col(S)*(pl.col(i)*(pl.col(g)*(pl.col(m)*((1*pl.col(P))*pl.col(a))))))), math.e))


def calc_val_2609_04690_form_2(S: float, a: float, f: float, m: float, o: float, t: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_04690.

    **Source**:
    - Title: Enhancing Multimodal Emotion Recognition via Multi-Feature Encoding and Attention-Based Fusion (2026)
    - Authors: Xu Lin, Ke Wang, Hui Kang et al.
    - Citation Key: `arxiv_2609_04690`

    **KaTeX Formula**:
    $$
    CrossAttention(XA, XV ) = Softmax( QV K^T A \sqrt dV )VA
    $$

    Args:
        S (float): Input parameter `S`.
        a (float): Input parameter `a`.
        f (float): Input parameter `f`.
        m (float): Input parameter `m`.
        o (float): Input parameter `o`.
        t (float): Input parameter `t`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(S*(o*(f*(t*(m*(a*x))))))


def expr_val_2609_04690_form_2(S: str = "S", a: str = "a", f: str = "f", m: str = "m", o: str = "o", t: str = "t", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_04690_form_2`."""
    return (pl.col(S)*(pl.col(o)*(pl.col(f)*(pl.col(t)*(pl.col(m)*(pl.col(a)*pl.col(x)))))))


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


def expr_b_gneiti(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_b_gneiti`."""
    return (pl.col(P))


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
    return float(-H*L*g*o)


def expr_l_o_b_g_gneiti(H: str = "H", L: str = "L", g: str = "g", o: str = "o") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_o_b_g_gneiti`."""
    return (-pl.col(H)*pl.col(L)*pl.col(g)*pl.col(o))


def calc_val_2609_24299_form_4(Q: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    d dt ( \partial L \partial   \theta  ) - \partial L \partial \theta  = Q\theta
    $$

    Args:
        Q (float): Input parameter `Q`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(Q*theta)


def expr_val_2609_24299_form_4(Q: str = "Q", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_24299_form_4`."""
    return (pl.col(Q)*pl.col(theta))


def calc_a_l_r_1_form_5(L: float, R: float, phi: float, psi: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_08746.

    **Source**:
    - Title: Kinematics of Single-Winged Spinning Seeds: A Study on Mahogany and Buddha Coconut Samaras (2026)
    - Authors: Yogeshwaran G, Srisha M. V. Rao, Jagadeesh G
    - Citation Key: `arxiv_2603_08746`

    **KaTeX Formula**:
    $$
    aLR 1 =  \cos \theta LR \cos \psi LR \sin \phi LR \sin \theta LR \cos \psi LR - \cos \phi LR \sin \psi LR \cos \phi LR \sin \theta LR \cos \psi LR + \sin \phi LR \sin \psi LR
    $$

    Args:
        L (float): Input parameter `L`.
        R (float): Input parameter `R`.
        phi (float): Input parameter `phi`.
        psi (float): Input parameter `psi`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.sin(L*R*phi)*math.sin(L*R*psi) + math.sin(L*R*phi)*math.sin(L*R*theta)*math.cos(L*R*psi)**2*math.cos(L*R*theta) - math.sin(L*R*psi)*math.sin(L*R*theta)*math.cos(L*R*phi)**2*math.cos(L*R*psi))


def expr_a_l_r_1_form_5(L: str = "L", R: str = "R", phi: str = "phi", psi: str = "psi", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_l_r_1_form_5`."""
    return (math.sin(pl.col(L)*pl.col(R)*pl.col(phi))*math.sin(pl.col(L)*pl.col(R)*pl.col(psi)) + math.sin(pl.col(L)*pl.col(R)*pl.col(phi))*math.sin(pl.col(L)*pl.col(R)*pl.col(theta))*math.cos(pl.col(L)*pl.col(R)*pl.col(psi))**2*math.cos(pl.col(L)*pl.col(R)*pl.col(theta)) - math.sin(pl.col(L)*pl.col(R)*pl.col(psi))*math.sin(pl.col(L)*pl.col(R)*pl.col(theta))*math.cos(pl.col(L)*pl.col(R)*pl.col(phi))**2*math.cos(pl.col(L)*pl.col(R)*pl.col(psi)))


def calc_u_form_4(nu: float, t: float, x: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_27423.

    **Source**:
    - Title: High-order stabilized matrix-free simulation of rotating mixing devices using the Mortar Element Method (2026)
    - Authors: B. Campos, P. Munch, V. O. Ferreira et al.
    - Citation Key: `arxiv_2608_27423`

    **KaTeX Formula**:
    $$
    u = \exp(-2\nu t) \cos(x) \sin(y)
    $$

    Args:
        nu (float): Input parameter `nu`.
        t (float): Input parameter `t`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.exp(-2*nu*t)*math.sin(y)*math.cos(x))


def expr_u_form_4(nu: str = "nu", t: str = "t", x: str = "x", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_form_4`."""
    return ((-2*pl.col(nu).exp()*pl.col(t))*math.sin(pl.col(y))*math.cos(pl.col(x)))


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
    return float((1 - Z*r)/(n - 1) - 1/(2*r))


def expr_s_2_harvey(Z: str = "Z", n: str = "n", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_2_harvey`."""
    return ((1 - pl.col(Z)*pl.col(r))/(pl.col(n) - 1) - 1/(2*pl.col(r)))


def calc_l_s_h_a_r_e_d_i_form_d(K: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    Lshared(i) = K\sum  s=1 KL(R(s) i |||Pi)
    $$

    Args:
        K (float): Input parameter `K`.

    Returns:
        float: Calculated metric value.
    """
    return float(K)


def expr_l_s_h_a_r_e_d_i_form_d(K: str = "K") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_s_h_a_r_e_d_i_form_d`."""
    return (pl.col(K))


def calc_c_v_a_r_alpha_x_c_form_3(eta: float, p: float, s: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_26568.

    **Source**:
    - Title: Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games (2026)
    - Authors: Durgam Latha, Dion Reji, Dorde Zikelic et al.
    - Citation Key: `arxiv_2610_26568`

    **KaTeX Formula**:
    $$
    CVaR\alpha (cX) = sup \eta ' {c\eta ' - 1\alpha  E[(c\eta ' - cX)+]} = c CVaR\alpha (X)
    $$

    Args:
        eta (float): Input parameter `eta`.
        p (float): Input parameter `p`.
        s (float): Input parameter `s`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(eta*p*s*u)


def expr_c_v_a_r_alpha_x_c_form_3(eta: str = "eta", p: str = "p", s: str = "s", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_v_a_r_alpha_x_c_form_3`."""
    return (pl.col(eta)*pl.col(p)*pl.col(s)*pl.col(u))


def calc_j_f_k_l_s_j_f_k_l_pi_form_a(H: float, eta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    JFKL(\pi ) - JFKL(S) = \eta H \sum t Eht\sim S(\cdot ) [\sum a T(a | ht) S(a | ht) v(a | ht)] + O(\eta 2 ), KL(S|\pi ) = \eta 2 2H \sum t Eht\sim S(\cdot ) [\sum a v(a | ht)2 S(a | ht) ] + O(\eta 3 )
    $$

    Args:
        H (float): Input parameter `H`.
        eta (float): Input parameter `eta`.

    Returns:
        float: Calculated metric value.
    """
    return float(H*eta)


def expr_j_f_k_l_s_j_f_k_l_pi_form_a(H: str = "H", eta: str = "eta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_f_k_l_s_j_f_k_l_pi_form_a`."""
    return (pl.col(H)*pl.col(eta))


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


def expr_val_1_12_2_harvey(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1_12_2_harvey`."""
    return (pl.col(n))


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
    return float(u*x)


def expr_c_i_maher_(u: str = "u", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_i_maher_`."""
    return (pl.col(u)*pl.col(x))


def calc_f_s_b_y_2005_0(e: float, n: float, p: float, t: float, y: float) -> float:
    r"""Compute mathematical metric extracted from 2005_07742.

    **Source**:
    - Title: SEAM methodology for context-rich player matchup evaluations (2020)
    - Authors: Julia Wapner, David Dalpiaz, Daniel J. Eck
    - Citation Key: `2005_07742`

    **KaTeX Formula**:
    $$
    fsb(y) = ntype \sum  t=1 \rho tfsb,t(y|xp,t)
    $$

    Args:
        e (float): Input parameter `e`.
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.
        t (float): Input parameter `t`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(e*n*p*t*y)


def expr_f_s_b_y_2005_0(e: str = "e", n: str = "n", p: str = "p", t: str = "t", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_s_b_y_2005_0`."""
    return (pl.col(e)*pl.col(n)*pl.col(p)*pl.col(t)*pl.col(y))


def calc_u_form_0(x: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_27423.

    **Source**:
    - Title: High-order stabilized matrix-free simulation of rotating mixing devices using the Mortar Element Method (2026)
    - Authors: B. Campos, P. Munch, V. O. Ferreira et al.
    - Citation Key: `arxiv_2608_27423`

    **KaTeX Formula**:
    $$
    u = -2 \sin(\pi x)2 \cos(\pi y) \sin(\pi y)
    $$

    Args:
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(-4*math.sin(math.pi*x)*math.sin(math.pi*y)*math.cos(math.pi*y))


def expr_u_form_0(x: str = "x", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_form_0`."""
    return (-4*math.sin(math.pi*pl.col(x))*math.sin(math.pi*pl.col(y))*math.cos(math.pi*pl.col(y)))


def calc_w_form_0(x: float, y: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_27423.

    **Source**:
    - Title: High-order stabilized matrix-free simulation of rotating mixing devices using the Mortar Element Method (2026)
    - Authors: B. Campos, P. Munch, V. O. Ferreira et al.
    - Citation Key: `arxiv_2608_27423`

    **KaTeX Formula**:
    $$
    w = 4\pi 2 [3 \cos(2\pi z) - 2] \sin(\pi x) \sin(\pi y) \cos(\pi x) \cos(\pi y) + 2\pi [\cos(\pi x)2 + \cos(\pi y)2 ] \sin(\pi x)2 \sin(\pi y)2 \sin(\pi z)3 \cos(\pi z), (42) p = 0
    $$

    Args:
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(24*math.pi*(2*math.cos(math.pi*x) + 2*math.cos(math.pi*y))*math.sin(math.pi*x)*math.sin(math.pi*y)*math.sin(math.pi*z)*math.cos(math.pi*z) + 8*math.pi*(3*math.cos(2*math.pi*z) - 2)*math.sin(math.pi*x)*math.sin(math.pi*y)*math.cos(math.pi*x)*math.cos(math.pi*y))


def expr_w_form_0(x: str = "x", y: str = "y", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_form_0`."""
    return (24*math.pi*(2*math.cos(math.pi*pl.col(x)) + 2*math.cos(math.pi*pl.col(y)))*math.sin(math.pi*pl.col(x))*math.sin(math.pi*pl.col(y))*math.sin(math.pi*pl.col(z))*math.cos(math.pi*pl.col(z)) + 8*math.pi*(3*math.cos(2*math.pi*pl.col(z)) - 2)*math.sin(math.pi*pl.col(x))*math.sin(math.pi*pl.col(y))*math.cos(math.pi*pl.col(x))*math.cos(math.pi*pl.col(y)))


def calc_v_form_0(N: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_27423.

    **Source**:
    - Title: High-order stabilized matrix-free simulation of rotating mixing devices using the Mortar Element Method (2026)
    - Authors: B. Campos, P. Munch, V. O. Ferreira et al.
    - Citation Key: `arxiv_2608_27423`

    **KaTeX Formula**:
    $$
    v = Nu\sum  i=1 vi \phi i, u = Nu\sum  j=1 uj \phi j , q = Np\sum  k=1 qk \psi k, p* = Np\sum  l=1 p*l \psi l
    $$

    Args:
        N (float): Input parameter `N`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(N*u)


def expr_v_form_0(N: str = "N", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_form_0`."""
    return (pl.col(N)*pl.col(u))


def calc_p_w_i_g_n_form_1(g: float, i: float, n: float, omega: float, tau: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_23163.

    **Source**:
    - Title: Spinning Quadrotor: Hover Thrust Augmentation with Passive Lifting Surfaces (2026)
    - Authors: Aniketh Parkala, Harikumar Kandath
    - Citation Key: `arxiv_2608_23163`

    **KaTeX Formula**:
    $$
    Pwing = \tau wing \omega
    $$

    Args:
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        omega (float): Input parameter `omega`.
        tau (float): Input parameter `tau`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(g*i*n*omega*tau*w)


def expr_p_w_i_g_n_form_1(g: str = "g", i: str = "i", n: str = "n", omega: str = "omega", tau: str = "tau", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_w_i_g_n_form_1`."""
    return (pl.col(g)*pl.col(i)*pl.col(n)*pl.col(omega)*pl.col(tau)*pl.col(w))


def calc_v_a_l_m_psi_x_form_2(f: float, i: float, n: float, p: float, s: float, sigma: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_26568.

    **Source**:
    - Title: Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games (2026)
    - Authors: Durgam Latha, Dion Reji, Dorde Zikelic et al.
    - Citation Key: `arxiv_2610_26568`

    **KaTeX Formula**:
    $$
    ValM(\Psi , X) = \beta (sup \sigma  inf \pi  p\sigma ,\pi  )
    $$

    Args:
        f (float): Input parameter `f`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.
        s (float): Input parameter `s`.
        sigma (float): Input parameter `sigma`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float((math.gamma(math.pi)*math.gamma(math.pi*f*i*n*p**2*s*sigma**2*u)/math.gamma(math.pi*f*i*n*p**2*s*sigma**2*u + math.pi)))


def expr_v_a_l_m_psi_x_form_2(f: str = "f", i: str = "i", n: str = "n", p: str = "p", s: str = "s", sigma: str = "sigma", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_a_l_m_psi_x_form_2`."""
    return ((math.gamma(math.pi)*math.gamma(math.pi*pl.col(f)*pl.col(i)*pl.col(n)*pl.col(p)**2*pl.col(s)*pl.col(sigma)**2*pl.col(u))/math.gamma(math.pi*pl.col(f)*pl.col(i)*pl.col(n)*pl.col(p)**2*pl.col(s)*pl.col(sigma)**2*pl.col(u) + math.pi)))


def calc_c_e_b_c_w_e_i_j_form_2(C: float, H: float, W: float, e: float, g: float, i: float, j: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27057.

    **Source**:
    - Title: Probing Lepton Flavor Violation at FCC-ee (2026)
    - Authors: L. Allwicher, R. Bartocci, M. Cepeda et al.
    - Citation Key: `arxiv_2610_27057`

    **KaTeX Formula**:
    $$
    (  CeB  CeW ) ij = 3g3 2 8(16\pi 2 )2 (tW - 3t3W 1 - t2W ) CeH ij + . . . , (B21)
    $$

    Args:
        C (float): Input parameter `C`.
        H (float): Input parameter `H`.
        W (float): Input parameter `W`.
        e (float): Input parameter `e`.
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(-629760*math.pi*C*H*W*e*g*i*j*t)


def expr_c_e_b_c_w_e_i_j_form_2(C: str = "C", H: str = "H", W: str = "W", e: str = "e", g: str = "g", i: str = "i", j: str = "j", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_e_b_c_w_e_i_j_form_2`."""
    return (-629760*math.pi*pl.col(C)*pl.col(H)*pl.col(W)*pl.col(e)*pl.col(g)*pl.col(i)*pl.col(j)*pl.col(t))


def calc_v_form_2(nu: float, t: float, x: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_27423.

    **Source**:
    - Title: High-order stabilized matrix-free simulation of rotating mixing devices using the Mortar Element Method (2026)
    - Authors: B. Campos, P. Munch, V. O. Ferreira et al.
    - Citation Key: `arxiv_2608_27423`

    **KaTeX Formula**:
    $$
    v = - \exp(-2\nu t) \sin(x) \cos(y)
    $$

    Args:
        nu (float): Input parameter `nu`.
        t (float): Input parameter `t`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(-math.exp(-2*nu*t)*math.sin(x)*math.cos(y))


def expr_v_form_2(nu: str = "nu", t: str = "t", x: str = "x", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_form_2`."""
    return (-(-2*pl.col(nu).exp()*pl.col(t))*math.sin(pl.col(x))*math.cos(pl.col(y)))


def calc_l_e_q_u_2333_c_1_form_3(C: float, Y: float, d: float, dq: float, e: float, l: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27057.

    **Source**:
    - Title: Probing Lepton Flavor Violation at FCC-ee (2026)
    - Authors: L. Allwicher, R. Bartocci, M. Cepeda et al.
    - Citation Key: `arxiv_2610_27057`

    **KaTeX Formula**:
    $$
    C (1) lequ 2333 = - 1 4\pi 2 (Yd)33(Yu)33 Cledq 2333 + . . . , (B26)
    $$

    Args:
        C (float): Input parameter `C`.
        Y (float): Input parameter `Y`.
        d (float): Input parameter `d`.
        dq (float): Input parameter `dq`.
        e (float): Input parameter `e`.
        l (float): Input parameter `l`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(-71137836*math.pi*C*Y**2*d*dq*e*l*u)


def expr_l_e_q_u_2333_c_1_form_3(C: str = "C", Y: str = "Y", d: str = "d", dq: str = "dq", e: str = "e", l: str = "l", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_e_q_u_2333_c_1_form_3`."""
    return (-71137836*math.pi*pl.col(C)*pl.col(Y)**2*pl.col(d)*pl.col(dq)*pl.col(e)*pl.col(l)*pl.col(u))


def calc_l_w_i_g_n_form_3(T: float, g: float, m: float, o: float, r: float, t: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_23163.

    **Source**:
    - Title: Spinning Quadrotor: Hover Thrust Augmentation with Passive Lifting Surfaces (2026)
    - Authors: Aniketh Parkala, Harikumar Kandath
    - Citation Key: `arxiv_2608_23163`

    **KaTeX Formula**:
    $$
    Lwing = mg - Tmotor \cos \theta
    $$

    Args:
        T (float): Input parameter `T`.
        g (float): Input parameter `g`.
        m (float): Input parameter `m`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(-T*m*o**2*r*t*math.cos(theta) + g*m)


def expr_l_w_i_g_n_form_3(T: str = "T", g: str = "g", m: str = "m", o: str = "o", r: str = "r", t: str = "t", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_w_i_g_n_form_3`."""
    return (-pl.col(T)*pl.col(m)*pl.col(o)**2*pl.col(r)*pl.col(t)*math.cos(pl.col(theta)) + pl.col(g)*pl.col(m))


def calc_p_form_4(v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2303_03898.

    **Source**:
    - Title: Virtual Omnidirectional Perception for Downwash Prediction within a Team of Nano Multirotors Flying in Close Proximity (2023)
    - Authors: Akmaral Moldagalieva, Wolfgang Hönig
    - Citation Key: `arxiv_2303_03898`

    **KaTeX Formula**:
    $$
    p = v, m v = mg + Rfu + fa, (1a)
    $$

    Args:
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(v)


def expr_p_form_4(v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_form_4`."""
    return (pl.col(v))


def calc_r_form_4(n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2303_04802.

    **Source**:
    - Title: Estimating Ball Flight Characteristics and Spin Rate from Radar Tracking (2023)
    - Authors: David Kagan, Alan M. Nathan
    - Citation Key: `arxiv_2303_04802`

    **KaTeX Formula**:
    $$
    R = 1n \sqrt \sqrt \sqrt \sqrt ( n\sum  i=1 \cos \phi i)2 + ( n\sum  i=1 \sin \phi i)2
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(n)


def expr_r_form_4(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_form_4`."""
    return (pl.col(n))


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


def expr_h_p_form_6(U: str = "U", e: str = "e") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_p_form_6`."""
    return (-pl.col(U) + pl.col(e) + 11)


def calc_delta_1_form_6(H: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_27423.

    **Source**:
    - Title: High-order stabilized matrix-free simulation of rotating mixing devices using the Mortar Element Method (2026)
    - Authors: B. Campos, P. Munch, V. O. Ferreira et al.
    - Citation Key: `arxiv_2608_27423`

    **KaTeX Formula**:
    $$
    \delta 1 = H nH
    $$

    Args:
        H (float): Input parameter `H`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(H**2*n)


def expr_delta_1_form_6(H: str = "H", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_1_form_6`."""
    return (pl.col(H)**2*pl.col(n))


def calc_m_e_r_e_g_g_3_form_3(G: float, cup: float, e: float, i: float, n: float, r: float, s: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    G(3) merge = Gs \cup  G1 \cup  G2 \cup  Einter s1 \cup Einter s2 \cup Einter 12
    $$

    Args:
        G (float): Input parameter `G`.
        cup (float): Input parameter `cup`.
        e (float): Input parameter `e`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(48*G**3*cup**5*e**3*i**3*n**3*r**3*s**3*t**3*math.exp(3))


def expr_m_e_r_e_g_g_3_form_3(G: str = "G", cup: str = "cup", e: str = "e", i: str = "i", n: str = "n", r: str = "r", s: str = "s", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_e_r_e_g_g_3_form_3`."""
    return (48*pl.col(G)**3*pl.col(cup)**5*pl.col(e)**3*pl.col(i)**3*pl.col(n)**3*pl.col(r)**3*pl.col(s)**3*pl.col(t)**3*math.exp(3))


def calc_d_form_7(w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_04690.

    **Source**:
    - Title: Enhancing Multimodal Emotion Recognition via Multi-Feature Encoding and Attention-Based Fusion (2026)
    - Authors: Xu Lin, Ke Wang, Hui Kang et al.
    - Citation Key: `arxiv_2609_04690`

    **KaTeX Formula**:
    $$
    d = 2 |w|
    $$

    Args:
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*abs(w))


def expr_d_form_7(w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_form_7`."""
    return (2*abs(pl.col(w)))


def calc_h_t_form_7(h: float, o: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_05500.

    **Source**:
    - Title: Performance comparison of tethered and self-propelled models of fish locomotion using unsteady thin airfoil theory (2026)
    - Authors: Anshul Nayak, Emad Masroor, Hodjat Pendar
    - Citation Key: `arxiv_2609_05500`

    **KaTeX Formula**:
    $$
    h(t) = ho \sin(2\pi t), and \theta (t) = \theta o \sin(2\pi t +\phi )
    $$

    Args:
        h (float): Input parameter `h`.
        o (float): Input parameter `o`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(h*o*math.sin(2*math.pi*t))


def expr_h_t_form_7(h: str = "h", o: str = "o", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_t_form_7`."""
    return (pl.col(h)*pl.col(o)*math.sin(2*math.pi*pl.col(t)))


def calc_openalex_sutton1988_w2100677568_form_0(t: float) -> float:
    r"""Compute mathematical metric extracted from openalex_sutton1988_w2100677568.

    **Source**:
    - Title: Learning to Predict by the Methods of Temporal Differences (1988)
    - Authors: Richard S. Sutton
    - Citation Key: `openalex_sutton1988_w2100677568`

    **KaTeX Formula**:
    $$
    z - Pt = E(Pk+I Pk) where Pm+l def k=t
    $$

    Args:
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(t)


def expr_openalex_sutton1988_w2100677568_form_0(t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_openalex_sutton1988_w2100677568_form_0`."""
    return (pl.col(t))


def calc_i_f_w_form_7(C: float, a: float, c: float, e: float, f: float, i: float, k: float, l: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29049.

    **Source**:
    - Title: ART-MPG: Autoregressive R/T Manifold Path Guiding (2026)
    - Authors: Zehao Zhao, Yanyang Yang, Xiaole Zhang et al.
    - Citation Key: `arxiv_2610_29049`

    **KaTeX Formula**:
    $$
    Ifw =  clippeak Cf (Hz\eta  (A)min {Cw, Jimpl qT }) max{\epsilon N , qN } , A ̸= \emptyset , Jimpl \le M, 0
    $$

    Args:
        C (float): Input parameter `C`.
        a (float): Input parameter `a`.
        c (float): Input parameter `c`.
        e (float): Input parameter `e`.
        f (float): Input parameter `f`.
        i (float): Input parameter `i`.
        k (float): Input parameter `k`.
        l (float): Input parameter `l`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(C*a*c*e*f*i*k*l*p**2)


def expr_i_f_w_form_7(C: str = "C", a: str = "a", c: str = "c", e: str = "e", f: str = "f", i: str = "i", k: str = "k", l: str = "l", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_f_w_form_7`."""
    return (pl.col(C)*pl.col(a)*pl.col(c)*pl.col(e)*pl.col(f)*pl.col(i)*pl.col(k)*pl.col(l)*pl.col(p)**2)


def calc_r_e_form_7(D: float, N: float, i: float, nu: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_27423.

    **Source**:
    - Title: High-order stabilized matrix-free simulation of rotating mixing devices using the Mortar Element Method (2026)
    - Authors: B. Campos, P. Munch, V. O. Ferreira et al.
    - Citation Key: `arxiv_2608_27423`

    **KaTeX Formula**:
    $$
    Re = D2 i N \nu
    $$

    Args:
        D (float): Input parameter `D`.
        N (float): Input parameter `N`.
        i (float): Input parameter `i`.
        nu (float): Input parameter `nu`.

    Returns:
        float: Calculated metric value.
    """
    return float(D*(2*(i*(N*nu))))


def expr_r_e_form_7(D: str = "D", N: str = "N", i: str = "i", nu: str = "nu") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_e_form_7`."""
    return (pl.col(D)*(2*(pl.col(i)*(pl.col(N)*pl.col(nu)))))


def calc_n_e_v_x_form_7(xi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    N e v (x) = [1 - \xi  0 \xi  0] , N ew (x) = [0 1 - \xi  0 \xi  ]
    $$

    Args:
        xi (float): Input parameter `xi`.

    Returns:
        float: Calculated metric value.
    """
    return float(1 - xi*0*(0*xi))


def expr_n_e_v_x_form_7(xi: str = "xi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_n_e_v_x_form_7`."""
    return (1 - pl.col(xi)*0*(0*pl.col(xi)))


def calc_k_t_form_9(l: float) -> float:
    r"""Compute mathematical metric extracted from openalex_sutton1988_w2100677568.

    **Source**:
    - Title: Learning to Predict by the Methods of Temporal Differences (1988)
    - Authors: Richard S. Sutton
    - Citation Key: `openalex_sutton1988_w2100677568`

    **KaTeX Formula**:
    $$
    t k=l
    $$

    Args:
        l (float): Input parameter `l`.

    Returns:
        float: Calculated metric value.
    """
    return float(l)


def expr_k_t_form_9(l: str = "l") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_t_form_9`."""
    return (pl.col(l))


def calc_e_c_o_n_t_a_c_t_form_9(C: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_08059.

    **Source**:
    - Title: Perceptive Behavior Foundation Model: Adapting Human Motion Priors to Robot-Centric Terrain (2026)
    - Authors: Zifan Wang, Yizhao Li, Teli Ma et al.
    - Citation Key: `arxiv_2606_08059`

    **KaTeX Formula**:
    $$
    Econtact = 1 |C| \sum  (f,t)\in C |d\tau (pf,t)|, Rfloat = 1 |C| \sum  (f,t)\in C I[d\tau  (pf,t) > \epsilon float]
    $$

    Args:
        C (float): Input parameter `C`.

    Returns:
        float: Calculated metric value.
    """
    return float(abs(C))


def expr_e_c_o_n_t_a_c_t_form_9(C: str = "C") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_c_o_n_t_a_c_t_form_9`."""
    return (abs(pl.col(C)))


def calc_sim_h_dagger_n_form_1(M: float, alpha: float, d: float, dagger: float, n: float, sim: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    \sim h\dagger [n] = d- \sim \alpha 2 \dagger  [n] M\sum  m=1 I\sum  i=1 \sqrt q\dagger ,m,i[n] ej\Phi \dagger ,m,i[n]
    $$

    Args:
        M (float): Input parameter `M`.
        alpha (float): Input parameter `alpha`.
        d (float): Input parameter `d`.
        dagger (float): Input parameter `dagger`.
        n (float): Input parameter `n`.
        sim (float): Input parameter `sim`.

    Returns:
        float: Calculated metric value.
    """
    return float(-2*M*alpha*dagger*n*sim + d)


def expr_sim_h_dagger_n_form_1(M: str = "M", alpha: str = "alpha", d: str = "d", dagger: str = "dagger", n: str = "n", sim: str = "sim") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sim_h_dagger_n_form_1`."""
    return (-2*pl.col(M)*pl.col(alpha)*pl.col(dagger)*pl.col(n)*pl.col(sim) + pl.col(d))


def calc_d_xi_xi_form_2(T: float, dT: float, gamma: float, h: float, phi: float, q: float, s: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    d(\xi ,  \xi ) = [dTq hs h\phi  h\theta  h\gamma  ]T
    $$

    Args:
        T (float): Input parameter `T`.
        dT (float): Input parameter `dT`.
        gamma (float): Input parameter `gamma`.
        h (float): Input parameter `h`.
        phi (float): Input parameter `phi`.
        q (float): Input parameter `q`.
        s (float): Input parameter `s`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(T*(dT*(q*(h*(s*(h*(phi*(h*(theta*(gamma*h))))))))))


def expr_d_xi_xi_form_2(T: str = "T", dT: str = "dT", gamma: str = "gamma", h: str = "h", phi: str = "phi", q: str = "q", s: str = "s", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_xi_xi_form_2`."""
    return (pl.col(T)*(pl.col(dT)*(pl.col(q)*(pl.col(h)*(pl.col(s)*(pl.col(h)*(pl.col(phi)*(pl.col(h)*(pl.col(theta)*(pl.col(gamma)*pl.col(h)))))))))))


def calc_a_v_g_t_i_e_m_form_3(N: float, c: float, s: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29142.

    **Source**:
    - Title: State-Dependent Objective Coordination for End-to-End Balance and Navigation (2026)
    - Authors: Xuhao Huang, Xitao Xu, Yuxin Zheng et al.
    - Citation Key: `arxiv_2610_29142`

    **KaTeX Formula**:
    $$
    AvgTime = 1 Nsucc \sum  i\in Esucc Ti
    $$

    Args:
        N (float): Input parameter `N`.
        c (float): Input parameter `c`.
        s (float): Input parameter `s`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*(s*(u*(c*c)))))


def expr_a_v_g_t_i_e_m_form_3(N: str = "N", c: str = "c", s: str = "s", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_v_g_t_i_e_m_form_3`."""
    return (1*(pl.col(N)*(pl.col(s)*(pl.col(u)*(pl.col(c)*pl.col(c))))))


def calc_t_form_8(l: float) -> float:
    r"""Compute mathematical metric extracted from openalex_sutton1988_w2100677568.

    **Source**:
    - Title: Learning to Predict by the Methods of Temporal Differences (1988)
    - Authors: Richard S. Sutton
    - Citation Key: `openalex_sutton1988_w2100677568`

    **KaTeX Formula**:
    $$
    t=l
    $$

    Args:
        l (float): Input parameter `l`.

    Returns:
        float: Calculated metric value.
    """
    return float(l)


def expr_t_form_8(l: str = "l") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_form_8`."""
    return (pl.col(l))


def calc_theta_w_form_1(B: float, q: float, theta: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29565.

    **Source**:
    - Title: Preserving Operator Intent Under Actuation Constraints: Teleoperation of Manipulators with Coupled Transmissions (2026)
    - Authors: Xuhan Miao, Zijin Han, Yutong Shen et al.
    - Citation Key: `arxiv_2610_29565`

    **KaTeX Formula**:
    $$
    \theta w = Bqw + \theta w,0, ˙ \theta w = B ˙ qw, \tau w = BT\tau m, B = [-\kappa p \kappa r \kappa p \kappa r ]
    $$

    Args:
        B (float): Input parameter `B`.
        q (float): Input parameter `q`.
        theta (float): Input parameter `theta`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(B*q*w + theta*w)


def expr_theta_w_form_1(B: str = "B", q: str = "q", theta: str = "theta", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_theta_w_form_1`."""
    return (pl.col(B)*pl.col(q)*pl.col(w) + pl.col(theta)*pl.col(w))


def calc_abs_n_r_n_t_a_r_g_e_t_22_form_0(approx: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_08157.

    **Source**:
    - Title: Event-Time Hybrid Optimal Control for Robotic Table Tennis Serves (2026)
    - Authors: Thomas Gossard, Till Köpff, Andreas Ziegler
    - Citation Key: `arxiv_2608_08157`

    **KaTeX Formula**:
    $$
    |nr - ntarget|22 = 2 (1 - \cos \theta ) \approx  \theta 2
    $$

    Args:
        approx (float): Input parameter `approx`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(4*approx*theta*(1 - math.cos(theta)))


def expr_abs_n_r_n_t_a_r_g_e_t_22_form_0(approx: str = "approx", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_abs_n_r_n_t_a_r_g_e_t_22_form_0`."""
    return (4*pl.col(approx)*pl.col(theta)*(1 - math.cos(pl.col(theta))))


def calc_q_form_1(delta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_03805.

    **Source**:
    - Title: Regularization in Paired Comparison Models via Pseudo-Games and Phantom Players (2026)
    - Authors: Mark E. Glickman
    - Citation Key: `arxiv_2606_03805`

    **KaTeX Formula**:
    $$
    q = 1 + \delta  1 + 2\delta
    $$

    Args:
        delta (float): Input parameter `delta`.

    Returns:
        float: Calculated metric value.
    """
    return float(3*delta + 1)


def expr_q_form_1(delta: str = "delta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_form_1`."""
    return (3*pl.col(delta) + 1)


def calc_val_0_form_5(A: float, T: float, y: float) -> float:
    r"""Compute mathematical metric extracted from openalex_sutton1988_w2100677568.

    **Source**:
    - Title: Learning to Predict by the Methods of Temporal Differences (1988)
    - Authors: Richard S. Sutton
    - Citation Key: `openalex_sutton1988_w2100677568`

    **KaTeX Formula**:
    $$
    0 = ATAy
    $$

    Args:
        A (float): Input parameter `A`.
        T (float): Input parameter `T`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(A**2*T*y)


def expr_val_0_form_5(A: str = "A", T: str = "T", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_0_form_5`."""
    return (pl.col(A)**2*pl.col(T)*pl.col(y))


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
    return float(G*(F*T))


def expr_s_form_e(F: str = "F", G: str = "G", T: str = "T") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_form_e`."""
    return (pl.col(G)*(pl.col(F)*pl.col(T)))


def calc_sigma_form_2(alpha: float, e: float, omega: float, p: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_06439.

    **Source**:
    - Title: Deep Reinforcement Learning based Control Design for Aircraft Recovery from Loss-of-Control Scenario (2026)
    - Authors: Imran Sayyed, Aayush Konar, Nandan Kumar Sinha
    - Citation Key: `arxiv_2601_06439`

    **KaTeX Formula**:
    $$
    \sigma  = -e2\alpha  - wp21 ||\omega ||2
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        e (float): Input parameter `e`.
        omega (float): Input parameter `omega`.
        p (float): Input parameter `p`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(-2*alpha*e - 42*p*w*abs(omega))


def expr_sigma_form_2(alpha: str = "alpha", e: str = "e", omega: str = "omega", p: str = "p", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sigma_form_2`."""
    return (-2*pl.col(alpha)*pl.col(e) - 42*pl.col(p)*pl.col(w)*abs(pl.col(omega)))


def calc_f_a_e_o_r_form_3(e: float, l: float, p: float, r: float, rho: float, s: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2309_15318.

    **Source**:
    - Title: A Global 3-D Simulation of Magnetospheric Accretion: I. Magnetically Disrupted Disks and Surface Accretion (2023)
    - Authors: Zhaohuan Zhu, James M. Stone, Nuria Calvet
    - Citation Key: `arxiv_2309_15318`

    **KaTeX Formula**:
    $$
    faero = -\pi s2p\rho vrelvrel
    $$

    Args:
        e (float): Input parameter `e`.
        l (float): Input parameter `l`.
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.
        rho (float): Input parameter `rho`.
        s (float): Input parameter `s`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(-2*math.pi*e**2*l**2*p*r**2*rho*s*v**2)


def expr_f_a_e_o_r_form_3(e: str = "e", l: str = "l", p: str = "p", r: str = "r", rho: str = "rho", s: str = "s", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_a_e_o_r_form_3`."""
    return (-2*math.pi*pl.col(e)**2*pl.col(l)**2*pl.col(p)*pl.col(r)**2*pl.col(rho)*pl.col(s)*pl.col(v)**2)


def calc_c_tau_form_4(eta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1905_04632.

    **Source**:
    - Title: Ceiling Effects for Hybrid Aerial-Surface Locomotion of Small Rotorcraft (2019)
    - Authors: Yi Hsuan Hsiao, Pakpong Chirarattananon
    - Citation Key: `arxiv_1905_04632`

    **KaTeX Formula**:
    $$
    c\tau  = 1 \eta \sqrt 2\rho A c3/2 T
    $$

    Args:
        eta (float): Input parameter `eta`.

    Returns:
        float: Calculated metric value.
    """
    return float(eta)


def expr_c_tau_form_4(eta: str = "eta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_tau_form_4`."""
    return (pl.col(eta))


def calc_tau_e_t_x_form_4(dB: float, dp: float, f: float, p: float, tau: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1709_07969.

    **Source**:
    - Title: Optimal-power Configurations for Hover Solutions in Mono-spinners (2017)
    - Authors: Mojtaba Hedayatpour, Mehran Mehrandezh, Farrokh Janabi-Sharifi
    - Citation Key: `arxiv_1709_07969`

    **KaTeX Formula**:
    $$
    \tau ext =\tau  f +\tau  p+\tau dp +\tau dB
    $$

    Args:
        dB (float): Input parameter `dB`.
        dp (float): Input parameter `dp`.
        f (float): Input parameter `f`.
        p (float): Input parameter `p`.
        tau (float): Input parameter `tau`.

    Returns:
        float: Calculated metric value.
    """
    return float(dB*tau + dp*tau + f*tau + p*tau)


def expr_tau_e_t_x_form_4(dB: str = "dB", dp: str = "dp", f: str = "f", p: str = "p", tau: str = "tau") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_tau_e_t_x_form_4`."""
    return (pl.col(dB)*pl.col(tau) + pl.col(dp)*pl.col(tau) + pl.col(f)*pl.col(tau) + pl.col(p)*pl.col(tau))


def calc_theta_l_r_t_form_5(A: float, C: float, b: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_08746.

    **Source**:
    - Title: Kinematics of Single-Winged Spinning Seeds: A Study on Mahogany and Buddha Coconut Samaras (2026)
    - Authors: Yogeshwaran G, Srisha M. V. Rao, Jagadeesh G
    - Citation Key: `arxiv_2603_08746`

    **KaTeX Formula**:
    $$
    \theta LR(t) = A1 \cos(b1t + C1), \phi LR(t) = A2 \cos(b2t + C2), \psi LR(t) = mt + \psi 0
    $$

    Args:
        A (float): Input parameter `A`.
        C (float): Input parameter `C`.
        b (float): Input parameter `b`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(A*math.cos(C + b*t))


def expr_theta_l_r_t_form_5(A: str = "A", C: str = "C", b: str = "b", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_theta_l_r_t_form_5`."""
    return (pl.col(A)*math.cos(pl.col(C) + pl.col(b)*pl.col(t)))


def calc_p_a_form_5(P: float, eta: float, m: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1905_04632.

    **Source**:
    - Title: Ceiling Effects for Hybrid Aerial-Surface Locomotion of Small Rotorcraft (2019)
    - Authors: Yi Hsuan Hsiao, Pakpong Chirarattananon
    - Citation Key: `arxiv_1905_04632`

    **KaTeX Formula**:
    $$
    Pa = \eta Pm
    $$

    Args:
        P (float): Input parameter `P`.
        eta (float): Input parameter `eta`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(P*eta*m)


def expr_p_a_form_5(P: str = "P", eta: str = "eta", m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_a_form_5`."""
    return (pl.col(P)*pl.col(eta)*pl.col(m))


def calc_u_h_i_n_form_e(J: float, f: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    uhni = fJ \sum  j |∆p h nij |2, Frozenn = \sum i 1[urni \ge  50] 1[uni < 10 ∧ uni < 0.1urni ] \sum i 1[urni \ge  50]
    $$

    Args:
        J (float): Input parameter `J`.
        f (float): Input parameter `f`.

    Returns:
        float: Calculated metric value.
    """
    return float(J*f)


def expr_u_h_i_n_form_e(J: str = "J", f: str = "f") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_h_i_n_form_e`."""
    return (pl.col(J)*pl.col(f))


def calc_i_d_s_form_8(N: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_26031.

    **Source**:
    - Title: AuDQ: Auditable Data Quality through Agentic Rule Discovery (2026)
    - Authors: Jacopo Biggiogera, Nicolas Colombo, Krati Saxena et al.
    - Citation Key: `arxiv_2610_26031`

    **KaTeX Formula**:
    $$
    IDS = 1- 1 (N2 ) \sum  i<j simij
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(1 - 1*2*N)


def expr_i_d_s_form_8(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_d_s_form_8`."""
    return (1 - 1*2*pl.col(N))


def calc_psi_form_f(O: float, x: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_20570.

    **Source**:
    - Title: Walking on the Slope: Stable Bipedal Gaits with Genetic-Algorithm-Optimized Trajectories (2026)
    - Authors: Madhav Rijal
    - Citation Key: `arxiv_2609_20570`

    **KaTeX Formula**:
    $$
    \psi  = \arctan Ox4 - Ox2 Oz4 - Oz2
    $$

    Args:
        O (float): Input parameter `O`.
        x (float): Input parameter `x`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(-O*2*z + (-O*x*(2*(O*(4*z))) + math.atan(O*(4*x))))


def expr_psi_form_f(O: str = "O", x: str = "x", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_psi_form_f`."""
    return (-pl.col(O)*2*pl.col(z) + (-pl.col(O)*pl.col(x)*(2*(pl.col(O)*(4*pl.col(z)))) + math.atan(pl.col(O)*(4*pl.col(x)))))


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
    return float(P*r)


def expr_q_s_form_9(P: str = "P", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_s_form_9`."""
    return (pl.col(P)*pl.col(r))


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
    return float(W*(s*(N*s)))


def expr_w_e_s_form_9(N: str = "N", W: str = "W", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_e_s_form_9`."""
    return (pl.col(W)*(pl.col(s)*(pl.col(N)*pl.col(s))))


def calc_r_t_theta_form_9(theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_06439.

    **Source**:
    - Title: Deep Reinforcement Learning based Control Design for Aircraft Recovery from Loss-of-Control Scenario (2026)
    - Authors: Imran Sayyed, Aayush Konar, Nandan Kumar Sinha
    - Citation Key: `arxiv_2601_06439`

    **KaTeX Formula**:
    $$
    rt(\theta ) = \pi \theta (at | st) \pi \theta old (at | st)
    $$

    Args:
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.pi*theta)


def expr_r_t_theta_form_9(theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_t_theta_form_9`."""
    return (math.pi*pl.col(theta))


def calc_f_i_form_9(f: float, i: float, k: float, omega: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_23163.

    **Source**:
    - Title: Spinning Quadrotor: Hover Thrust Augmentation with Passive Lifting Surfaces (2026)
    - Authors: Aniketh Parkala, Harikumar Kandath
    - Citation Key: `arxiv_2608_23163`

    **KaTeX Formula**:
    $$
    fi = kf\omega 2 i
    $$

    Args:
        f (float): Input parameter `f`.
        i (float): Input parameter `i`.
        k (float): Input parameter `k`.
        omega (float): Input parameter `omega`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*f*i*k*omega)


def expr_f_i_form_9(f: str = "f", i: str = "i", k: str = "k", omega: str = "omega") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_i_form_9`."""
    return (2*pl.col(f)*pl.col(i)*pl.col(k)*pl.col(omega))


def calc_v_form_9(x: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_27423.

    **Source**:
    - Title: High-order stabilized matrix-free simulation of rotating mixing devices using the Mortar Element Method (2026)
    - Authors: B. Campos, P. Munch, V. O. Ferreira et al.
    - Citation Key: `arxiv_2608_27423`

    **KaTeX Formula**:
    $$
    v = 2 \cos(\pi x) \sin(\pi x) \sin(\pi y)2
    $$

    Args:
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(4*math.sin(math.pi*x)*math.sin(math.pi*y)*math.cos(math.pi*x))


def expr_v_form_9(x: str = "x", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_form_9`."""
    return (4*math.sin(math.pi*pl.col(x))*math.sin(math.pi*pl.col(y))*math.cos(math.pi*pl.col(x)))


def calc_h_d_form_a(H: float, S: float, alpha: float, g: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1408_4306.

    **Source**:
    - Title: Effect of lift force on the aerodynamics of dust grains in the protoplanetary disk (2014)
    - Authors: Masaki S. Yamaguchi, Shigeo S. Kimura
    - Citation Key: `arxiv_1408_4306`

    **KaTeX Formula**:
    $$
    Hd = Hg \cdot  ( \alpha  St 1 + 2St 1 + St2 )1/2
    $$

    Args:
        H (float): Input parameter `H`.
        S (float): Input parameter `S`.
        alpha (float): Input parameter `alpha`.
        g (float): Input parameter `g`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(((1*(S*(2*t) + (2*(S*(1*t)) + alpha*(S*(1*t)))))*(H*g))/2)


def expr_h_d_form_a(H: str = "H", S: str = "S", alpha: str = "alpha", g: str = "g", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_d_form_a`."""
    return (((1*(pl.col(S)*(2*pl.col(t)) + (2*(pl.col(S)*(1*pl.col(t))) + pl.col(alpha)*(pl.col(S)*(1*pl.col(t))))))*(pl.col(H)*pl.col(g)))/2)


def calc_r_c_l_e_a_r_form_c(S: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_08059.

    **Source**:
    - Title: Perceptive Behavior Foundation Model: Adapting Human Motion Priors to Robot-Centric Terrain (2026)
    - Authors: Zifan Wang, Yizhao Li, Teli Ma et al.
    - Citation Key: `arxiv_2606_08059`

    **KaTeX Formula**:
    $$
    Rclear = 1 |S| \sum  (f,t)\in S I[d\tau  (pf,t) < cmin]
    $$

    Args:
        S (float): Input parameter `S`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*abs(S))


def expr_r_c_l_e_a_r_form_c(S: str = "S") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_c_l_e_a_r_form_c`."""
    return (1*abs(pl.col(S)))


def calc_r_e_form_d(V: float, c: float, mu: float, rho: float, sim: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_23163.

    **Source**:
    - Title: Spinning Quadrotor: Hover Thrust Augmentation with Passive Lifting Surfaces (2026)
    - Authors: Aniketh Parkala, Harikumar Kandath
    - Citation Key: `arxiv_2608_23163`

    **KaTeX Formula**:
    $$
    Re = \rho V c \mu  \sim  105
    $$

    Args:
        V (float): Input parameter `V`.
        c (float): Input parameter `c`.
        mu (float): Input parameter `mu`.
        rho (float): Input parameter `rho`.
        sim (float): Input parameter `sim`.

    Returns:
        float: Calculated metric value.
    """
    return float(105*V*c*mu*rho*sim)


def expr_r_e_form_d(V: str = "V", c: str = "c", mu: str = "mu", rho: str = "rho", sim: str = "sim") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_e_form_d`."""
    return (105*pl.col(V)*pl.col(c)*pl.col(mu)*pl.col(rho)*pl.col(sim))


def calc_h_l_i_j_c_1_form_d(g: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27057.

    **Source**:
    - Title: Probing Lepton Flavor Violation at FCC-ee (2026)
    - Authors: L. Allwicher, R. Bartocci, M. Cepeda et al.
    - Citation Key: `arxiv_2610_27057`

    **KaTeX Formula**:
    $$
    C (1) Hl ij = - g2 1 48\pi 2 (2C le ijkk +2C ll ijkk +C ll ikkj
    $$

    Args:
        g (float): Input parameter `g`.

    Returns:
        float: Calculated metric value.
    """
    return float(-4296*math.pi*g)


def expr_h_l_i_j_c_1_form_d(g: str = "g") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_l_i_j_c_1_form_d`."""
    return (-4296*math.pi*pl.col(g))


def calc_false_form_e(h: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_06739.

    **Source**:
    - Title: The profit-bias identity in sports betting: bookmaker profit as the public's prediction error (2026)
    - Authors: Jacek P. Dmochowski
    - Citation Key: `arxiv_2609_06739`

    **KaTeX Formula**:
    $$
    1- 1O = D- (1+\phi h)(1+\phi v) D = 1 - \phi h\phi v D = h
    $$

    Args:
        h (float): Input parameter `h`.

    Returns:
        float: Calculated metric value.
    """
    return float(h)


def expr_false_form_e(h: str = "h") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_false_form_e`."""
    return (pl.col(h))


def calc_p_r_form_e(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2006_03348.

    **Source**:
    - Title: Same-Score Streaks: A Case Study in Probability Modeling (2020)
    - Authors: Peter Staab, Rick Cleary
    - Citation Key: `arxiv_2006_03348`

    **KaTeX Formula**:
    $$
    P (r) = P (X = r runs) = F (r + 1) - F (r) = \int  r+1 r f (x; \alpha , \beta , \gamma ) dx
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_p_r_form_e(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_r_form_e`."""
    return (pl.col(P))


def calc_r_i_t_form_c(n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1810_06655.

    **Source**:
    - Title: Rank Dynamics for Functional Data (2018)
    - Authors: Yaqing Chen, Matthew Dawson, Hans-Georg Müller
    - Citation Key: `arxiv_1810_06655`

    **KaTeX Formula**:
    $$
    Ri(t) = 1n \sum  l̸=i 1{Yl(t)\le Yi(t)}
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(n)


def expr_r_i_t_form_c(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_i_t_form_c`."""
    return (pl.col(n))


def calc_q_l_y_t_form_7(n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1810_06655.

    **Source**:
    - Title: Rank Dynamics for Functional Data (2018)
    - Authors: Yaqing Chen, Matthew Dawson, Hans-Georg Müller
    - Citation Key: `arxiv_1810_06655`

    **KaTeX Formula**:
    $$
    Ql(y, t) = 1n n\sum  i=1 \sim Qli(y, t)
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(n*n))


def expr_q_l_y_t_form_7(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_l_y_t_form_7`."""
    return (1*(pl.col(n)*pl.col(n)))


def calc_q_l_y_t_form_a(n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1810_06655.

    **Source**:
    - Title: Rank Dynamics for Functional Data (2018)
    - Authors: Yaqing Chen, Matthew Dawson, Hans-Georg Müller
    - Citation Key: `arxiv_1810_06655`

    **KaTeX Formula**:
    $$
    Ql(y, t) = 1n n\sum  i=1 \sim Qli(y, t)
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(n*n))


def expr_q_l_y_t_form_a(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_l_y_t_form_a`."""
    return (1*(pl.col(n)*pl.col(n)))


def calc_q_l_y_t_form_c(n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1810_06655.

    **Source**:
    - Title: Rank Dynamics for Functional Data (2018)
    - Authors: Yaqing Chen, Matthew Dawson, Hans-Georg Müller
    - Citation Key: `arxiv_1810_06655`

    **KaTeX Formula**:
    $$
    Ql(y, t) = 1n n\sum  i=1 Qli(y, t)
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(n*n))


def expr_q_l_y_t_form_c(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_l_y_t_form_c`."""
    return (1*(pl.col(n)*pl.col(n)))


def calc_p_i_i_l_form_5(i: float, l: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1701_05976.

    **Source**:
    - Title: How often does the best team win? A unified approach to understanding randomness in North American sport (2017)
    - Authors: Michael J. Lopez, Gregory J. Matthews, Benjamin S. Baumer
    - Citation Key: `arxiv_1701_05976`

    **KaTeX Formula**:
    $$
    pi(li) = { 100 100+li}
    $$

    Args:
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*l + 100100)


def expr_p_i_i_l_form_5(i: str = "i", l: str = "l") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_i_l_form_5`."""
    return (pl.col(i)*pl.col(l) + 100100)


def calc_p_o_s_t_p_a_r_i_t_y_z_form_d(F: float, f: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1701_05976.

    **Source**:
    - Title: How often does the best team win? A unified approach to understanding randomness in North American sport (2017)
    - Authors: Michael J. Lopez, Gregory J. Matthews, Benjamin S. Baumer
    - Citation Key: `arxiv_1701_05976`

    **KaTeX Formula**:
    $$
    PostParityz = 1 - (E[F] - fz1z)' (E[F] - fz1z) \sum zd=1 (⌈log2 d+1⌉ - fz)2
    $$

    Args:
        F (float): Input parameter `F`.
        f (float): Input parameter `f`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(-math.e*F + f*z**2 + 1)


def expr_p_o_s_t_p_a_r_i_t_y_z_form_d(F: str = "F", f: str = "f", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_o_s_t_p_a_r_i_t_y_z_form_d`."""
    return (-math.e*pl.col(F) + pl.col(f)*pl.col(z)**2 + 1)


def calc_w_i_j_form_a(i: float, j: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_09673.

    **Source**:
    - Title: A probabilistic match classification model for low-scoring sports (2026)
    - Authors: László Csató, András Gyimesi
    - Citation Key: `arxiv_2601_09673`

    **KaTeX Formula**:
    $$
    Wij = 1 1 + 10-(Ei-Ej )/400
    $$

    Args:
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.

    Returns:
        float: Calculated metric value.
    """
    return float(-1/400*math.e*i + (1/400)*math.e*j + 21)


def expr_w_i_j_form_a(i: str = "i", j: str = "j") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_i_j_form_a`."""
    return (-1/400*math.e*pl.col(i) + (1/400)*math.e*pl.col(j) + 21)


def calc_i_m_form_0(di: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_25525.

    **Source**:
    - Title: When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review (2026)
    - Authors: Kichang Lee, Gyeongmin Han, Sungmin Lee et al.
    - Citation Key: `arxiv_2609_25525`

    **KaTeX Formula**:
    $$
    mi =    -di
    $$

    Args:
        di (float): Input parameter `di`.

    Returns:
        float: Calculated metric value.
    """
    return float(-di)


def expr_i_m_form_0(di: str = "di") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_m_form_0`."""
    return (-pl.col(di))


def calc_epsilon_i_1312_7(B: float, alpha: float, delta: float, i: float) -> float:
    r"""Compute mathematical metric extracted from 1312_7158.

    **Source**:
    - Title: openWAR: An Open Source System for Evaluating Overall Player Performance in Major League Baseball (2013)
    - Authors: Benjamin S. Baumer, Shane T. Jensen, Gregory J. Matthews
    - Citation Key: `1312_7158`

    **KaTeX Formula**:
    $$
    \epsilon i = \delta i -Bi \cdot   \alpha
    $$

    Args:
        B (float): Input parameter `B`.
        alpha (float): Input parameter `alpha`.
        delta (float): Input parameter `delta`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(-B*alpha*i + delta*i)


def expr_epsilon_i_1312_7(B: str = "B", alpha: str = "alpha", delta: str = "delta", i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_epsilon_i_1312_7`."""
    return (-pl.col(B)*pl.col(alpha)*pl.col(i) + pl.col(delta)*pl.col(i))


def calc_i_y_2209_0(R: float, d: float, n: float, o: float, u: float) -> float:
    r"""Compute mathematical metric extracted from 2209_07274.

    **Source**:
    - Title: Introducing Grid WAR: Rethinking WAR for Starting Pitchers (2022)
    - Authors: Ryan S. Brill, Abraham J. Wyner
    - Citation Key: `2209_07274`

    **KaTeX Formula**:
    $$
    yi =Round(N+(Xi*\beta , 1))
    $$

    Args:
        R (float): Input parameter `R`.
        d (float): Input parameter `d`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(R*d*n*o*u)


def expr_i_y_2209_0(R: str = "R", d: str = "d", n: str = "n", o: str = "o", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_y_2209_0`."""
    return (pl.col(R)*pl.col(d)*pl.col(n)*pl.col(o)*pl.col(u))


def calc_u_s_form_c(Delta: float, U: float, a: float, b: float, e: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    Us = Ubase s +\Delta Us
    $$

    Args:
        Delta (float): Input parameter `Delta`.
        U (float): Input parameter `U`.
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        e (float): Input parameter `e`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(Delta*U*s + U*a*b*e*s**2)


def expr_u_s_form_c(Delta: str = "Delta", U: str = "U", a: str = "a", b: str = "b", e: str = "e", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_s_form_c`."""
    return (pl.col(Delta)*pl.col(U)*pl.col(s) + pl.col(U)*pl.col(a)*pl.col(b)*pl.col(e)*pl.col(s)**2)


def calc_m_p_j_p_b_e_form_e(T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_20558.

    **Source**:
    - Title: Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction (2026)
    - Authors: Songyang Liu, Shuai Li
    - Citation Key: `arxiv_2609_20558`

    **KaTeX Formula**:
    $$
    MPJPEB = 1 |T | \sum  t \in T et
    $$

    Args:
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(abs(T))


def expr_m_p_j_p_b_e_form_e(T: str = "T") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_p_j_p_b_e_form_e`."""
    return (abs(pl.col(T)))


def calc_m_omega_v_v_form_9(R: float, T: float, g: float, m: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_23163.

    **Source**:
    - Title: Spinning Quadrotor: Hover Thrust Augmentation with Passive Lifting Surfaces (2026)
    - Authors: Aniketh Parkala, Harikumar Kandath
    - Citation Key: `arxiv_2608_23163`

    **KaTeX Formula**:
    $$
    m( v + \omega  \times  v) = mR^Tg + \sum  i Fi
    $$

    Args:
        R (float): Input parameter `R`.
        T (float): Input parameter `T`.
        g (float): Input parameter `g`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(R**T*g*m)


def expr_m_omega_v_v_form_9(R: str = "R", T: str = "T", g: str = "g", m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_omega_v_v_form_9`."""
    return (pl.col(R)**pl.col(T)*pl.col(g)*pl.col(m))


def calc_m_form_1(L: float, omega: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    M = \omega 2 x L
    $$

    Args:
        L (float): Input parameter `L`.
        omega (float): Input parameter `omega`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*L*omega*x)


def expr_m_form_1(L: str = "L", omega: str = "omega", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_form_1`."""
    return (2*pl.col(L)*pl.col(omega)*pl.col(x))


def calc_tau_t_form_f(g: float, m: float, r: float, tau: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    \tau  (t) =  \tau  * r - mgr \sin \theta
    $$

    Args:
        g (float): Input parameter `g`.
        m (float): Input parameter `m`.
        r (float): Input parameter `r`.
        tau (float): Input parameter `tau`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(-g*m*r*math.sin(theta) + r*tau)


def expr_tau_t_form_f(g: str = "g", m: str = "m", r: str = "r", tau: str = "tau", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_tau_t_form_f`."""
    return (-pl.col(g)*pl.col(m)*pl.col(r)*math.sin(pl.col(theta)) + pl.col(r)*pl.col(tau))


def calc_b_f_form_2(B: float, C: float, L: float, R: float, c: float, e: float, f: float, r: float, rho: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1709_07969.

    **Source**:
    - Title: Optimal-power Configurations for Hover Solutions in Mono-spinners (2017)
    - Authors: Mojtaba Hedayatpour, Mehran Mehrandezh, Farrokh Janabi-Sharifi
    - Citation Key: `arxiv_1709_07969`

    **KaTeX Formula**:
    $$
    f B = 1 3 \rho  cBCLB R 3 Br 2 e fB
    $$

    Args:
        B (float): Input parameter `B`.
        C (float): Input parameter `C`.
        L (float): Input parameter `L`.
        R (float): Input parameter `R`.
        c (float): Input parameter `c`.
        e (float): Input parameter `e`.
        f (float): Input parameter `f`.
        r (float): Input parameter `r`.
        rho (float): Input parameter `rho`.

    Returns:
        float: Calculated metric value.
    """
    return float(78*B**4*C*L*R*c*e*f*r*rho)


def expr_b_f_form_2(B: str = "B", C: str = "C", L: str = "L", R: str = "R", c: str = "c", e: str = "e", f: str = "f", r: str = "r", rho: str = "rho") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_b_f_form_2`."""
    return (78*pl.col(B)**4*pl.col(C)*pl.col(L)*pl.col(R)*pl.col(c)*pl.col(e)*pl.col(f)*pl.col(r)*pl.col(rho))


def calc_r_beta_form_4(G: float, M: float, P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    \beta R = P*G/M
    $$

    Args:
        G (float): Input parameter `G`.
        M (float): Input parameter `M`.
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float((G*P)/M)


def expr_r_beta_form_4(G: str = "G", M: str = "M", P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_beta_form_4`."""
    return ((pl.col(G)*pl.col(P))/pl.col(M))


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
    return float((-c_x + u_k)/r)


def expr_begin_x_k_a_l_i_g_n_d_e_form_4(c_x: str = "c_x", r: str = "r", u_k: str = "u_k") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_begin_x_k_a_l_i_g_n_d_e_form_4`."""
    return ((-pl.col(c_x) + pl.col(u_k))/pl.col(r))


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
    return float(12*e**2*h*l*r + 12*e*o*r*t)


def expr_r_m_d_i_form_5(e: str = "e", h: str = "h", l: str = "l", o: str = "o", r: str = "r", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_m_d_i_form_5`."""
    return (12*pl.col(e)**2*pl.col(h)*pl.col(l)*pl.col(r) + 12*pl.col(e)*pl.col(o)*pl.col(r)*pl.col(t))


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
    return float(P*r)


def expr_p_i_j_form_6(P: str = "P", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_j_form_6`."""
    return (pl.col(P)*pl.col(r))


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


def expr_eq_e_x_e_f_y_form_8(f: str = "f") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_eq_e_x_e_f_y_form_8`."""
    return (pl.col(f))


def calc_f_tau_form_c(f: float, l: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1709_07969.

    **Source**:
    - Title: Optimal-power Configurations for Hover Solutions in Mono-spinners (2017)
    - Authors: Mojtaba Hedayatpour, Mehran Mehrandezh, Farrokh Janabi-Sharifi
    - Citation Key: `arxiv_1709_07969`

    **KaTeX Formula**:
    $$
    \tau  f = f pl
    $$

    Args:
        f (float): Input parameter `f`.
        l (float): Input parameter `l`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(f*l*p)


def expr_f_tau_form_c(f: str = "f", l: str = "l", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_tau_form_c`."""
    return (pl.col(f)*pl.col(l)*pl.col(p))


def calc_x_form_c(K: float, eta: float, r: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1408_4306.

    **Source**:
    - Title: Effect of lift force on the aerodynamics of dust grains in the protoplanetary disk (2014)
    - Authors: Masaki S. Yamaguchi, Shigeo S. Kimura
    - Citation Key: `arxiv_1408_4306`

    **KaTeX Formula**:
    $$
    x = vr \eta vK , y = v'\theta  \eta vK , gD = FD uΩK , gL = FL uΩK
    $$

    Args:
        K (float): Input parameter `K`.
        eta (float): Input parameter `eta`.
        r (float): Input parameter `r`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(K*eta*r*v**2)


def expr_x_form_c(K: str = "K", eta: str = "eta", r: str = "r", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_form_c`."""
    return (pl.col(K)*pl.col(eta)*pl.col(r)*pl.col(v)**2)


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


def expr_l_z_form_a(y: str = "y", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_z_form_a`."""
    return (abs(pl.col(y) - pl.col(z)))


def calc_p_a_form_b(T: float, gamma: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1905_04632.

    **Source**:
    - Title: Ceiling Effects for Hybrid Aerial-Surface Locomotion of Small Rotorcraft (2019)
    - Authors: Yi Hsuan Hsiao, Pakpong Chirarattananon
    - Citation Key: `arxiv_1905_04632`

    **KaTeX Formula**:
    $$
    Pa = \gamma -1T \sqrt  T 2\rho A
    $$

    Args:
        T (float): Input parameter `T`.
        gamma (float): Input parameter `gamma`.

    Returns:
        float: Calculated metric value.
    """
    return float(-1*T + gamma)


def expr_p_a_form_b(T: str = "T", gamma: str = "gamma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_a_form_b`."""
    return (-1*pl.col(T) + pl.col(gamma))


def calc_v_f_f_form_c(G: float, M: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2309_15318.

    **Source**:
    - Title: A Global 3-D Simulation of Magnetospheric Accretion: I. Magnetically Disrupted Disks and Surface Accretion (2023)
    - Authors: Zhaohuan Zhu, James M. Stone, Nuria Calvet
    - Citation Key: `arxiv_2309_15318`

    **KaTeX Formula**:
    $$
    vff = ( 2GM* r )1/2 (1- r R0 )1/2
    $$

    Args:
        G (float): Input parameter `G`.
        M (float): Input parameter `M`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float((1/2)*G*M*r)


def expr_v_f_f_form_c(G: str = "G", M: str = "M", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_f_f_form_c`."""
    return ((1/2)*pl.col(G)*pl.col(M)*pl.col(r))


def calc_l_k_x_k_u_form_c(e: float, f: float, k: float, r: float, u: float, w: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_08157.

    **Source**:
    - Title: Event-Time Hybrid Optimal Control for Robotic Table Tennis Serves (2026)
    - Authors: Thomas Gossard, Till Köpff, Andreas Ziegler
    - Citation Key: `arxiv_2608_08157`

    **KaTeX Formula**:
    $$
    l(xk, uk) = wx|xk - xref k |22 +wu|uk|22
    $$

    Args:
        e (float): Input parameter `e`.
        f (float): Input parameter `f`.
        k (float): Input parameter `k`.
        r (float): Input parameter `r`.
        u (float): Input parameter `u`.
        w (float): Input parameter `w`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(22*w*x*abs(e*f*k**2*r*u*x*abs(u*w + 22) - k*x))


def expr_l_k_x_k_u_form_c(e: str = "e", f: str = "f", k: str = "k", r: str = "r", u: str = "u", w: str = "w", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_k_x_k_u_form_c`."""
    return (22*pl.col(w)*pl.col(x)*abs(pl.col(e)*pl.col(f)*pl.col(k)**2*pl.col(r)*pl.col(u)*pl.col(x)*abs(pl.col(u)*pl.col(w) + 22) - pl.col(k)*pl.col(x)))


def calc_u_i_brown_(F: float, X: float, chi: float, i: float, m: float) -> float:
    r"""Compute mathematical metric extracted from brown_2008_arxiv.

    **Source**:
    - Title: In-season prediction of batting averages: a field test of empirical Bayes and Bayes methodologies (2008)
    - Authors: Brown, L. D.
    - Citation Key: `brown_2008_arxiv`

    **KaTeX Formula**:
    $$
    Ui = F \chi 2 mi-1 (Xi)
    $$

    Args:
        F (float): Input parameter `F`.
        X (float): Input parameter `X`.
        chi (float): Input parameter `chi`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*F*chi*i*m - X*i)


def expr_u_i_brown_(F: str = "F", X: str = "X", chi: str = "chi", i: str = "i", m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_i_brown_`."""
    return (2*pl.col(F)*pl.col(chi)*pl.col(i)*pl.col(m) - pl.col(X)*pl.col(i))


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
    return float(20*z + 100)


def expr_i_n_de_x_form_0(z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_n_de_x_form_0`."""
    return (20*pl.col(z) + 100)


def calc_c_v_z_form_0(mu: float, sigma: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_11733.

    **Source**:
    - Title: Reflex-Informed Neuromuscular Reinforcement Learning for Muscle-Driven Locomotion (2026)
    - Authors: Jian Zhou, Xingyu Zhang, Rui Ma et al.
    - Citation Key: `arxiv_2609_11733`

    **KaTeX Formula**:
    $$
    CVz = 100 \sigma z \mu z
    $$

    Args:
        mu (float): Input parameter `mu`.
        sigma (float): Input parameter `sigma`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(100*mu*sigma*z**2)


def expr_c_v_z_form_0(mu: str = "mu", sigma: str = "sigma", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_v_z_form_0`."""
    return (100*pl.col(mu)*pl.col(sigma)*pl.col(z)**2)


def calc_m_p_p_form_4(n: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_02991.

    **Source**:
    - Title: Subject-Specific Predictive Musculoskeletal Simulations of Lower-Limb Exoskeleton Assistance: Metabolic and Biomechanical Effects of Joint Assistance Strategies (2026)
    - Authors: Neethan Ratnakumar, Mariya Tohfafarosh, Xianlian Zhou
    - Citation Key: `arxiv_2610_02991`

    **KaTeX Formula**:
    $$
    MPP = 1/n np\sum  i=1 \tau i ˙ qi, (for \tau i ˙ qi > 0)
    $$

    Args:
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(1/(n**2*p))


def expr_m_p_p_form_4(n: str = "n", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_p_p_form_4`."""
    return (1/(pl.col(n)**2*pl.col(p)))


def calc_m_n_p_form_5(n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_02991.

    **Source**:
    - Title: Subject-Specific Predictive Musculoskeletal Simulations of Lower-Limb Exoskeleton Assistance: Metabolic and Biomechanical Effects of Joint Assistance Strategies (2026)
    - Authors: Neethan Ratnakumar, Mariya Tohfafarosh, Xianlian Zhou
    - Citation Key: `arxiv_2610_02991`

    **KaTeX Formula**:
    $$
    MNP = 1/n nn\sum  i=1 \tau i ˙ qi (for \tau i ˙ qi < 0)
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(1/((n*(n*n))))


def expr_m_n_p_form_5(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_n_p_form_5`."""
    return (1/((pl.col(n)*(pl.col(n)*pl.col(n)))))


def calc_m_p_j_e_p_form_5(J: float, N: float, T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    MPJPE = 1 NT J \sum  n,i,j |Jcan nij -Jcan nij |2
    $$

    Args:
        J (float): Input parameter `J`.
        N (float): Input parameter `N`.
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*(J*T)))


def expr_m_p_j_e_p_form_5(J: str = "J", N: str = "N", T: str = "T") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_p_j_e_p_form_5`."""
    return (1*(pl.col(N)*(pl.col(J)*pl.col(T))))


def calc_c_e_form_5(D: float, alpha: float, m: float, omega: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    EC = (m/2)*(D*\omega 2)2 *\alpha 2
    $$

    Args:
        D (float): Input parameter `D`.
        alpha (float): Input parameter `alpha`.
        m (float): Input parameter `m`.
        omega (float): Input parameter `omega`.

    Returns:
        float: Calculated metric value.
    """
    return float(4*D*alpha*m*omega)


def expr_c_e_form_5(D: str = "D", alpha: str = "alpha", m: str = "m", omega: str = "omega") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_e_form_5`."""
    return (4*pl.col(D)*pl.col(alpha)*pl.col(m)*pl.col(omega))


def calc_c_e_form_6(D: float, alpha: float, m: float, omega: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    EC = (m/2)*(D*\omega 2)2 *\alpha 2
    $$

    Args:
        D (float): Input parameter `D`.
        alpha (float): Input parameter `alpha`.
        m (float): Input parameter `m`.
        omega (float): Input parameter `omega`.

    Returns:
        float: Calculated metric value.
    """
    return float(4*D*alpha*m*omega)


def expr_c_e_form_6(D: str = "D", alpha: str = "alpha", m: str = "m", omega: str = "omega") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_e_form_6`."""
    return (4*pl.col(D)*pl.col(alpha)*pl.col(m)*pl.col(omega))


def calc_delta_e_alpha_t_2_2_form_6(C: float, D: float, S: float, T: float, V: float, alpha: float, q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    \Delta E\alpha (T2/2) = q*S*V*CD\alpha *(T2/2)*\alpha 2
    $$

    Args:
        C (float): Input parameter `C`.
        D (float): Input parameter `D`.
        S (float): Input parameter `S`.
        T (float): Input parameter `T`.
        V (float): Input parameter `V`.
        alpha (float): Input parameter `alpha`.
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float((2*alpha)*(((2*T)/2)*((C*(D*alpha))*(V*(S*q)))))


def expr_delta_e_alpha_t_2_2_form_6(C: str = "C", D: str = "D", S: str = "S", T: str = "T", V: str = "V", alpha: str = "alpha", q: str = "q") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_e_alpha_t_2_2_form_6`."""
    return ((2*pl.col(alpha))*(((2*pl.col(T))/2)*((pl.col(C)*(pl.col(D)*pl.col(alpha)))*(pl.col(V)*(pl.col(S)*pl.col(q))))))


def calc_mu_h_i_form_7(J: float, N: float, h: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    \mu h(i) = 1 NhJ Nh\sum  n=1 J\sum  j=1 |f 3∆3Jhnij |2
    $$

    Args:
        J (float): Input parameter `J`.
        N (float): Input parameter `N`.
        h (float): Input parameter `h`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*(h*(J*(N*h)))))


def expr_mu_h_i_form_7(J: str = "J", N: str = "N", h: str = "h") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_mu_h_i_form_7`."""
    return (1*(pl.col(N)*(pl.col(h)*(pl.col(J)*(pl.col(N)*pl.col(h))))))


def calc_theta_3_form_8(phi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_20570.

    **Source**:
    - Title: Walking on the Slope: Stable Bipedal Gaits with Genetic-Algorithm-Optimized Trajectories (2026)
    - Authors: Madhav Rijal
    - Citation Key: `arxiv_2609_20570`

    **KaTeX Formula**:
    $$
    \theta 3 = 2\phi  (L1=L2), \theta 4 = \theta 3 - \theta 2
    $$

    Args:
        phi (float): Input parameter `phi`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*phi)


def expr_theta_3_form_8(phi: str = "phi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_theta_3_form_8`."""
    return (2*pl.col(phi))


def calc_a_j_u_form_9(K: float, f: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    AUJ = 1 f K-1 \sum  i=1 |\mu g(i) - \mu r(i)| + |\mu g(i + 1) - \mu r(i + 1)| 2
    $$

    Args:
        K (float): Input parameter `K`.
        f (float): Input parameter `f`.

    Returns:
        float: Calculated metric value.
    """
    return float(K*f - 1)


def expr_a_j_u_form_9(K: str = "K", f: str = "f") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_j_u_form_9`."""
    return (pl.col(K)*pl.col(f) - 1)


def calc_w_a_p_form_9(W: float, a: float, b: float, e: float, f: float, o: float, r: float, t: float) -> float:
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
    return float(math.e*W*a*e*f*r*t - math.e*W*b*e**2*f*o*r)


def expr_w_a_p_form_9(W: str = "W", a: str = "a", b: str = "b", e: str = "e", f: str = "f", o: str = "o", r: str = "r", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_a_p_form_9`."""
    return (math.e*pl.col(W)*pl.col(a)*pl.col(e)*pl.col(f)*pl.col(r)*pl.col(t) - math.e*pl.col(W)*pl.col(b)*pl.col(e)**2*pl.col(f)*pl.col(o)*pl.col(r))


def calc_val_1205_2071_form_9(C: float, D: float, S: float, T: float, V: float, alpha: float, e: float, q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    [m*(D*\omega 2)2]*\alpha *\Delta \alpha  = q*S*V *\alpha 2 *e*CD\alpha *T2/2
    $$

    Args:
        C (float): Input parameter `C`.
        D (float): Input parameter `D`.
        S (float): Input parameter `S`.
        T (float): Input parameter `T`.
        V (float): Input parameter `V`.
        alpha (float): Input parameter `alpha`.
        e (float): Input parameter `e`.
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float(((2*T)*((C*(D*alpha))*(e*((2*alpha)*(V*(S*q))))))/2)


def expr_val_1205_2071_form_9(C: str = "C", D: str = "D", S: str = "S", T: str = "T", V: str = "V", alpha: str = "alpha", e: str = "e", q: str = "q") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1205_2071_form_9`."""
    return (((2*pl.col(T))*((pl.col(C)*(pl.col(D)*pl.col(alpha)))*(pl.col(e)*((2*pl.col(alpha))*(pl.col(V)*(pl.col(S)*pl.col(q)))))))/2)


def calc_e_form_a(N: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_11733.

    **Source**:
    - Title: Reflex-Informed Neuromuscular Reinforcement Learning for Muscle-Driven Locomotion (2026)
    - Authors: Jian Zhou, Xingyu Zhang, Rui Ma et al.
    - Citation Key: `arxiv_2609_11733`

    **KaTeX Formula**:
    $$
    e = 1N N\sum  k=1 [ymin(xk) - ¯ y(xk)] + + [¯ y(xk) - ymax(xk)] + max (0.01, ymax(xk) - ymin(xk))
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*N))


def expr_e_form_a(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_form_a`."""
    return (1*(pl.col(N)*pl.col(N)))


def calc_d_i_v_form_c(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10457.

    **Source**:
    - Title: AnimateCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues (2026)
    - Authors: Zeyu Ling, Di Kang, Qing Shuai et al.
    - Citation Key: `arxiv_2609_10457`

    **KaTeX Formula**:
    $$
    Div = 1P P\sum  p=1 |zgap - zgbp |2
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P**2)


def expr_d_i_v_form_c(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_i_v_form_c`."""
    return (pl.col(P)**2)


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
    return float(L*c - 1.2)


def expr_c_g_f_r_form_c(L: str = "L", c: str = "c") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_g_f_r_form_c`."""
    return (pl.col(L)*pl.col(c) - 1.2)


def calc_g_rho_form_d(Sigma: float, g: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1408_4306.

    **Source**:
    - Title: Effect of lift force on the aerodynamics of dust grains in the protoplanetary disk (2014)
    - Authors: Masaki S. Yamaguchi, Shigeo S. Kimura
    - Citation Key: `arxiv_1408_4306`

    **KaTeX Formula**:
    $$
    \rho g = \Sigma g \sqrt \pi Hg = \Sigma 0Ω0 \sqrt 2\pi cs,0 Rp-q-3/2 1
    $$

    Args:
        Sigma (float): Input parameter `Sigma`.
        g (float): Input parameter `g`.

    Returns:
        float: Calculated metric value.
    """
    return float(Sigma*g)


def expr_g_rho_form_d(Sigma: str = "Sigma", g: str = "g") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_rho_form_d`."""
    return (pl.col(Sigma)*pl.col(g))


def calc_n_alpha_form_d(N: float, alpha: float, delta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    {\alpha  N} = {\alpha  N-1} + {\delta N}
    $$

    Args:
        N (float): Input parameter `N`.
        alpha (float): Input parameter `alpha`.
        delta (float): Input parameter `delta`.

    Returns:
        float: Calculated metric value.
    """
    return float(N*delta + (N*alpha - 1))


def expr_n_alpha_form_d(N: str = "N", alpha: str = "alpha", delta: str = "delta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_n_alpha_form_d`."""
    return (pl.col(N)*pl.col(delta) + (pl.col(N)*pl.col(alpha) - 1))


def calc_tan_0_psi_psi_form_d(alpha: float, beta: float, phi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2604_25278.

    **Source**:
    - Title: The GMRT High-Resolution Southern Sky Survey for pulsars and transients -- VIII: Orbital Variability and the Evolution of a 1-Day He-WD Millisecond Pulsar J2101-4802 (2026)
    - Authors: Ankita Ghosh, Bhaswati Bhattacharyya, David L. Kaplan et al.
    - Citation Key: `arxiv_2604_25278`

    **KaTeX Formula**:
    $$
    \tan(\psi -\psi 0) = \sin \alpha  \sin(\phi  - \phi 0) \sin(\alpha  + \beta ) \cos \alpha  - \cos(\alpha  + \beta ) \sin \alpha  \cos(\phi  - \phi 0)
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        beta (float): Input parameter `beta`.
        phi (float): Input parameter `phi`.

    Returns:
        float: Calculated metric value.
    """
    return float(-math.sin(alpha)*math.cos(-0*phi + phi)*math.cos(alpha + beta) + ((math.sin(alpha + beta)*math.cos(alpha))*math.sin(-0*phi + phi))*math.sin(alpha))


def expr_tan_0_psi_psi_form_d(alpha: str = "alpha", beta: str = "beta", phi: str = "phi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_tan_0_psi_psi_form_d`."""
    return (-math.sin(pl.col(alpha))*math.cos(-0*pl.col(phi) + pl.col(phi))*math.cos(pl.col(alpha) + pl.col(beta)) + ((math.sin(pl.col(alpha) + pl.col(beta))*math.cos(pl.col(alpha)))*math.sin(-0*pl.col(phi) + pl.col(phi)))*math.sin(pl.col(alpha)))


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
    return float(a*m*x)


def expr_v_v_1_form_e(a: str = "a", m: str = "m", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_v_1_form_e`."""
    return (pl.col(a)*pl.col(m)*pl.col(x))


def calc_lambda_2_form_e(C: float, D: float, S: float, V: float, alpha: float, e: float, m: float, omega: float, q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    \lambda 2 = [q*S*V*e*CD\alpha ]/[2*m*(D*\omega 2)2]
    $$

    Args:
        C (float): Input parameter `C`.
        D (float): Input parameter `D`.
        S (float): Input parameter `S`.
        V (float): Input parameter `V`.
        alpha (float): Input parameter `alpha`.
        e (float): Input parameter `e`.
        m (float): Input parameter `m`.
        omega (float): Input parameter `omega`.
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float(((C*(D*alpha))*(e*(V*(S*q))))/(((2*m)*(2*(D*(2*omega))))))


def expr_lambda_2_form_e(C: str = "C", D: str = "D", S: str = "S", V: str = "V", alpha: str = "alpha", e: str = "e", m: str = "m", omega: str = "omega", q: str = "q") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_lambda_2_form_e`."""
    return (((pl.col(C)*(pl.col(D)*pl.col(alpha)))*(pl.col(e)*(pl.col(V)*(pl.col(S)*pl.col(q)))))/(((2*pl.col(m))*(2*(pl.col(D)*(2*pl.col(omega)))))))


def calc_r_beta_form_e(H: float, T: float, beta: float, epsilon: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    \beta R = \beta T + \epsilon H
    $$

    Args:
        H (float): Input parameter `H`.
        T (float): Input parameter `T`.
        beta (float): Input parameter `beta`.
        epsilon (float): Input parameter `epsilon`.

    Returns:
        float: Calculated metric value.
    """
    return float(H*epsilon + T*beta)


def expr_r_beta_form_e(H: str = "H", T: str = "T", beta: str = "beta", epsilon: str = "epsilon") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_beta_form_e`."""
    return (pl.col(H)*pl.col(epsilon) + pl.col(T)*pl.col(beta))


def calc_s_w_form_0(l: float, pi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2507_16328.

    **Source**:
    - Title: Design and Dimensional Optimization of Legged Structures for Construction Robots (2025)
    - Authors: Xiao Liu, Xianlong Yang, Weijun Wang et al.
    - Citation Key: `arxiv_2507_16328`

    **KaTeX Formula**:
    $$
    SW = (l2 + l3)2 \pi  3 + l 2 3 \pi  12 -[ 5l 2 2 \pi  12 +( l 2 2 \pi  3 - l 2 3 \sqrt 3 4 )+ l 2 2 \sqrt 3 4 ] = 2l2l3\pi  3
    $$

    Args:
        l (float): Input parameter `l`.
        pi (float): Input parameter `pi`.

    Returns:
        float: Calculated metric value.
    """
    return float(l*(23*(12*pi)) + (2*(3*pi))*(2*l + 3*l))


def expr_s_w_form_0(l: str = "l", pi: str = "pi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_w_form_0`."""
    return (pl.col(l)*(23*(12*pl.col(pi))) + (2*(3*pl.col(pi)))*(2*pl.col(l) + 3*pl.col(l)))


def calc_j_a_o_p_d_theta_form_1(E: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    JAOPD(\theta ) = Ex, y\sim S(\cdot |x) [ 1 H H-1 \sum  t=0 Ea\sim T(\cdot |ht ) [ A S (ht, a) logS\theta (a | ht)]]
    $$

    Args:
        E (float): Input parameter `E`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(E*x)


def expr_j_a_o_p_d_theta_form_1(E: str = "E", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_a_o_p_d_theta_form_1`."""
    return (pl.col(E)*pl.col(x))


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
    return float(T*k*p**2*s + T*s*z + 1)


def expr_y_r_s_h_s_y_p_s_form_1(T: str = "T", k: str = "k", p: str = "p", s: str = "s", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_y_r_s_h_s_y_p_s_form_1`."""
    return (pl.col(T)*pl.col(k)*pl.col(p)**2*pl.col(s) + pl.col(T)*pl.col(s)*pl.col(z) + 1)


def calc_j_0_form_2(psi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2511_10021.

    **Source**:
    - Title: DecARt Leg: Design and Evaluation of a Novel Humanoid Robot Leg with Decoupled Actuation for Agile Locomotion (2025)
    - Authors: Egor Davydenko, Andrei Volchenkov, Vladimir Gerasimov et al.
    - Citation Key: `arxiv_2511_10021`

    **KaTeX Formula**:
    $$
    j0 = \psi
    $$

    Args:
        psi (float): Input parameter `psi`.

    Returns:
        float: Calculated metric value.
    """
    return float(psi)


def expr_j_0_form_2(psi: str = "psi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_0_form_2`."""
    return (pl.col(psi))


def calc_j_i_form_3(alpha: float, dp: float, o: float, p: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_20645.

    **Source**:
    - Title: TACT-ful: Multi-Channel Terrain Affordance and Compliance Training for Payload-Robust Perceptive Humanoid Locomotion (2026)
    - Authors: Thanh Ly, Truong-Duy Dang, Chien Le et al.
    - Citation Key: `arxiv_2606_20645`

    **KaTeX Formula**:
    $$
    Ji = \alpha pos dpos,i + \alpha dcm ddcm,i + \alpha E Ei + \alpha Q Qi + \alpha M Mi - \alpha climb bi
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        dp (float): Input parameter `dp`.
        o (float): Input parameter `o`.
        p (float): Input parameter `p`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(alpha*dp*o**2*p*s**2)


def expr_j_i_form_3(alpha: str = "alpha", dp: str = "dp", o: str = "o", p: str = "p", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_i_form_3`."""
    return (pl.col(alpha)*pl.col(dp)*pl.col(o)**2*pl.col(p)*pl.col(s)**2)


def calc_d_m_s_w_form_3(A: float, U: float, c: float, m: float, p: float, rho: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2604_25278.

    **Source**:
    - Title: The GMRT High-Resolution Southern Sky Survey for pulsars and transients -- VIII: Orbital Variability and the Evolution of a 1-Day He-WD Millisecond Pulsar J2101-4802 (2026)
    - Authors: Ankita Ghosh, Bhaswati Bhattacharyya, David L. Kaplan et al.
    - Citation Key: `arxiv_2604_25278`

    **KaTeX Formula**:
    $$
    DMsw = 4.85 \times  10-6 AAU \rho  \sin\rho  pc cm-3
    $$

    Args:
        A (float): Input parameter `A`.
        U (float): Input parameter `U`.
        c (float): Input parameter `c`.
        m (float): Input parameter `m`.
        p (float): Input parameter `p`.
        rho (float): Input parameter `rho`.

    Returns:
        float: Calculated metric value.
    """
    return float(-6*A**2*U*rho*math.sin(c**2*m*p*rho) + 45.5)


def expr_d_m_s_w_form_3(A: str = "A", U: str = "U", c: str = "c", m: str = "m", p: str = "p", rho: str = "rho") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_m_s_w_form_3`."""
    return (-6*pl.col(A)**2*pl.col(U)*pl.col(rho)*math.sin(pl.col(c)**2*pl.col(m)*pl.col(p)*pl.col(rho)) + 45.5)


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
    return float(c*e*v)


def expr_z_form_4(c: str = "c", e: str = "e", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_form_4`."""
    return (pl.col(c)*pl.col(e)*pl.col(v))


def calc_w_c_y_form_6(B: float, C: float, W: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    W yC = W zB - (W zC \cdot  W zB ) W zC |W zB - (W zC \cdot  W zB) W zC|
    $$

    Args:
        B (float): Input parameter `B`.
        C (float): Input parameter `C`.
        W (float): Input parameter `W`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(-B*C**2*W**3*z**3*abs(B*C**2*W**3*z**3 - B*W*z) + B*W*z)


def expr_w_c_y_form_6(B: str = "B", C: str = "C", W: str = "W", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_c_y_form_6`."""
    return (-pl.col(B)*pl.col(C)**2*pl.col(W)**3*pl.col(z)**3*abs(pl.col(B)*pl.col(C)**2*pl.col(W)**3*pl.col(z)**3 - pl.col(B)*pl.col(W)*pl.col(z)) + pl.col(B)*pl.col(W)*pl.col(z))


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
    return float(L*(P*(C*C)) + L*(M*(E*S)))


def expr_l_a_a_i_form_6(C: str = "C", E: str = "E", L: str = "L", M: str = "M", P: str = "P", S: str = "S") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_a_a_i_form_6`."""
    return (pl.col(L)*(pl.col(P)*(pl.col(C)*pl.col(C))) + pl.col(L)*(pl.col(M)*(pl.col(E)*pl.col(S))))


def calc_h_e_f_f_form_7(a: float, c: float, h: float, i: float, l: float, m: float, n: float, p: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_20645.

    **Source**:
    - Title: TACT-ful: Multi-Channel Terrain Affordance and Compliance Training for Payload-Robust Perceptive Humanoid Locomotion (2026)
    - Authors: Thanh Ly, Truong-Duy Dang, Chien Le et al.
    - Citation Key: `arxiv_2606_20645`

    **KaTeX Formula**:
    $$
    h*eff = h*min + (h*max - h*min ) clip( vx v* , 0, 1)
    $$

    Args:
        a (float): Input parameter `a`.
        c (float): Input parameter `c`.
        h (float): Input parameter `h`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(c*i*l*p*(a*h*m*x - h*i*m*n) + h*i*m*n)


def expr_h_e_f_f_form_7(a: str = "a", c: str = "c", h: str = "h", i: str = "i", l: str = "l", m: str = "m", n: str = "n", p: str = "p", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_e_f_f_form_7`."""
    return (pl.col(c)*pl.col(i)*pl.col(l)*pl.col(p)*(pl.col(a)*pl.col(h)*pl.col(m)*pl.col(x) - pl.col(h)*pl.col(i)*pl.col(m)*pl.col(n)) + pl.col(h)*pl.col(i)*pl.col(m)*pl.col(n))


def calc_omega_o_b_s_form_7(Gamma: float, c: float, k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_18323.

    **Source**:
    - Title: On Lorentz Variability of Magnetically Dominated Relativistic Outflows (2025)
    - Authors: V. I. Berezhiani, N. L. Shatashvili, A. G. Tevzadze
    - Citation Key: `arxiv_2512_18323`

    **KaTeX Formula**:
    $$
    \omega obs = 2kc\Gamma
    $$

    Args:
        Gamma (float): Input parameter `Gamma`.
        c (float): Input parameter `c`.
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*Gamma*c*k)


def expr_omega_o_b_s_form_7(Gamma: str = "Gamma", c: str = "c", k: str = "k") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_omega_o_b_s_form_7`."""
    return (2*pl.col(Gamma)*pl.col(c)*pl.col(k))


def calc_k_theta_l_form_7(L: float, g: float, n: float, omega: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_05895.

    **Source**:
    - Title: Residual Reinforcement Learning for Waste-Container Lifting Using Large-Scale Cranes with Underactuated Tools (2026)
    - Authors: Qi Li, Karsten Berns
    - Citation Key: `arxiv_2602_05895`

    **KaTeX Formula**:
    $$
    k\theta (L) = L\omega 2n - g, k\omega (L) = 2\zeta L\omega n
    $$

    Args:
        L (float): Input parameter `L`.
        g (float): Input parameter `g`.
        n (float): Input parameter `n`.
        omega (float): Input parameter `omega`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*L*n*omega - g)


def expr_k_theta_l_form_7(L: str = "L", g: str = "g", n: str = "n", omega: str = "omega") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_theta_l_form_7`."""
    return (2*pl.col(L)*pl.col(n)*pl.col(omega) - pl.col(g))


def calc_e_u_p_p_e_r_form_a(J: float, T: float, b: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_08059.

    **Source**:
    - Title: Perceptive Behavior Foundation Model: Adapting Human Motion Priors to Robot-Centric Terrain (2026)
    - Authors: Zifan Wang, Yizhao Li, Teli Ma et al.
    - Citation Key: `arxiv_2606_08059`

    **KaTeX Formula**:
    $$
    Eupper = 1 T |Jub| \sum  t,j\in Jub |xtcrs j,t -xraw j,t |2
    $$

    Args:
        J (float): Input parameter `J`.
        T (float): Input parameter `T`.
        b (float): Input parameter `b`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(T*abs(J*b*u))


def expr_e_u_p_p_e_r_form_a(J: str = "J", T: str = "T", b: str = "b", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_u_p_p_e_r_form_a`."""
    return (pl.col(T)*abs(pl.col(J)*pl.col(b)*pl.col(u)))


def calc_e_s_m_o_o_h_t_form_b(F: float, T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_08059.

    **Source**:
    - Title: Perceptive Behavior Foundation Model: Adapting Human Motion Priors to Robot-Centric Terrain (2026)
    - Authors: Zifan Wang, Yizhao Li, Teli Ma et al.
    - Citation Key: `arxiv_2606_08059`

    **KaTeX Formula**:
    $$
    Esmooth = 1 (T - 2)|F| T -1 \sum  t=2 \sum  f\in F |||| pf,t+1 - 2pf,t + pf,t-1 ∆t2 ||||2
    $$

    Args:
        F (float): Input parameter `F`.
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(T*(T - 2)*abs(F) - 1)


def expr_e_s_m_o_o_h_t_form_b(F: str = "F", T: str = "T") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_s_m_o_o_h_t_form_b`."""
    return (pl.col(T)*(pl.col(T) - 2)*abs(pl.col(F)) - 1)


def calc_g_theta_form_b(i: float, m: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    G(\theta ) = 10- 1 10 min{12( \theta  \theta 3dB )2 ,SLA}
    $$

    Args:
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(-110*i*m*n + 10)


def expr_g_theta_form_b(i: str = "i", m: str = "m", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_theta_form_b`."""
    return (-110*pl.col(i)*pl.col(m)*pl.col(n) + 10)


def calc_k_l_l_s_form_c(B: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    L(s) KL = 1 |B| \sum  i\in B \sum  j\in B\{i} R(s) i (j) \log R(s) i (j) P (s) i (j)
    $$

    Args:
        B (float): Input parameter `B`.

    Returns:
        float: Calculated metric value.
    """
    return float(abs(B))


def expr_k_l_l_s_form_c(B: str = "B") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_l_l_s_form_c`."""
    return (abs(pl.col(B)))


def calc_e_p_e_n_form_d(B: float, T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_08059.

    **Source**:
    - Title: Perceptive Behavior Foundation Model: Adapting Human Motion Priors to Robot-Centric Terrain (2026)
    - Authors: Zifan Wang, Yizhao Li, Teli Ma et al.
    - Citation Key: `arxiv_2606_08059`

    **KaTeX Formula**:
    $$
    Epen = 1 T |B| T\sum  t=1 \sum  b\in B[-d\tau  (pb,t)]+
    $$

    Args:
        B (float): Input parameter `B`.
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(T**2*abs(B))


def expr_e_p_e_n_form_d(B: str = "B", T: str = "T") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_p_e_n_form_d`."""
    return (pl.col(T)**2*abs(pl.col(B)))


def calc_q_form_f(G: float, R: float, Sigma: float, kappa: float, sigma: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18161.

    **Source**:
    - Title: In-depth analysis of bar formation mechanisms of disk galaxies in halos of different concentrations (2026)
    - Authors: T. Worrakitpoonpon
    - Citation Key: `arxiv_2601_18161`

    **KaTeX Formula**:
    $$
    Q = \sigma R\kappa  3.36G\Sigma
    $$

    Args:
        G (float): Input parameter `G`.
        R (float): Input parameter `R`.
        Sigma (float): Input parameter `Sigma`.
        kappa (float): Input parameter `kappa`.
        sigma (float): Input parameter `sigma`.

    Returns:
        float: Calculated metric value.
    """
    return float(sigma*(R*(kappa*(3.36*(G*Sigma)))))


def expr_q_form_f(G: str = "G", R: str = "R", Sigma: str = "Sigma", kappa: str = "kappa", sigma: str = "sigma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_form_f`."""
    return (pl.col(sigma)*(pl.col(R)*(pl.col(kappa)*(3.36*(pl.col(G)*pl.col(Sigma))))))


def calc_d_d_form_f(C: float, D: float, L: float, M: float, R: float, alpha: float, k: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    D/d = kx2 *(Iy/Ix)*(R + 1)*(CL\alpha +CD)/CM\alpha
    $$

    Args:
        C (float): Input parameter `C`.
        D (float): Input parameter `D`.
        L (float): Input parameter `L`.
        M (float): Input parameter `M`.
        R (float): Input parameter `R`.
        alpha (float): Input parameter `alpha`.
        k (float): Input parameter `k`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*k*y*(R + 1)*(C*D + C*L*alpha)/(C*M*alpha))


def expr_d_d_form_f(C: str = "C", D: str = "D", L: str = "L", M: str = "M", R: str = "R", alpha: str = "alpha", k: str = "k", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_d_form_f`."""
    return (2*pl.col(k)*pl.col(y)*(pl.col(R) + 1)*(pl.col(C)*pl.col(D) + pl.col(C)*pl.col(L)*pl.col(alpha))/(pl.col(C)*pl.col(M)*pl.col(alpha)))


def calc_r_c_o_m_p_l_y_form_f(B: float, e: float, i: float, l: float, p: float, phi: float, psi: float, r: float, s: float, t: float, v: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2606_20645.

    **Source**:
    - Title: TACT-ful: Multi-Channel Terrain Affordance and Compliance Training for Payload-Robust Perceptive Humanoid Locomotion (2026)
    - Authors: Thanh Ly, Truong-Duy Dang, Chien Le et al.
    - Citation Key: `arxiv_2606_20645`

    **KaTeX Formula**:
    $$
    rcomply = -(zpelvis - z* virt )2 - (\phi B - \phi *virt )2 - (\psi B - \psi * virt )2
    $$

    Args:
        B (float): Input parameter `B`.
        e (float): Input parameter `e`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        p (float): Input parameter `p`.
        phi (float): Input parameter `phi`.
        psi (float): Input parameter `psi`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.
        v (float): Input parameter `v`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(-2*B*phi - 2*B*psi - 2*e*i*l*p*s*v*z + 2*i*phi*r*t*v + 2*i*psi*r*t*v + 2*i*r*t*v*z)


def expr_r_c_o_m_p_l_y_form_f(B: str = "B", e: str = "e", i: str = "i", l: str = "l", p: str = "p", phi: str = "phi", psi: str = "psi", r: str = "r", s: str = "s", t: str = "t", v: str = "v", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_c_o_m_p_l_y_form_f`."""
    return (-2*pl.col(B)*pl.col(phi) - 2*pl.col(B)*pl.col(psi) - 2*pl.col(e)*pl.col(i)*pl.col(l)*pl.col(p)*pl.col(s)*pl.col(v)*pl.col(z) + 2*pl.col(i)*pl.col(phi)*pl.col(r)*pl.col(t)*pl.col(v) + 2*pl.col(i)*pl.col(psi)*pl.col(r)*pl.col(t)*pl.col(v) + 2*pl.col(i)*pl.col(r)*pl.col(t)*pl.col(v)*pl.col(z))


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
    return float(4*y**2)


def expr_l_0_p_w_form_0(y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_0_p_w_form_0`."""
    return (4*pl.col(y)**2)


def calc_r_s_r_s_m_i_x_form_0(eta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    R(S+mix ) - R(S) = \eta  \sum t Eht\sim S(\cdot ) [\sum a S(a | ht)A S (ht, a)2 +\lambda \sum a (T(a | ht) -S(a | ht)) A S (ht, a)] + O(\eta 2 ) = \eta  \sum t Eht\sim S(\cdot ) [Ea\sim S[A S (ht, a)2 ] + \lambda Ea\sim T[A S (ht, a)]] +O(\eta 2 )
    $$

    Args:
        eta (float): Input parameter `eta`.

    Returns:
        float: Calculated metric value.
    """
    return float(eta)


def expr_r_s_r_s_m_i_x_form_0(eta: str = "eta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_s_r_s_m_i_x_form_0`."""
    return (pl.col(eta))


def calc_e_a_sim_t_a_s_h_0_a_form_0(epsilon: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    Ea\sim T[A S (h0, a)] = -(1 - 2\epsilon )2
    $$

    Args:
        epsilon (float): Input parameter `epsilon`.

    Returns:
        float: Calculated metric value.
    """
    return float(4*epsilon - 2)


def expr_e_a_sim_t_a_s_h_0_a_form_0(epsilon: str = "epsilon") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_a_sim_t_a_s_h_0_a_form_0`."""
    return (4*pl.col(epsilon) - 2)


def calc_t_di_f_f_i_c_u_l_t_form_0(epsilon: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    T(difficult) = 1- \epsilon , T(success | difficult) = T(success | safe) = 1- \epsilon
    $$

    Args:
        epsilon (float): Input parameter `epsilon`.

    Returns:
        float: Calculated metric value.
    """
    return float(1 - epsilon)


def expr_t_di_f_f_i_c_u_l_t_form_0(epsilon: str = "epsilon") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_di_f_f_i_c_u_l_t_form_0`."""
    return (1 - pl.col(epsilon))


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
    return float(c*h**2*x + dh*(-p*y + r))


def expr_h_y_form_2(c: str = "c", dh: str = "dh", h: str = "h", p: str = "p", r: str = "r", x: str = "x", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_y_form_2`."""
    return (pl.col(c)*pl.col(h)**2*pl.col(x) + pl.col(dh)*(-pl.col(p)*pl.col(y) + pl.col(r)))


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
    return float(math.e*c)


def expr_l_b_a_e_s_form_a(c: str = "c") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_b_a_e_s_form_a`."""
    return (math.e*pl.col(c))


def calc_l_f_k_l_theta_form_a(H: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    LFKL(\theta ) = 1 H H-1 \sum  t=0 Eht\sim S(.) [KL(T(\cdot  | ht)|S\theta (\cdot  | ht))]
    $$

    Args:
        H (float): Input parameter `H`.

    Returns:
        float: Calculated metric value.
    """
    return float(H**2 - 1)


def expr_l_f_k_l_theta_form_a(H: str = "H") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_f_k_l_theta_form_a`."""
    return (pl.col(H)**2 - 1)


def calc_w_form_4(l: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2507_16328.

    **Source**:
    - Title: Design and Dimensional Optimization of Legged Structures for Construction Robots (2025)
    - Authors: Xiao Liu, Xianlong Yang, Weijun Wang et al.
    - Citation Key: `arxiv_2507_16328`

    **KaTeX Formula**:
    $$
    w = |-l2l3(l1 \sin \theta 3 - l3 \sin \theta 2 + l2 \cos \theta 2 \sin \theta 3 + l3 \cos 2 \theta 3 \sin \theta 2 + l3 \cos \theta 2 \cos \theta 3 \sin \theta 3)|
    $$

    Args:
        l (float): Input parameter `l`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*abs(l**2*(9*l*math.sin(2*theta)*math.cos(6*theta) - 9*l*math.sin(2*theta) + 9*l*math.sin(3*theta)*math.cos(2*theta)*math.cos(3*theta) + 6*l*math.sin(3*theta)*math.cos(2*theta) + 3*l*math.sin(3*theta))))


def expr_w_form_4(l: str = "l", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_form_4`."""
    return (2*abs(pl.col(l)**2*(9*pl.col(l)*math.sin(2*pl.col(theta))*math.cos(6*pl.col(theta)) - 9*pl.col(l)*math.sin(2*pl.col(theta)) + 9*pl.col(l)*math.sin(3*pl.col(theta))*math.cos(2*pl.col(theta))*math.cos(3*pl.col(theta)) + 6*pl.col(l)*math.sin(3*pl.col(theta))*math.cos(2*pl.col(theta)) + 3*pl.col(l)*math.sin(3*pl.col(theta)))))


def calc_r_s_r_pi_form_4(E: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    R(\pi ) - R(S) = Ex,y\sim \pi  [H-1 \sum  t=0 A S (ht, at)] = H-1 \sum  t=0 Eht\sim \pi (\cdot ) [Ea\sim \pi (\cdot |ht)[A S (ht, a)]]
    $$

    Args:
        E (float): Input parameter `E`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(E*x)


def expr_r_s_r_pi_form_4(E: str = "E", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_s_r_pi_form_4`."""
    return (pl.col(E)*pl.col(x))


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
    return float(a*y + h*y)


def expr_p_u_form_5(a: str = "a", h: str = "h", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_u_form_5`."""
    return (pl.col(a)*pl.col(y) + pl.col(h)*pl.col(y))


def calc_g_s_p_e_c_t_r_a_l_form_5(a: float, b: float, e: float, f: float, i: float, l: float, n: float, s: float) -> float:
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
    return float(-a**2*b*e*f*i*l*n*s*math.exp(2) + 100*math.e*a*b*e*s)


def expr_g_s_p_e_c_t_r_a_l_form_5(a: str = "a", b: str = "b", e: str = "e", f: str = "f", i: str = "i", l: str = "l", n: str = "n", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_s_p_e_c_t_r_a_l_form_5`."""
    return (-pl.col(a)**2*pl.col(b)*pl.col(e)*pl.col(f)*pl.col(i)*pl.col(l)*pl.col(n)*pl.col(s)*math.exp(2) + 100*math.e*pl.col(a)*pl.col(b)*pl.col(e)*pl.col(s))


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
    return float(a*m*s*x)


def expr_e_r_e_c_n_o_form_c(a: str = "a", m: str = "m", s: str = "s", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_r_e_c_n_o_form_c`."""
    return (pl.col(a)*pl.col(m)*pl.col(s)*pl.col(x))


def calc_f_form_5(p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2507_16328.

    **Source**:
    - Title: Design and Dimensional Optimization of Legged Structures for Construction Robots (2025)
    - Authors: Xiao Liu, Xianlong Yang, Weijun Wang et al.
    - Citation Key: `arxiv_2507_16328`

    **KaTeX Formula**:
    $$
    F = p\sum  i=1 fi - L\sum  i=1 \lambda i - fp -F ' +\lambda 0
    $$

    Args:
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(p)


def expr_f_form_5(p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_form_5`."""
    return (pl.col(p))


def calc_sim_j_a_o_p_d_theta_form_d(H: float, R: float, S: float, sim: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    \sim JAOPD(\theta ) = \sim R S H H-1 \sum  t=0 [ \sim wt logS\theta (at | ht) - \sum  a\in V \sim  T(a | ht) logS\theta (a | ht)]
    $$

    Args:
        H (float): Input parameter `H`.
        R (float): Input parameter `R`.
        S (float): Input parameter `S`.
        sim (float): Input parameter `sim`.

    Returns:
        float: Calculated metric value.
    """
    return float(sim*(R*(S*(H*H))) - 1)


def expr_sim_j_a_o_p_d_theta_form_d(H: str = "H", R: str = "R", S: str = "S", sim: str = "sim") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sim_j_a_o_p_d_theta_form_d`."""
    return (pl.col(sim)*(pl.col(R)*(pl.col(S)*(pl.col(H)*pl.col(H)))) - 1)


def calc_tau_form_d(l: float, p: float, x: float, y: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2507_16328.

    **Source**:
    - Title: Design and Dimensional Optimization of Legged Structures for Construction Robots (2025)
    - Authors: Xiao Liu, Xianlong Yang, Weijun Wang et al.
    - Citation Key: `arxiv_2507_16328`

    **KaTeX Formula**:
    $$
    \tau  = p 2 x + p 2 y + p 2 z -2l1\sqrt p 2 x + p 2 y
    $$

    Args:
        l (float): Input parameter `l`.
        p (float): Input parameter `p`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(-2*l + 2*p*x + 2*p*y + 2*p*z)


def expr_tau_form_d(l: str = "l", p: str = "p", x: str = "x", y: str = "y", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_tau_form_d`."""
    return (-2*pl.col(l) + 2*pl.col(p)*pl.col(x) + 2*pl.col(p)*pl.col(y) + 2*pl.col(p)*pl.col(z))


def calc_j_4_form_7(j: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2511_10021.

    **Source**:
    - Title: DecARt Leg: Design and Evaluation of a Novel Humanoid Robot Leg with Decoupled Actuation for Agile Locomotion (2025)
    - Authors: Egor Davydenko, Andrei Volchenkov, Vladimir Gerasimov et al.
    - Citation Key: `arxiv_2511_10021`

    **KaTeX Formula**:
    $$
    j4 = \theta  - j1
    $$

    Args:
        j (float): Input parameter `j`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(-j + theta)


def expr_j_4_form_7(j: str = "j", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_4_form_7`."""
    return (-pl.col(j) + pl.col(theta))


def calc_j_u_delta_u_form_7(Delta: float, J: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_13304.

    **Source**:
    - Title: Humanoid Robot Running Through Random Stepping Stones and Jumping Over Obstacles: Step Adaptation Using Spring-Mass Trajectories (2025)
    - Authors: Sait Sovukluk, Johannes Englsberger, Christian Ott
    - Citation Key: `arxiv_2512_13304`

    **KaTeX Formula**:
    $$
    Ju\Delta u = -Jx\Delta x
    $$

    Args:
        Delta (float): Input parameter `Delta`.
        J (float): Input parameter `J`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(-Delta*J*x**2)


def expr_j_u_delta_u_form_7(Delta: str = "Delta", J: str = "J", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_u_delta_u_form_7`."""
    return (-pl.col(Delta)*pl.col(J)*pl.col(x)**2)


def calc_g_k_form_7(A: float, b: float, j: float, nu: float, omega: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_13304.

    **Source**:
    - Title: Humanoid Robot Running Through Random Stepping Stones and Jumping Over Obstacles: Step Adaptation Using Spring-Mass Trajectories (2025)
    - Authors: Sait Sovukluk, Johannes Englsberger, Christian Ott
    - Citation Key: `arxiv_2512_13304`

    **KaTeX Formula**:
    $$
    kG =   A\omega  Aj     \omega b \nu  j
    $$

    Args:
        A (float): Input parameter `A`.
        b (float): Input parameter `b`.
        j (float): Input parameter `j`.
        nu (float): Input parameter `nu`.
        omega (float): Input parameter `omega`.

    Returns:
        float: Calculated metric value.
    """
    return float(A**2*b*j**2*nu*omega**2)


def expr_g_k_form_7(A: str = "A", b: str = "b", j: str = "j", nu: str = "nu", omega: str = "omega") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_k_form_7`."""
    return (pl.col(A)**2*pl.col(b)*pl.col(j)**2*pl.col(nu)*pl.col(omega)**2)


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
    return float(math.e*t)


def expr_l_f_m_form_8(t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_f_m_form_8`."""
    return (math.e*pl.col(t))


def calc_i_x_form_9(N: float, h: float, i: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_28285.

    **Source**:
    - Title: Conformal Koopman Certificates for Nonlinear Multi-Agent Consensus on Time-Evolving Graphs (2026)
    - Authors: Indrakshi Dey, Nicola Marchetti
    - Citation Key: `arxiv_2610_28285`

    **KaTeX Formula**:
    $$
    x+i = xi+h N\sum  j=1 amij tanh(xj -xi) , i = 1, . . . ,N
    $$

    Args:
        N (float): Input parameter `N`.
        h (float): Input parameter `h`.
        i (float): Input parameter `i`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(N*h + i*x)


def expr_i_x_form_9(N: str = "N", h: str = "h", i: str = "i", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_x_form_9`."""
    return (pl.col(N)*pl.col(h) + pl.col(i)*pl.col(x))


def calc_j_5_form_9(j: float, phi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2511_10021.

    **Source**:
    - Title: DecARt Leg: Design and Evaluation of a Novel Humanoid Robot Leg with Decoupled Actuation for Agile Locomotion (2025)
    - Authors: Egor Davydenko, Andrei Volchenkov, Vladimir Gerasimov et al.
    - Citation Key: `arxiv_2511_10021`

    **KaTeX Formula**:
    $$
    j5 = \phi  - j2 - j3
    $$

    Args:
        j (float): Input parameter `j`.
        phi (float): Input parameter `phi`.

    Returns:
        float: Calculated metric value.
    """
    return float(-5*j + phi)


def expr_j_5_form_9(j: str = "j", phi: str = "phi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_5_form_9`."""
    return (-5*pl.col(j) + pl.col(phi))


def calc_p_x_z_form_c(l: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2507_16328.

    **Source**:
    - Title: Design and Dimensional Optimization of Legged Structures for Construction Robots (2025)
    - Authors: Xiao Liu, Xianlong Yang, Weijun Wang et al.
    - Citation Key: `arxiv_2507_16328`

    **KaTeX Formula**:
    $$
    p (x, z) = [l1 + l2 \cos \theta 2 + l3 \cos (\theta 2 + \theta 3) l2 \sin \theta 2 + l3 \sin (\theta 2 + \theta 3) ]
    $$

    Args:
        l (float): Input parameter `l`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(6*l**2*math.sin(2*theta)*math.cos(5*theta) + 3*l*math.sin(5*theta) + 2*l*math.cos(2*theta) + l)


def expr_p_x_z_form_c(l: str = "l", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_x_z_form_c`."""
    return (6*pl.col(l)**2*math.sin(2*pl.col(theta))*math.cos(5*pl.col(theta)) + 3*pl.col(l)*math.sin(5*pl.col(theta)) + 2*pl.col(l)*math.cos(2*pl.col(theta)) + pl.col(l))


def calc_sim_t_w_form_c(i: float, m: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    \sim wt = min ( T(at | ht) S(at | ht) , c)
    $$

    Args:
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*m*n)


def expr_sim_t_w_form_c(i: str = "i", m: str = "m", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sim_t_w_form_c`."""
    return (pl.col(i)*pl.col(m)*pl.col(n))


def calc_l_r_e_c_n_o_form_d(L: float, h: float, l: float, m: float, o: float, s: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2506_17505.

    **Source**:
    - Title: Learning golf swing signatures from a single wrist-worn inertial sensor (2025)
    - Authors: Jessy Lauer
    - Citation Key: `arxiv_2506_17505`

    **KaTeX Formula**:
    $$
    Lrecon = Lsmooth-l1 (M1:T , M1:T ) + \lambda  \cdot  Lsmooth-l1 (V1:T , V1:T )
    $$

    Args:
        L (float): Input parameter `L`.
        h (float): Input parameter `h`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.
        o (float): Input parameter `o`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(L*h*m*o**2*s*t - l)


def expr_l_r_e_c_n_o_form_d(L: str = "L", h: str = "h", l: str = "l", m: str = "m", o: str = "o", s: str = "s", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_r_e_c_n_o_form_d`."""
    return (pl.col(L)*pl.col(h)*pl.col(m)*pl.col(o)**2*pl.col(s)*pl.col(t) - pl.col(l))


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
    return float(math.e*s)


def expr_e_f_i_n_a_l_form_e(s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_f_i_n_a_l_form_e`."""
    return (math.e*pl.col(s))


def calc_j_f_k_l_theta_form_e(x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    JFKL(\theta ) = Ex, y\sim S(\cdot |x) [ 1 H H-1 \sum  t=0 Ea\sim T(\cdot |ht) [logS\theta (a | ht)]]
    $$

    Args:
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e*x)


def expr_j_f_k_l_theta_form_e(x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_f_k_l_theta_form_e`."""
    return (math.e*pl.col(x))


def calc_n_q_form_0(q: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29049.

    **Source**:
    - Title: ART-MPG: Autoregressive R/T Manifold Path Guiding (2026)
    - Authors: Zehao Zhao, Yanyang Yang, Xiaole Zhang et al.
    - Citation Key: `arxiv_2610_29049`

    **KaTeX Formula**:
    $$
    qN = q\theta (n | x), qT = n\prod  i=1 q\theta (ti | t<i, n, x)
    $$

    Args:
        q (float): Input parameter `q`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(q*theta)


def expr_n_q_form_0(q: str = "q", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_n_q_form_0`."""
    return (pl.col(q)*pl.col(theta))


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
    return float(240*T*U)


def expr_c_t_form_0(T: str = "T", U: str = "U") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_t_form_0`."""
    return (240*pl.col(T)*pl.col(U))


def calc_e_0_a_4_i_form_2(A: float, kappa: float, sigma: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    E0(A4i ) = 3\sigma 4A +\kappa
    $$

    Args:
        A (float): Input parameter `A`.
        kappa (float): Input parameter `kappa`.
        sigma (float): Input parameter `sigma`.

    Returns:
        float: Calculated metric value.
    """
    return float(12*A*sigma + kappa)


def expr_e_0_a_4_i_form_2(A: str = "A", kappa: str = "kappa", sigma: str = "sigma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_0_a_4_i_form_2`."""
    return (12*pl.col(A)*pl.col(sigma) + pl.col(kappa))


def calc_l_omega_b_form_3(g: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29049.

    **Source**:
    - Title: ART-MPG: Autoregressive R/T Manifold Path Guiding (2026)
    - Authors: Zehao Zhao, Yanyang Yang, Xiaole Zhang et al.
    - Citation Key: `arxiv_2610_29049`

    **KaTeX Formula**:
    $$
    l\omega (b) = -\log g\theta (\omega b | db, xb)
    $$

    Args:
        g (float): Input parameter `g`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(-math.log(g*theta))


def expr_l_omega_b_form_3(g: str = "g", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_omega_b_form_3`."""
    return (-(pl.col(g).log()*pl.col(theta)))


def calc_log_z_e_form_4(A: float, B: float, N: float, a: float, b: float, i: float, n: float, r: float, sigma: float, t: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    \ln(Z) = -Ntrain \ln(\sigma A) - 12 \ln(|B|) - 1 2\sigma 2A yaB-1 ab yb
    $$

    Args:
        A (float): Input parameter `A`.
        B (float): Input parameter `B`.
        N (float): Input parameter `N`.
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.
        sigma (float): Input parameter `sigma`.
        t (float): Input parameter `t`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(-1*a*(b*(b*y)) + (-12*sigma*(2*(A*(y*(B*a)))) + (-N*t*(r*(a*(i*(n*math.log(A*sigma, math.e))))) - 12*math.log(abs(B), math.e))))


def expr_log_z_e_form_4(A: str = "A", B: str = "B", N: str = "N", a: str = "a", b: str = "b", i: str = "i", n: str = "n", r: str = "r", sigma: str = "sigma", t: str = "t", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_log_z_e_form_4`."""
    return (-1*pl.col(a)*(pl.col(b)*(pl.col(b)*pl.col(y))) + (-12*pl.col(sigma)*(2*(pl.col(A)*(pl.col(y)*(pl.col(B)*pl.col(a))))) + (-pl.col(N)*pl.col(t)*(pl.col(r)*(pl.col(a)*(pl.col(i)*(pl.col(n)*(pl.col(A).log()*pl.col(sigma), math.e))))) - 12*(abs(pl.col(B).log()), math.e))))


def calc_f_k_l_s_form_5(T: float, eta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    S+ FKL = T + \eta T
    $$

    Args:
        T (float): Input parameter `T`.
        eta (float): Input parameter `eta`.

    Returns:
        float: Calculated metric value.
    """
    return float(T*eta + T)


def expr_f_k_l_s_form_5(T: str = "T", eta: str = "eta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_k_l_s_form_5`."""
    return (pl.col(T)*pl.col(eta) + pl.col(T))


def calc_r_s_form_6(N: float, a: float, c: float, e: float, l: float, s: float, u: float, v: float) -> float:
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
    return float(N*(s*(u*(c*(c*(N*(e*(v*(a*l)))))))))


def expr_r_s_form_6(N: str = "N", a: str = "a", c: str = "c", e: str = "e", l: str = "l", s: str = "s", u: str = "u", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_s_form_6`."""
    return (pl.col(N)*(pl.col(s)*(pl.col(u)*(pl.col(c)*(pl.col(c)*(pl.col(N)*(pl.col(e)*(pl.col(v)*(pl.col(a)*pl.col(l))))))))))


def calc_n_pi_form_6(C: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31153.

    **Source**:
    - Title: Balanced Posted Prices in Stationary Two-Sided Markets (2026)
    - Authors: Ilan Reuven Cohen
    - Citation Key: `arxiv_2610_31153`

    **KaTeX Formula**:
    $$
    \pi n = 1 C +1 , n = 0, . . . ,C
    $$

    Args:
        C (float): Input parameter `C`.

    Returns:
        float: Calculated metric value.
    """
    return float(C + 1)


def expr_n_pi_form_6(C: str = "C") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_n_pi_form_6`."""
    return (pl.col(C) + 1)


def calc_val_1_h_r_s_r_pi_form_8(H: float, eta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    1 H (R(\pi ) -R(S)) = \eta H \sum t Eht\sim S(\cdot ) [\sum a v(a | ht)A S (ht, a)] + O(\eta 2 )
    $$

    Args:
        H (float): Input parameter `H`.
        eta (float): Input parameter `eta`.

    Returns:
        float: Calculated metric value.
    """
    return float(H*eta)


def expr_val_1_h_r_s_r_pi_form_8(H: str = "H", eta: str = "eta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1_h_r_s_r_pi_form_8`."""
    return (pl.col(H)*pl.col(eta))


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
    return float(2*A*B*H*a*y**2)


def expr_l_g_a_p_w_form_8(A: str = "A", B: str = "B", H: str = "H", a: str = "a", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_g_a_p_w_form_8`."""
    return (2*pl.col(A)*pl.col(B)*pl.col(H)*pl.col(a)*pl.col(y)**2)


def calc_e_u_s_t_form_9(T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31153.

    **Source**:
    - Title: Balanced Posted Prices in Stationary Two-Sided Markets (2026)
    - Authors: Ilan Reuven Cohen
    - Citation Key: `arxiv_2610_31153`

    **KaTeX Formula**:
    $$
    E[US(T )] = T \sum  j qS j (T)Lj(pj)
    $$

    Args:
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(T)


def expr_e_u_s_t_form_9(T: str = "T") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_u_s_t_form_9`."""
    return (pl.col(T))


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
    return float(W*i*v)


def expr_p_b_a_s_e_l_i_e_n_form_9(W: str = "W", i: str = "i", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_b_a_s_e_l_i_e_n_form_9`."""
    return (pl.col(W)*pl.col(i)*pl.col(v))


def calc_g_a_form_9(T: float, f: float, i: float, l: float, m: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31153.

    **Source**:
    - Title: Balanced Posted Prices in Stationary Two-Sided Markets (2026)
    - Authors: Ilan Reuven Cohen
    - Citation Key: `arxiv_2610_31153`

    **KaTeX Formula**:
    $$
    G(A) = lim inf T\to \infty  1 T E  \sum  sales before T bj - \sum  purchases before T ai 
    $$

    Args:
        T (float): Input parameter `T`.
        f (float): Input parameter `f`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(T*f*i**2*l*m*n)


def expr_g_a_form_9(T: str = "T", f: str = "f", i: str = "i", l: str = "l", m: str = "m", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_a_form_9`."""
    return (pl.col(T)*pl.col(f)*pl.col(i)**2*pl.col(l)*pl.col(m)*pl.col(n))


def calc_l_p_m_form_a(a: float, m: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31153.

    **Source**:
    - Title: Balanced Posted Prices in Stationary Two-Sided Markets (2026)
    - Authors: Ilan Reuven Cohen
    - Citation Key: `arxiv_2610_31153`

    **KaTeX Formula**:
    $$
    LPm = max \sum  k,S ykSvk(S) - \sum  j,r zjrajr : (3) through (6)
    $$

    Args:
        a (float): Input parameter `a`.
        m (float): Input parameter `m`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*m*x)


def expr_l_p_m_form_a(a: str = "a", m: str = "m", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_p_m_form_a`."""
    return (pl.col(a)*pl.col(m)*pl.col(x))


def calc_o_b_k_s_form_9(B: float, k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_07617.

    **Source**:
    - Title: Forecasting the Winner of a Live Tennis Match (2026)
    - Authors: Charles Xie, Aneesh Muppidi
    - Citation Key: `arxiv_2609_07617`

    **KaTeX Formula**:
    $$
    Obsk = 1 |Bk | \sum  i\in Bk yi
    $$

    Args:
        B (float): Input parameter `B`.
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*abs(B*k))


def expr_o_b_k_s_form_9(B: str = "B", k: str = "k") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_o_b_k_s_form_9`."""
    return (1*abs(pl.col(B)*pl.col(k)))


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
    return float(360*P*U*i*n)


def expr_c_p_form_a(P: str = "P", U: str = "U", i: str = "i", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_p_form_a`."""
    return (360*pl.col(P)*pl.col(U)*pl.col(i)*pl.col(n))


def calc_val_2610_31563_form_b(epsilon: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    Ea\sim T[A S (hdifficult, a)] = 1 - 2\epsilon
    $$

    Args:
        epsilon (float): Input parameter `epsilon`.

    Returns:
        float: Calculated metric value.
    """
    return float(1 - 2*epsilon)


def expr_val_2610_31563_form_b(epsilon: str = "epsilon") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_31563_form_b`."""
    return (1 - 2*pl.col(epsilon))


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
    return float(-R*k*r)


def expr_f_r_form_4(R: str = "R", k: str = "k", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_r_form_4`."""
    return (-pl.col(R)*pl.col(k)*pl.col(r))


def calc_q_s_h_0_di_f_f_i_c_u_l_t_form_c(epsilon: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    Q S (h0, difficult) = \epsilon , Q S (h0, safe) = 1- \epsilon
    $$

    Args:
        epsilon (float): Input parameter `epsilon`.

    Returns:
        float: Calculated metric value.
    """
    return float(epsilon)


def expr_q_s_h_0_di_f_f_i_c_u_l_t_form_c(epsilon: str = "epsilon") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_s_h_0_di_f_f_i_c_u_l_t_form_c`."""
    return (pl.col(epsilon))


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
    return float(0.5*C**2*d*l + 0.3*C*l + 0.2*C*p)


def expr_j_form_5(C: str = "C", d: str = "d", l: str = "l", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_form_5`."""
    return (0.5*pl.col(C)**2*pl.col(d)*pl.col(l) + 0.3*pl.col(C)*pl.col(l) + 0.2*pl.col(C)*pl.col(p))


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
    return float((0.1325*W)/N)


def expr_p_s_form_5(N: str = "N", W: str = "W") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_s_form_5`."""
    return ((0.1325*pl.col(W))/pl.col(N))


def calc_e_m_d_n_o_r_m_p_q_form_d(M: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    EMDnorm(p, q) = 1M M\sum  b=1 |Fp(b) - Fq(b)|
    $$

    Args:
        M (float): Input parameter `M`.

    Returns:
        float: Calculated metric value.
    """
    return float(M**2)


def expr_e_m_d_n_o_r_m_p_q_form_d(M: str = "M") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_m_d_n_o_r_m_p_q_form_d`."""
    return (pl.col(M)**2)


def calc_e_a_s_sim_c_a_s_h_a_form_f(eta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31563.

    **Source**:
    - Title: When to Follow the Teacher: Advantage-Based On-Policy Distillation (2026)
    - Authors: Mahdi Sabbaghi, George Pappas, Hamed Hassani et al.
    - Citation Key: `arxiv_2610_31563`

    **KaTeX Formula**:
    $$
    Ea\sim S+ c [A S (h, a)] = \eta \sum a \sim  T(a | h)A S (h, a)2 1+\eta \sum a \sim  T(a | h)A S (h, a) \ge  0
    $$

    Args:
        eta (float): Input parameter `eta`.

    Returns:
        float: Calculated metric value.
    """
    return float(eta)


def expr_e_a_s_sim_c_a_s_h_a_form_f(eta: str = "eta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_a_s_sim_c_a_s_h_a_form_f`."""
    return (pl.col(eta))


def calc_phi_x_form_0(n: float, q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_28993.

    **Source**:
    - Title: Digital Quantum Simulation of Dynamics in Interacting Fields (2026)
    - Authors: Zhiyao Li
    - Citation Key: `arxiv_2610_28993`

    **KaTeX Formula**:
    $$
    \phi x = 2nq -1 \sum  j=0 \phi j |\phi j⟩ ⟨\phi j|x , \phi j = -\phi max + j \delta \phi
    $$

    Args:
        n (float): Input parameter `n`.
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*n*q - 1)


def expr_phi_x_form_0(n: str = "n", q: str = "q") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_phi_x_form_0`."""
    return (2*pl.col(n)*pl.col(q) - 1)


def calc_m_r_s_form_1(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27193.

    **Source**:
    - Title: Low Residuals, Wrong Value: Learning the Viscosity Solution of Hamilton-Jacobi-Isaacs Equations with PINNs (2026)
    - Authors: Raul Jimenez, Pablo Tejerina-Pérez, Leonid Sarieddine et al.
    - Citation Key: `arxiv_2610_27193`

    **KaTeX Formula**:
    $$
    MSR = 1P \sum  P r[VNN] 2
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*P)


def expr_m_r_s_form_1(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_r_s_form_1`."""
    return (1*pl.col(P))


def calc_h_g_form_1(g: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_28993.

    **Source**:
    - Title: Digital Quantum Simulation of Dynamics in Interacting Fields (2026)
    - Authors: Zhiyao Li
    - Citation Key: `arxiv_2610_28993`

    **KaTeX Formula**:
    $$
    Hg = g2 2 \sum  a=1,2,3 2L-2 \sum  b=0 (E(a) b )2 , H\lambda  = \lambda 2 2 \sum  a=1,2,3 (E(a) b=2L-1)2
    $$

    Args:
        g (float): Input parameter `g`.

    Returns:
        float: Calculated metric value.
    """
    return float(22*g)


def expr_h_g_form_1(g: str = "g") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_g_form_1`."""
    return (22*pl.col(g))


def calc_val_2610_28223_form_1(a: float, c: float, n: float, o: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_28223.

    **Source**:
    - Title: Local Inference of LLMs on Long Contexts: A Data Systems Perspective (2026)
    - Authors: Mattias Dürrmeier, Alberto Lerner
    - Citation Key: `arxiv_2610_28223`

    **KaTeX Formula**:
    $$
    MultiHeadAttention(Q, K,V) = concat(H1, . . . , Hℎ)Wout where Hi = Attention(Qi, Ki,Vi )
    $$

    Args:
        a (float): Input parameter `a`.
        c (float): Input parameter `c`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(c*(o*(n*(c*(a*t)))))


def expr_val_2610_28223_form_1(a: str = "a", c: str = "c", n: str = "n", o: str = "o", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_28223_form_1`."""
    return (pl.col(c)*(pl.col(o)*(pl.col(n)*(pl.col(c)*(pl.col(a)*pl.col(t))))))


def calc_sigma_a_a_sigma_form_4(A: float, N: float, a: float, i: float, n: float, r: float, sigma: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    \sigma A\sigma A = 2Ntrain \sigma 2A , (71) W -1 \sigma A\Lambda  = -1 \Lambda 3\sigma A Tr(B'B-1 ), W -1 \Lambda \Lambda  = + 1 2\Lambda 6 Tr(B'B-1B'B-1 )
    $$

    Args:
        A (float): Input parameter `A`.
        N (float): Input parameter `N`.
        a (float): Input parameter `a`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.
        sigma (float): Input parameter `sigma`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*(N*(t*(r*(a*(i*(n*((2*A)*sigma))))))))


def expr_sigma_a_a_sigma_form_4(A: str = "A", N: str = "N", a: str = "a", i: str = "i", n: str = "n", r: str = "r", sigma: str = "sigma", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sigma_a_a_sigma_form_4`."""
    return (2*(pl.col(N)*(pl.col(t)*(pl.col(r)*(pl.col(a)*(pl.col(i)*(pl.col(n)*((2*pl.col(A))*pl.col(sigma)))))))))


def calc_n_q_1_form_4(n: float, sigma: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_28993.

    **Source**:
    - Title: Digital Quantum Simulation of Dynamics in Interacting Fields (2026)
    - Authors: Zhiyao Li
    - Citation Key: `arxiv_2610_28993`

    **KaTeX Formula**:
    $$
    Q(1) n = 12 ( \sigma + 2n \sigma 2n+1 + \sigma 2n \sigma + 2n+1) , Q(2) n = -i 2 ( \sigma + 2n \sigma 2n+1 - \sigma 2n \sigma + 2n+1) , Q(3) n = 14 (  Z2n -  Z2n+1)
    $$

    Args:
        n (float): Input parameter `n`.
        sigma (float): Input parameter `sigma`.

    Returns:
        float: Calculated metric value.
    """
    return float(12*((2*n + (sigma*(2*(n*sigma)) + ((2*(n*((2*n)*sigma)) + sigma) + 1))) + 1))


def expr_n_q_1_form_4(n: str = "n", sigma: str = "sigma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_n_q_1_form_4`."""
    return (12*((2*pl.col(n) + (pl.col(sigma)*(2*(pl.col(n)*pl.col(sigma))) + ((2*(pl.col(n)*((2*pl.col(n))*pl.col(sigma))) + pl.col(sigma)) + 1))) + 1))


def calc_log_b_e_form_5(q: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29049.

    **Source**:
    - Title: ART-MPG: Autoregressive R/T Manifold Path Guiding (2026)
    - Authors: Zehao Zhao, Yanyang Yang, Xiaole Zhang et al.
    - Citation Key: `arxiv_2610_29049`

    **KaTeX Formula**:
    $$
    \ln(b) = -\log q\theta (nb | xb)
    $$

    Args:
        q (float): Input parameter `q`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(-math.log(q*theta))


def expr_log_b_e_form_5(q: str = "q", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_log_b_e_form_5`."""
    return (-(pl.col(q).log()*pl.col(theta)))


def calc_w_sigma_a_a_sigma_form_5(A: float, B: float, N: float, a: float, b: float, i: float, n: float, r: float, sigma: float, t: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    W -1 \sigma A\sigma A = -Ntrain \sigma 2A + 3 \sigma 4A yaB-1 ab yb, (56) W -1 \sigma A\Lambda  \approx  1 \sigma 3A ya ( d d\Lambda  B-1) ab yb, W -1 \Lambda \Lambda  \approx  1 2 d2 d\Lambda 2 \ln(|B|) - 1 2\sigma 2A ya ( d d\Lambda  )2 B-1 ab yb
    $$

    Args:
        A (float): Input parameter `A`.
        B (float): Input parameter `B`.
        N (float): Input parameter `N`.
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.
        sigma (float): Input parameter `sigma`.
        t (float): Input parameter `t`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(-1*a*(b*(b*y)) + (-N*t*(r*(a*(i*(n*((2*A)*sigma))))) + 3*(sigma*(4*(A*(y*(B*a)))))))


def expr_w_sigma_a_a_sigma_form_5(A: str = "A", B: str = "B", N: str = "N", a: str = "a", b: str = "b", i: str = "i", n: str = "n", r: str = "r", sigma: str = "sigma", t: str = "t", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_sigma_a_a_sigma_form_5`."""
    return (-1*pl.col(a)*(pl.col(b)*(pl.col(b)*pl.col(y))) + (-pl.col(N)*pl.col(t)*(pl.col(r)*(pl.col(a)*(pl.col(i)*(pl.col(n)*((2*pl.col(A))*pl.col(sigma)))))) + 3*(pl.col(sigma)*(4*(pl.col(A)*(pl.col(y)*(pl.col(B)*pl.col(a))))))))


def calc_lambda_v_form_5(Phi: float, Psi: float, a: float, cap: float, n: float, p: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29066.

    **Source**:
    - Title: Zero Knowledge for Free up to Linear Query Bounds: Quasilinear-Size Constant-Query Zero-Knowledge PCPs (2026)
    - Authors: Inhyuk Park, Chenglin Fan
    - Citation Key: `arxiv_2610_29066`

    **KaTeX Formula**:
    $$
    \Lambda (V ) = span\Phi  \cap  span\Psi
    $$

    Args:
        Phi (float): Input parameter `Phi`.
        Psi (float): Input parameter `Psi`.
        a (float): Input parameter `a`.
        cap (float): Input parameter `cap`.
        n (float): Input parameter `n`.
        p (float): Input parameter `p`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(s*(p*(a*(n*(Phi*(cap*(s*(p*(a*(Psi*n))))))))))


def expr_lambda_v_form_5(Phi: str = "Phi", Psi: str = "Psi", a: str = "a", cap: str = "cap", n: str = "n", p: str = "p", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_lambda_v_form_5`."""
    return (pl.col(s)*(pl.col(p)*(pl.col(a)*(pl.col(n)*(pl.col(Phi)*(pl.col(cap)*(pl.col(s)*(pl.col(p)*(pl.col(a)*(pl.col(Psi)*pl.col(n)))))))))))


def calc_val_0_form_6(A: float, B: float, N: float, Z: float, a: float, b: float, i: float, n: float, r: float, sigma: float, t: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    0 = Ntrain \sigma 2A Z - Z \sigma 4A yaB-1 ab yb
    $$

    Args:
        A (float): Input parameter `A`.
        B (float): Input parameter `B`.
        N (float): Input parameter `N`.
        Z (float): Input parameter `Z`.
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.
        sigma (float): Input parameter `sigma`.
        t (float): Input parameter `t`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(-1*a*(b*(b*y)) + (N*(t*(r*(a*(i*(n*(sigma*(2*(A*Z)))))))) - Z*sigma*(4*(A*(y*(B*a))))))


def expr_val_0_form_6(A: str = "A", B: str = "B", N: str = "N", Z: str = "Z", a: str = "a", b: str = "b", i: str = "i", n: str = "n", r: str = "r", sigma: str = "sigma", t: str = "t", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_0_form_6`."""
    return (-1*pl.col(a)*(pl.col(b)*(pl.col(b)*pl.col(y))) + (pl.col(N)*(pl.col(t)*(pl.col(r)*(pl.col(a)*(pl.col(i)*(pl.col(n)*(pl.col(sigma)*(2*(pl.col(A)*pl.col(Z))))))))) - pl.col(Z)*pl.col(sigma)*(4*(pl.col(A)*(pl.col(y)*(pl.col(B)*pl.col(a)))))))


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
    return float(T*a + T*b + T*c + T*w - V*a - V*b - V*c - V*w)


def expr_l_form_9(T: str = "T", V: str = "V", a: str = "a", b: str = "b", c: str = "c", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_form_9`."""
    return (pl.col(T)*pl.col(a) + pl.col(T)*pl.col(b) + pl.col(T)*pl.col(c) + pl.col(T)*pl.col(w) - pl.col(V)*pl.col(a) - pl.col(V)*pl.col(b) - pl.col(V)*pl.col(c) - pl.col(V)*pl.col(w))


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
    return float((1.3296*W)/N)


def expr_p_s_form_b(N: str = "N", W: str = "W") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_s_form_b`."""
    return ((1.3296*pl.col(W))/pl.col(N))


def calc_val_2_a_sigma_form_b(B: float, N: float, a: float, b: float, i: float, n: float, r: float, t: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    \sigma 2A = 1 Ntrain yaB-1 ab yb
    $$

    Args:
        B (float): Input parameter `B`.
        N (float): Input parameter `N`.
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*(t*(r*(a*(i*(n*(y*(B*a)))))))) - 1*a*(b*(b*y)))


def expr_val_2_a_sigma_form_b(B: str = "B", N: str = "N", a: str = "a", b: str = "b", i: str = "i", n: str = "n", r: str = "r", t: str = "t", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2_a_sigma_form_b`."""
    return (1*(pl.col(N)*(pl.col(t)*(pl.col(r)*(pl.col(a)*(pl.col(i)*(pl.col(n)*(pl.col(y)*(pl.col(B)*pl.col(a))))))))) - 1*pl.col(a)*(pl.col(b)*(pl.col(b)*pl.col(y))))


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
    return float(L*a**2*de*i*l*m**2*x)


def expr_l_form_c(L: str = "L", a: str = "a", de: str = "de", i: str = "i", l: str = "l", m: str = "m", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_form_c`."""
    return (pl.col(L)*pl.col(a)**2*pl.col(de)*pl.col(i)*pl.col(l)*pl.col(m)**2*pl.col(x))


def calc_d_form_d(K: float, m: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_31153.

    **Source**:
    - Title: Balanced Posted Prices in Stationary Two-Sided Markets (2026)
    - Authors: Ilan Reuven Cohen
    - Citation Key: `arxiv_2610_31153`

    **KaTeX Formula**:
    $$
    d = |K| + m + \sum  j |Rj |
    $$

    Args:
        K (float): Input parameter `K`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(m + abs(K))


def expr_d_form_d(K: str = "K", m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_form_d`."""
    return (pl.col(m) + abs(pl.col(K)))


def calc_val_2_a_sigma_form_e(N: float, a: float, chi: float, i: float, n: float, r: float, t: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    \sigma 2A = 1 Ntrain \chi aya, (68) Z(\sigma 2A,\Lambda ) = \sigma -Ntrain A |B|-1/2 \exp [- 1 2\sigma 2A yaB-1 ab yb] = \sigma -Ntrain A |B|-1/2 e-1/(2Ntrain) when \sigma a is optimized, Y (⃗ \theta ) = \chi aC0(⃗ \theta a, ⃗ \theta ), \sigma 2Y (⃗ \theta ) = \sigma 2A [C0(⃗ \theta , ⃗ \theta ) - C0(⃗ \theta , ⃗ \theta a)B-1 ab C0(⃗ \theta b, ⃗ \theta )] + W\Lambda \Lambda  ( \partial Y \partial \Lambda  )2
    $$

    Args:
        N (float): Input parameter `N`.
        a (float): Input parameter `a`.
        chi (float): Input parameter `chi`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*(t*(r*(a*(i*(n*(chi*(a*(a*y))))))))))


def expr_val_2_a_sigma_form_e(N: str = "N", a: str = "a", chi: str = "chi", i: str = "i", n: str = "n", r: str = "r", t: str = "t", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2_a_sigma_form_e`."""
    return (1*(pl.col(N)*(pl.col(t)*(pl.col(r)*(pl.col(a)*(pl.col(i)*(pl.col(n)*(pl.col(chi)*(pl.col(a)*(pl.col(a)*pl.col(y)))))))))))


def calc_i_theta_form_f(a: float, m: float, theta: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29685.

    **Source**:
    - Title: Optimally Emulating Smooth Functions for Bayesian Analyses (2026)
    - Authors: Scott Pratt, Oleh Savchuk, Eren Erdogan et al.
    - Citation Key: `arxiv_2610_29685`

    **KaTeX Formula**:
    $$
    \theta i = 2\theta max,i (bi - ai) (xi - (ai + bi)/2)
    $$

    Args:
        a (float): Input parameter `a`.
        m (float): Input parameter `m`.
        theta (float): Input parameter `theta`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*a*m*theta*x)


def expr_i_theta_form_f(a: str = "a", m: str = "m", theta: str = "theta", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_theta_form_f`."""
    return (2*pl.col(a)*pl.col(m)*pl.col(theta)*pl.col(x))


def calc_l_s_k_k_l_form_1(B: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    Lsk KL = 1 |B| \sum  xi\in B KL(Rsk i |P sk i )
    $$

    Args:
        B (float): Input parameter `B`.

    Returns:
        float: Calculated metric value.
    """
    return float(abs(B))


def expr_l_s_k_k_l_form_1(B: str = "B") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_s_k_k_l_form_1`."""
    return (abs(pl.col(B)))


def calc_val_2610_26568_form_2(N: float, k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_26568.

    **Source**:
    - Title: Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games (2026)
    - Authors: Durgam Latha, Dion Reji, Dorde Zikelic et al.
    - Citation Key: `arxiv_2610_26568`

    **KaTeX Formula**:
    $$
    X TotN Tot LimAvg X' TotN ' Tot LimAvg c 1 1 1/k N ' = {kN}
    $$

    Args:
        N (float): Input parameter `N`.
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(N*k)


def expr_val_2610_26568_form_2(N: str = "N", k: str = "k") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_26568_form_2`."""
    return (pl.col(N)*pl.col(k))


def calc_g_eta_form_2(alpha: float, eta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_26568.

    **Source**:
    - Title: Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games (2026)
    - Authors: Durgam Latha, Dion Reji, Dorde Zikelic et al.
    - Citation Key: `arxiv_2610_26568`

    **KaTeX Formula**:
    $$
    g(\eta ) = \eta  - 1\alpha  [(1 - p) \eta + + p (\eta  - v)+]
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        eta (float): Input parameter `eta`.

    Returns:
        float: Calculated metric value.
    """
    return float(-alpha + eta)


def expr_g_eta_form_2(alpha: str = "alpha", eta: str = "eta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_eta_form_2`."""
    return (-pl.col(alpha) + pl.col(eta))


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
    return float(3*c*m*r**2)


def expr_a_form_2(c: str = "c", m: str = "m", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_form_2`."""
    return (3*pl.col(c)*pl.col(m)*pl.col(r)**2)


def calc_pi_beta_w_form_3(m: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_26568.

    **Source**:
    - Title: Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games (2026)
    - Authors: Durgam Latha, Dion Reji, Dorde Zikelic et al.
    - Citation Key: `arxiv_2610_26568`

    **KaTeX Formula**:
    $$
    \pi \times (w)(\beta ) = m\prod  i=1 \pi (w)(ti)(\beta i)
    $$

    Args:
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(m)


def expr_pi_beta_w_form_3(m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_pi_beta_w_form_3`."""
    return (pl.col(m))


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


def expr_a_w_form_3(V: str = "V", W: str = "W") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_w_form_3`."""
    return (-pl.col(V) + pl.col(W))


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
    return float((C*D)*(S*q))


def expr_d_f_form_4(C: str = "C", D: str = "D", S: str = "S", q: str = "q") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_f_form_4`."""
    return ((pl.col(C)*pl.col(D))*(pl.col(S)*pl.col(q)))


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
    return float(D*F + F*L)


def expr_f_form_4(D: str = "D", F: str = "F", L: str = "L") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_form_4`."""
    return (pl.col(D)*pl.col(F) + pl.col(F)*pl.col(L))


def calc_h_form_6(a: float, d: float, g: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_28993.

    **Source**:
    - Title: Digital Quantum Simulation of Dynamics in Interacting Fields (2026)
    - Authors: Zhiyao Li
    - Citation Key: `arxiv_2610_28993`

    **KaTeX Formula**:
    $$
    H = g2 2ad-2 \sum  b, links ||| E(b) |||2 + 1 2a4-dg2 \sum  plaquettes [2Nc - □(x) - □† (x)]
    $$

    Args:
        a (float): Input parameter `a`.
        d (float): Input parameter `d`.
        g (float): Input parameter `g`.

    Returns:
        float: Calculated metric value.
    """
    return float(22*a*d*g - 2)


def expr_h_form_6(a: str = "a", d: str = "d", g: str = "g") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_form_6`."""
    return (22*pl.col(a)*pl.col(d)*pl.col(g) - 2)


def calc_e_y_form_6(C: float, H: float, M: float, e: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27057.

    **Source**:
    - Title: Probing Lepton Flavor Violation at FCC-ee (2026)
    - Authors: L. Allwicher, R. Bartocci, M. Cepeda et al.
    - Citation Key: `arxiv_2610_27057`

    **KaTeX Formula**:
    $$
    ye = Me v -CeH v2 \sqrt 2 , (B10)
    $$

    Args:
        C (float): Input parameter `C`.
        H (float): Input parameter `H`.
        M (float): Input parameter `M`.
        e (float): Input parameter `e`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(-2*C*H*e*v + M*e*v)


def expr_e_y_form_6(C: str = "C", H: str = "H", M: str = "M", e: str = "e", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_y_form_6`."""
    return (-2*pl.col(C)*pl.col(H)*pl.col(e)*pl.col(v) + pl.col(M)*pl.col(e)*pl.col(v))


def calc_z_m_i_x_form_e(alpha: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    zmix = \alpha 1z1 + \alpha 2z2,  y = fmix([zsol; zmix; t])
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(5*alpha*z)


def expr_z_m_i_x_form_e(alpha: str = "alpha", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_m_i_x_form_e`."""
    return (5*pl.col(alpha)*pl.col(z))


def calc_r_m_a_x_r_m_i_n_form_7(c: float, e: float, s: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_30305.

    **Source**:
    - Title: Exact turning invariants for projectile motion under quadratic drag and a vertical-axis Magnus force (2026)
    - Authors: Pragyaan Gaur
    - Citation Key: `arxiv_2609_30305`

    **KaTeX Formula**:
    $$
    Rmax Rmin = sec \theta
    $$

    Args:
        c (float): Input parameter `c`.
        e (float): Input parameter `e`.
        s (float): Input parameter `s`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(c*e*s*theta)


def expr_r_m_a_x_r_m_i_n_form_7(c: str = "c", e: str = "e", s: str = "s", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_m_a_x_r_m_i_n_form_7`."""
    return (pl.col(c)*pl.col(e)*pl.col(s)*pl.col(theta))


def calc_sim_j_m_form_8(J: float, i: float, l: float, m: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_29049.

    **Source**:
    - Title: ART-MPG: Autoregressive R/T Manifold Path Guiding (2026)
    - Authors: Zehao Zhao, Yanyang Yang, Xiaole Zhang et al.
    - Citation Key: `arxiv_2610_29049`

    **KaTeX Formula**:
    $$
    \sim  JM = Jimpl1{Jimpl \le  M} obeys
    $$

    Args:
        J (float): Input parameter `J`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(J*i*l*m*p)


def expr_sim_j_m_form_8(J: str = "J", i: str = "i", l: str = "l", m: str = "m", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sim_j_m_form_8`."""
    return (pl.col(J)*pl.col(i)*pl.col(l)*pl.col(m)*pl.col(p))


def calc_r_h_form_a(L: float, gamma: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_30305.

    **Source**:
    - Title: Exact turning invariants for projectile motion under quadratic drag and a vertical-axis Magnus force (2026)
    - Authors: Pragyaan Gaur
    - Citation Key: `arxiv_2609_30305`

    **KaTeX Formula**:
    $$
    Rh = LL \cos \gamma
    $$

    Args:
        L (float): Input parameter `L`.
        gamma (float): Input parameter `gamma`.

    Returns:
        float: Calculated metric value.
    """
    return float(L*(L*math.cos(gamma)))


def expr_r_h_form_a(L: str = "L", gamma: str = "gamma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_h_form_a`."""
    return (pl.col(L)*(pl.col(L)*math.cos(pl.col(gamma))))


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
    return float(6*L**3*R**3*a**3)


def expr_a_l_r_form_a(L: str = "L", R: str = "R", a: str = "a") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_l_r_form_a`."""
    return (6*pl.col(L)**3*pl.col(R)**3*pl.col(a)**3)


def calc_l_e_gamma_i_j_form_a(v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27057.

    **Source**:
    - Title: Probing Lepton Flavor Violation at FCC-ee (2026)
    - Authors: L. Allwicher, R. Bartocci, M. Cepeda et al.
    - Citation Key: `arxiv_2610_27057`

    **KaTeX Formula**:
    $$
    Le\gamma  ij = v \sqrt 2 (cW CeB ij - sW CeW ij ) (B18) + e 48\pi 2 [4mi s2W CHe ij + 2mj (s2W - c2W ) C (1) Hl ij + mj (3c2W + 7s2W ) C (3) Hl ij -24mt \log ( m2Z m2t ) C (3) lequ ij33 ] + \cdot  \cdot  \cdot
    $$

    Args:
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(v)


def expr_l_e_gamma_i_j_form_a(v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_e_gamma_i_j_form_a`."""
    return (pl.col(v))


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
    return float(i*v*y + v*x)


def expr_w_form_a(i: str = "i", v: str = "v", x: str = "x", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_form_a`."""
    return (pl.col(i)*pl.col(v)*pl.col(y) + pl.col(v)*pl.col(x))


def calc_h_m_form_b(Q: float, m: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_28993.

    **Source**:
    - Title: Digital Quantum Simulation of Dynamics in Interacting Fields (2026)
    - Authors: Zhiyao Li
    - Citation Key: `arxiv_2610_28993`

    **KaTeX Formula**:
    $$
    Hm = mQ \sum  n\in Q 1 2 (  I +  Z )n + mq \sum  n\in q 12 (  I +  Z )n + mq \sum  n\in q 12 (  I -  Z )n \to  mq 2 \sum  n\in q,q \sum  c=0,1(-1)\eta n  Z2n+c
    $$

    Args:
        Q (float): Input parameter `Q`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(Q*m)


def expr_h_m_form_b(Q: str = "Q", m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_m_form_b`."""
    return (pl.col(Q)*pl.col(m))


def calc_o_v_x_y_e_e_i_j_k_l_form_b(X: float, Y: float, e: float, gamma: float, i: float, j: float, k: float, l: float, mu: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27057.

    **Source**:
    - Title: Probing Lepton Flavor Violation at FCC-ee (2026)
    - Authors: L. Allwicher, R. Bartocci, M. Cepeda et al.
    - Citation Key: `arxiv_2610_27057`

    **KaTeX Formula**:
    $$
    OVXY ee ijkl = (eXi\gamma  \mu  eXj) (eY k\gamma \mu eY l) , (B14) Oe\gamma  ij = eLi \sigma \mu \nu  eRjF\mu \nu
    $$

    Args:
        X (float): Input parameter `X`.
        Y (float): Input parameter `Y`.
        e (float): Input parameter `e`.
        gamma (float): Input parameter `gamma`.
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.
        k (float): Input parameter `k`.
        l (float): Input parameter `l`.
        mu (float): Input parameter `mu`.

    Returns:
        float: Calculated metric value.
    """
    return float((e*(X*(i*(gamma*(mu*(e*(X*j)))))))*(e*(Y*(k*(gamma*(mu*(e*(Y*l))))))))


def expr_o_v_x_y_e_e_i_j_k_l_form_b(X: str = "X", Y: str = "Y", e: str = "e", gamma: str = "gamma", i: str = "i", j: str = "j", k: str = "k", l: str = "l", mu: str = "mu") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_o_v_x_y_e_e_i_j_k_l_form_b`."""
    return ((pl.col(e)*(pl.col(X)*(pl.col(i)*(pl.col(gamma)*(pl.col(mu)*(pl.col(e)*(pl.col(X)*pl.col(j))))))))*(pl.col(e)*(pl.col(Y)*(pl.col(k)*(pl.col(gamma)*(pl.col(mu)*(pl.col(e)*(pl.col(Y)*pl.col(l)))))))))


def calc_l_o_t_v_form_c(L: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_28203.

    **Source**:
    - Title: JAXbounce: A Continuous-Control Pong-Like Benchmark for Active Inference Beyond Low Dimensional Environments (2026)
    - Authors: Chaitanya Kaul, Markus Klar, Sebastian Stein et al.
    - Citation Key: `arxiv_2610_28203`

    **KaTeX Formula**:
    $$
    lov t = r + L2 - | yl,t - ybat t |
    $$

    Args:
        L (float): Input parameter `L`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*L + r)


def expr_l_o_t_v_form_c(L: str = "L", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_o_t_v_form_c`."""
    return (2*pl.col(L) + pl.col(r))


def calc_l_e_gamma_i_j_h_m_form_c(pi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27057.

    **Source**:
    - Title: Probing Lepton Flavor Violation at FCC-ee (2026)
    - Authors: L. Allwicher, R. Bartocci, M. Cepeda et al.
    - Citation Key: `arxiv_2610_27057`

    **KaTeX Formula**:
    $$
    Le\gamma  ij (mh) = 1 (16\pi 2 )2 8\sqrt 2 3 e3 v Floop( m2t m2h )CeH ij (mh) , (B19)
    $$

    Args:
        pi (float): Input parameter `pi`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(28*(16*(2*pi))))


def expr_l_e_gamma_i_j_h_m_form_c(pi: str = "pi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_e_gamma_i_j_h_m_form_c`."""
    return (1*(28*(16*(2*pl.col(pi)))))


def calc_p_w_t_form_2(Phi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    PWt = 1 -\Phi  ( c - T*(t, a(t), b(t)) \sqrt (1 - t)(\tau  2 + \sigma 2 ) )
    $$

    Args:
        Phi (float): Input parameter `Phi`.

    Returns:
        float: Calculated metric value.
    """
    return float(1 - Phi)


def expr_p_w_t_form_2(Phi: str = "Phi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_w_t_form_2`."""
    return (1 - pl.col(Phi))


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
    return float(w*(-D*k + L*i*k))


def expr_ds_dw_form_d(D: str = "D", L: str = "L", i: str = "i", k: str = "k", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_ds_dw_form_d`."""
    return (pl.col(w)*(-pl.col(D)*pl.col(k) + pl.col(L)*pl.col(i)*pl.col(k)))


def calc_h_form_f(A: float, B: float, H: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_28993.

    **Source**:
    - Title: Digital Quantum Simulation of Dynamics in Interacting Fields (2026)
    - Authors: Zhiyao Li
    - Citation Key: `arxiv_2610_28993`

    **KaTeX Formula**:
    $$
    H = HA + HB, [ HA, HB] ̸= 0
    $$

    Args:
        A (float): Input parameter `A`.
        B (float): Input parameter `B`.
        H (float): Input parameter `H`.

    Returns:
        float: Calculated metric value.
    """
    return float(A*H + B*H)


def expr_h_form_f(A: str = "A", B: str = "B", H: str = "H") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_form_f`."""
    return (pl.col(A)*pl.col(H) + pl.col(B)*pl.col(H))


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
    return float(w*(-D*k + L*i*k)*abs(v))


def expr_dt_dw_form_f(D: str = "D", L: str = "L", i: str = "i", k: str = "k", v: str = "v", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_dt_dw_form_f`."""
    return (pl.col(w)*(-pl.col(D)*pl.col(k) + pl.col(L)*pl.col(i)*pl.col(k))*abs(pl.col(v)))


def calc_z_i_de_a_l_form_0(alpha: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    zideal = \alpha 1z1 +\alpha 2z2, \alpha 1 +\alpha 2 = 1
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(5*alpha*z)


def expr_z_i_de_a_l_form_0(alpha: str = "alpha", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_i_de_a_l_form_0`."""
    return (5*pl.col(alpha)*pl.col(z))


def calc_rho_t_x_p_d_2_form_0(D: float, G: float, K: float, P: float, S: float, T: float, W: float, alpha: float, rho: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25581.

    **Source**:
    - Title: Characterization of integrating-sphere systematic effects for photon calibration of the KAGRA gravitational wave detector (2026)
    - Authors: Shingo Hido, Misato Onishi, Shinji Miyoki et al.
    - Citation Key: `arxiv_2610_25581`

    **KaTeX Formula**:
    $$
    \rho TxPD2 = \rho GSK\alpha WSK/GSK\alpha TxPD2/WSK
    $$

    Args:
        D (float): Input parameter `D`.
        G (float): Input parameter `G`.
        K (float): Input parameter `K`.
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.
        T (float): Input parameter `T`.
        W (float): Input parameter `W`.
        alpha (float): Input parameter `alpha`.
        rho (float): Input parameter `rho`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(((rho*(G*(S*(K*(alpha*(W*(K*S)))))))/((G*(S*(K*(alpha*(T*(x*(P*(2*D))))))))))/((W*(K*S))))


def expr_rho_t_x_p_d_2_form_0(D: str = "D", G: str = "G", K: str = "K", P: str = "P", S: str = "S", T: str = "T", W: str = "W", alpha: str = "alpha", rho: str = "rho", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_rho_t_x_p_d_2_form_0`."""
    return (((pl.col(rho)*(pl.col(G)*(pl.col(S)*(pl.col(K)*(pl.col(alpha)*(pl.col(W)*(pl.col(K)*pl.col(S))))))))/((pl.col(G)*(pl.col(S)*(pl.col(K)*(pl.col(alpha)*(pl.col(T)*(pl.col(x)*(pl.col(P)*(2*pl.col(D)))))))))))/((pl.col(W)*(pl.col(K)*pl.col(S)))))


def calc_w_k_s_form_1(k: float, l: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    w(sk) = \exp(lk) \sum Km=1 \exp(lm)
    $$

    Args:
        k (float): Input parameter `k`.
        l (float): Input parameter `l`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.exp(k*l))


def expr_w_k_s_form_1(k: str = "k", l: str = "l") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_k_s_form_1`."""
    return ((pl.col(k).exp()*pl.col(l)))


def calc_p_r_i_s_m_i_l_s_form_1(K: float, L: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    L(s) PRISM(i) = KL(R(s) i |||P (s) i )
    $$

    Args:
        K (float): Input parameter `K`.
        L (float): Input parameter `L`.

    Returns:
        float: Calculated metric value.
    """
    return float(K*L)


def expr_p_r_i_s_m_i_l_s_form_1(K: str = "K", L: str = "L") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_r_i_s_m_i_l_s_form_1`."""
    return (pl.col(K)*pl.col(L))


def calc_rho_r_x_form_1(D: float, G: float, K: float, P: float, R: float, S: float, W: float, alpha: float, rho: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25581.

    **Source**:
    - Title: Characterization of integrating-sphere systematic effects for photon calibration of the KAGRA gravitational wave detector (2026)
    - Authors: Shingo Hido, Misato Onishi, Shinji Miyoki et al.
    - Citation Key: `arxiv_2610_25581`

    **KaTeX Formula**:
    $$
    \rho Rx = \rho GSK\alpha WSK/GSK\alpha RxPD/WSK
    $$

    Args:
        D (float): Input parameter `D`.
        G (float): Input parameter `G`.
        K (float): Input parameter `K`.
        P (float): Input parameter `P`.
        R (float): Input parameter `R`.
        S (float): Input parameter `S`.
        W (float): Input parameter `W`.
        alpha (float): Input parameter `alpha`.
        rho (float): Input parameter `rho`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(((rho*(G*(S*(K*(alpha*(W*(K*S)))))))/((G*(S*(K*(alpha*(R*(x*(D*P)))))))))/((W*(K*S))))


def expr_rho_r_x_form_1(D: str = "D", G: str = "G", K: str = "K", P: str = "P", R: str = "R", S: str = "S", W: str = "W", alpha: str = "alpha", rho: str = "rho", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_rho_r_x_form_1`."""
    return (((pl.col(rho)*(pl.col(G)*(pl.col(S)*(pl.col(K)*(pl.col(alpha)*(pl.col(W)*(pl.col(K)*pl.col(S))))))))/((pl.col(G)*(pl.col(S)*(pl.col(K)*(pl.col(alpha)*(pl.col(R)*(pl.col(x)*(pl.col(D)*pl.col(P))))))))))/((pl.col(W)*(pl.col(K)*pl.col(S)))))


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
    return float(4*L**2)


def expr_k_1_form_3(L: str = "L") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_1_form_3`."""
    return (4*pl.col(L)**2)


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
    return float((2*v)*(m/2))


def expr_e_v_form_3(m: str = "m", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_v_form_3`."""
    return ((2*pl.col(v))*(pl.col(m)/2))


def calc_l_p_r_i_s_m_i_form_3(K: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    LPRISM(i) = K\sum  s=1 KL(R(s) i |||P (s) i )
    $$

    Args:
        K (float): Input parameter `K`.

    Returns:
        float: Calculated metric value.
    """
    return float(K)


def expr_l_p_r_i_s_m_i_form_3(K: str = "K") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_p_r_i_s_m_i_form_3`."""
    return (pl.col(K))


def calc_psi_t_form_4(n: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2604_21851.

    **Source**:
    - Title: Betting on Bets: Anytime-Valid Tests for Stochastic Dominance (2026)
    - Authors: Sebastian Arnold, Yo Joong Choe, Marco Scarsini et al.
    - Citation Key: `arxiv_2604_21851`

    **KaTeX Formula**:
    $$
    \psi t = nt\sum i=1 wt (zt i )\delta zt i
    $$

    Args:
        n (float): Input parameter `n`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(n*t)


def expr_psi_t_form_4(n: str = "n", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_psi_t_form_4`."""
    return (pl.col(n)*pl.col(t))


def calc_n_g_n_l_s_form_5(B: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    L(s) NNG = 1 |B| \sum  i\in B -1 |P (s) i | \sum  j\in P (s) i \log \exp(sim(r(s) i , r(s) j )/\tau  ) \sum l\in B\{i} \exp(sim(r(s) i , r(s) l )/\tau  )
    $$

    Args:
        B (float): Input parameter `B`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*abs(B))


def expr_n_g_n_l_s_form_5(B: str = "B") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_n_g_n_l_s_form_5`."""
    return (1*abs(pl.col(B)))


def calc_phi_eta_form_5(alpha: float, eta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_26568.

    **Source**:
    - Title: Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games (2026)
    - Authors: Durgam Latha, Dion Reji, Dorde Zikelic et al.
    - Citation Key: `arxiv_2610_26568`

    **KaTeX Formula**:
    $$
    \phi (\eta ) = \eta  - 1\alpha  \sum  u pu (\eta  - xu)+
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        eta (float): Input parameter `eta`.

    Returns:
        float: Calculated metric value.
    """
    return float(-alpha + eta)


def expr_phi_eta_form_5(alpha: str = "alpha", eta: str = "eta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_phi_eta_form_5`."""
    return (-pl.col(alpha) + pl.col(eta))


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
    return float(-A*R*e*p*x + C*G*R)


def expr_d_form_6(A: str = "A", C: str = "C", G: str = "G", R: str = "R", e: str = "e", p: str = "p", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_form_6`."""
    return (-pl.col(A)*pl.col(R)*pl.col(e)*pl.col(p)*pl.col(x) + pl.col(C)*pl.col(G)*pl.col(R))


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
    return float(i*p)


def expr_p_i_t_form_6(i: str = "i", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_t_form_6`."""
    return (pl.col(i)*pl.col(p))


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
    return float(0.03*m)


def expr_c_p_form_f(m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_p_form_f`."""
    return (0.03*pl.col(m))


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
    return float(-4*D*g*(L*g - 1/2) + (L*g - 2)*(L*g - 1/2) - 1)


def expr_y_form_f(D: str = "D", L: str = "L", g: str = "g") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_y_form_f`."""
    return (-4*pl.col(D)*pl.col(g)*(pl.col(L)*pl.col(g) - 1/2) + (pl.col(L)*pl.col(g) - 2)*(pl.col(L)*pl.col(g) - 1/2) - 1)


def calc_l_s_h_a_r_e_d_i_form_7(K: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    Lshared(i) = K\sum  s=1 \sum  j R(s) i (j) logR(s) i (j) -K \sum  j ¯Ri(j) \log Pi(j)
    $$

    Args:
        K (float): Input parameter `K`.

    Returns:
        float: Calculated metric value.
    """
    return float(K)


def expr_l_s_h_a_r_e_d_i_form_7(K: str = "K") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_s_h_a_r_e_d_i_form_7`."""
    return (pl.col(K))


def calc_val_2610_25605_form_8(K: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    \partial Lshared(i) \partial uij = K\sum  s=1 (Pi(j) - R(s) i (j)) =K (Pi(j) - ¯Ri(j))
    $$

    Args:
        K (float): Input parameter `K`.

    Returns:
        float: Calculated metric value.
    """
    return float(K)


def expr_val_2610_25605_form_8(K: str = "K") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2610_25605_form_8`."""
    return (pl.col(K))


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
    return float(V*i*m)


def expr_p_m_form_9(V: str = "V", i: str = "i", m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_m_form_9`."""
    return (pl.col(V)*pl.col(i)*pl.col(m))


def calc_true_form_9(v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_26568.

    **Source**:
    - Title: Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games (2026)
    - Authors: Durgam Latha, Dion Reji, Dorde Zikelic et al.
    - Citation Key: `arxiv_2610_26568`

    **KaTeX Formula**:
    $$
    sup \sigma \in \Sigma ' inf \pi \in \Pi ' f(\sigma , \pi ) = inf \pi \in \Pi ' sup \sigma \in \Sigma ' f (\sigma , \pi ) = v
    $$

    Args:
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(v)


def expr_true_form_9(v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_true_form_9`."""
    return (pl.col(v))


def calc_beta_c_v_a_r_alpha_v_p_form_9(a: float, m: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_26568.

    **Source**:
    - Title: Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games (2026)
    - Authors: Durgam Latha, Dion Reji, Dorde Zikelic et al.
    - Citation Key: `arxiv_2610_26568`

    **KaTeX Formula**:
    $$
    \beta CVaR\alpha  v (p) =max{g(0), g(v)} =max{0, v(1- 1-p \alpha  )}
    $$

    Args:
        a (float): Input parameter `a`.
        m (float): Input parameter `m`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(m*(a*x))


def expr_beta_c_v_a_r_alpha_v_p_form_9(a: str = "a", m: str = "m", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_beta_c_v_a_r_alpha_v_p_form_9`."""
    return (pl.col(m)*(pl.col(a)*pl.col(x)))


def calc_e_s_k_n_y_form_b(Q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    E sk n (y) = 1 |Q| \sum  i\in Q 1n \sum  j\in N sk n (xi)(yi - yj)2
    $$

    Args:
        Q (float): Input parameter `Q`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*abs(Q))


def expr_e_s_k_n_y_form_b(Q: str = "Q") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_s_k_n_y_form_b`."""
    return (1*abs(pl.col(Q)))


def calc_f_p_b_form_d(b: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    Fp(b) = b\sum  m=1 pm, Fq(b) = b\sum  m=1 qm
    $$

    Args:
        b (float): Input parameter `b`.

    Returns:
        float: Calculated metric value.
    """
    return float(b)


def expr_f_p_b_form_d(b: str = "b") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_p_b_form_d`."""
    return (pl.col(b))


def calc_g_eta_form_e(alpha: float, eta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_26568.

    **Source**:
    - Title: Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games (2026)
    - Authors: Durgam Latha, Dion Reji, Dorde Zikelic et al.
    - Citation Key: `arxiv_2610_26568`

    **KaTeX Formula**:
    $$
    g(\eta ) = \eta  - 1\alpha  E[(\eta  - Z)+], so that CVaR\alpha (Z) = sup \eta \in R g(\eta )
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        eta (float): Input parameter `eta`.

    Returns:
        float: Calculated metric value.
    """
    return float(-math.e*alpha + eta)


def expr_g_eta_form_e(alpha: str = "alpha", eta: str = "eta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_eta_form_e`."""
    return (-math.e*pl.col(alpha) + pl.col(eta))


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
    return float(B**3*W**3*x*y*z)


def expr_w_b_r_form_0(B: str = "B", W: str = "W", x: str = "x", y: str = "y", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_b_r_form_0`."""
    return (pl.col(B)**3*pl.col(W)**3*pl.col(x)*pl.col(y)*pl.col(z))


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
    return float(0.08*e**2)


def expr_e_form_1(e: str = "e") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_form_1`."""
    return (0.08*pl.col(e)**2)


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
    return float(B**2*W**2*y*z)


def expr_w_b_x_form_1(B: str = "B", W: str = "W", y: str = "y", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_b_x_form_1`."""
    return (pl.col(B)**2*pl.col(W)**2*pl.col(y)*pl.col(z))


def calc_l_form_2(N: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_07617.

    **Source**:
    - Title: Forecasting the Winner of a Live Tennis Match (2026)
    - Authors: Charles Xie, Aneesh Muppidi
    - Citation Key: `arxiv_2609_07617`

    **KaTeX Formula**:
    $$
    L = - 1N N\sum  i=1 [yi \log(pi) + (1 - yi) \log(1 - pi)]
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(-N*N)


def expr_l_form_2(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_form_2`."""
    return (-pl.col(N)*pl.col(N))


def calc_p_r_dk_e_form_3(B: float, k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_07617.

    **Source**:
    - Title: Forecasting the Winner of a Live Tennis Match (2026)
    - Authors: Charles Xie, Aneesh Muppidi
    - Citation Key: `arxiv_2609_07617`

    **KaTeX Formula**:
    $$
    Predk = 1 |Bk | \sum  i\in Bk pi
    $$

    Args:
        B (float): Input parameter `B`.
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(abs(B*k))


def expr_p_r_dk_e_form_3(B: str = "B", k: str = "k") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_r_dk_e_form_3`."""
    return (abs(pl.col(B)*pl.col(k)))


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
    return float(e*f*r*x - x)


def expr_e_p_form_3(e: str = "e", f: str = "f", r: str = "r", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_p_form_3`."""
    return (pl.col(e)*pl.col(f)*pl.col(r)*pl.col(x) - pl.col(x))


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
    return float(B**3*W**3*x*y*z)


def expr_w_b_r_form_3(B: str = "B", W: str = "W", x: str = "x", y: str = "y", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_b_r_form_3`."""
    return (pl.col(B)**3*pl.col(W)**3*pl.col(x)*pl.col(y)*pl.col(z))


def calc_a_p_form_5(kappa: float, n: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_07617.

    **Source**:
    - Title: Forecasting the Winner of a Live Tennis Match (2026)
    - Authors: Charles Xie, Aneesh Muppidi
    - Citation Key: `arxiv_2609_07617`

    **KaTeX Formula**:
    $$
    pa = n1r1 + \kappa \pi 1 n1 +\kappa  , pb = n2r2 + \kappa \pi 2 n2 +\kappa
    $$

    Args:
        kappa (float): Input parameter `kappa`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.pi*kappa*n + kappa + n*r)


def expr_a_p_form_5(kappa: str = "kappa", n: str = "n", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_p_form_5`."""
    return (math.pi*pl.col(kappa)*pl.col(n) + pl.col(kappa) + pl.col(n)*pl.col(r))


def calc_a_j_h_form_8(a: float, di: float, i: float, l: float, m: float, n: float, r: float, s: float) -> float:
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
    return float(0.1129*a**2*di*i**2*l**2*m*n*r*s)


def expr_a_j_h_form_8(a: str = "a", di: str = "di", i: str = "i", l: str = "l", m: str = "m", n: str = "n", r: str = "r", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_j_h_form_8`."""
    return (0.1129*pl.col(a)**2*pl.col(di)*pl.col(i)**2*pl.col(l)**2*pl.col(m)*pl.col(n)*pl.col(r)*pl.col(s))


def calc_i_z_form_8(K: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    zi = K\sum  k=1 w(sk) i h(sk) i
    $$

    Args:
        K (float): Input parameter `K`.

    Returns:
        float: Calculated metric value.
    """
    return float(K)


def expr_i_z_form_8(K: str = "K") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_z_form_8`."""
    return (pl.col(K))


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
    return float(-l*w + 1)


def expr_s_w_form_8(l: str = "l", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_w_form_8`."""
    return (-pl.col(l)*pl.col(w) + 1)


def calc_z_m_i_x_form_8(alpha: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    zmix = \alpha 1z1 +\alpha 2z2, \alpha 1 +\alpha 2 = 1
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(5*alpha*z)


def expr_z_m_i_x_form_8(alpha: str = "alpha", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_m_i_x_form_8`."""
    return (5*pl.col(alpha)*pl.col(z))


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
    return float(12*R)


def expr_l_r_o_l_l_j_o_i_n_form_9(R: str = "R") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_r_o_l_l_j_o_i_n_form_9`."""
    return (12*pl.col(R))


def calc_rho_t_x_p_d_1_form_9(D: float, G: float, K: float, P: float, S: float, T: float, W: float, alpha: float, rho: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25581.

    **Source**:
    - Title: Characterization of integrating-sphere systematic effects for photon calibration of the KAGRA gravitational wave detector (2026)
    - Authors: Shingo Hido, Misato Onishi, Shinji Miyoki et al.
    - Citation Key: `arxiv_2610_25581`

    **KaTeX Formula**:
    $$
    \rho TxPD1 = \rho GSK\alpha WSK/GSK\alpha TxPD1/WSK
    $$

    Args:
        D (float): Input parameter `D`.
        G (float): Input parameter `G`.
        K (float): Input parameter `K`.
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.
        T (float): Input parameter `T`.
        W (float): Input parameter `W`.
        alpha (float): Input parameter `alpha`.
        rho (float): Input parameter `rho`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(((rho*(G*(S*(K*(alpha*(W*(K*S)))))))/((G*(S*(K*(alpha*(T*(x*(P*(1*D))))))))))/((W*(K*S))))


def expr_rho_t_x_p_d_1_form_9(D: str = "D", G: str = "G", K: str = "K", P: str = "P", S: str = "S", T: str = "T", W: str = "W", alpha: str = "alpha", rho: str = "rho", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_rho_t_x_p_d_1_form_9`."""
    return (((pl.col(rho)*(pl.col(G)*(pl.col(S)*(pl.col(K)*(pl.col(alpha)*(pl.col(W)*(pl.col(K)*pl.col(S))))))))/((pl.col(G)*(pl.col(S)*(pl.col(K)*(pl.col(alpha)*(pl.col(T)*(pl.col(x)*(pl.col(P)*(1*pl.col(D)))))))))))/((pl.col(W)*(pl.col(K)*pl.col(S)))))


def calc_f_m_a_x_form_9(F: float, G: float, H: float, K: float, M: float, R: float, S: float, a: float, m: float, x: float) -> float:
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
    return float((R*(M*(S*(K*(R*(G*(M*(K*S))))))))*(((M*(F*(G*(m*(a*x)))))/((H*(G*M))))/((G*H))))


def expr_f_m_a_x_form_9(F: str = "F", G: str = "G", H: str = "H", K: str = "K", M: str = "M", R: str = "R", S: str = "S", a: str = "a", m: str = "m", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_m_a_x_form_9`."""
    return ((pl.col(R)*(pl.col(M)*(pl.col(S)*(pl.col(K)*(pl.col(R)*(pl.col(G)*(pl.col(M)*(pl.col(K)*pl.col(S)))))))))*(((pl.col(M)*(pl.col(F)*(pl.col(G)*(pl.col(m)*(pl.col(a)*pl.col(x))))))/((pl.col(H)*(pl.col(G)*pl.col(M)))))/((pl.col(G)*pl.col(H)))))


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
    return float(J*c*i*j - c*i*r)


def expr_p_c_i_j_form_9(J: str = "J", c: str = "c", i: str = "i", j: str = "j", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_c_i_j_form_9`."""
    return (pl.col(J)*pl.col(c)*pl.col(i)*pl.col(j) - pl.col(c)*pl.col(i)*pl.col(r))


def calc_z_m_i_x_form_9(alpha: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    zmix = \alpha 1z1 + \alpha 2z2,  y = fmix ([zsol; zmix; t])
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(5*alpha*z)


def expr_z_m_i_x_form_9(alpha: str = "alpha", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_m_i_x_form_9`."""
    return (5*pl.col(alpha)*pl.col(z))


def calc_a_v_e_phi_t_form_a(gamma: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_1205_2071.

    **Source**:
    - Title: A Coning Theory of Bullet Motions (2012)
    - Authors: James A. Boatright
    - Citation Key: `arxiv_1205_2071`

    **KaTeX Formula**:
    $$
    AVE{\phi (t)} = \gamma 0*((R2 - 1)/(n*2\pi *R)*[1 - Cos(n*2\pi /(R - 1))] AVE{\phi (t)} = -4.151 milliradians
    $$

    Args:
        gamma (float): Input parameter `gamma`.

    Returns:
        float: Calculated metric value.
    """
    return float(0*gamma)


def expr_a_v_e_phi_t_form_a(gamma: str = "gamma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_v_e_phi_t_form_a`."""
    return (0*pl.col(gamma))


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


def expr_l_r_o_l_l_e_x_c_e_s_s_form_c(R: str = "R") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_r_o_l_l_e_x_c_e_s_s_form_c`."""
    return (pl.col(R))


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


def expr_o_form_c(p: str = "p", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_o_form_c`."""
    return (pl.col(p) + pl.col(w))


def calc_l_s_h_a_r_e_d_i_form_c(K: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    Lshared(i) = K\sum  s=1 \sum  j\in Ci R(s) i (j) \log R(s) i (j) Pi(j) = K\sum  s=1 \sum  j R(s) i (j) logR(s) i (j) - K\sum  s=1 \sum  j R(s) i (j) logPi(j)
    $$

    Args:
        K (float): Input parameter `K`.

    Returns:
        float: Calculated metric value.
    """
    return float(K)


def expr_l_s_h_a_r_e_d_i_form_c(K: str = "K") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_s_h_a_r_e_d_i_form_c`."""
    return (pl.col(K))


def calc_i_z_form_f(K: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    zi = K\sum  k=1 w(sk)h(sk) i
    $$

    Args:
        K (float): Input parameter `K`.

    Returns:
        float: Calculated metric value.
    """
    return float(K)


def expr_i_z_form_f(K: str = "K") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_z_form_f`."""
    return (pl.col(K))


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
    return float((p*(z*(2*c)) + (p*(x*(2*a)) + p*(y*(2*b)))) - 1)


def expr_e_p_form_1(a: str = "a", b: str = "b", c: str = "c", p: str = "p", x: str = "x", y: str = "y", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_p_form_1`."""
    return ((pl.col(p)*(pl.col(z)*(2*pl.col(c))) + (pl.col(p)*(pl.col(x)*(2*pl.col(a))) + pl.col(p)*(pl.col(y)*(2*pl.col(b))))) - 1)


def calc_v_infty_t_x_form_1(T: float, i: float, l: float, m: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    V\infty (t, x) = lim T\to \infty  VT (t, x) = E [\int  \tau  *\infty (t,x) 0 c(t + u) du + g(Xx \tau  *\infty (t,x) )]
    $$

    Args:
        T (float): Input parameter `T`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(T*i*l*m)


def expr_v_infty_t_x_form_1(T: str = "T", i: str = "i", l: str = "l", m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_infty_t_x_form_1`."""
    return (pl.col(T)*pl.col(i)*pl.col(l)*pl.col(m))


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
    return float(C*T**2*u*v*w)


def expr_t_p_x_p_y_p_z_1_form_5(C: str = "C", T: str = "T", u: str = "u", v: str = "v", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_p_x_p_y_p_z_1_form_5`."""
    return (pl.col(C)*pl.col(T)**2*pl.col(u)*pl.col(v)*pl.col(w))


def calc_v_t_t_x_form_5(i: float, l: float, m: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    V T (t, x) = lim n\to \infty  V n T (t, x) \le  lim n\to \infty  E [Ft(\tau n) + g(Xx \tau n )] = E [Ft(\tau  ) + g(Xx \tau  )]
    $$

    Args:
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*l*m*n)


def expr_v_t_t_x_form_5(i: str = "i", l: str = "l", m: str = "m", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_t_t_x_form_5`."""
    return (pl.col(i)*pl.col(l)*pl.col(m)*pl.col(n))


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
    return float(C**2*W**2*y*z)


def expr_w_c_x_form_9(C: str = "C", W: str = "W", y: str = "y", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_c_x_form_9`."""
    return (pl.col(C)**2*pl.col(W)**2*pl.col(y)*pl.col(z))


def calc_i_w_form_a(i: float, sigma: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25581.

    **Source**:
    - Title: Characterization of integrating-sphere systematic effects for photon calibration of the KAGRA gravitational wave detector (2026)
    - Authors: Shingo Hido, Misato Onishi, Shinji Miyoki et al.
    - Citation Key: `arxiv_2610_25581`

    **KaTeX Formula**:
    $$
    wi = 1 \sigma 2 i
    $$

    Args:
        i (float): Input parameter `i`.
        sigma (float): Input parameter `sigma`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*i*sigma)


def expr_i_w_form_a(i: str = "i", sigma: str = "sigma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_w_form_a`."""
    return (2*pl.col(i)*pl.col(sigma))


def calc_f_c_d_m_form_a(K: float, M: float, da: float, e: float, i: float, p: float, v: float, x: float, y: float) -> float:
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
    return float(K*e*i**2 + K*e*p**2 + K*e*v**2 + M*da*x*y)


def expr_f_c_d_m_form_a(K: str = "K", M: str = "M", da: str = "da", e: str = "e", i: str = "i", p: str = "p", v: str = "v", x: str = "x", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_c_d_m_form_a`."""
    return (pl.col(K)*pl.col(e)*pl.col(i)**2 + pl.col(K)*pl.col(e)*pl.col(p)**2 + pl.col(K)*pl.col(e)*pl.col(v)**2 + pl.col(M)*pl.col(da)*pl.col(x)*pl.col(y))


def calc_theta_form_b(e: float, i: float, kappa: float, l: float, n: float, o: float, p: float, r: float, theta: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_07617.

    **Source**:
    - Title: Forecasting the Winner of a Live Tennis Match (2026)
    - Authors: Charles Xie, Aneesh Muppidi
    - Citation Key: `arxiv_2609_07617`

    **KaTeX Formula**:
    $$
    \theta  = n n + \kappa   \theta live + \kappa  n + \kappa  \theta prior
    $$

    Args:
        e (float): Input parameter `e`.
        i (float): Input parameter `i`.
        kappa (float): Input parameter `kappa`.
        l (float): Input parameter `l`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.
        theta (float): Input parameter `theta`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(e*i*kappa*l*theta*v + i*kappa*o*p*r**2*theta + kappa*n + n**2)


def expr_theta_form_b(e: str = "e", i: str = "i", kappa: str = "kappa", l: str = "l", n: str = "n", o: str = "o", p: str = "p", r: str = "r", theta: str = "theta", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_theta_form_b`."""
    return (pl.col(e)*pl.col(i)*pl.col(kappa)*pl.col(l)*pl.col(theta)*pl.col(v) + pl.col(i)*pl.col(kappa)*pl.col(o)*pl.col(p)*pl.col(r)**2*pl.col(theta) + pl.col(kappa)*pl.col(n) + pl.col(n)**2)


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
    return float(a*t + c*dt*m*q)


def expr_q_dt_p_form_c(a: str = "a", c: str = "c", dt: str = "dt", m: str = "m", q: str = "q", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_dt_p_form_c`."""
    return (pl.col(a)*pl.col(t) + pl.col(c)*pl.col(dt)*pl.col(m)*pl.col(q))


def calc_val_2_r_phi_form_d(a: float, n: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18161.

    **Source**:
    - Title: In-depth analysis of bar formation mechanisms of disk galaxies in halos of different concentrations (2026)
    - Authors: T. Worrakitpoonpon
    - Citation Key: `arxiv_2601_18161`

    **KaTeX Formula**:
    $$
    \phi 2(R) = atan2(b2, a2)
    $$

    Args:
        a (float): Input parameter `a`.
        n (float): Input parameter `n`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*a**2*n*t)


def expr_val_2_r_phi_form_d(a: str = "a", n: str = "n", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2_r_phi_form_d`."""
    return (2*pl.col(a)**2*pl.col(n)*pl.col(t))


def calc_tau_t_l_form_0(f: float, i: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    \tau (t, l) = inf{s \ge  0 : (t + s, Lls) \in  A}
    $$

    Args:
        f (float): Input parameter `f`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(f*i*n)


def expr_tau_t_l_form_0(f: str = "f", i: str = "i", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_tau_t_l_form_0`."""
    return (pl.col(f)*pl.col(i)*pl.col(n))


def calc_v_infty_t_x_v_infty_t_y_form_1(T: float, i: float, l: float, m: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    V\infty (t, x) -V\infty (t, y) = lim T\to \infty  \int  x y \partial xVT (t, z) dz = \int  x y U(t, z) dz
    $$

    Args:
        T (float): Input parameter `T`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(T*i*l*m)


def expr_v_infty_t_x_v_infty_t_y_form_1(T: str = "T", i: str = "i", l: str = "l", m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_infty_t_x_v_infty_t_y_form_1`."""
    return (pl.col(T)*pl.col(i)*pl.col(l)*pl.col(m))


def calc_sigma_j_l_form_6(f: float, i: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    \sigma Jl = inf{0 < s < \delta  ∧ \tau  J : BJ s > 0}
    $$

    Args:
        f (float): Input parameter `f`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(f*i*n)


def expr_sigma_j_l_form_6(f: str = "f", i: str = "i", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sigma_j_l_form_6`."""
    return (pl.col(f)*pl.col(i)*pl.col(n))


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
    return float(c*m*o*p)


def expr_h_a_p_e_x_form_b(c: str = "c", m: str = "m", o: str = "o", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_a_p_e_x_form_b`."""
    return (pl.col(c)*pl.col(m)*pl.col(o)*pl.col(p))


def calc_s_form_c(H: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    s = H(x* ) - H(x) x* -x = 1 x* - x \int  x* x H' (y) dy > 1 x* - x \int  x* x H' (x) dy = H' (x)
    $$

    Args:
        H (float): Input parameter `H`.

    Returns:
        float: Calculated metric value.
    """
    return float(H)


def expr_s_form_c(H: str = "H") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_form_c`."""
    return (pl.col(H))


def calc_v_beta_t_t_x_form_f(E: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    V \beta  T (t, x) = E [\int  \tau  \beta  0 F \beta  (t + u, Xx u ) du + 1{\tau  \beta  <T -t}V \beta  T (t + \tau  \beta  ,Xx \tau  \beta  ) + 1{\tau  \beta  =T -t}g(Xx T-t)]
    $$

    Args:
        E (float): Input parameter `E`.

    Returns:
        float: Calculated metric value.
    """
    return float(E)


def expr_v_beta_t_t_x_form_f(E: str = "E") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_beta_t_t_x_form_f`."""
    return (pl.col(E))


def calc_y_s_form_0(R: float, W: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    Ys = Rs + Ws
    $$

    Args:
        R (float): Input parameter `R`.
        W (float): Input parameter `W`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(R*s + W*s)


def expr_y_s_form_0(R: str = "R", W: str = "W", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_y_s_form_0`."""
    return (pl.col(R)*pl.col(s) + pl.col(W)*pl.col(s))


def calc_sim_s_t_form_0(N: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    \sim  S(t) = Nt\sum  k=1 Xk
    $$

    Args:
        N (float): Input parameter `N`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(N*t)


def expr_sim_s_t_form_0(N: str = "N", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sim_s_t_form_0`."""
    return (pl.col(N)*pl.col(t))


def calc_u_t_x_form_1(t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    u(t, x) = \cos(2\pi t), x \in  {1 - B, B}
    $$

    Args:
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.cos(2*math.pi*t))


def expr_u_t_x_form_1(t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_t_x_form_1`."""
    return (math.cos(2*math.pi*pl.col(t)))


def calc_t_s_s_k_form_3(J: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    TSSk = J\sum  j=1 P SSk,j
    $$

    Args:
        J (float): Input parameter `J`.

    Returns:
        float: Calculated metric value.
    """
    return float(J)


def expr_t_s_s_k_form_3(J: str = "J") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_s_s_k_form_3`."""
    return (pl.col(J))


def calc_pi_i_j_form_7(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_18467.

    **Source**:
    - Title: Analysing Skill Predominance in Generalized Fantasy Cricket (2025)
    - Authors: Supratim Das, Sarthak Sarkar, Subhamoy Maitra et al.
    - Citation Key: `arxiv_2512_18467`

    **KaTeX Formula**:
    $$
    \pi ij = P(Bij \ge  Bkl \forall (k, l) ̸= (i, j))
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_pi_i_j_form_7(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_pi_i_j_form_7`."""
    return (pl.col(P))


def calc_omega_s_form_6(B: float, Omega: float, R: float, k: float, phi: float, rho: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2309_15318.

    **Source**:
    - Title: A Global 3-D Simulation of Magnetospheric Accretion: I. Magnetically Disrupted Disks and Surface Accretion (2023)
    - Authors: Zhaohuan Zhu, James M. Stone, Nuria Calvet
    - Citation Key: `arxiv_2309_15318`

    **KaTeX Formula**:
    $$
    \omega s = \Omega  - kB\phi  \rho R
    $$

    Args:
        B (float): Input parameter `B`.
        Omega (float): Input parameter `Omega`.
        R (float): Input parameter `R`.
        k (float): Input parameter `k`.
        phi (float): Input parameter `phi`.
        rho (float): Input parameter `rho`.

    Returns:
        float: Calculated metric value.
    """
    return float(-B*R*k*phi*rho + Omega)


def expr_omega_s_form_6(B: str = "B", Omega: str = "Omega", R: str = "R", k: str = "k", phi: str = "phi", rho: str = "rho") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_omega_s_form_6`."""
    return (-pl.col(B)*pl.col(R)*pl.col(k)*pl.col(phi)*pl.col(rho) + pl.col(Omega))


def calc_sigma_a_x_form_7(x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    \sigma A(x) = \sin(\pi x) \pi  , \sigma B(x) = \phi (\Phi -1 (x)), \sigma I(x) = x(1-x)
    $$

    Args:
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.pi*math.sin(math.pi*x))


def expr_sigma_a_x_form_7(x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sigma_a_x_form_7`."""
    return (math.pi*math.sin(math.pi*pl.col(x)))


def calc_partial_p_w_t_partial_s_i_form_8(phi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    \partial PWt \partial Si = \phi  ( c - T*(t, a(t), b(t)) \sqrt (1 - t)(\tau  2 + \sigma 2 ) ) \alpha i \sqrt (1 - t)(\tau  2 + \sigma 2 )
    $$

    Args:
        phi (float): Input parameter `phi`.

    Returns:
        float: Calculated metric value.
    """
    return float(phi)


def expr_partial_p_w_t_partial_s_i_form_8(phi: str = "phi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_partial_p_w_t_partial_s_i_form_8`."""
    return (pl.col(phi))


def calc_kappa_form_8(delta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    \kappa  = \delta
    $$

    Args:
        delta (float): Input parameter `delta`.

    Returns:
        float: Calculated metric value.
    """
    return float(delta)


def expr_kappa_form_8(delta: str = "delta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_kappa_form_8`."""
    return (pl.col(delta))


def calc_t_k_form_8(J: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    T k = \alpha 0 + J\sum  j=1 f\alpha (Sk,j 1 , . . . , Sk,j d ) + \epsilon k
    $$

    Args:
        J (float): Input parameter `J`.

    Returns:
        float: Calculated metric value.
    """
    return float(J)


def expr_t_k_form_8(J: str = "J") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_k_form_8`."""
    return (pl.col(J))


def calc_k_epsilon_s_l_l_s_form_8(B: float, J: float, l: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    Lls - K\epsilon s = l + BJ s
    $$

    Args:
        B (float): Input parameter `B`.
        J (float): Input parameter `J`.
        l (float): Input parameter `l`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(B*J*s + l)


def expr_k_epsilon_s_l_l_s_form_8(B: str = "B", J: str = "J", l: str = "l", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_epsilon_s_l_l_s_form_8`."""
    return (pl.col(B)*pl.col(J)*pl.col(s) + pl.col(l))


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
    return float(2*A*j**2*x + W*j)


def expr_j_p_form_d(A: str = "A", W: str = "W", j: str = "j", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_p_form_d`."""
    return (2*pl.col(A)*pl.col(j)**2*pl.col(x) + pl.col(W)*pl.col(j))


def calc_g_i_form_1(C: float, E: float, Sigma: float, V: float, beta: float, epsilon: float, i: float, mu: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_18467.

    **Source**:
    - Title: Analysing Skill Predominance in Generalized Fantasy Cricket (2025)
    - Authors: Supratim Das, Sarthak Sarkar, Subhamoy Maitra et al.
    - Citation Key: `arxiv_2512_18467`

    **KaTeX Formula**:
    $$
    Gi = \beta 0 + \beta 1C + \beta 2C 2 + \beta 3E + \beta 4V\mu  + \beta 5\Sigma 2 + \epsilon i
    $$

    Args:
        C (float): Input parameter `C`.
        E (float): Input parameter `E`.
        Sigma (float): Input parameter `Sigma`.
        V (float): Input parameter `V`.
        beta (float): Input parameter `beta`.
        epsilon (float): Input parameter `epsilon`.
        i (float): Input parameter `i`.
        mu (float): Input parameter `mu`.

    Returns:
        float: Calculated metric value.
    """
    return float(epsilon*i + (beta*(5*(2*Sigma)) + (beta*(4*(V*mu)) + ((3*E)*beta + (beta*(2*(2*C)) + ((1*C)*beta + 0*beta))))))


def expr_g_i_form_1(C: str = "C", E: str = "E", Sigma: str = "Sigma", V: str = "V", beta: str = "beta", epsilon: str = "epsilon", i: str = "i", mu: str = "mu") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_i_form_1`."""
    return (pl.col(epsilon)*pl.col(i) + (pl.col(beta)*(5*(2*pl.col(Sigma))) + (pl.col(beta)*(4*(pl.col(V)*pl.col(mu))) + ((3*pl.col(E))*pl.col(beta) + (pl.col(beta)*(2*(2*pl.col(C))) + ((1*pl.col(C))*pl.col(beta) + 0*pl.col(beta)))))))


def calc_e_l_form_2(M: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2508_19848.

    **Source**:
    - Title: Hierarchy and ranking in pairwise sports contests (2025)
    - Authors: Bogdán Asztalos, Boldizsár Balázs, Gergely Palla et al.
    - Citation Key: `arxiv_2508_19848`

    **KaTeX Formula**:
    $$
    LE= 1 M \cdot \sum m (1 - pm)
    $$

    Args:
        M (float): Input parameter `M`.

    Returns:
        float: Calculated metric value.
    """
    return float(M)


def expr_e_l_form_2(M: str = "M") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_l_form_2`."""
    return (pl.col(M))


def calc_i_pi_form_3(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_18467.

    **Source**:
    - Title: Analysing Skill Predominance in Generalized Fantasy Cricket (2025)
    - Authors: Supratim Das, Sarthak Sarkar, Subhamoy Maitra et al.
    - Citation Key: `arxiv_2512_18467`

    **KaTeX Formula**:
    $$
    \pi i = P(Pi \ge  Pj \forall j ̸= i)
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_i_pi_form_3(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_pi_form_3`."""
    return (pl.col(P))


def calc_i_p_form_4(eta: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_15673.

    **Source**:
    - Title: Leicester's Tale: Another Perspective on the EPL 2015/16 Through Expected Goals (xG) Modelling (2026)
    - Authors: Sheikh Badar Ud Din Tahir, Leonardo Egidi, Nicola Torelli
    - Citation Key: `arxiv_2602_15673`

    **KaTeX Formula**:
    $$
    pi = 1 1 + \exp(-\eta i)
    $$

    Args:
        eta (float): Input parameter `eta`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(11 + math.exp(-eta*i))


def expr_i_p_form_4(eta: str = "eta", i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_p_form_4`."""
    return (11 + (-pl.col(eta).exp()*pl.col(i)))


def calc_f_h_form_4(L: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2508_19848.

    **Source**:
    - Title: Hierarchy and ranking in pairwise sports contests (2025)
    - Authors: Bogdán Asztalos, Boldizsár Balázs, Gergely Palla et al.
    - Citation Key: `arxiv_2508_19848`

    **KaTeX Formula**:
    $$
    FH = 1 L \cdot \sum  i\in E ei
    $$

    Args:
        L (float): Input parameter `L`.

    Returns:
        float: Calculated metric value.
    """
    return float(L)


def expr_f_h_form_4(L: str = "L") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_h_form_4`."""
    return (pl.col(L))


def calc_i_l_form_5(alpha: float, d: float, e: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_18417.

    **Source**:
    - Title: Resource-Efficient 3D Shape and Orientation Estimation of Road Users using Roadside RGB Camera and 3D Radar (2026)
    - Authors: Shiva Agrawal, Savankumar Bhanderi, Gordon Elger
    - Citation Key: `arxiv_2610_18417`

    **KaTeX Formula**:
    $$
    li = \alpha ped,l \cdot  |yg,right - yg,left|
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        d (float): Input parameter `d`.
        e (float): Input parameter `e`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(alpha*d*e*p)


def expr_i_l_form_5(alpha: str = "alpha", d: str = "d", e: str = "e", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_l_form_5`."""
    return (pl.col(alpha)*pl.col(d)*pl.col(e)*pl.col(p))


def calc_e_i_p_form_5(i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_18467.

    **Source**:
    - Title: Analysing Skill Predominance in Generalized Fantasy Cricket (2025)
    - Authors: Supratim Das, Sarthak Sarkar, Subhamoy Maitra et al.
    - Citation Key: `arxiv_2512_18467`

    **KaTeX Formula**:
    $$
    E[pi] = \pi i, Var(pi) = \pi i(1 - \pi i) \alpha +1
    $$

    Args:
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.pi*i)


def expr_e_i_p_form_5(i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_i_p_form_5`."""
    return (math.pi*pl.col(i))


def calc_i_y_form_5(H: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_11492.

    **Source**:
    - Title: BoxMind: Closed-loop AI strategy optimization for elite boxing validated in the 2024 Olympics (2026)
    - Authors: Kaiwen Wang, Kaili Zheng, Rongrong Deng et al.
    - Citation Key: `arxiv_2601_11492`

    **KaTeX Formula**:
    $$
    yi = H\sum  k=1 w(i) k \cdot  E(i) k (Fv|Fs), i = 1, 2, 3, 4 (S6)
    $$

    Args:
        H (float): Input parameter `H`.

    Returns:
        float: Calculated metric value.
    """
    return float(H)


def expr_i_y_form_5(H: str = "H") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_y_form_5`."""
    return (pl.col(H))


def calc_delta_p_w_t_form_5(phi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    \Delta PWt = \phi (\cdot ) s(t) \Delta T*
    $$

    Args:
        phi (float): Input parameter `phi`.

    Returns:
        float: Calculated metric value.
    """
    return float(phi)


def expr_delta_p_w_t_form_5(phi: str = "phi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_p_w_t_form_5`."""
    return (pl.col(phi))


def calc_n_i_form_6(N: float, i: float, tau: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_18467.

    **Source**:
    - Title: Analysing Skill Predominance in Generalized Fantasy Cricket (2025)
    - Authors: Supratim Das, Sarthak Sarkar, Subhamoy Maitra et al.
    - Citation Key: `arxiv_2512_18467`

    **KaTeX Formula**:
    $$
    Ni = N \tau  i +N 1-\tau  i
    $$

    Args:
        N (float): Input parameter `N`.
        i (float): Input parameter `i`.
        tau (float): Input parameter `tau`.

    Returns:
        float: Calculated metric value.
    """
    return float(-i*tau + (N*(i*tau) + 1*N))


def expr_n_i_form_6(N: str = "N", i: str = "i", tau: str = "tau") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_n_i_form_6`."""
    return (-pl.col(i)*pl.col(tau) + (pl.col(N)*(pl.col(i)*pl.col(tau)) + 1*pl.col(N)))


def calc_e_s_form_6(M: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2508_19848.

    **Source**:
    - Title: Hierarchy and ranking in pairwise sports contests (2025)
    - Authors: Bogdán Asztalos, Boldizsár Balázs, Gergely Palla et al.
    - Citation Key: `arxiv_2508_19848`

    **KaTeX Formula**:
    $$
    SE= 1 M \cdot \sum m (1 - pm)2
    $$

    Args:
        M (float): Input parameter `M`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*M)


def expr_e_s_form_6(M: str = "M") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_s_form_6`."""
    return (1*pl.col(M))


def calc_h_x_form_6(delta: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    h(x) = \delta x, \delta  > 0
    $$

    Args:
        delta (float): Input parameter `delta`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(delta*x)


def expr_h_x_form_6(delta: str = "delta", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_x_form_6`."""
    return (pl.col(delta)*pl.col(x))


def calc_f_m_lambda_x_form_7(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    FM\lambda  (x) = P(M\lambda  \le  x) = P(M\lambda  \le  x | Y = 0)(1 - p0) + P(M\lambda  \le  x | Y = 1)p0
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_f_m_lambda_x_form_7(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_m_lambda_x_form_7`."""
    return (pl.col(P))


def calc_t_a_b_form_9(a: float, b: float, kappa: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    T(a, b) = a- b a+ b +\kappa  , \kappa  > 0, c = 0
    $$

    Args:
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        kappa (float): Input parameter `kappa`.

    Returns:
        float: Calculated metric value.
    """
    return float(-a*b + a + b + kappa)


def expr_t_a_b_form_9(a: str = "a", b: str = "b", kappa: str = "kappa") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_a_b_form_9`."""
    return (-pl.col(a)*pl.col(b) + pl.col(a) + pl.col(b) + pl.col(kappa))


def calc_f_m_lambda_x_form_9(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    FM\lambda  (x) = P(M\lambda  \le  x) =  0 for 0 \le  x < 1 - p0, 1 - 1-p0 x for 1 - p0 \le  x < p0, 2 - 1x for p0 \le  x < 1, 1 for x = 1
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_f_m_lambda_x_form_9(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_m_lambda_x_form_9`."""
    return (pl.col(P))


def calc_t_a_b_form_a(a: float, b: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    T(a, b) = a- b \sqrt a + b + \kappa
    $$

    Args:
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.

    Returns:
        float: Calculated metric value.
    """
    return float(a - b)


def expr_t_a_b_form_a(a: str = "a", b: str = "b") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_a_b_form_a`."""
    return (pl.col(a) - pl.col(b))


def calc_l_c_x_form_b(x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    LC(x) = 2\pi S(x), LS(x) = -2\pi C(x)
    $$

    Args:
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*math.pi*x)


def expr_l_c_x_form_b(x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_c_x_form_b`."""
    return (2*math.pi*pl.col(x))


def calc_v_form_c(N: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2604_13861.

    **Source**:
    - Title: Simulation-Based Optimisation of Batting Order and Bowling Plans in T20 Cricket (2026)
    - Authors: Tinniam V Ganesh
    - Citation Key: `arxiv_2604_13861`

    **KaTeX Formula**:
    $$
    V = 1N N\sum n=1 1[trajectory(n) results in win/defend]
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*N))


def expr_v_form_c(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_form_c`."""
    return (1*(pl.col(N)*pl.col(N)))


def calc_t_a_b_form_c(a: float, b: float, kappa: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    T (a, b) = \log a + \kappa  b +\kappa  , \kappa  > 0, c = 0
    $$

    Args:
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        kappa (float): Input parameter `kappa`.

    Returns:
        float: Calculated metric value.
    """
    return float(b*kappa + kappa + math.log(a))


def expr_t_a_b_form_c(a: str = "a", b: str = "b", kappa: str = "kappa") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_a_b_form_c`."""
    return (pl.col(b)*pl.col(kappa) + pl.col(kappa) + (pl.col(a).log()))


def calc_pi_s_form_d(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_12291.

    **Source**:
    - Title: When should one stop the most exciting game? Sequential Inference for win-martingales (2026)
    - Authors: Steven Campbell, Karl Kristian Engelund
    - Citation Key: `arxiv_2608_12291`

    **KaTeX Formula**:
    $$
    \Pi s = P(R \ge  0 | Gs)
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_pi_s_form_d(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_pi_s_form_d`."""
    return (pl.col(P))


def calc_t_k_form_d(F: float, alpha: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    T k = \alpha 0 + F\alpha (Sk 1 , . . . , Sk d ) + \epsilon k
    $$

    Args:
        F (float): Input parameter `F`.
        alpha (float): Input parameter `alpha`.

    Returns:
        float: Calculated metric value.
    """
    return float(F*alpha)


def expr_t_k_form_d(F: str = "F", alpha: str = "alpha") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_k_form_d`."""
    return (pl.col(F)*pl.col(alpha))


def calc_v_b_t_r_b_w_form_e(W: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2604_13861.

    **Source**:
    - Title: Simulation-Based Optimisation of Batting Order and Bowling Plans in T20 Cricket (2026)
    - Authors: Tinniam V Ganesh
    - Citation Key: `arxiv_2604_13861`

    **KaTeX Formula**:
    $$
    V B t (r, b,w) = pW,φ i ⋅ V B t-1 (r, b -1, w-1) + \sum  ρ\in {0,1,2,3,4,6} pρ,φ i ⋅ V B t-1 (r -ρ, b -1, w)
    $$

    Args:
        W (float): Input parameter `W`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(W*p)


def expr_v_b_t_r_b_w_form_e(W: str = "W", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_b_t_r_b_w_form_e`."""
    return (pl.col(W)*pl.col(p))


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
    return float(2*a*g*l*o + 280*g*l*o + (math.e*C + math.e*L)*(22660*g*l*o + 15) + 27)


def expr_c_e_x_a_c_t_form_f(C: str = "C", L: str = "L", a: str = "a", g: str = "g", l: str = "l", o: str = "o") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_e_x_a_c_t_form_f`."""
    return (2*pl.col(a)*pl.col(g)*pl.col(l)*pl.col(o) + 280*pl.col(g)*pl.col(l)*pl.col(o) + (math.e*pl.col(C) + math.e*pl.col(L))*(22660*pl.col(g)*pl.col(l)*pl.col(o) + 15) + 27)


def calc_e_a_g_v_form_0(N: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_04435.

    **Source**:
    - Title: STEMPix: A Phase-Transition-Material-Based Pixel Sensor for Resolving Edge-Movement Direction (2026)
    - Authors: Md Rahatul Islam Udoy, Sumeet Kumar Gupta, Deep Jariwala et al.
    - Citation Key: `arxiv_2609_04435`

    **KaTeX Formula**:
    $$
    Eavg = 1N \sum Ecase,k N k=1
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*N)


def expr_e_a_g_v_form_0(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_a_g_v_form_0`."""
    return (1*pl.col(N))


def calc_i_z_form_1(T: float, i: float, k: float, q: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_03810.

    **Source**:
    - Title: Unified Pitch Graphs for Diagnosing Pitching Strategy (2026)
    - Authors: Kichang Lee, JeongGil Ko
    - Citation Key: `arxiv_2609_03810`

    **KaTeX Formula**:
    $$
    zi = u ^T k  qi
    $$

    Args:
        T (float): Input parameter `T`.
        i (float): Input parameter `i`.
        k (float): Input parameter `k`.
        q (float): Input parameter `q`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*k*q*u**T)


def expr_i_z_form_1(T: str = "T", i: str = "i", k: str = "k", q: str = "q", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_z_form_1`."""
    return (pl.col(i)*pl.col(k)*pl.col(q)*pl.col(u)**pl.col(T))


def calc_s_form_1(N: float, X: float, beta: float, gamma: float, s: float, tau: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_14820.

    **Source**:
    - Title: POLARIS: Training-Free Audio Fingerprinting with Saliency-Based Landmarks and Delaunay Grouping (2026)
    - Authors: Jiheng Li
    - Citation Key: `arxiv_2609_14820`

    **KaTeX Formula**:
    $$
    S = \beta N + \gamma [Xs - \tau  ]+
    $$

    Args:
        N (float): Input parameter `N`.
        X (float): Input parameter `X`.
        beta (float): Input parameter `beta`.
        gamma (float): Input parameter `gamma`.
        s (float): Input parameter `s`.
        tau (float): Input parameter `tau`.

    Returns:
        float: Calculated metric value.
    """
    return float(N*beta + gamma*(X*s - tau))


def expr_s_form_1(N: str = "N", X: str = "X", beta: str = "beta", gamma: str = "gamma", s: str = "s", tau: str = "tau") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_form_1`."""
    return (pl.col(N)*pl.col(beta) + pl.col(gamma)*(pl.col(X)*pl.col(s) - pl.col(tau)))


def calc_dt_k_form_1(K: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_25621.

    **Source**:
    - Title: Dissonance Spectrum explicitly models perceptual frequency interactions for better music understanding (2026)
    - Authors: Tianle Wang, Xinyi Tong, Liangke Zhao et al.
    - Citation Key: `arxiv_2608_25621`

    **KaTeX Formula**:
    $$
    dtk = 1K K-1 \sum  l=0 xtk xtl ¯D(pl -pk)
    $$

    Args:
        K (float): Input parameter `K`.

    Returns:
        float: Calculated metric value.
    """
    return float(K**2 - 1)


def expr_dt_k_form_1(K: str = "K") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_dt_k_form_1`."""
    return (pl.col(K)**2 - 1)


def calc_d_a_form_1(A: float, C: float, D: float, m: float, rho: float, v: float) -> float:
    r"""Compute mathematical metric extracted from openalex_meyer2008_w1992303757.

    **Source**:
    - Title: Influence of a humidor on the aerodynamics of baseballs (2008)
    - Authors: Edmund Meyer, John L. Bohn
    - Citation Key: `openalex_meyer2008_w1992303757`

    **KaTeX Formula**:
    $$
    aD = - 1 2 \rho A m CDv2
    $$

    Args:
        A (float): Input parameter `A`.
        C (float): Input parameter `C`.
        D (float): Input parameter `D`.
        m (float): Input parameter `m`.
        rho (float): Input parameter `rho`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(-24*A*C*D*m*rho*v)


def expr_d_a_form_1(A: str = "A", C: str = "C", D: str = "D", m: str = "m", rho: str = "rho", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_a_form_1`."""
    return (-24*pl.col(A)*pl.col(C)*pl.col(D)*pl.col(m)*pl.col(rho)*pl.col(v))


def calc_ds_h_o_e_r_form_2(a: float, alpha: float, c: float, e: float, h: float, m: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_21276.

    **Source**:
    - Title: The Coastline as a Structural Constraint: Harnessing Scene Geometry for Autonomous Surface Vessel Localization (2026)
    - Authors: Derek R. Benham, Joshua G. Mangelson
    - Citation Key: `arxiv_2608_21276`

    **KaTeX Formula**:
    $$
    dshore = hcamera \tan(\alpha )
    $$

    Args:
        a (float): Input parameter `a`.
        alpha (float): Input parameter `alpha`.
        c (float): Input parameter `c`.
        e (float): Input parameter `e`.
        h (float): Input parameter `h`.
        m (float): Input parameter `m`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(a**2*c*e*h*m*r*math.tan(alpha))


def expr_ds_h_o_e_r_form_2(a: str = "a", alpha: str = "alpha", c: str = "c", e: str = "e", h: str = "h", m: str = "m", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_ds_h_o_e_r_form_2`."""
    return (pl.col(a)**2*pl.col(c)*pl.col(e)*pl.col(h)*pl.col(m)*pl.col(r)*math.tan(pl.col(alpha)))


def calc_eta_i_form_4(T: float, a: float, beta: float, c: float, dd: float, gamma: float, i: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_25525.

    **Source**:
    - Title: When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review (2026)
    - Authors: Kichang Lee, Gyeongmin Han, Sungmin Lee et al.
    - Citation Key: `arxiv_2609_25525`

    **KaTeX Formula**:
    $$
    \eta i = aci + \beta ddi + x ^T i \gamma  + \sum  m,v,s \tau m,v,sAm,v,s i
    $$

    Args:
        T (float): Input parameter `T`.
        a (float): Input parameter `a`.
        beta (float): Input parameter `beta`.
        c (float): Input parameter `c`.
        dd (float): Input parameter `dd`.
        gamma (float): Input parameter `gamma`.
        i (float): Input parameter `i`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(x**T*(gamma*i) + (a*(c*i) + beta*(dd*i)))


def expr_eta_i_form_4(T: str = "T", a: str = "a", beta: str = "beta", c: str = "c", dd: str = "dd", gamma: str = "gamma", i: str = "i", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_eta_i_form_4`."""
    return (pl.col(x)**pl.col(T)*(pl.col(gamma)*pl.col(i)) + (pl.col(a)*(pl.col(c)*pl.col(i)) + pl.col(beta)*(pl.col(dd)*pl.col(i))))


def calc_dt_k_form_4(K: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_25621.

    **Source**:
    - Title: Dissonance Spectrum explicitly models perceptual frequency interactions for better music understanding (2026)
    - Authors: Tianle Wang, Xinyi Tong, Liangke Zhao et al.
    - Citation Key: `arxiv_2608_25621`

    **KaTeX Formula**:
    $$
    dtk = 1K K-1 \sum  l=0 xtk xtl ¯D(pl -pk)
    $$

    Args:
        K (float): Input parameter `K`.

    Returns:
        float: Calculated metric value.
    """
    return float(K**2 - 1)


def expr_dt_k_form_4(K: str = "K") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_dt_k_form_4`."""
    return (pl.col(K)**2 - 1)


def calc_g_sigma_form_5(beta: float, d: float, delta: float, g: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_25525.

    **Source**:
    - Title: When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review (2026)
    - Authors: Kichang Lee, Gyeongmin Han, Sungmin Lee et al.
    - Citation Key: `arxiv_2609_25525`

    **KaTeX Formula**:
    $$
    \sigma g = 1 \beta d + \delta g
    $$

    Args:
        beta (float): Input parameter `beta`.
        d (float): Input parameter `d`.
        delta (float): Input parameter `delta`.
        g (float): Input parameter `g`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(beta*d) + delta*g)


def expr_g_sigma_form_5(beta: str = "beta", d: str = "d", delta: str = "delta", g: str = "g") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_sigma_form_5`."""
    return (1*(pl.col(beta)*pl.col(d)) + pl.col(delta)*pl.col(g))


def calc_a_c_u_form_5(Phi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_15144.

    **Source**:
    - Title: Automated Perceptually-Motivated Assessment of Photographic Consistency in Paired Clinical Photographs: Pipeline Development and Internal Evaluation (2026)
    - Authors: Derrick Lin, Samantha Rabinovich, Joclin Rabinovich et al.
    - Citation Key: `arxiv_2609_15144`

    **KaTeX Formula**:
    $$
    AUC = \Phi (d'/\sqrt 2)
    $$

    Args:
        Phi (float): Input parameter `Phi`.

    Returns:
        float: Calculated metric value.
    """
    return float(Phi)


def expr_a_c_u_form_5(Phi: str = "Phi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_c_u_form_5`."""
    return (pl.col(Phi))


def calc_log_y_i_e_form_6(L: float, a: float, beta: float, epsilon: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_25621.

    **Source**:
    - Title: Dissonance Spectrum explicitly models perceptual frequency interactions for better music understanding (2026)
    - Authors: Tianle Wang, Xinyi Tong, Liangke Zhao et al.
    - Citation Key: `arxiv_2608_25621`

    **KaTeX Formula**:
    $$
    \ln Yi = a + \beta  \ln Li + \epsilon i
    $$

    Args:
        L (float): Input parameter `L`.
        a (float): Input parameter `a`.
        beta (float): Input parameter `beta`.
        epsilon (float): Input parameter `epsilon`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(epsilon*i + (a + beta*math.log(L*i, math.e)))


def expr_log_y_i_e_form_6(L: str = "L", a: str = "a", beta: str = "beta", epsilon: str = "epsilon", i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_log_y_i_e_form_6`."""
    return (pl.col(epsilon)*pl.col(i) + (pl.col(a) + pl.col(beta)*(pl.col(L).log()*pl.col(i), math.e)))


def calc_s_form_6(a: float, g: float, i: float, m: float, n: float, r: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_30471.

    **Source**:
    - Title: HorizonNet for visual terrain navigation (2026)
    - Authors: Bertil Grelsson, Andreas Robinson, Michael Felsberg et al.
    - Citation Key: `arxiv_2608_30471`

    **KaTeX Formula**:
    $$
    s = argmin \theta ,\phi ,\psi  \sum  i D {R(\psi )\pi (R(\theta , \phi )\pi -1 (hi))}
    $$

    Args:
        a (float): Input parameter `a`.
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*g*i*m*n*r*theta)


def expr_s_form_6(a: str = "a", g: str = "g", i: str = "i", m: str = "m", n: str = "n", r: str = "r", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_form_6`."""
    return (pl.col(a)*pl.col(g)*pl.col(i)*pl.col(m)*pl.col(n)*pl.col(r)*pl.col(theta))


def calc_l_c_a_3_d_m_form_7(N: float, j: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10498.

    **Source**:
    - Title: Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts (2026)
    - Authors: Simon Khan, Laurent Gajny, Jennyfer Lecompte et al.
    - Citation Key: `arxiv_2609_10498`

    **KaTeX Formula**:
    $$
    Lcam3D = 1 3Nj \sum  i,t,j vi,tmi,t,j \times  \sum  a\in {x,y,z} \rho 1( ̂Xc i,t,j,a - Xc,gt i,t,j,a)
    $$

    Args:
        N (float): Input parameter `N`.
        j (float): Input parameter `j`.

    Returns:
        float: Calculated metric value.
    """
    return float(13*(N*j))


def expr_l_c_a_3_d_m_form_7(N: str = "N", j: str = "j") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_c_a_3_d_m_form_7`."""
    return (13*(pl.col(N)*pl.col(j)))


def calc_g_c_r_form_8(N: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2508_19848.

    **Source**:
    - Title: Hierarchy and ranking in pairwise sports contests (2025)
    - Authors: Bogdán Asztalos, Boldizsár Balázs, Gergely Palla et al.
    - Citation Key: `arxiv_2508_19848`

    **KaTeX Formula**:
    $$
    GRC= 1 N-1 \cdot  \sum  i\in V [2RC max - 2RC(i)]
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*N - 1)


def expr_g_c_r_form_8(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_c_r_form_8`."""
    return (1*pl.col(N) - 1)


def calc_a_s_t_form_1(n: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    A*s (t) = (ns 2 )-1 \sum  a<b WsaWsb Ns,ab \sum  l=1 ht(Us,abl),  B* s = (ns 2 )-1 \sum  a<b WsaWsbNs,ab,  F * s (t-) =  A*s (t)  B* s
    $$

    Args:
        n (float): Input parameter `n`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*n*s - 1)


def expr_a_s_t_form_1(n: str = "n", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_s_t_form_1`."""
    return (2*pl.col(n)*pl.col(s) - 1)


def calc_t_k_form_9(J: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_19513.

    **Source**:
    - Title: Real-time Win Probability and Latent Player Ability via STATS X in Team Sports (2026)
    - Authors: Yasutaka Shimizu, Atsushi Yamanobe
    - Citation Key: `arxiv_2602_19513`

    **KaTeX Formula**:
    $$
    T k = \alpha 0 + J\sum  j=1 {\alpha 1Sk,j 1 + \cdot  \cdot  \cdot  +\alpha 8Sk,j 8 } + \epsilon k
    $$

    Args:
        J (float): Input parameter `J`.

    Returns:
        float: Calculated metric value.
    """
    return float(J)


def expr_t_k_form_9(J: str = "J") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_k_form_9`."""
    return (pl.col(J))


def calc_eta_i_form_9(beta: float, k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2602_15673.

    **Source**:
    - Title: Leicester's Tale: Another Perspective on the EPL 2015/16 Through Expected Goals (xG) Modelling (2026)
    - Authors: Sheikh Badar Ud Din Tahir, Leonardo Egidi, Nicola Torelli
    - Citation Key: `arxiv_2602_15673`

    **KaTeX Formula**:
    $$
    \eta i =  \beta 0 + k\sum  j=1  \beta jXij
    $$

    Args:
        beta (float): Input parameter `beta`.
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(0*beta + k)


def expr_eta_i_form_9(beta: str = "beta", k: str = "k") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_eta_i_form_9`."""
    return (0*pl.col(beta) + pl.col(k))


def calc_r_p_r_i_form_a(dN: float, dcdot: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2508_19848.

    **Source**:
    - Title: Hierarchy and ranking in pairwise sports contests (2025)
    - Authors: Bogdán Asztalos, Boldizsár Balázs, Gergely Palla et al.
    - Citation Key: `arxiv_2508_19848`

    **KaTeX Formula**:
    $$
    RPR(i) = 1-d N +d \cdot  \sum  j\in M(i) RPR( j) L( j)
    $$

    Args:
        dN (float): Input parameter `dN`.
        dcdot (float): Input parameter `dcdot`.

    Returns:
        float: Calculated metric value.
    """
    return float(-dN + dcdot + 1)


def expr_r_p_r_i_form_a(dN: str = "dN", dcdot: str = "dcdot") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_p_r_i_form_a`."""
    return (-pl.col(dN) + pl.col(dcdot) + 1)


def calc_d_form_a(A: float, C: float, D: float, rho: float, v: float) -> float:
    r"""Compute mathematical metric extracted from openalex_meyer2008_w1992303757.

    **Source**:
    - Title: Influence of a humidor on the aerodynamics of baseballs (2008)
    - Authors: Edmund Meyer, John L. Bohn
    - Citation Key: `openalex_meyer2008_w1992303757`

    **KaTeX Formula**:
    $$
    D = - 1 2 \rho CDAv2 v
    $$

    Args:
        A (float): Input parameter `A`.
        C (float): Input parameter `C`.
        D (float): Input parameter `D`.
        rho (float): Input parameter `rho`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(-24*A*C*D*rho*v**2)


def expr_d_form_a(A: str = "A", C: str = "C", D: str = "D", rho: str = "rho", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_form_a`."""
    return (-24*pl.col(A)*pl.col(C)*pl.col(D)*pl.col(rho)*pl.col(v)**2)


def calc_x_i_t_form_b(Y: float, i: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    Xi(t) = tYi + \sigma B0 i (t), \sigma  = 0.5
    $$

    Args:
        Y (float): Input parameter `Y`.
        i (float): Input parameter `i`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(Y*i*t)


def expr_x_i_t_form_b(Y: str = "Y", i: str = "i", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_i_t_form_b`."""
    return (pl.col(Y)*pl.col(i)*pl.col(t))


def calc_p_0_form_c(P: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    p0 = x P(\tau x < 1) + E[Y 1{\tau x \ge  1}]
    $$

    Args:
        P (float): Input parameter `P`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(P*x)


def expr_p_0_form_c(P: str = "P", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_0_form_c`."""
    return (pl.col(P)*pl.col(x))


def calc_e_b_t_form_c(C: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_11492.

    **Source**:
    - Title: BoxMind: Closed-loop AI strategy optimization for elite boxing validated in the 2024 Olympics (2026)
    - Authors: Kaiwen Wang, Kaili Zheng, Rongrong Deng et al.
    - Citation Key: `arxiv_2601_11492`

    **KaTeX Formula**:
    $$
    Eb(t) = C-1 \sum  c=0 E(c) b \cdot  tc
    $$

    Args:
        C (float): Input parameter `C`.

    Returns:
        float: Calculated metric value.
    """
    return float(C - 1)


def expr_e_b_t_form_c(C: str = "C") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_b_t_form_c`."""
    return (pl.col(C) - 1)


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
    return float(2*T + r)


def expr_u_o_t_v_form_c(T: str = "T", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_o_t_v_form_c`."""
    return (2*pl.col(T) + pl.col(r))


def calc_r_form_c(Y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_18774.

    **Source**:
    - Title: The Blown Lead Paradox: A Pathwise Calibration Benchmark for Win Probability Forecasts (2026)
    - Authors: Jonathan Pipping-Gamón, Abraham J. Wyner
    - Citation Key: `arxiv_2601_18774`

    **KaTeX Formula**:
    $$
    R = (1 - Y ) - (1 - p\tau .95 ) = p\tau .95 - Y
    $$

    Args:
        Y (float): Input parameter `Y`.

    Returns:
        float: Calculated metric value.
    """
    return float(1 - Y)


def expr_r_form_c(Y: str = "Y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_form_c`."""
    return (1 - pl.col(Y))


def calc_g_i_form_d(C: float, E: float, Sigma: float, V: float, beta: float, epsilon: float, i: float, mu: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_18467.

    **Source**:
    - Title: Analysing Skill Predominance in Generalized Fantasy Cricket (2025)
    - Authors: Supratim Das, Sarthak Sarkar, Subhamoy Maitra et al.
    - Citation Key: `arxiv_2512_18467`

    **KaTeX Formula**:
    $$
    Gi = \beta 0 + \beta 1E + \beta 2C + \beta 3V\mu  + \beta 4\Sigma 2 + \epsilon i
    $$

    Args:
        C (float): Input parameter `C`.
        E (float): Input parameter `E`.
        Sigma (float): Input parameter `Sigma`.
        V (float): Input parameter `V`.
        beta (float): Input parameter `beta`.
        epsilon (float): Input parameter `epsilon`.
        i (float): Input parameter `i`.
        mu (float): Input parameter `mu`.

    Returns:
        float: Calculated metric value.
    """
    return float(epsilon*i + (beta*(4*(2*Sigma)) + (beta*(3*(V*mu)) + ((2*C)*beta + ((1*E)*beta + 0*beta)))))


def expr_g_i_form_d(C: str = "C", E: str = "E", Sigma: str = "Sigma", V: str = "V", beta: str = "beta", epsilon: str = "epsilon", i: str = "i", mu: str = "mu") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_i_form_d`."""
    return (pl.col(epsilon)*pl.col(i) + (pl.col(beta)*(4*(2*pl.col(Sigma))) + (pl.col(beta)*(3*(pl.col(V)*pl.col(mu))) + ((2*pl.col(C))*pl.col(beta) + ((1*pl.col(E))*pl.col(beta) + 0*pl.col(beta))))))


def calc_i_x_form_f(K: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_18417.

    **Source**:
    - Title: Resource-Efficient 3D Shape and Orientation Estimation of Road Users using Roadside RGB Camera and 3D Radar (2026)
    - Authors: Shiva Agrawal, Savankumar Bhanderi, Gordon Elger
    - Citation Key: `arxiv_2610_18417`

    **KaTeX Formula**:
    $$
    xi = 1Ki Ki\sum  k=1 x(k) y(k) z(k) 
    $$

    Args:
        K (float): Input parameter `K`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(K**2*i**2)


def expr_i_x_form_f(K: str = "K", i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_x_form_f`."""
    return (pl.col(K)**2*pl.col(i)**2)


def calc_i_w_form_f(alpha: float, d: float, e: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_18417.

    **Source**:
    - Title: Resource-Efficient 3D Shape and Orientation Estimation of Road Users using Roadside RGB Camera and 3D Radar (2026)
    - Authors: Shiva Agrawal, Savankumar Bhanderi, Gordon Elger
    - Citation Key: `arxiv_2610_18417`

    **KaTeX Formula**:
    $$
    wi = \alpha ped,w \cdot  |yg,right - yg,left|
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        d (float): Input parameter `d`.
        e (float): Input parameter `e`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(alpha*d*e*p)


def expr_i_w_form_f(alpha: str = "alpha", d: str = "d", e: str = "e", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_w_form_f`."""
    return (pl.col(alpha)*pl.col(d)*pl.col(e)*pl.col(p))


def calc_l_x_form_f(m: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2506_05866.

    **Source**:
    - Title: Analysis of points outcome in ATP Grand Slam Tennis using big data and machine learning (2025)
    - Authors: Martin Illum, Hans Christian Bechsøfft Mikkelsen, Emil Hovad
    - Citation Key: `arxiv_2506_05866`

    **KaTeX Formula**:
    $$
    L(x) = 1m m\sum  i=1 -(1 - yi )\log(1 + yi - G(xi )) - yi \log(G(xi ))
    $$

    Args:
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(m**2)


def expr_l_x_form_f(m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_x_form_f`."""
    return (pl.col(m)**2)


def calc_t_x_1_form_f(t: float, w: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2505_05120.

    **Source**:
    - Title: Simulating MLB Seasons using Bayesian Inference and Random Walks (2025)
    - Authors: Simon Cha
    - Citation Key: `arxiv_2505_05120`

    **KaTeX Formula**:
    $$
    xt+1 = xt +wt , wt \sim  N(0, σ 2 process) yt = xt + vt , vt \sim  N(0, σ 2 obs )
    $$

    Args:
        t (float): Input parameter `t`.
        w (float): Input parameter `w`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(t*w + t*x)


def expr_t_x_1_form_f(t: str = "t", w: str = "w", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_x_1_form_f`."""
    return (pl.col(t)*pl.col(w) + pl.col(t)*pl.col(x))


def calc_l_o_s_s_2206_0(N: float) -> float:
    r"""Compute mathematical metric extracted from 2206_01871.

    **Source**:
    - Title: Estimating the Effect of Team Hitting Strategies Using Counterfactual Virtual Simulation in Baseball (2022)
    - Authors: Hiroshi Nakahara, Kazuya Takeda, Keisuke Fujii
    - Citation Key: `2206_01871`

    **KaTeX Formula**:
    $$
    loss = 1N N\sum  i=1 ⎧⎪⎨⎪⎩ \sum   p'i\in   P ' i ,^ p'i\in  ^ P ' i ( p'i - ^ p'i)2 - \alpha  \sum  ^ p'i\in  ^ P ' i min( ^ p'i, 0) +\beta (w_{OBA}(  P ' i ) - w_{OBA}( ^ P ' i ))2 ,
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*N))


def expr_l_o_s_s_2206_0(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_o_s_s_2206_0`."""
    return (1*(pl.col(N)*pl.col(N)))


def calc_delta_r_e_e_v_e_n_t_2208_0(N: float) -> float:
    r"""Compute mathematical metric extracted from 2208_03492.

    **Source**:
    - Title: Pitching strategy evaluation via stratified analysis using propensity score (2022)
    - Authors: Hiroshi Nakahara, Kazuya Takeda, Keisuke Fujii
    - Citation Key: `2208_03492`

    **KaTeX Formula**:
    $$
    \Delta RE(event) = 1N N\sum  i\in event \Delta REi
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*N))


def expr_delta_r_e_e_v_e_n_t_2208_0(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_r_e_e_v_e_n_t_2208_0`."""
    return (1*(pl.col(N)*pl.col(N)))


def calc_w_k_form_0(N: float, i: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2512_18467.

    **Source**:
    - Title: Analysing Skill Predominance in Generalized Fantasy Cricket (2025)
    - Authors: Supratim Das, Sarthak Sarkar, Subhamoy Maitra et al.
    - Citation Key: `arxiv_2512_18467`

    **KaTeX Formula**:
    $$
    Wk =  20000 Ni
    $$

    Args:
        N (float): Input parameter `N`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(20000*(N*i))


def expr_w_k_form_0(N: str = "N", i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_k_form_0`."""
    return (20000*(pl.col(N)*pl.col(i)))


def calc_l_i_m_i_n_f_n_b_n_form_0(A: float, f: float, i: float, k: float, l: float, m: float, n: float) -> float:
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
    return float(A*f*i**2*k*l*m**3*n)


def expr_l_i_m_i_n_f_n_b_n_form_0(A: str = "A", f: str = "f", i: str = "i", k: str = "k", l: str = "l", m: str = "m", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_i_m_i_n_f_n_b_n_form_0`."""
    return (pl.col(A)*pl.col(f)*pl.col(i)**2*pl.col(k)*pl.col(l)*pl.col(m)**3*pl.col(n))


def calc_b_r_s_form_1(R: float, R_S: float, T_B: float, W: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    BRS = W R^T_{B} W R_{S}
    $$

    Args:
        R (float): Input parameter `R`.
        R_S (float): Input parameter `R_S`.
        T_B (float): Input parameter `T_B`.
        W (float): Input parameter `W`.

    Returns:
        float: Calculated metric value.
    """
    return float(W*(R**T_B*(R_S*W)))


def expr_b_r_s_form_1(R: str = "R", R_S: str = "R_S", T_B: str = "T_B", W: str = "W") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_b_r_s_form_1`."""
    return (pl.col(W)*(pl.col(R)**pl.col(T_B)*(pl.col(R_S)*pl.col(W))))


def calc_r_i_j_form_1(K: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    Ri(j) = 1K K\sum  s=1 R(s) i (j)
    $$

    Args:
        K (float): Input parameter `K`.

    Returns:
        float: Calculated metric value.
    """
    return float(K**2)


def expr_r_i_j_form_1(K: str = "K") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_i_j_form_1`."""
    return (pl.col(K)**2)


def calc_lambda_s_form_2(alpha: float, beta: float, gamma: float, r: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2505_05120.

    **Source**:
    - Title: Simulating MLB Seasons using Bayesian Inference and Random Walks (2025)
    - Authors: Simon Cha
    - Citation Key: `arxiv_2505_05120`

    **KaTeX Formula**:
    $$
    \lambda s = \alpha  r1 s \cdot  \beta r2 s \cdot  \gamma  r3 s
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        beta (float): Input parameter `beta`.
        gamma (float): Input parameter `gamma`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float((gamma*(r*(3*s)))*((alpha*(r*(1*s)))*(beta*(r*(2*s)))))


def expr_lambda_s_form_2(alpha: str = "alpha", beta: str = "beta", gamma: str = "gamma", r: str = "r", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_lambda_s_form_2`."""
    return ((pl.col(gamma)*(pl.col(r)*(3*pl.col(s))))*((pl.col(alpha)*(pl.col(r)*(1*pl.col(s))))*(pl.col(beta)*(pl.col(r)*(2*pl.col(s))))))


def calc_delta_h_form_2(K: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_07533.

    **Source**:
    - Title: SkillFormer: Skill-Decomposed Adaptation for Audio Language Models (2026)
    - Authors: Lee Seung-woo, Bowen Qi, Kim Min-jun et al.
    - Citation Key: `arxiv_2610_07533`

    **KaTeX Formula**:
    $$
    \Delta H = K\sum  k=1 \alpha k \Delta Hk , H = H + \Delta H
    $$

    Args:
        K (float): Input parameter `K`.

    Returns:
        float: Calculated metric value.
    """
    return float(K)


def expr_delta_h_form_2(K: str = "K") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_h_form_2`."""
    return (pl.col(K))


def calc_delta_h_k_form_2(A: float, B: float, H: float, k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_07533.

    **Source**:
    - Title: SkillFormer: Skill-Decomposed Adaptation for Audio Language Models (2026)
    - Authors: Lee Seung-woo, Bowen Qi, Kim Min-jun et al.
    - Citation Key: `arxiv_2610_07533`

    **KaTeX Formula**:
    $$
    \Delta Hk =HBk Ak, Bk \in  Rd\times r , Ak \in  Rr\times d
    $$

    Args:
        A (float): Input parameter `A`.
        B (float): Input parameter `B`.
        H (float): Input parameter `H`.
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(A*B*H*k**2)


def expr_delta_h_k_form_2(A: str = "A", B: str = "B", H: str = "H", k: str = "k") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_h_k_form_2`."""
    return (pl.col(A)*pl.col(B)*pl.col(H)*pl.col(k)**2)


def calc_i_y_i_y_form_2(k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    yi -  yi = 1 k \sum  j\in N (s) k (i)(yi - yj)
    $$

    Args:
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(k)


def expr_i_y_i_y_form_2(k: str = "k") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_y_i_y_form_2`."""
    return (pl.col(k))


def calc_c_t_form_3(R: float, T: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10498.

    **Source**:
    - Title: Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts (2026)
    - Authors: Simon Khan, Laurent Gajny, Jennyfer Lecompte et al.
    - Citation Key: `arxiv_2609_10498`

    **KaTeX Formula**:
    $$
    Ct = -R^Tt tt
    $$

    Args:
        R (float): Input parameter `R`.
        T (float): Input parameter `T`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(-R**T*t**3)


def expr_c_t_form_3(R: str = "R", T: str = "T", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_t_form_3`."""
    return (-pl.col(R)**pl.col(T)*pl.col(t)**3)


def calc_omega_b_w_form_4(C: float, R: float, v: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    \Omega wb = C vC [1] Rw
    $$

    Args:
        C (float): Input parameter `C`.
        R (float): Input parameter `R`.
        v (float): Input parameter `v`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(C**2*R*v*w)


def expr_omega_b_w_form_4(C: str = "C", R: str = "R", v: str = "v", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_omega_b_w_form_4`."""
    return (pl.col(C)**2*pl.col(R)*pl.col(v)*pl.col(w))


def calc_l_a_form_8(A: float, C: float, L: float, m: float, rho: float, v: float) -> float:
    r"""Compute mathematical metric extracted from openalex_meyer2008_w1992303757.

    **Source**:
    - Title: Influence of a humidor on the aerodynamics of baseballs (2008)
    - Authors: Edmund Meyer, John L. Bohn
    - Citation Key: `openalex_meyer2008_w1992303757`

    **KaTeX Formula**:
    $$
    aL = - 1 2 \rho A m CLv2
    $$

    Args:
        A (float): Input parameter `A`.
        C (float): Input parameter `C`.
        L (float): Input parameter `L`.
        m (float): Input parameter `m`.
        rho (float): Input parameter `rho`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(-24*A*C*L*m*rho*v)


def expr_l_a_form_8(A: str = "A", C: str = "C", L: str = "L", m: str = "m", rho: str = "rho", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_a_form_8`."""
    return (-24*pl.col(A)*pl.col(C)*pl.col(L)*pl.col(m)*pl.col(rho)*pl.col(v))


def calc_e_pi_s_form_8(D: float, F: float, b: float, delta: float, h: float, m: float, phi: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_06739.

    **Source**:
    - Title: The profit-bias identity in sports betting: bookmaker profit as the public's prediction error (2026)
    - Authors: Jacek P. Dmochowski
    - Citation Key: `arxiv_2609_06739`

    **KaTeX Formula**:
    $$
    E[\pi (s)] = Fm[(1 + \phi v)bh - \phi v ] +  Fm[(1 + \phi h)(1 - bh) - \phi h ] + D Fm  Fm \delta
    $$

    Args:
        D (float): Input parameter `D`.
        F (float): Input parameter `F`.
        b (float): Input parameter `b`.
        delta (float): Input parameter `delta`.
        h (float): Input parameter `h`.
        m (float): Input parameter `m`.
        phi (float): Input parameter `phi`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(D*(F*(m*(F*(delta*m)))) + (F*(m*(-h*phi + (1 - b*h)*(h*phi + 1))) + F*(m*(-phi*v + (b*h)*(phi*v + 1)))))


def expr_e_pi_s_form_8(D: str = "D", F: str = "F", b: str = "b", delta: str = "delta", h: str = "h", m: str = "m", phi: str = "phi", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_pi_s_form_8`."""
    return (pl.col(D)*(pl.col(F)*(pl.col(m)*(pl.col(F)*(pl.col(delta)*pl.col(m))))) + (pl.col(F)*(pl.col(m)*(-pl.col(h)*pl.col(phi) + (1 - pl.col(b)*pl.col(h))*(pl.col(h)*pl.col(phi) + 1))) + pl.col(F)*(pl.col(m)*(-pl.col(phi)*pl.col(v) + (pl.col(b)*pl.col(h))*(pl.col(phi)*pl.col(v) + 1)))))


def calc_l_v_e_l_form_8(N: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10498.

    **Source**:
    - Title: Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts (2026)
    - Authors: Simon Khan, Laurent Gajny, Jennyfer Lecompte et al.
    - Citation Key: `arxiv_2609_10498`

    **KaTeX Formula**:
    $$
    Lvel = 1 3Nv \sum  i,t mvi,t \sum  a\in {x,y,z} \rho \beta  (̂ vi,t,a - vgt i,t,a )
    $$

    Args:
        N (float): Input parameter `N`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(13*(N*v))


def expr_l_v_e_l_form_8(N: str = "N", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_v_e_l_form_8`."""
    return (13*(pl.col(N)*pl.col(v)))


def calc_n_form_9(C: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_14820.

    **Source**:
    - Title: POLARIS: Training-Free Audio Fingerprinting with Saliency-Based Landmarks and Delaunay Grouping (2026)
    - Authors: Jiheng Li
    - Citation Key: `arxiv_2609_14820`

    **KaTeX Formula**:
    $$
    N = C \sqrt Gn(C2 ) + \epsilon 2
    $$

    Args:
        C (float): Input parameter `C`.

    Returns:
        float: Calculated metric value.
    """
    return float(C)


def expr_n_form_9(C: str = "C") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_n_form_9`."""
    return (pl.col(C))


def calc_dt_k_form_a(K: float, k: float, t: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_25621.

    **Source**:
    - Title: Dissonance Spectrum explicitly models perceptual frequency interactions for better music understanding (2026)
    - Authors: Tianle Wang, Xinyi Tong, Liangke Zhao et al.
    - Citation Key: `arxiv_2608_25621`

    **KaTeX Formula**:
    $$
    d t k = 1K xtk K-1 \sum  l=0 xtl ¯D(pl -pk)
    $$

    Args:
        K (float): Input parameter `K`.
        k (float): Input parameter `k`.
        t (float): Input parameter `t`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(K**2*k*t*x - 1)


def expr_dt_k_form_a(K: str = "K", k: str = "k", t: str = "t", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_dt_k_form_a`."""
    return (pl.col(K)**2*pl.col(k)*pl.col(t)*pl.col(x) - 1)


def calc_v_z_form_b(i: float, m: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27193.

    **Source**:
    - Title: Low Residuals, Wrong Value: Learning the Viscosity Solution of Hamilton-Jacobi-Isaacs Equations with PINNs (2026)
    - Authors: Raul Jimenez, Pablo Tejerina-Pérez, Leonid Sarieddine et al.
    - Citation Key: `arxiv_2610_27193`

    **KaTeX Formula**:
    $$
    VZ = min(V * , dist(∆, Z) ∆v ), dist(∆, Z) = min ∆'\in Z|||w(∆ - ∆' )|||
    $$

    Args:
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*m*n)


def expr_v_z_form_b(i: str = "i", m: str = "m", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_z_form_b`."""
    return (pl.col(i)*pl.col(m)*pl.col(n))


def calc_r_form_b(dnu: float, v: float) -> float:
    r"""Compute mathematical metric extracted from openalex_meyer2008_w1992303757.

    **Source**:
    - Title: Influence of a humidor on the aerodynamics of baseballs (2008)
    - Authors: Edmund Meyer, John L. Bohn
    - Citation Key: `openalex_meyer2008_w1992303757`

    **KaTeX Formula**:
    $$
    R = vd \nu
    $$

    Args:
        dnu (float): Input parameter `dnu`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(dnu*v)


def expr_r_form_b(dnu: str = "dnu", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_form_b`."""
    return (pl.col(dnu)*pl.col(v))


def calc_alpha_form_c(beta: float, d: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_25525.

    **Source**:
    - Title: When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review (2026)
    - Authors: Kichang Lee, Gyeongmin Han, Sungmin Lee et al.
    - Citation Key: `arxiv_2609_25525`

    **KaTeX Formula**:
    $$
    \alpha  = \beta 0 \beta d , \sigma  = 1 \beta d
    $$

    Args:
        beta (float): Input parameter `beta`.
        d (float): Input parameter `d`.

    Returns:
        float: Calculated metric value.
    """
    return float(beta*(0*(beta*d)))


def expr_alpha_form_c(beta: str = "beta", d: str = "d") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_alpha_form_c`."""
    return (pl.col(beta)*(0*(pl.col(beta)*pl.col(d))))


def calc_sim_r_t_o_b_p_form_c(R: float, b: float, o: float, p: float, rho: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_25525.

    **Source**:
    - Title: When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review (2026)
    - Authors: Kichang Lee, Gyeongmin Han, Sungmin Lee et al.
    - Citation Key: `arxiv_2609_25525`

    **KaTeX Formula**:
    $$
    \sim Rtop b = Rtop b + \rho , \sim Rbot b = Rbot b - \rho , \sim Rside = Rside + \rho
    $$

    Args:
        R (float): Input parameter `R`.
        b (float): Input parameter `b`.
        o (float): Input parameter `o`.
        p (float): Input parameter `p`.
        rho (float): Input parameter `rho`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(R*b*o*p*t + rho)


def expr_sim_r_t_o_b_p_form_c(R: str = "R", b: str = "b", o: str = "o", p: str = "p", rho: str = "rho", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sim_r_t_o_b_p_form_c`."""
    return (pl.col(R)*pl.col(b)*pl.col(o)*pl.col(p)*pl.col(t) + pl.col(rho))


def calc_df_o_r_w_a_dt_r_form_d(R: float, T: float, e: float, t: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10498.

    **Source**:
    - Title: Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts (2026)
    - Authors: Simon Khan, Laurent Gajny, Jennyfer Lecompte et al.
    - Citation Key: `arxiv_2609_10498`

    **KaTeX Formula**:
    $$
    dforward t =R^Tt ez, ez = [0 0 1]^T
    $$

    Args:
        R (float): Input parameter `R`.
        T (float): Input parameter `T`.
        e (float): Input parameter `e`.
        t (float): Input parameter `t`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(R**T*e*t*z)


def expr_df_o_r_w_a_dt_r_form_d(R: str = "R", T: str = "T", e: str = "e", t: str = "t", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_df_o_r_w_a_dt_r_form_d`."""
    return (pl.col(R)**pl.col(T)*pl.col(e)*pl.col(t)*pl.col(z))


def calc_y_i_form_d(A: float, B: float, S: float, X: float, beta: float, epsilon: float, i: float, l: float, mu: float, p: float, t: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27576.

    **Source**:
    - Title: Who Gains When the Umpire Is a Machine? Evidence from the Automated Ball-Strike System (ABS) (2026)
    - Authors: Seung Jin Cho, Jun Yeong Lee
    - Citation Key: `arxiv_2610_27576`

    **KaTeX Formula**:
    $$
    Yi = \beta 1Xi + \beta 2 Xi \times ABSt + \mu lt + \mu p + \mu u + \epsilon i
    $$

    Args:
        A (float): Input parameter `A`.
        B (float): Input parameter `B`.
        S (float): Input parameter `S`.
        X (float): Input parameter `X`.
        beta (float): Input parameter `beta`.
        epsilon (float): Input parameter `epsilon`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        mu (float): Input parameter `mu`.
        p (float): Input parameter `p`.
        t (float): Input parameter `t`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(epsilon*i + (mu*u + (mu*p + (mu*(l*t) + (beta*(1*(X*i)) + (A*(B*(S*t)))*(beta*(2*(X*i))))))))


def expr_y_i_form_d(A: str = "A", B: str = "B", S: str = "S", X: str = "X", beta: str = "beta", epsilon: str = "epsilon", i: str = "i", l: str = "l", mu: str = "mu", p: str = "p", t: str = "t", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_y_i_form_d`."""
    return (pl.col(epsilon)*pl.col(i) + (pl.col(mu)*pl.col(u) + (pl.col(mu)*pl.col(p) + (pl.col(mu)*(pl.col(l)*pl.col(t)) + (pl.col(beta)*(1*(pl.col(X)*pl.col(i))) + (pl.col(A)*(pl.col(B)*(pl.col(S)*pl.col(t))))*(pl.col(beta)*(2*(pl.col(X)*pl.col(i)))))))))


def calc_rho_beta_e_form_d(beta: float, e: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10498.

    **Source**:
    - Title: Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts (2026)
    - Authors: Simon Khan, Laurent Gajny, Jennyfer Lecompte et al.
    - Citation Key: `arxiv_2609_10498`

    **KaTeX Formula**:
    $$
    \rho \beta (e) =  e2 2\beta  , |e| < \beta , |e| - \beta 2 , |e| \ge  \beta , \beta  = 1
    $$

    Args:
        beta (float): Input parameter `beta`.
        e (float): Input parameter `e`.

    Returns:
        float: Calculated metric value.
    """
    return float((22*beta)*e)


def expr_rho_beta_e_form_d(beta: str = "beta", e: str = "e") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_rho_beta_e_form_d`."""
    return ((22*pl.col(beta))*pl.col(e))


def calc_delta_1312_7(Delta: float, r: float, rho: float) -> float:
    r"""Compute mathematical metric extracted from 1312_7158.

    **Source**:
    - Title: openWAR: An Open Source System for Evaluating Overall Player Performance in Major League Baseball (2013)
    - Authors: Benjamin S. Baumer, Shane T. Jensen, Gregory J. Matthews
    - Citation Key: `1312_7158`

    **KaTeX Formula**:
    $$
    \delta  = \Delta \rho  + r
    $$

    Args:
        Delta (float): Input parameter `Delta`.
        r (float): Input parameter `r`.
        rho (float): Input parameter `rho`.

    Returns:
        float: Calculated metric value.
    """
    return float(Delta*rho + r)


def expr_delta_1312_7(Delta: str = "Delta", r: str = "r", rho: str = "rho") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_1312_7`."""
    return (pl.col(Delta)*pl.col(rho) + pl.col(r))


def calc_eta_i_1312_7(S: float, beta: float, epsilon: float, i: float) -> float:
    r"""Compute mathematical metric extracted from 1312_7158.

    **Source**:
    - Title: openWAR: An Open Source System for Evaluating Overall Player Performance in Major League Baseball (2013)
    - Authors: Benjamin S. Baumer, Shane T. Jensen, Gregory J. Matthews
    - Citation Key: `1312_7158`

    **KaTeX Formula**:
    $$
    \eta i =  \epsilon i -Si \cdot   \beta
    $$

    Args:
        S (float): Input parameter `S`.
        beta (float): Input parameter `beta`.
        epsilon (float): Input parameter `epsilon`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(-beta*S*i + epsilon*i)


def expr_eta_i_1312_7(S: str = "S", beta: str = "beta", epsilon: str = "epsilon", i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_eta_i_1312_7`."""
    return (-pl.col(beta)*pl.col(S)*pl.col(i) + pl.col(epsilon)*pl.col(i))


def calc_kappa_i_j_1312_7(P: float, r: float) -> float:
    r"""Compute mathematical metric extracted from 1312_7158.

    **Source**:
    - Title: openWAR: An Open Source System for Evaluating Overall Player Performance in Major League Baseball (2013)
    - Authors: Benjamin S. Baumer, Shane T. Jensen, Gregory J. Matthews
    - Citation Key: `1312_7158`

    **KaTeX Formula**:
    $$
    \kappa ij =  Pr(K \le  kij |mi)
    $$

    Args:
        P (float): Input parameter `P`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(P*r)


def expr_kappa_i_j_1312_7(P: str = "P", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_kappa_i_j_1312_7`."""
    return (pl.col(P)*pl.col(r))


def calc_alpha_t_1_1706_1(a: float, alpha: float, g: float, i: float, m: float, n: float, r: float) -> float:
    r"""Compute mathematical metric extracted from 1706_10272.

    **Source**:
    - Title: Nuclear penalized multinomial regression with an application to predicting at bat outcomes in baseball (2017)
    - Authors: Scott Powers, Trevor Hastie, Robert Tibshirani
    - Citation Key: `1706_10272`

    **KaTeX Formula**:
    $$
    \alpha (t+1) = argmin \alpha  {\langle 1Tn (Y-P(t) ), \alpha -\alpha (t) \rangle  + 1 2s ||\alpha  - \alpha (t) ||22} = \alpha (t) + s1Tn (Y-P(t) ), and
    $$

    Args:
        a (float): Input parameter `a`.
        alpha (float): Input parameter `alpha`.
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*alpha*g*i*m*n*r)


def expr_alpha_t_1_1706_1(a: str = "a", alpha: str = "alpha", g: str = "g", i: str = "i", m: str = "m", n: str = "n", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_alpha_t_1_1706_1`."""
    return (pl.col(a)*pl.col(alpha)*pl.col(g)*pl.col(i)*pl.col(m)*pl.col(n)*pl.col(r))


def calc_b_t_1_1706_1(B: float, a: float, g: float, i: float, m: float, n: float, r: float) -> float:
    r"""Compute mathematical metric extracted from 1706_10272.

    **Source**:
    - Title: Nuclear penalized multinomial regression with an application to predicting at bat outcomes in baseball (2017)
    - Authors: Scott Powers, Trevor Hastie, Robert Tibshirani
    - Citation Key: `1706_10272`

    **KaTeX Formula**:
    $$
    B(t+1) = argmin B {\langle XT (Y-P(t) ),B-B(t) \rangle  + 1 2s ||B - B(t) ||2F + \lambda ||B||*} = S * s\lambda  (B(t) + sXT (Y - P(t) ))
    $$

    Args:
        B (float): Input parameter `B`.
        a (float): Input parameter `a`.
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(B*a*g*i*m*n*r)


def expr_b_t_1_1706_1(B: str = "B", a: str = "a", g: str = "g", i: str = "i", m: str = "m", n: str = "n", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_b_t_1_1706_1`."""
    return (pl.col(B)*pl.col(a)*pl.col(g)*pl.col(i)*pl.col(m)*pl.col(n)*pl.col(r))


def calc_h_sigma_sigma_1712_0(N: float, sigma: float) -> float:
    r"""Compute mathematical metric extracted from 1712_05879.

    **Source**:
    - Title: Hierarchical Bayesian Bradley-Terry for Applications in Major League Baseball (2017)
    - Authors: Gabriel C. Phelan, John T. Whelan
    - Citation Key: `1712_05879`

    **KaTeX Formula**:
    $$
    H\sigma \sigma  = 3 \sigma -4 N\sum  i=1 \lambda 2i -N \sigma -2 = 2N \sigma -2 (20a)
    $$

    Args:
        N (float): Input parameter `N`.
        sigma (float): Input parameter `sigma`.

    Returns:
        float: Calculated metric value.
    """
    return float(-4*N + 3*sigma)


def expr_h_sigma_sigma_1712_0(N: str = "N", sigma: str = "sigma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_sigma_sigma_1712_0`."""
    return (-4*pl.col(N) + 3*pl.col(sigma))


def calc_v_mu_form_2(Delta: float, d: float, e: float, epsilon: float, mu: float, tau: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27193.

    **Source**:
    - Title: Low Residuals, Wrong Value: Learning the Viscosity Solution of Hamilton-Jacobi-Isaacs Equations with PINNs (2026)
    - Authors: Raul Jimenez, Pablo Tejerina-Pérez, Leonid Sarieddine et al.
    - Citation Key: `arxiv_2610_27193`

    **KaTeX Formula**:
    $$
    V\mu  = -\mu  \log(e-\tau  /\mu  + e-(d-\epsilon )/(\Delta v \mu ))
    $$

    Args:
        Delta (float): Input parameter `Delta`.
        d (float): Input parameter `d`.
        e (float): Input parameter `e`.
        epsilon (float): Input parameter `epsilon`.
        mu (float): Input parameter `mu`.
        tau (float): Input parameter `tau`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(-mu*math.log(2*e - tau/mu - (d - epsilon)/(Delta*mu*v)))


def expr_v_mu_form_2(Delta: str = "Delta", d: str = "d", e: str = "e", epsilon: str = "epsilon", mu: str = "mu", tau: str = "tau", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_mu_form_2`."""
    return (-pl.col(mu)*(2*pl.col(e).log() - pl.col(tau)/pl.col(mu) - (pl.col(d) - pl.col(epsilon))/(pl.col(Delta)*pl.col(mu)*pl.col(v))))


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
    return float(3*M*P*T)


def expr_p_form_2(M: str = "M", P: str = "P", T: str = "T") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_form_2`."""
    return (3*pl.col(M)*pl.col(P)*pl.col(T))


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
    return float(u*(2*(G*(P*S))))


def expr_u_2_s_3_form_2(G: str = "G", P: str = "P", S: str = "S", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_2_s_3_form_2`."""
    return (pl.col(u)*(2*(pl.col(G)*(pl.col(P)*pl.col(S)))))


def calc_c_form_2(a: float, f: float, m: float, o: float, s: float, t: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_25621.

    **Source**:
    - Title: Dissonance Spectrum explicitly models perceptual frequency interactions for better music understanding (2026)
    - Authors: Tianle Wang, Xinyi Tong, Liangke Zhao et al.
    - Citation Key: `arxiv_2608_25621`

    **KaTeX Formula**:
    $$
    C = softmax( (H(l)WQ)(ZWK)^T \sqrt da ) (ZWV )
    $$

    Args:
        a (float): Input parameter `a`.
        f (float): Input parameter `f`.
        m (float): Input parameter `m`.
        o (float): Input parameter `o`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*f*m*o*s*t*x)


def expr_c_form_2(a: str = "a", f: str = "f", m: str = "m", o: str = "o", s: str = "s", t: str = "t", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_form_2`."""
    return (pl.col(a)*pl.col(f)*pl.col(m)*pl.col(o)*pl.col(s)*pl.col(t)*pl.col(x))


def calc_p_k_form_5(N: float, k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_36769.

    **Source**:
    - Title: Externalizing Hand Grip Pressure Through Real-Time Visual Feedback (2026)
    - Authors: Andrew L. Huard, Avinash Ajit Nargund, Misha Sra
    - Citation Key: `arxiv_2610_36769`

    **KaTeX Formula**:
    $$
    Pk = 1 Nk \sum  i\in Zk Pnorm,i
    $$

    Args:
        N (float): Input parameter `N`.
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*k))


def expr_p_k_form_5(N: str = "N", k: str = "k") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_k_form_5`."""
    return (1*(pl.col(N)*pl.col(k)))


def calc_delta_h_form_6(Q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_14820.

    **Source**:
    - Title: POLARIS: Training-Free Audio Fingerprinting with Saliency-Based Landmarks and Delaunay Grouping (2026)
    - Authors: Jiheng Li
    - Citation Key: `arxiv_2609_14820`

    **KaTeX Formula**:
    $$
    h\Delta  =Q( [f1, f2 - f1, t2 - t1, f3 - f1, t3 - t1] )
    $$

    Args:
        Q (float): Input parameter `Q`.

    Returns:
        float: Calculated metric value.
    """
    return float(Q)


def expr_delta_h_form_6(Q: str = "Q") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_h_form_6`."""
    return (pl.col(Q))


def calc_l_v_r_r_e_e_2223_form_7(C: float, H: float, Z: float, e: float, g: float, m: float, v: float) -> float:
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
    return float(21252*C*H*Z*e*g*m*v + 8*C*e**2)


def expr_l_v_r_r_e_e_2223_form_7(C: str = "C", H: str = "H", Z: str = "Z", e: str = "e", g: str = "g", m: str = "m", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_v_r_r_e_e_2223_form_7`."""
    return (21252*pl.col(C)*pl.col(H)*pl.col(Z)*pl.col(e)*pl.col(g)*pl.col(m)*pl.col(v) + 8*pl.col(C)*pl.col(e)**2)


def calc_c_r_r_form_7(C: float, R: float, T: float, W: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    C RR = W R^TC W RR
    $$

    Args:
        C (float): Input parameter `C`.
        R (float): Input parameter `R`.
        T (float): Input parameter `T`.
        W (float): Input parameter `W`.

    Returns:
        float: Calculated metric value.
    """
    return float(C*R**2*R**T*W**2)


def expr_c_r_r_form_7(C: str = "C", R: str = "R", T: str = "T", W: str = "W") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_r_r_form_7`."""
    return (pl.col(C)*pl.col(R)**2*pl.col(R)**pl.col(T)*pl.col(W)**2)


def calc_lambda_i_phi_form_7(i: float, m: float, n: float, phi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2604_13861.

    **Source**:
    - Title: Simulation-Based Optimisation of Batting Order and Bowling Plans in T20 Cricket (2026)
    - Authors: Tinniam V Ganesh
    - Citation Key: `arxiv_2604_13861`

    **KaTeX Formula**:
    $$
    \lambda \phi i = n\phi i n\phi i +nmin , nmin = 50
    $$

    Args:
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        phi (float): Input parameter `phi`.

    Returns:
        float: Calculated metric value.
    """
    return float(n*(m*(i*n)) + n*(phi*(i*(n*(i*phi)))))


def expr_lambda_i_phi_form_7(i: str = "i", m: str = "m", n: str = "n", phi: str = "phi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_lambda_i_phi_form_7`."""
    return (pl.col(n)*(pl.col(m)*(pl.col(i)*pl.col(n))) + pl.col(n)*(pl.col(phi)*(pl.col(i)*(pl.col(n)*(pl.col(i)*pl.col(phi))))))


def calc_val_2507_16328_form_7(C: float, T: float, u: float, v: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2507_16328.

    **Source**:
    - Title: Design and Dimensional Optimization of Legged Structures for Construction Robots (2025)
    - Authors: Xiao Liu, Xianlong Yang, Weijun Wang et al.
    - Citation Key: `arxiv_2507_16328`

    **KaTeX Formula**:
    $$
    px1 px2 px3 px4 px5 px6 py1 py2 py3 py4 py5 py6 pz1 pz2 pz3 pz4 pz5 pz6 1 1 1 1 1 1  = TC  u1 u2 u3 u4 u5 u6 v1 v2 v3 v4 v5 v6 w1 w2 w3 w4 w5 w6 1 1 1 1 1 1
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
    return float(380159993088000*C*T*u**6*v**6*w**6)


def expr_val_2507_16328_form_7(C: str = "C", T: str = "T", u: str = "u", v: str = "v", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2507_16328_form_7`."""
    return (380159993088000*pl.col(C)*pl.col(T)*pl.col(u)**6*pl.col(v)**6*pl.col(w)**6)


def calc_val_2507_16328_form_9(C: float, T: float, u: float, v: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2507_16328.

    **Source**:
    - Title: Design and Dimensional Optimization of Legged Structures for Construction Robots (2025)
    - Authors: Xiao Liu, Xianlong Yang, Weijun Wang et al.
    - Citation Key: `arxiv_2507_16328`

    **KaTeX Formula**:
    $$
    px1 px2 px3 py1 py2 py3 pz1 pz2 pz3 1 1 1  = TC  u1 u2 u3 v1 v2 v3 w1 w2 w3 1 1 1
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
    return float(223992*C*T*u**3*v**3*w**3)


def expr_val_2507_16328_form_9(C: str = "C", T: str = "T", u: str = "u", v: str = "v", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2507_16328_form_9`."""
    return (223992*pl.col(C)*pl.col(T)*pl.col(u)**3*pl.col(v)**3*pl.col(w)**3)


def calc_l_r_o_o_t_form_9(N: float, Omega: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_10498.

    **Source**:
    - Title: Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts (2026)
    - Authors: Simon Khan, Laurent Gajny, Jennyfer Lecompte et al.
    - Citation Key: `arxiv_2609_10498`

    **KaTeX Formula**:
    $$
    Lroot = 1 Nr\Omega  \sum  i,t vi,t \sum  a\in {x,y,z} \omega a \rho \beta  ( rc i,t,a - rc,gt i,t,a )
    $$

    Args:
        N (float): Input parameter `N`.
        Omega (float): Input parameter `Omega`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*(Omega*r)))


def expr_l_r_o_o_t_form_9(N: str = "N", Omega: str = "Omega", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_r_o_o_t_form_9`."""
    return (1*(pl.col(N)*(pl.col(Omega)*pl.col(r))))


def calc_i_y_form_a(k: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_25605.

    **Source**:
    - Title: PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization (2026)
    - Authors: Xinyi Chen, Jiahuan Pang, Titus Chima et al.
    - Citation Key: `arxiv_2610_25605`

    **KaTeX Formula**:
    $$
    yi = 1 k \sum  j\in N (s) k (i) yj
    $$

    Args:
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(k)


def expr_i_y_form_a(k: str = "k") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_y_form_a`."""
    return (pl.col(k))


def calc_c_b_r_form_f(B: float, C: float, R: float, T: float, W: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_29935.

    **Source**:
    - Title: System Identification of Admittance Models for Large Real-World Objects (2026)
    - Authors: Nathan I. Baum, Nathaniel G. Luttmer, Mark A. Minor
    - Citation Key: `arxiv_2608_29935`

    **KaTeX Formula**:
    $$
    C RB = W R^TC W RB
    $$

    Args:
        B (float): Input parameter `B`.
        C (float): Input parameter `C`.
        R (float): Input parameter `R`.
        T (float): Input parameter `T`.
        W (float): Input parameter `W`.

    Returns:
        float: Calculated metric value.
    """
    return float(B*C*R*R**T*W**2)


def expr_c_b_r_form_f(B: str = "B", C: str = "C", R: str = "R", T: str = "T", W: str = "W") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_b_r_form_f`."""
    return (pl.col(B)*pl.col(C)*pl.col(R)*pl.col(R)**pl.col(T)*pl.col(W)**2)


def calc_val_2506_22350_2506_2(B: float, P: float, Z: float, beta: float, i: float) -> float:
    r"""Compute mathematical metric extracted from 2506_22350.

    **Source**:
    - Title: Personnel-adjustment for home run park effects in Major League Baseball (2025)
    - Authors: Jason A. Osborne, Richard A. Levine
    - Citation Key: `2506_22350`

    **KaTeX Formula**:
    $$
    \log \lambda i(XS i ,Z B i ,Z P i ,XLHB i , XRHB i , XLHP i , XRHP i , XP i ) = \beta 0 + \beta B Z B i +\beta P Z P i + 13\sum  s=1 SsXS i,s + 30\sum  p=1 (︀\beta LL p XLHB i XLHP i +\beta LR p XLHB i XRHP i +\beta RL p XRHB i XLHP i +\beta RR p XRHB i XRHP i )︀ Xp i
    $$

    Args:
        B (float): Input parameter `B`.
        P (float): Input parameter `P`.
        Z (float): Input parameter `Z`.
        beta (float): Input parameter `beta`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float((beta*(P*(Z*(P*i))) + (beta*(B*(Z*(B*i))) + 0*beta)) + 13)


def expr_val_2506_22350_2506_2(B: str = "B", P: str = "P", Z: str = "Z", beta: str = "beta", i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2506_22350_2506_2`."""
    return ((pl.col(beta)*(pl.col(P)*(pl.col(Z)*(pl.col(P)*pl.col(i)))) + (pl.col(beta)*(pl.col(B)*(pl.col(Z)*(pl.col(B)*pl.col(i)))) + 0*pl.col(beta))) + 13)


def calc_theta_1_2510_2(Delta: float) -> float:
    r"""Compute mathematical metric extracted from 2510_25961.

    **Source**:
    - Title: Tractable Algorithms for Changepoint Detection in Player Performance Metrics (2025)
    - Authors: Amanda Glazer
    - Citation Key: `2510_25961`

    **KaTeX Formula**:
    $$
    \theta 1 = \theta 0 +\Delta
    $$

    Args:
        Delta (float): Input parameter `Delta`.

    Returns:
        float: Calculated metric value.
    """
    return float(Delta)


def expr_theta_1_2510_2(Delta: str = "Delta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_theta_1_2510_2`."""
    return (pl.col(Delta))


def calc_beta_p_a_r_k_p_2603_2(a: float, beta: float, k: float, p: float, r: float) -> float:
    r"""Compute mathematical metric extracted from 2603_21163.

    **Source**:
    - Title: Simultaneous Estimation of Ballpark Effects and Team Defense Using Total Bases Residuals (2026)
    - Authors: Jhe-Jia Wu, Tian-Li Yan, Ting-Li Chen
    - Citation Key: `2603_21163`

    **KaTeX Formula**:
    $$
    \beta park p =  \beta park p -  \beta park , \sim  \beta def d =  \beta def d -  \beta def
    $$

    Args:
        a (float): Input parameter `a`.
        beta (float): Input parameter `beta`.
        k (float): Input parameter `k`.
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(-beta*p*(a*(k*r)) + beta*(p*(a*(r*(k*p)))))


def expr_beta_p_a_r_k_p_2603_2(a: str = "a", beta: str = "beta", k: str = "k", p: str = "p", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_beta_p_a_r_k_p_2603_2`."""
    return (-pl.col(beta)*pl.col(p)*(pl.col(a)*(pl.col(k)*pl.col(r))) + pl.col(beta)*(pl.col(p)*(pl.col(a)*(pl.col(r)*(pl.col(k)*pl.col(p))))))


def calc_sim_beta_0_2603_2(a: float, beta: float, de: float, f: float, k: float, p: float, r: float) -> float:
    r"""Compute mathematical metric extracted from 2603_21163.

    **Source**:
    - Title: Simultaneous Estimation of Ballpark Effects and Team Defense Using Total Bases Residuals (2026)
    - Authors: Jhe-Jia Wu, Tian-Li Yan, Ting-Li Chen
    - Citation Key: `2603_21163`

    **KaTeX Formula**:
    $$
    \sim  \beta 0 =  \beta 0 +  \beta park -  \beta def
    $$

    Args:
        a (float): Input parameter `a`.
        beta (float): Input parameter `beta`.
        de (float): Input parameter `de`.
        f (float): Input parameter `f`.
        k (float): Input parameter `k`.
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(-beta*de*f + (beta*(p*(a*(k*r))) + 0*beta))


def expr_sim_beta_0_2603_2(a: str = "a", beta: str = "beta", de: str = "de", f: str = "f", k: str = "k", p: str = "p", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sim_beta_0_2603_2`."""
    return (-pl.col(beta)*pl.col(de)*pl.col(f) + (pl.col(beta)*(pl.col(p)*(pl.col(a)*(pl.col(k)*pl.col(r)))) + 0*pl.col(beta)))


def calc_z_2603_2(beta: float, s: float) -> float:
    r"""Compute mathematical metric extracted from 2603_21163.

    **Source**:
    - Title: Simultaneous Estimation of Ballpark Effects and Team Defense Using Total Bases Residuals (2026)
    - Authors: Jhe-Jia Wu, Tian-Li Yan, Ting-Li Chen
    - Citation Key: `2603_21163`

    **KaTeX Formula**:
    $$
    z =  \beta  -  \beta  s\beta
    $$

    Args:
        beta (float): Input parameter `beta`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(-beta*beta*s + beta)


def expr_z_2603_2(beta: str = "beta", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_2603_2`."""
    return (-pl.col(beta)*pl.col(beta)*pl.col(s) + pl.col(beta))


def calc_i_z_2609_0(T: float, i: float, k: float, q: float, u: float) -> float:
    r"""Compute mathematical metric extracted from 2609_03810.

    **Source**:
    - Title: Unified Pitch Graphs for Diagnosing Pitching Strategy (2026)
    - Authors: Kichang Lee, JeongGil Ko
    - Citation Key: `2609_03810`

    **KaTeX Formula**:
    $$
    zi = u ^T k  qi
    $$

    Args:
        T (float): Input parameter `T`.
        i (float): Input parameter `i`.
        k (float): Input parameter `k`.
        q (float): Input parameter `q`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*k*q*u**T)


def expr_i_z_2609_0(T: str = "T", i: str = "i", k: str = "k", q: str = "q", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_z_2609_0`."""
    return (pl.col(i)*pl.col(k)*pl.col(q)*pl.col(u)**pl.col(T))


def calc_t_s_e_delta_brown_(E: float, P: float, S: float, delta: float) -> float:
    r"""Compute mathematical metric extracted from brown_2008_aoas.

    **Source**:
    - Title: Supplement to 'In-season prediction of batting averages...': Major league batting records for 2005 (2008)
    - Authors: Brown, L. D.
    - Citation Key: `brown_2008_aoas`

    **KaTeX Formula**:
    $$
    TSE[\delta ] =SSPE[\delta ]- \sum  i\in S1\cap S2 1 4N2i
    $$

    Args:
        E (float): Input parameter `E`.
        P (float): Input parameter `P`.
        S (float): Input parameter `S`.
        delta (float): Input parameter `delta`.

    Returns:
        float: Calculated metric value.
    """
    return float(S*(S*(P*(E*delta))))


def expr_t_s_e_delta_brown_(E: str = "E", P: str = "P", S: str = "S", delta: str = "delta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_s_e_delta_brown_`."""
    return (pl.col(S)*(pl.col(S)*(pl.col(P)*(pl.col(E)*pl.col(delta)))))


def calc_delta_t_e_s_brown_(E: float, S: float, T: float, delta: float) -> float:
    r"""Compute mathematical metric extracted from brown_2008_aoas.

    **Source**:
    - Title: Supplement to 'In-season prediction of batting averages...': Major league batting records for 2005 (2008)
    - Authors: Brown, L. D.
    - Citation Key: `brown_2008_aoas`

    **KaTeX Formula**:
    $$
    TSE * [\delta ] =  TSE[\delta ]  TSE[\delta 0]
    $$

    Args:
        E (float): Input parameter `E`.
        S (float): Input parameter `S`.
        T (float): Input parameter `T`.
        delta (float): Input parameter `delta`.

    Returns:
        float: Calculated metric value.
    """
    return float(T*(S*(E*(delta*(T*(S*(E*(0*delta))))))))


def expr_delta_t_e_s_brown_(E: str = "E", S: str = "S", T: str = "T", delta: str = "delta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_t_e_s_brown_`."""
    return (pl.col(T)*(pl.col(S)*(pl.col(E)*(pl.col(delta)*(pl.col(T)*(pl.col(S)*(pl.col(E)*(0*pl.col(delta)))))))))


def calc_p_egidi_(M: float) -> float:
    r"""Compute mathematical metric extracted from egidi_2018_arxiv1802.

    **Source**:
    - Title: arxiv1802.08848
    - Authors: Scientific Literature
    - Citation Key: `egidi_2018_arxiv1802`

    **KaTeX Formula**:
    $$
    p = 1M M\sum  m=1 \prod  i\in \Delta m pi,m\delta im
    $$

    Args:
        M (float): Input parameter `M`.

    Returns:
        float: Calculated metric value.
    """
    return float(M**2)


def expr_p_egidi_(M: str = "M") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_egidi_`."""
    return (pl.col(M)**2)


def calc_k_tau_form_0(f: float, tau: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    \tau k = \tau ff,k + f(dx) , (37a)
    $$

    Args:
        f (float): Input parameter `f`.
        tau (float): Input parameter `tau`.

    Returns:
        float: Calculated metric value.
    """
    return float(f**2*tau)


def expr_k_tau_form_0(f: str = "f", tau: str = "tau") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_tau_form_0`."""
    return (pl.col(f)**2*pl.col(tau))


def calc_eta_g_form_2(L: float, P: float, alpha: float, c: float, g: float, i: float, l: float, o: float, r: float, rho: float, s: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_21639.

    **Source**:
    - Title: Liquid-Nitrogen Micropillar-Wick Cooling for Cryogenic Electronics: A Numerical Study of Thermal Performance and Capillary Dry-Out Limits (2026)
    - Authors: Felix Mende, Marcus Wislicenus, Dianping Jiang et al.
    - Citation Key: `arxiv_2609_21639`

    **KaTeX Formula**:
    $$
    \eta g = \rho lgLcos \alpha  Pcr it
    $$

    Args:
        L (float): Input parameter `L`.
        P (float): Input parameter `P`.
        alpha (float): Input parameter `alpha`.
        c (float): Input parameter `c`.
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.
        rho (float): Input parameter `rho`.
        s (float): Input parameter `s`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(L*P*alpha*c**2*g*i*l*o*r*rho*s*t)


def expr_eta_g_form_2(L: str = "L", P: str = "P", alpha: str = "alpha", c: str = "c", g: str = "g", i: str = "i", l: str = "l", o: str = "o", r: str = "r", rho: str = "rho", s: str = "s", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_eta_g_form_2`."""
    return (pl.col(L)*pl.col(P)*pl.col(alpha)*pl.col(c)**2*pl.col(g)*pl.col(i)*pl.col(l)*pl.col(o)*pl.col(r)*pl.col(rho)*pl.col(s)*pl.col(t))


def calc_p_z_l_o_form_3(a: float, b: float, e: float, l: float, o: float, psi: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    pzlo = ae \cos(\theta lo + \psi e) (61b)
    $$

    Args:
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        e (float): Input parameter `e`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.
        psi (float): Input parameter `psi`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(61*a*b*e*math.cos(e*psi + l*o*theta))


def expr_p_z_l_o_form_3(a: str = "a", b: str = "b", e: str = "e", l: str = "l", o: str = "o", psi: str = "psi", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_z_l_o_form_3`."""
    return (61*pl.col(a)*pl.col(b)*pl.col(e)*math.cos(pl.col(e)*pl.col(psi) + pl.col(l)*pl.col(o)*pl.col(theta)))


def calc_a_q_form_6(phi: float, tau: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    q* a = \phi * \phi *  \tau  *  =  \phi d 0 mg r0 (\chi dx - r0 \sin (\Xi \theta ,g))
    $$

    Args:
        phi (float): Input parameter `phi`.
        tau (float): Input parameter `tau`.

    Returns:
        float: Calculated metric value.
    """
    return float(phi**2*tau)


def expr_a_q_form_6(phi: str = "phi", tau: str = "tau") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_q_form_6`."""
    return (pl.col(phi)**2*pl.col(tau))


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
    return float(R*T*e**2*j**2)


def expr_e_j_form_6(R: str = "R", T: str = "T", e: str = "e", j: str = "j") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_j_form_6`."""
    return (pl.col(R)*pl.col(T)*pl.col(e)**2*pl.col(j)**2)


def calc_l_v_form_6(N: float, i: float, n: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27193.

    **Source**:
    - Title: Low Residuals, Wrong Value: Learning the Viscosity Solution of Hamilton-Jacobi-Isaacs Equations with PINNs (2026)
    - Authors: Raul Jimenez, Pablo Tejerina-Pérez, Leonid Sarieddine et al.
    - Citation Key: `arxiv_2610_27193`

    **KaTeX Formula**:
    $$
    L[V ] = 1 Nint \sum  i r[V ](\Delta i, \tau i) 2 + \lambda  1 N0 \sum  j V (\Delta j , 0) 2 + \lambda  1 N\epsilon  \sum  k V (\Delta k, \tau k) 2
    $$

    Args:
        N (float): Input parameter `N`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*(i*(n*t))))


def expr_l_v_form_6(N: str = "N", i: str = "i", n: str = "n", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_v_form_6`."""
    return (1*(pl.col(N)*(pl.col(i)*(pl.col(n)*pl.col(t)))))


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
    return float(2*(u*(2*(G*(P*S)))))


def expr_u_2_s_4_form_7(G: str = "G", P: str = "P", S: str = "S", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_2_s_4_form_7`."""
    return (2*(pl.col(u)*(2*(pl.col(G)*(pl.col(P)*pl.col(S))))))


def calc_z_m_i_x_form_7(a: float, de: float, i: float, l: float, n: float, o: float, z: float) -> float:
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
    return float(a*de*i*l*n**2*o*z + a*de*i*l*z)


def expr_z_m_i_x_form_7(a: str = "a", de: str = "de", i: str = "i", l: str = "l", n: str = "n", o: str = "o", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_m_i_x_form_7`."""
    return (pl.col(a)*pl.col(de)*pl.col(i)*pl.col(l)*pl.col(n)**2*pl.col(o)*pl.col(z) + pl.col(a)*pl.col(de)*pl.col(i)*pl.col(l)*pl.col(z))


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
    return float(R**2*c*o*p*s)


def expr_r_p_o_s_form_9(R: str = "R", c: str = "c", o: str = "o", p: str = "p", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_p_o_s_form_9`."""
    return (pl.col(R)**2*pl.col(c)*pl.col(o)*pl.col(p)*pl.col(s))


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
    return float(2*L*M*P*u)


def expr_u_2_s_1_form_f(L: str = "L", M: str = "M", P: str = "P", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_2_s_1_form_f`."""
    return (2*pl.col(L)*pl.col(M)*pl.col(P)*pl.col(u))


def calc_a_x_1_x_2_form_f(x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_25621.

    **Source**:
    - Title: Dissonance Spectrum explicitly models perceptual frequency interactions for better music understanding (2026)
    - Authors: Tianle Wang, Xinyi Tong, Liangke Zhao et al.
    - Citation Key: `arxiv_2608_25621`

    **KaTeX Formula**:
    $$
    A(x1, x2) = x1x2, D(\Delta p; x1, x2) = x1x2 D(\Delta p)
    $$

    Args:
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*x)


def expr_a_x_1_x_2_form_f(x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_x_1_x_2_form_f`."""
    return (2*pl.col(x))


def calc_v_r_form_f(Delta: float, V: float, nabla: float, partial: float, tau: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27193.

    **Source**:
    - Title: Low Residuals, Wrong Value: Learning the Viscosity Solution of Hamilton-Jacobi-Isaacs Equations with PINNs (2026)
    - Authors: Raul Jimenez, Pablo Tejerina-Pérez, Leonid Sarieddine et al.
    - Citation Key: `arxiv_2610_27193`

    **KaTeX Formula**:
    $$
    r[V ] = \partial \tau  V - 1 + \Delta v |\nabla V |
    $$

    Args:
        Delta (float): Input parameter `Delta`.
        V (float): Input parameter `V`.
        nabla (float): Input parameter `nabla`.
        partial (float): Input parameter `partial`.
        tau (float): Input parameter `tau`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(Delta*v*abs(V*nabla) + V*partial*tau - 1)


def expr_v_r_form_f(Delta: str = "Delta", V: str = "V", nabla: str = "nabla", partial: str = "partial", tau: str = "tau", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_r_form_f`."""
    return (pl.col(Delta)*pl.col(v)*abs(pl.col(V)*pl.col(nabla)) + pl.col(V)*pl.col(partial)*pl.col(tau) - 1)


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
    return float(11*r**4)


def expr_val_1205_4750_1205_4(r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1205_4750_1205_4`."""
    return (11*pl.col(r)**4)


def calc_w_a_r_q_1312_7(A: float, R: float, e: float, l: float, p: float, q: float, r: float) -> float:
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
    return float(-10*A**2*R*e*l*p*q*r + A**2*R*q)


def expr_w_a_r_q_1312_7(A: str = "A", R: str = "R", e: str = "e", l: str = "l", p: str = "p", q: str = "q", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_a_r_q_1312_7`."""
    return (-10*pl.col(A)**2*pl.col(R)*pl.col(e)*pl.col(l)*pl.col(p)*pl.col(q)*pl.col(r) + pl.col(A)**2*pl.col(R)*pl.col(q))


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
    return float(p*(R_A*R_S) + 11)


def expr_w_p_c_t_p_r_s_r_a_1312_7(R_A: str = "R_A", R_S: str = "R_S", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_p_c_t_p_r_s_r_a_1312_7`."""
    return (pl.col(p)*(pl.col(R_A)*pl.col(R_S)) + 11)


def calc_sim_omega_l_l_r_form_3(p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_08746.

    **Source**:
    - Title: Kinematics of Single-Winged Spinning Seeds: A Study on Mahogany and Buddha Coconut Samaras (2026)
    - Authors: Yogeshwaran G, Srisha M. V. Rao, Jagadeesh G
    - Citation Key: `arxiv_2603_08746`

    **KaTeX Formula**:
    $$
    \sim \omega L LR =  0 -r q r 0 -p -q p 0
    $$

    Args:
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(-p)


def expr_sim_omega_l_l_r_form_3(p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sim_omega_l_l_r_form_3`."""
    return (-pl.col(p))


def calc_p_form_5(L: float, R: float, phi: float, psi: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_08746.

    **Source**:
    - Title: Kinematics of Single-Winged Spinning Seeds: A Study on Mahogany and Buddha Coconut Samaras (2026)
    - Authors: Yogeshwaran G, Srisha M. V. Rao, Jagadeesh G
    - Citation Key: `arxiv_2603_08746`

    **KaTeX Formula**:
    $$
    p = \phi LR - \sin\theta LR \cdot  \psi LR
    $$

    Args:
        L (float): Input parameter `L`.
        R (float): Input parameter `R`.
        phi (float): Input parameter `phi`.
        psi (float): Input parameter `psi`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(L*R*phi - math.sin(L**2*R**2*psi*theta))


def expr_p_form_5(L: str = "L", R: str = "R", phi: str = "phi", psi: str = "psi", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_form_5`."""
    return (pl.col(L)*pl.col(R)*pl.col(phi) - math.sin(pl.col(L)**2*pl.col(R)**2*pl.col(psi)*pl.col(theta)))


def calc_sigma_a_c_form_5(l: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_21639.

    **Source**:
    - Title: Liquid-Nitrogen Micropillar-Wick Cooling for Cryogenic Electronics: A Numerical Study of Thermal Performance and Capillary Dry-Out Limits (2026)
    - Authors: Felix Mende, Marcus Wislicenus, Dianping Jiang et al.
    - Citation Key: `arxiv_2609_21639`

    **KaTeX Formula**:
    $$
    \sigma ac = (1 - l) \exp (- l 2 (1 - l) )
    $$

    Args:
        l (float): Input parameter `l`.

    Returns:
        float: Calculated metric value.
    """
    return float((1 - l)*math.exp(-2*l*(1 - l)))


def expr_sigma_a_c_form_5(l: str = "l") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sigma_a_c_form_5`."""
    return ((1 - pl.col(l))*(-2*pl.col(l).exp()*(1 - pl.col(l))))


def calc_j_l_v_form_5(a: float, c: float, sigma: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_21639.

    **Source**:
    - Title: Liquid-Nitrogen Micropillar-Wick Cooling for Cryogenic Electronics: A Numerical Study of Thermal Performance and Capillary Dry-Out Limits (2026)
    - Authors: Felix Mende, Marcus Wislicenus, Dianping Jiang et al.
    - Citation Key: `arxiv_2609_21639`

    **KaTeX Formula**:
    $$
    jlv = \sigma ac\sqrt  m 2\pi kB ( psat (Tl ) \sqrt Tl - \Gamma  ( ̄vn\beta v ) pv \sqrt Tv )
    $$

    Args:
        a (float): Input parameter `a`.
        c (float): Input parameter `c`.
        sigma (float): Input parameter `sigma`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*c*sigma)


def expr_j_l_v_form_5(a: str = "a", c: str = "c", sigma: str = "sigma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_l_v_form_5`."""
    return (pl.col(a)*pl.col(c)*pl.col(sigma))


def calc_y_form_6(F: float, epsilon: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    y = [F0(a) 0 ] + \epsilon F1(y, \epsilon )
    $$

    Args:
        F (float): Input parameter `F`.
        epsilon (float): Input parameter `epsilon`.

    Returns:
        float: Calculated metric value.
    """
    return float(F*epsilon)


def expr_y_form_6(F: str = "F", epsilon: str = "epsilon") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_y_form_6`."""
    return (pl.col(F)*pl.col(epsilon))


def calc_partial_v_tau_form_6(Delta: float, V: float, nabla: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27193.

    **Source**:
    - Title: Low Residuals, Wrong Value: Learning the Viscosity Solution of Hamilton-Jacobi-Isaacs Equations with PINNs (2026)
    - Authors: Raul Jimenez, Pablo Tejerina-Pérez, Leonid Sarieddine et al.
    - Citation Key: `arxiv_2610_27193`

    **KaTeX Formula**:
    $$
    \partial \tau V = 1 -\Delta v |\nabla V |, \Delta v := vP - vE = 0.2
    $$

    Args:
        Delta (float): Input parameter `Delta`.
        V (float): Input parameter `V`.
        nabla (float): Input parameter `nabla`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(-Delta*v*abs(V*nabla) + 1)


def expr_partial_v_tau_form_6(Delta: str = "Delta", V: str = "V", nabla: str = "nabla", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_partial_v_tau_form_6`."""
    return (-pl.col(Delta)*pl.col(v)*abs(pl.col(V)*pl.col(nabla)) + 1)


def calc_r_form_9(L: float, R: float, phi: float, psi: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_08746.

    **Source**:
    - Title: Kinematics of Single-Winged Spinning Seeds: A Study on Mahogany and Buddha Coconut Samaras (2026)
    - Authors: Yogeshwaran G, Srisha M. V. Rao, Jagadeesh G
    - Citation Key: `arxiv_2603_08746`

    **KaTeX Formula**:
    $$
    r = -\sin\phi LR \cdot   \theta LR + \cos\phi LR \cdot  \cos \theta LR \cdot  \psi LR
    $$

    Args:
        L (float): Input parameter `L`.
        R (float): Input parameter `R`.
        phi (float): Input parameter `phi`.
        psi (float): Input parameter `psi`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(-math.sin(L**2*R**2*phi*theta) + math.cos(L*R*phi*math.cos(L**2*R**2*psi*theta)))


def expr_r_form_9(L: str = "L", R: str = "R", phi: str = "phi", psi: str = "psi", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_form_9`."""
    return (-math.sin(pl.col(L)**2*pl.col(R)**2*pl.col(phi)*pl.col(theta)) + math.cos(pl.col(L)*pl.col(R)*pl.col(phi)*math.cos(pl.col(L)**2*pl.col(R)**2*pl.col(psi)*pl.col(theta))))


def calc_lambda_a_e_form_a(b: float, c: float, de: float, epsilon: float, gamma: float, m: float, o: float, omega: float, pi: float, psi: float, r: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    \lambda ae = 1 - \epsilon b\pi  cos2 (\gamma \psi d e ) 2m\omega r
    $$

    Args:
        b (float): Input parameter `b`.
        c (float): Input parameter `c`.
        de (float): Input parameter `de`.
        epsilon (float): Input parameter `epsilon`.
        gamma (float): Input parameter `gamma`.
        m (float): Input parameter `m`.
        o (float): Input parameter `o`.
        omega (float): Input parameter `omega`.
        pi (float): Input parameter `pi`.
        psi (float): Input parameter `psi`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(1 - epsilon*b*(pi*(c*(o*(s*(2*((gamma*(de*psi))*(2*(m*(omega*r))))))))))


def expr_lambda_a_e_form_a(b: str = "b", c: str = "c", de: str = "de", epsilon: str = "epsilon", gamma: str = "gamma", m: str = "m", o: str = "o", omega: str = "omega", pi: str = "pi", psi: str = "psi", r: str = "r", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_lambda_a_e_form_a`."""
    return (1 - pl.col(epsilon)*pl.col(b)*(pl.col(pi)*(pl.col(c)*(pl.col(o)*(pl.col(s)*(2*((pl.col(gamma)*(pl.col(de)*pl.col(psi)))*(2*(pl.col(m)*(pl.col(omega)*pl.col(r)))))))))))


def calc_psi_v_form_a(a: float, b: float, c: float, e: float, g: float, m: float, omega: float, psi: float, r: float, s: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    \psi v = \omega r + ae \cos \psi r \sin \psi e \tan \psi e r - b \cos \psi r \sin \psi r m - g \cos \theta  \cos \psi r sec \psi e ae (55a)
    $$

    Args:
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        c (float): Input parameter `c`.
        e (float): Input parameter `e`.
        g (float): Input parameter `g`.
        m (float): Input parameter `m`.
        omega (float): Input parameter `omega`.
        psi (float): Input parameter `psi`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*e*math.sin(e*psi)*math.cos(psi*r)*math.tan(e*psi*r) - b*math.sin(m*psi*r)*math.cos(psi*r) - g*math.cos(theta)*math.cos(55*a**2*c*e**3*psi**2*r*s) + omega*r)


def expr_psi_v_form_a(a: str = "a", b: str = "b", c: str = "c", e: str = "e", g: str = "g", m: str = "m", omega: str = "omega", psi: str = "psi", r: str = "r", s: str = "s", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_psi_v_form_a`."""
    return (pl.col(a)*pl.col(e)*math.sin(pl.col(e)*pl.col(psi))*math.cos(pl.col(psi)*pl.col(r))*math.tan(pl.col(e)*pl.col(psi)*pl.col(r)) - pl.col(b)*math.sin(pl.col(m)*pl.col(psi)*pl.col(r))*math.cos(pl.col(psi)*pl.col(r)) - pl.col(g)*math.cos(pl.col(theta))*math.cos(55*pl.col(a)**2*pl.col(c)*pl.col(e)**3*pl.col(psi)**2*pl.col(r)*pl.col(s)) + pl.col(omega)*pl.col(r))


def calc_e_psi_form_d(a: float, b: float, e: float, g: float, i: float, m: float, n: float, psi: float, r: float, s: float, tau: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    \psi e =  \tau  \cos \psi e mae + b \cos \psi e \sin \psi e sin2 \psi r m - ae \sin\psi e \sin\psi r r + g \sin \psi e \sin \psi r \cos \theta  ae (55b)
    $$

    Args:
        a (float): Input parameter `a`.
        b (float): Input parameter `b`.
        e (float): Input parameter `e`.
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        psi (float): Input parameter `psi`.
        r (float): Input parameter `r`.
        s (float): Input parameter `s`.
        tau (float): Input parameter `tau`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(-a*e*math.sin(e*psi)*math.sin(psi*r**2) + b*math.sin(2*e*i*m*n*psi**2*r*s)*math.cos(e*psi) + g*math.sin(e*psi)*math.sin(psi*r)*math.cos(55*a*b*e*theta) + tau*math.cos(a*e**2*m*psi))


def expr_e_psi_form_d(a: str = "a", b: str = "b", e: str = "e", g: str = "g", i: str = "i", m: str = "m", n: str = "n", psi: str = "psi", r: str = "r", s: str = "s", tau: str = "tau", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_psi_form_d`."""
    return (-pl.col(a)*pl.col(e)*math.sin(pl.col(e)*pl.col(psi))*math.sin(pl.col(psi)*pl.col(r)**2) + pl.col(b)*math.sin(2*pl.col(e)*pl.col(i)*pl.col(m)*pl.col(n)*pl.col(psi)**2*pl.col(r)*pl.col(s))*math.cos(pl.col(e)*pl.col(psi)) + pl.col(g)*math.sin(pl.col(e)*pl.col(psi))*math.sin(pl.col(psi)*pl.col(r))*math.cos(55*pl.col(a)*pl.col(b)*pl.col(e)*pl.col(theta)) + pl.col(tau)*math.cos(pl.col(a)*pl.col(e)**2*pl.col(m)*pl.col(psi)))


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


def expr_eq_a_p_b_p_form_e(p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_eq_a_p_b_p_form_e`."""
    return (pl.col(p))


def calc_theta_form_e(a: float, c: float, e: float, psi: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    \theta  = ae \sin\psi e r (55c)
    $$

    Args:
        a (float): Input parameter `a`.
        c (float): Input parameter `c`.
        e (float): Input parameter `e`.
        psi (float): Input parameter `psi`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*e*math.sin(55*c*e*psi*r))


def expr_theta_form_e(a: str = "a", c: str = "c", e: str = "e", psi: str = "psi", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_theta_form_e`."""
    return (pl.col(a)*pl.col(e)*math.sin(55*pl.col(c)*pl.col(e)*pl.col(psi)*pl.col(r)))


def calc_dd_t_m_r_2_theta_form_e(g: float, m: float, r: float, tau: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    d dt (mr2  \theta ) = \tau  + mgr \sin \theta
    $$

    Args:
        g (float): Input parameter `g`.
        m (float): Input parameter `m`.
        r (float): Input parameter `r`.
        tau (float): Input parameter `tau`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(g*m*r*math.sin(theta) + tau)


def expr_dd_t_m_r_2_theta_form_e(g: str = "g", m: str = "m", r: str = "r", tau: str = "tau", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_dd_t_m_r_2_theta_form_e`."""
    return (pl.col(g)*pl.col(m)*pl.col(r)*math.sin(pl.col(theta)) + pl.col(tau))


def calc_delta_glickm(m: float, v: float) -> float:
    r"""Compute mathematical metric extracted from glickman_2022_glicko2_example.

    **Source**:
    - Title: glicko2
    - Authors: Scientific Literature
    - Citation Key: `glickman_2022_glicko2_example`

    **KaTeX Formula**:
    $$
    \Delta  = v m\sum  j=1 g(\phi j ){sj - E(\mu , \mu j , \phi j )}
    $$

    Args:
        m (float): Input parameter `m`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(m*v)


def expr_delta_glickm(m: str = "m", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_glickm`."""
    return (pl.col(m)*pl.col(v))


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
    return float(R*(2*A) + R*(S*(2*(R*(2*S)))))


def expr_val_1406_3402_1406_3(A: str = "A", R: str = "R", S: str = "S") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1406_3402_1406_3`."""
    return (pl.col(R)*(2*pl.col(A)) + pl.col(R)*(pl.col(S)*(2*(pl.col(R)*(2*pl.col(S))))))


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
    return float(f*s)


def expr_f_s_form_0(f: str = "f", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_s_form_0`."""
    return (pl.col(f)*pl.col(s))


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
    return float(-a*b + 2)


def expr_t_a_b_form_0(a: str = "a", b: str = "b") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_a_b_form_0`."""
    return (-pl.col(a)*pl.col(b) + 2)


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


def expr_t_x_x_form_2(c: str = "c") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_x_x_form_2`."""
    return (pl.col(c))


def calc_p_g_i_form_3(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_25525.

    **Source**:
    - Title: When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review (2026)
    - Authors: Kichang Lee, Gyeongmin Han, Sungmin Lee et al.
    - Citation Key: `arxiv_2609_25525`

    **KaTeX Formula**:
    $$
    p G i = P(overturni = 1 | geometry)
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_p_g_i_form_3(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_g_i_form_3`."""
    return (pl.col(P))


def calc_r_l_i_i_form_3(delta: float, i: float, mu: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_06635.

    **Source**:
    - Title: Modelling Athletic Ageing Relative to an Estimated Performance Envelope (2026)
    - Authors: Dae-Jin Lee
    - Citation Key: `arxiv_2608_06635`

    **KaTeX Formula**:
    $$
    RLIi = 100 \cdot  \exp(\delta i - \mu \delta )
    $$

    Args:
        delta (float): Input parameter `delta`.
        i (float): Input parameter `i`.
        mu (float): Input parameter `mu`.

    Returns:
        float: Calculated metric value.
    """
    return float(100*math.exp(delta*i - delta*mu))


def expr_r_l_i_i_form_3(delta: str = "delta", i: str = "i", mu: str = "mu") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_l_i_i_form_3`."""
    return (100*(pl.col(delta).exp()*pl.col(i) - pl.col(delta)*pl.col(mu)))


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


def expr_p_t_form_4(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_t_form_4`."""
    return (pl.col(P))


def calc_val_2603_08746_form_4(f: float, mu: float, nabla: float, p: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_08746.

    **Source**:
    - Title: Kinematics of Single-Winged Spinning Seeds: A Study on Mahogany and Buddha Coconut Samaras (2026)
    - Authors: Yogeshwaran G, Srisha M. V. Rao, Jagadeesh G
    - Citation Key: `arxiv_2603_08746`

    **KaTeX Formula**:
    $$
    \rho  ( \partial u \partial t + u \cdot  \nabla u) = -\nabla p + \mu \nabla 2u +  f
    $$

    Args:
        f (float): Input parameter `f`.
        mu (float): Input parameter `mu`.
        nabla (float): Input parameter `nabla`.
        p (float): Input parameter `p`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(f + 2*mu*nabla*u - nabla*p)


def expr_val_2603_08746_form_4(f: str = "f", mu: str = "mu", nabla: str = "nabla", p: str = "p", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2603_08746_form_4`."""
    return (pl.col(f) + 2*pl.col(mu)*pl.col(nabla)*pl.col(u) - pl.col(nabla)*pl.col(p))


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


def expr_p_0_x_form_5(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_0_x_form_5`."""
    return (pl.col(P))


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
    return float(a*b)


def expr_t_a_b_form_6(a: str = "a", b: str = "b") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_a_b_form_6`."""
    return (pl.col(a)*pl.col(b))


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


def expr_p_w_t_form_9(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_w_t_form_9`."""
    return (pl.col(P))


def calc_xi_e_form_a(de: float, e: float, omega: float, psi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    \Xi e = \psi d e - \pi  2\omega e(a* ) (25a) \Xi \theta  = \pi  2\omega \theta (a* ) - \pi  2\omega e(a* ) - \pi  2\omega \theta (a* ) = - \pi  2\omega e(a* ) . (25b)
    $$

    Args:
        de (float): Input parameter `de`.
        e (float): Input parameter `e`.
        omega (float): Input parameter `omega`.
        psi (float): Input parameter `psi`.

    Returns:
        float: Calculated metric value.
    """
    return float(de*psi - 2*math.pi*e*omega)


def expr_xi_e_form_a(de: str = "de", e: str = "e", omega: str = "omega", psi: str = "psi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_xi_e_form_a`."""
    return (pl.col(de)*pl.col(psi) - 2*math.pi*pl.col(e)*pl.col(omega))


def calc_c_t_form_b(c: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27416.

    **Source**:
    - Title: Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization (2026)
    - Authors: Koichi Miyamoto
    - Citation Key: `arxiv_2610_27416`

    **KaTeX Formula**:
    $$
    c(t) =  c1 ... cN  :=  0N vec( B(t) BT (t)) 0N-N-N 2
    $$

    Args:
        c (float): Input parameter `c`.

    Returns:
        float: Calculated metric value.
    """
    return float(c)


def expr_c_t_form_b(c: str = "c") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_t_form_b`."""
    return (pl.col(c))


def calc_omega_l_l_r_sim_j_l_c_form_e(J: float, L: float, M: float, R: float, c: float, omega: float, sim: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_08746.

    **Source**:
    - Title: Kinematics of Single-Winged Spinning Seeds: A Study on Mahogany and Buddha Coconut Samaras (2026)
    - Authors: Yogeshwaran G, Srisha M. V. Rao, Jagadeesh G
    - Citation Key: `arxiv_2603_08746`

    **KaTeX Formula**:
    $$
    \sim  J L c \cdot  \omega L LR = M L - \sim \omega L LR \cdot  \sim  J L c \cdot  \omega L LR
    $$

    Args:
        J (float): Input parameter `J`.
        L (float): Input parameter `L`.
        M (float): Input parameter `M`.
        R (float): Input parameter `R`.
        c (float): Input parameter `c`.
        omega (float): Input parameter `omega`.
        sim (float): Input parameter `sim`.

    Returns:
        float: Calculated metric value.
    """
    return float(-J*L**5*R**2*c*omega**2*sim**2 + L*M)


def expr_omega_l_l_r_sim_j_l_c_form_e(J: str = "J", L: str = "L", M: str = "M", R: str = "R", c: str = "c", omega: str = "omega", sim: str = "sim") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_omega_l_l_r_sim_j_l_c_form_e`."""
    return (-pl.col(J)*pl.col(L)**5*pl.col(R)**2*pl.col(c)*pl.col(omega)**2*pl.col(sim)**2 + pl.col(L)*pl.col(M))


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
    return float(880*c*h*i*p*t - 6912)


def expr_f_r_e_q_p_i_t_c_h_form_1(c: str = "c", h: str = "h", i: str = "i", p: str = "p", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_r_e_q_p_i_t_c_h_form_1`."""
    return (880*pl.col(c)*pl.col(h)*pl.col(i)*pl.col(p)*pl.col(t) - 6912)


def calc_o_n_e_t_h_i_r_df_o_m_r_form_1(C: float, F: float, P: float, a: float, e: float, i: float, m: float, n: float, o: float, r: float, s: float, t: float) -> float:
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
    return float(23*(C*(a*(r*(e*(e*(r*(P*(o*(i*(n*(s*t))))))))))) + 13*(F*(o*(m*r))))


def expr_o_n_e_t_h_i_r_df_o_m_r_form_1(C: str = "C", F: str = "F", P: str = "P", a: str = "a", e: str = "e", i: str = "i", m: str = "m", n: str = "n", o: str = "o", r: str = "r", s: str = "s", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_o_n_e_t_h_i_r_df_o_m_r_form_1`."""
    return (23*(pl.col(C)*(pl.col(a)*(pl.col(r)*(pl.col(e)*(pl.col(e)*(pl.col(r)*(pl.col(P)*(pl.col(o)*(pl.col(i)*(pl.col(n)*(pl.col(s)*pl.col(t)))))))))))) + 13*(pl.col(F)*(pl.col(o)*(pl.col(m)*pl.col(r)))))


def calc_r_form_5(P: float, a: float, c: float, i: float, l: float, m: float, o: float, p: float, t: float, u: float) -> float:
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
    return float(-math.e*P*a**2*c*l*t*u + math.e*P*a*i*l*m*o*p*t)


def expr_r_form_5(P: str = "P", a: str = "a", c: str = "c", i: str = "i", l: str = "l", m: str = "m", o: str = "o", p: str = "p", t: str = "t", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_form_5`."""
    return (-math.e*pl.col(P)*pl.col(a)**2*pl.col(c)*pl.col(l)*pl.col(t)*pl.col(u) + math.e*pl.col(P)*pl.col(a)*pl.col(i)*pl.col(l)*pl.col(m)*pl.col(o)*pl.col(p)*pl.col(t))


def calc_f_x_form_6(F: float, Y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_06635.

    **Source**:
    - Title: Modelling Athletic Ageing Relative to an Estimated Performance Envelope (2026)
    - Authors: Dae-Jin Lee
    - Citation Key: `arxiv_2608_06635`

    **KaTeX Formula**:
    $$
    f (x) = F -1 Y |x (\tau  ), \tau  \in  (0, 1)
    $$

    Args:
        F (float): Input parameter `F`.
        Y (float): Input parameter `Y`.

    Returns:
        float: Calculated metric value.
    """
    return float(F - Y)


def expr_f_x_form_6(F: str = "F", Y: str = "Y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_x_form_6`."""
    return (pl.col(F) - pl.col(Y))


def calc_k_form_6(B: float, p: float, rho: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2309_15318.

    **Source**:
    - Title: A Global 3-D Simulation of Magnetospheric Accretion: I. Magnetically Disrupted Disks and Surface Accretion (2023)
    - Authors: Zhaohuan Zhu, James M. Stone, Nuria Calvet
    - Citation Key: `arxiv_2309_15318`

    **KaTeX Formula**:
    $$
    k = \rho vp Bp
    $$

    Args:
        B (float): Input parameter `B`.
        p (float): Input parameter `p`.
        rho (float): Input parameter `rho`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float(B*p**2*rho*v)


def expr_k_form_6(B: str = "B", p: str = "p", rho: str = "rho", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_form_6`."""
    return (pl.col(B)*pl.col(p)**2*pl.col(rho)*pl.col(v))


def calc_e_pi_l_e_v_i_t_t_form_6(f: float, p: float, v: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_06739.

    **Source**:
    - Title: The profit-bias identity in sports betting: bookmaker profit as the public's prediction error (2026)
    - Authors: Jacek P. Dmochowski
    - Citation Key: `arxiv_2609_06739`

    **KaTeX Formula**:
    $$
    E[\pi Levitt] = (2 + v) (f + p - 2pf ) - 1
    $$

    Args:
        f (float): Input parameter `f`.
        p (float): Input parameter `p`.
        v (float): Input parameter `v`.

    Returns:
        float: Calculated metric value.
    """
    return float((v + 2)*(-2*f*p + f + p) - 1)


def expr_e_pi_l_e_v_i_t_t_form_6(f: str = "f", p: str = "p", v: str = "v") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_pi_l_e_v_i_t_t_form_6`."""
    return ((pl.col(v) + 2)*(-2*pl.col(f)*pl.col(p) + pl.col(f) + pl.col(p)) - 1)


def calc_d_k_p_l_p_form_8(D: float, K: float, k: float, l: float, pm: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_25621.

    **Source**:
    - Title: Dissonance Spectrum explicitly models perceptual frequency interactions for better music understanding (2026)
    - Authors: Tianle Wang, Xinyi Tong, Liangke Zhao et al.
    - Citation Key: `arxiv_2608_25621`

    **KaTeX Formula**:
    $$
    D(pl -pk) =  D\pm K+l-k-1
    $$

    Args:
        D (float): Input parameter `D`.
        K (float): Input parameter `K`.
        k (float): Input parameter `k`.
        l (float): Input parameter `l`.
        pm (float): Input parameter `pm`.

    Returns:
        float: Calculated metric value.
    """
    return float(D*K*pm - k + l - 1)


def expr_d_k_p_l_p_form_8(D: str = "D", K: str = "K", k: str = "k", l: str = "l", pm: str = "pm") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_k_p_l_p_form_8`."""
    return (pl.col(D)*pl.col(K)*pl.col(pm) - pl.col(k) + pl.col(l) - 1)


def calc_k_p_form_8(B: float, c: float, h: float, i: float, k: float, m: float, n: float, p: float, t: float) -> float:
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
    return float(12*B*k + c*h*i**2*m*n*p*t)


def expr_k_p_form_8(B: str = "B", c: str = "c", h: str = "h", i: str = "i", k: str = "k", m: str = "m", n: str = "n", p: str = "p", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_p_form_8`."""
    return (12*pl.col(B)*pl.col(k) + pl.col(c)*pl.col(h)*pl.col(i)**2*pl.col(m)*pl.col(n)*pl.col(p)*pl.col(t))


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
    return float(e - t*w*x + 11)


def expr_g_x_form_9(e: str = "e", t: str = "t", w: str = "w", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_x_form_9`."""
    return (pl.col(e) - pl.col(t)*pl.col(w)*pl.col(x) + 11)


def calc_phi_form_a(p: float, phi: float, q: float, r: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_06439.

    **Source**:
    - Title: Deep Reinforcement Learning based Control Design for Aircraft Recovery from Loss-of-Control Scenario (2026)
    - Authors: Imran Sayyed, Aayush Konar, Nandan Kumar Sinha
    - Citation Key: `arxiv_2601_06439`

    **KaTeX Formula**:
    $$
    \phi  = p + q \sin \phi  \tan \theta  + r \cos \phi  \tan \theta
    $$

    Args:
        p (float): Input parameter `p`.
        phi (float): Input parameter `phi`.
        q (float): Input parameter `q`.
        r (float): Input parameter `r`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(p + q*math.sin(phi)*math.tan(theta) + r*math.cos(phi)*math.tan(theta))


def expr_phi_form_a(p: str = "p", phi: str = "phi", q: str = "q", r: str = "r", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_phi_form_a`."""
    return (pl.col(p) + pl.col(q)*math.sin(pl.col(phi))*math.tan(pl.col(theta)) + pl.col(r)*math.cos(pl.col(phi))*math.tan(pl.col(theta)))


def calc_omega_l_l_r_form_a(p: float, q: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_08746.

    **Source**:
    - Title: Kinematics of Single-Winged Spinning Seeds: A Study on Mahogany and Buddha Coconut Samaras (2026)
    - Authors: Yogeshwaran G, Srisha M. V. Rao, Jagadeesh G
    - Citation Key: `arxiv_2603_08746`

    **KaTeX Formula**:
    $$
    \omega L LR = pqr  , \omega L LR =  p qr
    $$

    Args:
        p (float): Input parameter `p`.
        q (float): Input parameter `q`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(p*q*r)


def expr_omega_l_l_r_form_a(p: str = "p", q: str = "q", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_omega_l_l_r_form_a`."""
    return (pl.col(p)*pl.col(q)*pl.col(r))


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
    return float(-a*b + 2)


def expr_t_a_b_form_b(a: str = "a", b: str = "b") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_a_b_form_b`."""
    return (-pl.col(a)*pl.col(b) + 2)


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


def expr_k_p_form_c(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_p_form_c`."""
    return (pl.col(P))


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


def expr_t_a_b_form_d(a: str = "a", b: str = "b") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_a_b_form_d`."""
    return (pl.col(a) - pl.col(b))


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
    return float(f*t)


def expr_f_form_e(f: str = "f", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_form_e`."""
    return (pl.col(f)*pl.col(t))


def calc_y_i_x_form_e(a: float, alpha: float, b: float, delta: float, e: float, gamma: float, i: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_06635.

    **Source**:
    - Title: Modelling Athletic Ageing Relative to an Estimated Performance Envelope (2026)
    - Authors: Dae-Jin Lee
    - Citation Key: `arxiv_2608_06635`

    **KaTeX Formula**:
    $$
    yi(x) = (\alpha i + a - b\gamma ie-\delta i ) + be-\delta i x
    $$

    Args:
        a (float): Input parameter `a`.
        alpha (float): Input parameter `alpha`.
        b (float): Input parameter `b`.
        delta (float): Input parameter `delta`.
        e (float): Input parameter `e`.
        gamma (float): Input parameter `gamma`.
        i (float): Input parameter `i`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(-delta*i*x + (b*e + (-delta*i + (-b*gamma*(e*i) + (a + alpha*i)))))


def expr_y_i_x_form_e(a: str = "a", alpha: str = "alpha", b: str = "b", delta: str = "delta", e: str = "e", gamma: str = "gamma", i: str = "i", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_y_i_x_form_e`."""
    return (-pl.col(delta)*pl.col(i)*pl.col(x) + (pl.col(b)*pl.col(e) + (-pl.col(delta)*pl.col(i) + (-pl.col(b)*pl.col(gamma)*(pl.col(e)*pl.col(i)) + (pl.col(a) + pl.col(alpha)*pl.col(i))))))


def calc_sim_j_l_c_form_f(J: float, L: float, c: float, x: float, y: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_08746.

    **Source**:
    - Title: Kinematics of Single-Winged Spinning Seeds: A Study on Mahogany and Buddha Coconut Samaras (2026)
    - Authors: Yogeshwaran G, Srisha M. V. Rao, Jagadeesh G
    - Citation Key: `arxiv_2603_08746`

    **KaTeX Formula**:
    $$
    \sim  J L c = J L cxx J L cxy J L cxz J L cyx J L cyy J L cyz J L czx J L czy J L czz
    $$

    Args:
        J (float): Input parameter `J`.
        L (float): Input parameter `L`.
        c (float): Input parameter `c`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(J**9*L**9*c**9*x**6*y**6*z**6)


def expr_sim_j_l_c_form_f(J: str = "J", L: str = "L", c: str = "c", x: str = "x", y: str = "y", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sim_j_l_c_form_f`."""
    return (pl.col(J)**9*pl.col(L)**9*pl.col(c)**9*pl.col(x)**6*pl.col(y)**6*pl.col(z)**6)


def calc_delta_i_1312_7(B: float, alpha: float, epsilon: float, i: float) -> float:
    r"""Compute mathematical metric extracted from 1312_7158.

    **Source**:
    - Title: openWAR: An Open Source System for Evaluating Overall Player Performance in Major League Baseball (2013)
    - Authors: Benjamin S. Baumer, Shane T. Jensen, Gregory J. Matthews
    - Citation Key: `1312_7158`

    **KaTeX Formula**:
    $$
    \delta i = Bi \cdot  \alpha  + \epsilon i
    $$

    Args:
        B (float): Input parameter `B`.
        alpha (float): Input parameter `alpha`.
        epsilon (float): Input parameter `epsilon`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(B*alpha*i + epsilon*i)


def expr_delta_i_1312_7(B: str = "B", alpha: str = "alpha", epsilon: str = "epsilon", i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_i_1312_7`."""
    return (pl.col(B)*pl.col(alpha)*pl.col(i) + pl.col(epsilon)*pl.col(i))


def calc_r_a_a_b_r_i_j_1312_7(i: float, j: float, kappa: float) -> float:
    r"""Compute mathematical metric extracted from 1312_7158.

    **Source**:
    - Title: openWAR: An Open Source System for Evaluating Overall Player Performance in Major League Baseball (2013)
    - Authors: Benjamin S. Baumer, Shane T. Jensen, Gregory J. Matthews
    - Citation Key: `1312_7158`

    **KaTeX Formula**:
    $$
    RAAbr ij = \kappa ij \sum j \kappa ij \cdot   \eta i
    $$

    Args:
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.
        kappa (float): Input parameter `kappa`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*j*kappa)


def expr_r_a_a_b_r_i_j_1312_7(i: str = "i", j: str = "j", kappa: str = "kappa") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_a_a_b_r_i_j_1312_7`."""
    return (pl.col(i)*pl.col(j)*pl.col(kappa))


def calc_i_mu_1312_7(epsilon: float, eta: float, i: float) -> float:
    r"""Compute mathematical metric extracted from 1312_7158.

    **Source**:
    - Title: openWAR: An Open Source System for Evaluating Overall Player Performance in Major League Baseball (2013)
    - Authors: Benjamin S. Baumer, Shane T. Jensen, Gregory J. Matthews
    - Citation Key: `1312_7158`

    **KaTeX Formula**:
    $$
    \mu i =  \epsilon i -  \eta i
    $$

    Args:
        epsilon (float): Input parameter `epsilon`.
        eta (float): Input parameter `eta`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(epsilon*i - eta*i)


def expr_i_mu_1312_7(epsilon: str = "epsilon", eta: str = "eta", i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_mu_1312_7`."""
    return (pl.col(epsilon)*pl.col(i) - pl.col(eta)*pl.col(i))


def calc_j_sigma_1603_0(a: float, g: float, m: float, r: float, sigma: float, x: float) -> float:
    r"""Compute mathematical metric extracted from 1603_00050.

    **Source**:
    - Title: Learning, Visualizing, and Exploiting a Model for the Intrinsic Value of a Batted Ball (2016)
    - Authors: Glenn Healey
    - Citation Key: `1603_00050`

    **KaTeX Formula**:
    $$
    \sigma * j = argmax \sigma  \prod  xi\in Sj ̂ p(xi )
    $$

    Args:
        a (float): Input parameter `a`.
        g (float): Input parameter `g`.
        m (float): Input parameter `m`.
        r (float): Input parameter `r`.
        sigma (float): Input parameter `sigma`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(a**2*g*m*r*sigma*x)


def expr_j_sigma_1603_0(a: str = "a", g: str = "g", m: str = "m", r: str = "r", sigma: str = "sigma", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_sigma_1603_0`."""
    return (pl.col(a)**2*pl.col(g)*pl.col(m)*pl.col(r)*pl.col(sigma)*pl.col(x))


def calc_r_t_o_t_x_y_v_46e930(r: float) -> float:
    r"""Compute mathematical metric extracted from jensen2009.

    **Source**:
    - Title: Bayesball: A Bayesian Hierarchical Model for Evaluating Historic Baseball Players (2009)
    - Authors: Shane T. Jensen, Kenneth E. Shirley, Abraham J. Wyner
    - Citation Key: `jensen2009`

    **KaTeX Formula**:
    $$
    rtot (x, y, v) = 0.5 \cdot   r1(x, y, v) + 0.8 \cdot   r2(x, y, v) + 1.1 \cdot   r3(x, y, v)
    $$

    Args:
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(0.5*r)


def expr_r_t_o_t_x_y_v_46e930(r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_t_o_t_x_y_v_46e930`."""
    return (0.5*pl.col(r))


def calc_p_j_l_m_beyond(K: float, N: float, eta: float, j: float, p: float) -> float:
    r"""Compute mathematical metric extracted from beyond_runs_expectancy_jsm2014.

    **Source**:
    - Title: 311431_85069
    - Authors: Scientific Literature
    - Citation Key: `beyond_runs_expectancy_jsm2014`

    **KaTeX Formula**:
    $$
    pjML = Nj Nj + K  pj + K Nj + K  \eta
    $$

    Args:
        K (float): Input parameter `K`.
        N (float): Input parameter `N`.
        eta (float): Input parameter `eta`.
        j (float): Input parameter `j`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(K*eta + (K*(N*j) + (K*(j*p) + N*(j*(N*j)))))


def expr_p_j_l_m_beyond(K: str = "K", N: str = "N", eta: str = "eta", j: str = "j", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_j_l_m_beyond`."""
    return (pl.col(K)*pl.col(eta) + (pl.col(K)*(pl.col(N)*pl.col(j)) + (pl.col(K)*(pl.col(j)*pl.col(p)) + pl.col(N)*(pl.col(j)*(pl.col(N)*pl.col(j))))))


def calc_c_theta_beyond(c: float, p: float) -> float:
    r"""Compute mathematical metric extracted from beyond_runs_expectancy_jsm2014.

    **Source**:
    - Title: 311431_85069
    - Authors: Scientific Literature
    - Citation Key: `beyond_runs_expectancy_jsm2014`

    **KaTeX Formula**:
    $$
    \theta c = pc + ... + pk
    $$

    Args:
        c (float): Input parameter `c`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(c*p)


def expr_c_theta_beyond(c: str = "c", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_theta_beyond`."""
    return (pl.col(c)*pl.col(p))


def calc_v_di_r_form_1(a: float, i: float, m: float, n: float, u: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_36769.

    **Source**:
    - Title: Externalizing Hand Grip Pressure Through Real-Time Visual Feedback (2026)
    - Authors: Andrew L. Huard, Avinash Ajit Nargund, Misha Sra
    - Citation Key: `arxiv_2610_36769`

    **KaTeX Formula**:
    $$
    vdir = umax - umin
    $$

    Args:
        a (float): Input parameter `a`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        u (float): Input parameter `u`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*m*u*x - i*m*n*u)


def expr_v_di_r_form_1(a: str = "a", i: str = "i", m: str = "m", n: str = "n", u: str = "u", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_di_r_form_1`."""
    return (pl.col(a)*pl.col(m)*pl.col(u)*pl.col(x) - pl.col(i)*pl.col(m)*pl.col(n)*pl.col(u))


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
    return float(1.5*S)


def expr_c_l_form_3(S: str = "S") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_l_form_3`."""
    return (1.5*pl.col(S))


def calc_delta_a_d_a_d_s_form_3(A: float, C: float, D: float, Delta: float, m: float, s: float) -> float:
    r"""Compute mathematical metric extracted from openalex_meyer2008_w1992303757.

    **Source**:
    - Title: Influence of a humidor on the aerodynamics of baseballs (2008)
    - Authors: Edmund Meyer, John L. Bohn
    - Citation Key: `openalex_meyer2008_w1992303757`

    **KaTeX Formula**:
    $$
    \Delta aD asD = \Delta CD C sD + \Delta A As - \Delta m ms
    $$

    Args:
        A (float): Input parameter `A`.
        C (float): Input parameter `C`.
        D (float): Input parameter `D`.
        Delta (float): Input parameter `Delta`.
        m (float): Input parameter `m`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(A**2*Delta*s + C**2*D**2*Delta*s - Delta*m**2*s)


def expr_delta_a_d_a_d_s_form_3(A: str = "A", C: str = "C", D: str = "D", Delta: str = "Delta", m: str = "m", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_a_d_a_d_s_form_3`."""
    return (pl.col(A)**2*pl.col(Delta)*pl.col(s) + pl.col(C)**2*pl.col(D)**2*pl.col(Delta)*pl.col(s) - pl.col(Delta)*pl.col(m)**2*pl.col(s))


def calc_delta_a_l_a_l_s_form_3(A: float, C: float, Delta: float, L: float, m: float, s: float) -> float:
    r"""Compute mathematical metric extracted from openalex_meyer2008_w1992303757.

    **Source**:
    - Title: Influence of a humidor on the aerodynamics of baseballs (2008)
    - Authors: Edmund Meyer, John L. Bohn
    - Citation Key: `openalex_meyer2008_w1992303757`

    **KaTeX Formula**:
    $$
    \Delta aL asL = \Delta CL C sL + \Delta A As - \Delta m ms
    $$

    Args:
        A (float): Input parameter `A`.
        C (float): Input parameter `C`.
        Delta (float): Input parameter `Delta`.
        L (float): Input parameter `L`.
        m (float): Input parameter `m`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(A**2*Delta*s + C**2*Delta*L**2*s - Delta*m**2*s)


def expr_delta_a_l_a_l_s_form_3(A: str = "A", C: str = "C", Delta: str = "Delta", L: str = "L", m: str = "m", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_a_l_a_l_s_form_3`."""
    return (pl.col(A)**2*pl.col(Delta)*pl.col(s) + pl.col(C)**2*pl.col(Delta)*pl.col(L)**2*pl.col(s) - pl.col(Delta)*pl.col(m)**2*pl.col(s))


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
    return float(2*B*i*k + 2*P*j*k)


def expr_q_i_j_form_9(B: str = "B", P: str = "P", i: str = "i", j: str = "j", k: str = "k") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_i_j_form_9`."""
    return (2*pl.col(B)*pl.col(i)*pl.col(k) + 2*pl.col(P)*pl.col(j)*pl.col(k))


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
    return float(math.e*x)


def expr_c_l_form_b(x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_l_form_b`."""
    return (math.e*pl.col(x))


def calc_delta_s_form_c(b: float, h: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_06739.

    **Source**:
    - Title: The profit-bias identity in sports betting: bookmaker profit as the public's prediction error (2026)
    - Authors: Jacek P. Dmochowski
    - Citation Key: `arxiv_2609_06739`

    **KaTeX Formula**:
    $$
    \delta (s) = bh,L(s) - bh,W (s) = 0
    $$

    Args:
        b (float): Input parameter `b`.
        h (float): Input parameter `h`.

    Returns:
        float: Calculated metric value.
    """
    return float(b*h)


def expr_delta_s_form_c(b: str = "b", h: str = "h") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_s_form_c`."""
    return (pl.col(b)*pl.col(h))


def calc_p_o_i_form_c(P: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_25525.

    **Source**:
    - Title: When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review (2026)
    - Authors: Kichang Lee, Gyeongmin Han, Sungmin Lee et al.
    - Citation Key: `arxiv_2609_25525`

    **KaTeX Formula**:
    $$
    p O i = P(overturni = 1 | observable information)
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_p_o_i_form_c(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_o_i_form_c`."""
    return (pl.col(P))


def calc_z_form_c(V: float, gamma: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2601_06439.

    **Source**:
    - Title: Deep Reinforcement Learning based Control Design for Aircraft Recovery from Loss-of-Control Scenario (2026)
    - Authors: Imran Sayyed, Aayush Konar, Nandan Kumar Sinha
    - Citation Key: `arxiv_2601_06439`

    **KaTeX Formula**:
    $$
    Z = -V \sin\gamma
    $$

    Args:
        V (float): Input parameter `V`.
        gamma (float): Input parameter `gamma`.

    Returns:
        float: Calculated metric value.
    """
    return float(-V*math.sin(gamma))


def expr_z_form_c(V: str = "V", gamma: str = "gamma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_form_c`."""
    return (-pl.col(V)*math.sin(pl.col(gamma)))


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
    return float(2*g*l*o*p*q)


def expr_c_p_q_form_c(g: str = "g", l: str = "l", o: str = "o", p: str = "p", q: str = "q") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_p_q_form_c`."""
    return (2*pl.col(g)*pl.col(l)*pl.col(o)*pl.col(p)*pl.col(q))


def calc_y_form_c(V: float, X: float, epsilon: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_06739.

    **Source**:
    - Title: The profit-bias identity in sports betting: bookmaker profit as the public's prediction error (2026)
    - Authors: Jacek P. Dmochowski
    - Citation Key: `arxiv_2609_06739`

    **KaTeX Formula**:
    $$
    Y =X + \epsilon  +V, M = X + U
    $$

    Args:
        V (float): Input parameter `V`.
        X (float): Input parameter `X`.
        epsilon (float): Input parameter `epsilon`.

    Returns:
        float: Calculated metric value.
    """
    return float(V + X + epsilon)


def expr_y_form_c(V: str = "V", X: str = "X", epsilon: str = "epsilon") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_y_form_c`."""
    return (pl.col(V) + pl.col(X) + pl.col(epsilon))


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
    return float(m*(a*x))


def expr_x_l_o_form_d(a: str = "a", m: str = "m", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_l_o_form_d`."""
    return (pl.col(m)*(pl.col(a)*pl.col(x)))


def calc_delta_a_l_a_l_s_form_d(Delta: float, dd: float, m: float, s: float) -> float:
    r"""Compute mathematical metric extracted from openalex_meyer2008_w1992303757.

    **Source**:
    - Title: Influence of a humidor on the aerodynamics of baseballs (2008)
    - Authors: Edmund Meyer, John L. Bohn
    - Citation Key: `openalex_meyer2008_w1992303757`

    **KaTeX Formula**:
    $$
    \Delta aL asL = 3 \Delta d ds - \Delta m ms
    $$

    Args:
        Delta (float): Input parameter `Delta`.
        dd (float): Input parameter `dd`.
        m (float): Input parameter `m`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(3*Delta*dd*s - Delta*m**2*s)


def expr_delta_a_l_a_l_s_form_d(Delta: str = "Delta", dd: str = "dd", m: str = "m", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_a_l_a_l_s_form_d`."""
    return (3*pl.col(Delta)*pl.col(dd)*pl.col(s) - pl.col(Delta)*pl.col(m)**2*pl.col(s))


def calc_delta_o_w_n_s_form_d(C: float, n: float, o: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_25525.

    **Source**:
    - Title: When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review (2026)
    - Authors: Kichang Lee, Gyeongmin Han, Sungmin Lee et al.
    - Citation Key: `arxiv_2609_25525`

    **KaTeX Formula**:
    $$
    \Delta own(s) = Cown,s βd , \Delta targeted(s) = Cown,s -Coth,s βd
    $$

    Args:
        C (float): Input parameter `C`.
        n (float): Input parameter `n`.
        o (float): Input parameter `o`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(C*n*o*w)


def expr_delta_o_w_n_s_form_d(C: str = "C", n: str = "n", o: str = "o", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_o_w_n_s_form_d`."""
    return (pl.col(C)*pl.col(n)*pl.col(o)*pl.col(w))


def calc_t_w_o_t_h_i_r_df_o_m_r_form_e(C: float, F: float, P: float, a: float, e: float, i: float, m: float, n: float, o: float, r: float, s: float, t: float) -> float:
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
    return float(13*C*P*a*e**2*i*n*o*r**2*s*t + 23*F*m*o*r)


def expr_t_w_o_t_h_i_r_df_o_m_r_form_e(C: str = "C", F: str = "F", P: str = "P", a: str = "a", e: str = "e", i: str = "i", m: str = "m", n: str = "n", o: str = "o", r: str = "r", s: str = "s", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_w_o_t_h_i_r_df_o_m_r_form_e`."""
    return (13*pl.col(C)*pl.col(P)*pl.col(a)*pl.col(e)**2*pl.col(i)*pl.col(n)*pl.col(o)*pl.col(r)**2*pl.col(s)*pl.col(t) + 23*pl.col(F)*pl.col(m)*pl.col(o)*pl.col(r))


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
    return float(-1/40*i*s + (1/40)*j*s + 11)


def expr_p_r_i_w_i_n_s_o_v_e_j_r_form_f(i: str = "i", j: str = "j", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_r_i_w_i_n_s_o_v_e_j_r_form_f`."""
    return (-1/40*pl.col(i)*pl.col(s) + (1/40)*pl.col(j)*pl.col(s) + 11)


def calc_val_1003_0134_formul(Gamma: float) -> float:
    r"""Compute mathematical metric extracted from 1003_0134.

    **Source**:
    - Title: Detrending career statistics in professional baseball: Accounting for the steroids era and beyond (2010)
    - Authors: Alexander M. Petersen, Orion Penner, H. Eugene Stanley
    - Citation Key: `1003_0134`

    **KaTeX Formula**:
    $$
    f = \int  \infty  x* x-\alpha e-x/xc x1-\alpha  c \Gamma (1-\alpha ) dx = \Gamma [1-\alpha , x* xc ] \Gamma (1 -\alpha ) =Q[1-\alpha , x* xc ]
    $$

    Args:
        Gamma (float): Input parameter `Gamma`.

    Returns:
        float: Calculated metric value.
    """
    return float(Gamma)


def expr_val_1003_0134_formul(Gamma: str = "Gamma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1003_0134_formul`."""
    return (pl.col(Gamma))


def calc_l_o_g_i_t_p_i_l_1312_7(X: float, i: float, l: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from 1312_7158.

    **Source**:
    - Title: openWAR: An Open Source System for Evaluating Overall Player Performance in Major League Baseball (2013)
    - Authors: Benjamin S. Baumer, Shane T. Jensen, Gregory J. Matthews
    - Citation Key: `1312_7158`

    **KaTeX Formula**:
    $$
    logit(pil) =Xi \cdot  \theta l
    $$

    Args:
        X (float): Input parameter `X`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(X*i*l*theta)


def expr_l_o_g_i_t_p_i_l_1312_7(X: str = "X", i: str = "i", l: str = "l", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_o_g_i_t_p_i_l_1312_7`."""
    return (pl.col(X)*pl.col(i)*pl.col(l)*pl.col(theta))


def calc_s_i_l_1312_7(i: float, l: float, p: float) -> float:
    r"""Compute mathematical metric extracted from 1312_7158.

    **Source**:
    - Title: openWAR: An Open Source System for Evaluating Overall Player Performance in Major League Baseball (2013)
    - Authors: Benjamin S. Baumer, Shane T. Jensen, Gregory J. Matthews
    - Citation Key: `1312_7158`

    **KaTeX Formula**:
    $$
    sil =  pil \sum l  pil
    $$

    Args:
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*l*p)


def expr_s_i_l_1312_7(i: str = "i", l: str = "l", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_i_l_1312_7`."""
    return (pl.col(i)*pl.col(l)*pl.col(p))


def calc_delta_f_i_s_i_l_1312_7(D: float, i: float, l: float, phi: float, tau: float) -> float:
    r"""Compute mathematical metric extracted from 1312_7158.

    **Source**:
    - Title: openWAR: An Open Source System for Evaluating Overall Player Performance in Major League Baseball (2013)
    - Authors: Benjamin S. Baumer, Shane T. Jensen, Gregory J. Matthews
    - Citation Key: `1312_7158`

    **KaTeX Formula**:
    $$
    \delta f i \cdot   sil =Di \cdot  \phi  + \tau il
    $$

    Args:
        D (float): Input parameter `D`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        phi (float): Input parameter `phi`.
        tau (float): Input parameter `tau`.

    Returns:
        float: Calculated metric value.
    """
    return float(D*i*phi + i*l*tau)


def expr_delta_f_i_s_i_l_1312_7(D: str = "D", i: str = "i", l: str = "l", phi: str = "phi", tau: str = "tau") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_f_i_s_i_l_1312_7`."""
    return (pl.col(D)*pl.col(i)*pl.col(phi) + pl.col(i)*pl.col(l)*pl.col(tau))


def calc_delta_i_p_1312_7(B: float, i: float, psi: float, xi: float) -> float:
    r"""Compute mathematical metric extracted from 1312_7158.

    **Source**:
    - Title: openWAR: An Open Source System for Evaluating Overall Player Performance in Major League Baseball (2013)
    - Authors: Benjamin S. Baumer, Shane T. Jensen, Gregory J. Matthews
    - Citation Key: `1312_7158`

    **KaTeX Formula**:
    $$
    \delta p i = Bi \cdot  \psi  + \xi i
    $$

    Args:
        B (float): Input parameter `B`.
        i (float): Input parameter `i`.
        psi (float): Input parameter `psi`.
        xi (float): Input parameter `xi`.

    Returns:
        float: Calculated metric value.
    """
    return float(B*i*psi + i*xi)


def expr_delta_i_p_1312_7(B: str = "B", i: str = "i", psi: str = "psi", xi: str = "xi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_i_p_1312_7`."""
    return (pl.col(B)*pl.col(i)*pl.col(psi) + pl.col(i)*pl.col(xi))


def calc_p_x_1603_0(n: float) -> float:
    r"""Compute mathematical metric extracted from 1603_00050.

    **Source**:
    - Title: Learning, Visualizing, and Exploiting a Model for the Intrinsic Value of a Batted Ball (2016)
    - Authors: Glenn Healey
    - Citation Key: `1603_00050`

    **KaTeX Formula**:
    $$
    p(x) = 1n n\sum  i=1 K(x - xi)
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(n**2)


def expr_p_x_1603_0(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_x_1603_0`."""
    return (pl.col(n)**2)


def calc_k_x_1603_0(Sigma: float, T: float, d: float, x: float) -> float:
    r"""Compute mathematical metric extracted from 1603_00050.

    **Source**:
    - Title: Learning, Visualizing, and Exploiting a Model for the Intrinsic Value of a Batted Ball (2016)
    - Authors: Glenn Healey
    - Citation Key: `1603_00050`

    **KaTeX Formula**:
    $$
    K(x) = 1 (2\pi )d/2 |\Sigma |1/2 \exp [- 12 xT \Sigma -1x]
    $$

    Args:
        Sigma (float): Input parameter `Sigma`.
        T (float): Input parameter `T`.
        d (float): Input parameter `d`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float((1/2)*math.pi*d*math.exp(12*Sigma*T*x + x)/abs(Sigma))


def expr_k_x_1603_0(Sigma: str = "Sigma", T: str = "T", d: str = "d", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_x_1603_0`."""
    return ((1/2)*math.pi*pl.col(d)*(12*pl.col(Sigma).exp()*pl.col(T)*pl.col(x) + pl.col(x))/abs(pl.col(Sigma)))


def calc_partial_l_partial_sigma_1712_0(N: float, sigma: float) -> float:
    r"""Compute mathematical metric extracted from 1712_05879.

    **Source**:
    - Title: Hierarchical Bayesian Bradley-Terry for Applications in Major League Baseball (2017)
    - Authors: Gabriel C. Phelan, John T. Whelan
    - Citation Key: `1712_05879`

    **KaTeX Formula**:
    $$
    \partial l \partial \sigma  = \sigma -3 N\sum  i=1 \lambda 2i -N\sigma -1 and \partial l \partial \lambda i = \sum  j (Vij + nij e\lambda i e\lambda i + e\lambda j ) - \sigma -2\lambda i
    $$

    Args:
        N (float): Input parameter `N`.
        sigma (float): Input parameter `sigma`.

    Returns:
        float: Calculated metric value.
    """
    return float(-3*N + sigma)


def expr_partial_l_partial_sigma_1712_0(N: str = "N", sigma: str = "sigma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_partial_l_partial_sigma_1712_0`."""
    return (-3*pl.col(N) + pl.col(sigma))


def calc_e_r_r_o_r_b_a_y_e_s_1712_0(N: float) -> float:
    r"""Compute mathematical metric extracted from 1712_05879.

    **Source**:
    - Title: Hierarchical Bayesian Bradley-Terry for Applications in Major League Baseball (2017)
    - Authors: Gabriel C. Phelan, John T. Whelan
    - Citation Key: `1712_05879`

    **KaTeX Formula**:
    $$
    errorBayes = 1N N\sum  i=1 (errorBayes i ) errorMLE = 1N N\sum  i=1 (errorMLE i )
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*N))


def expr_e_r_r_o_r_b_a_y_e_s_1712_0(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_r_r_o_r_b_a_y_e_s_1712_0`."""
    return (1*(pl.col(N)*pl.col(N)))


def calc_m_i_n_l_i_m_1811_0(i: float, w: float) -> float:
    r"""Compute mathematical metric extracted from 1811_07259.

    **Source**:
    - Title: Modeling Baseball Outcomes as Higher-Order Markov Chains (2018)
    - Authors: Jun Hee Kim
    - Citation Key: `1811_07259`

    **KaTeX Formula**:
    $$
    min l m   i=1 wi
    $$

    Args:
        i (float): Input parameter `i`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*w)


def expr_m_i_n_l_i_m_1811_0(i: str = "i", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_i_n_l_i_m_1811_0`."""
    return (pl.col(i)*pl.col(w))


def calc_x_d_i_2004_0(L: float, i: float) -> float:
    r"""Compute mathematical metric extracted from 2004_08428.

    **Source**:
    - Title: Renormalizing individual performance metrics for cultural heritage management of sports records (2020)
    - Authors: Alexander M. Petersen, Orion Penner
    - Citation Key: `2004_08428`

    **KaTeX Formula**:
    $$
    XD i = Li\sum  s=1 xDi (s)
    $$

    Args:
        L (float): Input parameter `L`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(L*i)


def expr_x_d_i_2004_0(L: str = "L", i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_d_i_2004_0`."""
    return (pl.col(L)*pl.col(i))


def calc_f_h_y_2005_0(H: float, n: float) -> float:
    r"""Compute mathematical metric extracted from 2005_07742.

    **Source**:
    - Title: SEAM methodology for context-rich player matchup evaluations (2020)
    - Authors: Julia Wapner, David Dalpiaz, Daniel J. Eck
    - Citation Key: `2005_07742`

    **KaTeX Formula**:
    $$
    fH(y) = 1 n|H| n\sum  i=1 K (H-1 (yi -y)) , y \in  Y
    $$

    Args:
        H (float): Input parameter `H`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(n**2*abs(H))


def expr_f_h_y_2005_0(H: str = "H", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_h_y_2005_0`."""
    return (pl.col(n)**2*abs(pl.col(H)))


def calc_l_o_g_i_t_i_j_p_g_2103_1(Gamma: float, Sigma: float, T: float, i: float, j: float, mu: float) -> float:
    r"""Compute mathematical metric extracted from 2103_12094.

    **Source**:
    - Title: Modelling intransitivity in pairwise comparisons with application to baseball data (2021)
    - Authors: Jess Spearing, Jonathan Tawn, David Irons et al.
    - Citation Key: `2103_12094`

    **KaTeX Formula**:
    $$
    logit (p(G) ij ) = \mu Ti \Sigma \mu j + \mu Ti \Gamma \mu i - \mu Tj \Gamma \mu j
    $$

    Args:
        Gamma (float): Input parameter `Gamma`.
        Sigma (float): Input parameter `Sigma`.
        T (float): Input parameter `T`.
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.
        mu (float): Input parameter `mu`.

    Returns:
        float: Calculated metric value.
    """
    return float(Gamma*T*i**2*mu**2 - Gamma*T*j**2*mu**2 + Sigma*T*i*j*mu**2)


def expr_l_o_g_i_t_i_j_p_g_2103_1(Gamma: str = "Gamma", Sigma: str = "Sigma", T: str = "T", i: str = "i", j: str = "j", mu: str = "mu") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_o_g_i_t_i_j_p_g_2103_1`."""
    return (pl.col(Gamma)*pl.col(T)*pl.col(i)**2*pl.col(mu)**2 - pl.col(Gamma)*pl.col(T)*pl.col(j)**2*pl.col(mu)**2 + pl.col(Sigma)*pl.col(T)*pl.col(i)*pl.col(j)*pl.col(mu)**2)


def calc_x_gamma_sigma_formul(Q: float) -> float:
    r"""Compute mathematical metric extracted from 1003_0134.

    **Source**:
    - Title: Detrending career statistics in professional baseball: Accounting for the steroids era and beyond (2010)
    - Authors: Alexander M. Petersen, Orion Penner, H. Eugene Stanley
    - Citation Key: `1003_0134`

    **KaTeX Formula**:
    $$
    x* \sigma \Gamma  = Q-1 [1 - \alpha , f ] \sqrt 1 - \alpha
    $$

    Args:
        Q (float): Input parameter `Q`.

    Returns:
        float: Calculated metric value.
    """
    return float(Q - 1)


def expr_x_gamma_sigma_formul(Q: str = "Q") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_gamma_sigma_formul`."""
    return (pl.col(Q) - 1)


def calc_alpha_m_e_l_formul(z: float) -> float:
    r"""Compute mathematical metric extracted from 1003_0134.

    **Source**:
    - Title: Detrending career statistics in professional baseball: Accounting for the steroids era and beyond (2010)
    - Authors: Alexander M. Petersen, Orion Penner, H. Eugene Stanley
    - Citation Key: `1003_0134`

    **KaTeX Formula**:
    $$
    \alpha MLE = 1 - 3 - z + \sqrt (z - 3)2 + 24z 12z
    $$

    Args:
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(-z - 2)


def expr_alpha_m_e_l_formul(z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_alpha_m_e_l_formul`."""
    return (-pl.col(z) - 2)


def calc_r_t_o_t_x_y_v_formul(r: float) -> float:
    r"""Compute mathematical metric extracted from 0802_4317.

    **Source**:
    - Title: Bayesball: A Bayesian hierarchical model for evaluating fielding in major league baseball (2008)
    - Authors: Shane T. Jensen, Kenneth E. Shirley, Abraham J. Wyner
    - Citation Key: `0802_4317`

    **KaTeX Formula**:
    $$
    rtot (x, y, v) = 0.5 \cdot   r1(x, y, v) + 0.8 \cdot   r2(x, y, v) + 1.1 \cdot   r3(x, y, v)
    $$

    Args:
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(0.5*r)


def expr_r_t_o_t_x_y_v_formul(r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_t_o_t_x_y_v_formul`."""
    return (0.5*pl.col(r))


def calc_a_c_c_b_m_guo_20(B: float, m: float) -> float:
    r"""Compute mathematical metric extracted from guo_2017_calibration.

    **Source**:
    - Title: arxiv1706.04599
    - Authors: Scientific Literature
    - Citation Key: `guo_2017_calibration`

    **KaTeX Formula**:
    $$
    acc(Bm) = 1 |Bm| \sum  i\in Bm 1( yi = yi)
    $$

    Args:
        B (float): Input parameter `B`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(abs(B*m))


def expr_a_c_c_b_m_guo_20(B: str = "B", m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_c_c_b_m_guo_20`."""
    return (abs(pl.col(B)*pl.col(m)))


def calc_p_i_k_2103_1(i: float, k: float, r: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from 2103_12094.

    **Source**:
    - Title: Modelling intransitivity in pairwise comparisons with application to baseball data (2021)
    - Authors: Jess Spearing, Jonathan Tawn, David Irons et al.
    - Citation Key: `2103_12094`

    **KaTeX Formula**:
    $$
    pik = 1 1+ \exp[-(\theta ik + ri - rk)] , \forall i ̸= k \in  I
    $$

    Args:
        i (float): Input parameter `i`.
        k (float): Input parameter `k`.
        r (float): Input parameter `r`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.exp(-i*k*theta - i*r + k*r) + 11)


def expr_p_i_k_2103_1(i: str = "i", k: str = "k", r: str = "r", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_k_2103_1`."""
    return ((-pl.col(i).exp()*pl.col(k)*pl.col(theta) - pl.col(i)*pl.col(r) + pl.col(k)*pl.col(r)) + 11)


def calc_sim_f_y_t_2207_1(i: float, n: float) -> float:
    r"""Compute mathematical metric extracted from 2207_11332.

    **Source**:
    - Title: Comparing baseball players across eras via novel Full House Modeling (2022)
    - Authors: Shen Yan, Adrian Burgos, Christopher Kinson et al.
    - Citation Key: `2207_11332`

    **KaTeX Formula**:
    $$
    \sim  FY (t) = ni\sum  j=1  j -1 ni + t - \sim  Yi,(j) ni ( \sim  Yi,(j+1) - \sim  Yi,(j))  1 ( \sim  Yi,(j) \le  t < \sim  Yi,(j+1)) + 1 (t \ge  \sim  Yi,(ni+1))
    $$

    Args:
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*n)


def expr_sim_f_y_t_2207_1(i: str = "i", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sim_f_y_t_2207_1`."""
    return (pl.col(i)*pl.col(n))


def calc_sim_f_y_i_y_i_i_n_2207_1(Y: float, i: float) -> float:
    r"""Compute mathematical metric extracted from 2207_11332.

    **Source**:
    - Title: Comparing baseball players across eras via novel Full House Modeling (2022)
    - Authors: Shen Yan, Adrian Burgos, Christopher Kinson et al.
    - Citation Key: `2207_11332`

    **KaTeX Formula**:
    $$
    \sim  FYi (Yi,(ni) ) = ni - 1 ni + Yi,(ni) - \sim  Yi,(ni) ni (Yi,(ni) + Y ⋆⋆ i - \sim  Yi,(ni)) = 1- 1 ni + 1 ni ( Yi,(ni)-Yi,(ni-1) 2 Yi,(ni)-Yi,(ni-1) 2 + Y ⋆⋆ i )
    $$

    Args:
        Y (float): Input parameter `Y`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(Y*i)


def expr_sim_f_y_i_y_i_i_n_2207_1(Y: str = "Y", i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sim_f_y_i_y_i_i_n_2207_1`."""
    return (pl.col(Y)*pl.col(i))


def calc_delta_e_r_2208_0(R: float, a: float, b: float, e: float, f: float, o: float, r: float, t: float) -> float:
    r"""Compute mathematical metric extracted from 2208_03492.

    **Source**:
    - Title: Pitching strategy evaluation via stratified analysis using propensity score (2022)
    - Authors: Hiroshi Nakahara, Kazuya Takeda, Keisuke Fujii
    - Citation Key: `2208_03492`

    **KaTeX Formula**:
    $$
    \Delta RE = REaf ter - REbef ore
    $$

    Args:
        R (float): Input parameter `R`.
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
    return float(math.e*R*a*e*f*r*t - math.e*R*b*e**2*f*o*r)


def expr_delta_e_r_2208_0(R: str = "R", a: str = "a", b: str = "b", e: str = "e", f: str = "f", o: str = "o", r: str = "r", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_e_r_2208_0`."""
    return (math.e*pl.col(R)*pl.col(a)*pl.col(e)*pl.col(f)*pl.col(r)*pl.col(t) - math.e*pl.col(R)*pl.col(b)*pl.col(e)**2*pl.col(f)*pl.col(o)*pl.col(r))


def calc_x_p_2209_0(N: float, p: float) -> float:
    r"""Compute mathematical metric extracted from 2209_07274.

    **Source**:
    - Title: Introducing Grid WAR: Rethinking WAR for Starting Pitchers (2022)
    - Authors: Ryan S. Brill, Abraham J. Wyner
    - Citation Key: `2209_07274`

    **KaTeX Formula**:
    $$
    Xp = Np\sum  g=1 Xpg
    $$

    Args:
        N (float): Input parameter `N`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(N*p)


def expr_x_p_2209_0(N: str = "N", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_p_2209_0`."""
    return (pl.col(N)*pl.col(p))


def calc_q_2210_0(m: float) -> float:
    r"""Compute mathematical metric extracted from 2210_02383.

    **Source**:
    - Title: Filling the Gaps: A Multiple Imputation Approach to Estimating Aging Curves in Baseball (2022)
    - Authors: Quang Nguyen, Gregory J. Matthews
    - Citation Key: `2210_02383`

    **KaTeX Formula**:
    $$
    Q = 1m m\sum  i=1 ̂Qi
    $$

    Args:
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(m*m))


def expr_q_2210_0(m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_2210_0`."""
    return (1*(pl.col(m)*pl.col(m)))


def calc_u_2210_0(m: float) -> float:
    r"""Compute mathematical metric extracted from 2210_02383.

    **Source**:
    - Title: Filling the Gaps: A Multiple Imputation Approach to Estimating Aging Curves in Baseball (2022)
    - Authors: Quang Nguyen, Gregory J. Matthews
    - Citation Key: `2210_02383`

    **KaTeX Formula**:
    $$
    U = 1m m\sum  i=1 ̂Ui
    $$

    Args:
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(m**2)


def expr_u_2210_0(m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_2210_0`."""
    return (pl.col(m)**2)


def calc_x_w_o_b_a_t_x_2210_0(K: float) -> float:
    r"""Compute mathematical metric extracted from 2210_06724.

    **Source**:
    - Title: A Bayesian analysis of the time through the order penalty in baseball (2022)
    - Authors: Ryan S. Brill, Sameer K. Deshpande, Abraham J. Wyner
    - Citation Key: `2210_06724`

    **KaTeX Formula**:
    $$
    xwOBA(t, x) = K\sum  k=1 1000 \cdot  wk \cdot  P(y = k|t, x)
    $$

    Args:
        K (float): Input parameter `K`.

    Returns:
        float: Calculated metric value.
    """
    return float(K)


def expr_x_w_o_b_a_t_x_2210_0(K: str = "K") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_w_o_b_a_t_x_2210_0`."""
    return (pl.col(K))


def calc_theta_b_j_2210_0(tau: float) -> float:
    r"""Compute mathematical metric extracted from 2210_06724.

    **Source**:
    - Title: A Bayesian analysis of the time through the order penalty in baseball (2022)
    - Authors: Ryan S. Brill, Sameer K. Deshpande, Abraham J. Wyner
    - Citation Key: `2210_06724`

    **KaTeX Formula**:
    $$
    \theta bj = \tau  -2 \sum ji=1 xbi + \nu  -2\theta b0 j\tau  -2 + \nu  -2
    $$

    Args:
        tau (float): Input parameter `tau`.

    Returns:
        float: Calculated metric value.
    """
    return float(tau - 2)


def expr_theta_b_j_2210_0(tau: str = "tau") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_theta_b_j_2210_0`."""
    return (pl.col(tau) - 2)


def calc_f_x_y_2310_0(gamma: float, x: float, y: float) -> float:
    r"""Compute mathematical metric extracted from 2310_01184.

    **Source**:
    - Title: Applications of Improvements to the Pythagorean Won-Loss Expectation in Optimizing Rosters (2023)
    - Authors: Alexander F. Almeida, Kevin Dayaratna, Steven J. Miller et al.
    - Citation Key: `2310_01184`

    **KaTeX Formula**:
    $$
    f(x, y) = x\gamma  x\gamma  + y\gamma
    $$

    Args:
        gamma (float): Input parameter `gamma`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(gamma*y + x*(gamma*(gamma*x)))


def expr_f_x_y_2310_0(gamma: str = "gamma", x: str = "x", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_x_y_2310_0`."""
    return (pl.col(gamma)*pl.col(y) + pl.col(x)*(pl.col(gamma)*(pl.col(gamma)*pl.col(x))))


def calc_theta_2402_0(T: float, U: float, V: float) -> float:
    r"""Compute mathematical metric extracted from 2402_01914.

    **Source**:
    - Title: Predicting Batting Averages in Specific Matchups Using Generalized Linked Matrix Factorization (2024)
    - Authors: Michael J. O'Connell
    - Citation Key: `2402_01914`

    **KaTeX Formula**:
    $$
    \Theta  = UV T
    $$

    Args:
        T (float): Input parameter `T`.
        U (float): Input parameter `U`.
        V (float): Input parameter `V`.

    Returns:
        float: Calculated metric value.
    """
    return float(T*U*V)


def expr_theta_2402_0(T: str = "T", U: str = "U", V: str = "V") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_theta_2402_0`."""
    return (pl.col(T)*pl.col(U)*pl.col(V))


def calc_a_k_2511_1(delta: float, h: float, k: float, m: float) -> float:
    r"""Compute mathematical metric extracted from 2511_19642.

    **Source**:
    - Title: A Win-Expectancy Framework for Contextualizing Runs Batted In: Introducing ARBI and CRBI (2025)
    - Authors: Wuhuan Deng
    - Citation Key: `2511_19642`

    **KaTeX Formula**:
    $$
    ak = mk + mk+1 - 2\delta k h2k , bk = 3\delta k - 2mk - mk+1 hk
    $$

    Args:
        delta (float): Input parameter `delta`.
        h (float): Input parameter `h`.
        k (float): Input parameter `k`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(-4*delta*h*k**2 + 2*k*m + 1)


def expr_a_k_2511_1(delta: str = "delta", h: str = "h", k: str = "k", m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_k_2511_1`."""
    return (-4*pl.col(delta)*pl.col(h)*pl.col(k)**2 + 2*pl.col(k)*pl.col(m) + 1)


def calc_mu_p_a_x_2602_2(P: float) -> float:
    r"""Compute mathematical metric extracted from 2602_23233.

    **Source**:
    - Title: The Counterfactual Combine: A Causal Framework for Player Evaluation (2026)
    - Authors: Herbert P. Susmann, Antonio D'Alessandro
    - Citation Key: `2602_23233`

    **KaTeX Formula**:
    $$
    \mu P(a,X) = EP[Y | A = a,X] mP(X) = EP[Y | X] \pi P(a | X) = P(A = a | X)
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e*P)


def expr_mu_p_a_x_2602_2(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_mu_p_a_x_2602_2`."""
    return (math.e*pl.col(P))


def calc_psi_p_2602_2(P: float) -> float:
    r"""Compute mathematical metric extracted from 2602_23233.

    **Source**:
    - Title: The Counterfactual Combine: A Causal Framework for Player Evaluation (2026)
    - Authors: Herbert P. Susmann, Antonio D'Alessandro
    - Citation Key: `2602_23233`

    **KaTeX Formula**:
    $$
    \psi (P) = EP [ \sum  a'\in A EP [Y | A = a' ,X] P(A* = a' | X) | X \in  X ' ,A \in  A']
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e*P)


def expr_psi_p_2602_2(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_psi_p_2602_2`."""
    return (math.e*pl.col(P))


def calc_psi_r_a_da_n_2602_2(m: float) -> float:
    r"""Compute mathematical metric extracted from 2602_23233.

    **Source**:
    - Title: The Counterfactual Combine: A Causal Framework for Player Evaluation (2026)
    - Authors: Herbert P. Susmann, Antonio D'Alessandro
    - Citation Key: `2602_23233`

    **KaTeX Formula**:
    $$
    \psi rand a = 1m m\sum  a'=1 E [E[Y | A = a' ,X] | A = a,X \in  X ' ] = 1m m\sum  a'=1 E [\mu P(a' ,X) | A = a,X \in  X ' ]
    $$

    Args:
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(m**2)


def expr_psi_r_a_da_n_2602_2(m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_psi_r_a_da_n_2602_2`."""
    return (pl.col(m)**2)


def calc_psi_r_a_da_n_psi_r_a_da_n_2602_2(P: float, o: float) -> float:
    r"""Compute mathematical metric extracted from 2602_23233.

    **Source**:
    - Title: The Counterfactual Combine: A Causal Framework for Player Evaluation (2026)
    - Authors: Herbert P. Susmann, Antonio D'Alessandro
    - Citation Key: `2602_23233`

    **KaTeX Formula**:
    $$
    \psi rand a -\psi rand a = oP
    $$

    Args:
        P (float): Input parameter `P`.
        o (float): Input parameter `o`.

    Returns:
        float: Calculated metric value.
    """
    return float(P*o)


def expr_psi_r_a_da_n_psi_r_a_da_n_2602_2(P: str = "P", o: str = "o") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_psi_r_a_da_n_psi_r_a_da_n_2602_2`."""
    return (pl.col(P)*pl.col(o))


def calc_eq_y_d_p_1_n_p_dsum_i_p_i_2603_2(p: float) -> float:
    r"""Compute mathematical metric extracted from 2603_21163.

    **Source**:
    - Title: Simultaneous Estimation of Ballpark Effects and Team Defense Using Total Bases Residuals (2026)
    - Authors: Jhe-Jia Wu, Tian-Li Yan, Ting-Li Chen
    - Citation Key: `2603_21163`

    **KaTeX Formula**:
    $$
    ypd = 1 npd \sum  i: p(i)=p, d(i)=d Ri
    $$

    Args:
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(p)


def expr_eq_y_d_p_1_n_p_dsum_i_p_i_2603_2(p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_eq_y_d_p_1_n_p_dsum_i_p_i_2603_2`."""
    return (pl.col(p))


def calc_y_d_p_2603_2(a: float, beta: float, d: float, de: float, epsilon: float, f: float, k: float, p: float, r: float) -> float:
    r"""Compute mathematical metric extracted from 2603_21163.

    **Source**:
    - Title: Simultaneous Estimation of Ballpark Effects and Team Defense Using Total Bases Residuals (2026)
    - Authors: Jhe-Jia Wu, Tian-Li Yan, Ting-Li Chen
    - Citation Key: `2603_21163`

    **KaTeX Formula**:
    $$
    ypd = \beta 0 + \beta park p -\beta def d + \epsilon pd
    $$

    Args:
        a (float): Input parameter `a`.
        beta (float): Input parameter `beta`.
        d (float): Input parameter `d`.
        de (float): Input parameter `de`.
        epsilon (float): Input parameter `epsilon`.
        f (float): Input parameter `f`.
        k (float): Input parameter `k`.
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(epsilon*(d*p) + (-beta*de*(d*f) + (beta*(p*(a*(r*(k*p)))) + 0*beta)))


def expr_y_d_p_2603_2(a: str = "a", beta: str = "beta", d: str = "d", de: str = "de", epsilon: str = "epsilon", f: str = "f", k: str = "k", p: str = "p", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_y_d_p_2603_2`."""
    return (pl.col(epsilon)*(pl.col(d)*pl.col(p)) + (-pl.col(beta)*pl.col(de)*(pl.col(d)*pl.col(f)) + (pl.col(beta)*(pl.col(p)*(pl.col(a)*(pl.col(r)*(pl.col(k)*pl.col(p))))) + 0*pl.col(beta))))


def calc_h_x_beyond(x: float) -> float:
    r"""Compute mathematical metric extracted from beyond_runs_expectancy_jsm2014.

    **Source**:
    - Title: 311431_85069
    - Authors: Scientific Literature
    - Citation Key: `beyond_runs_expectancy_jsm2014`

    **KaTeX Formula**:
    $$
    h(x) = x+6 \sum  x+3 f (N )g(x|N )
    $$

    Args:
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(x + 6)


def expr_h_x_beyond(x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_x_beyond`."""
    return (pl.col(x) + 6)


def calc_theta_i_j_beyond(j: float, y: float) -> float:
    r"""Compute mathematical metric extracted from beyond_runs_expectancy_jsm2014.

    **Source**:
    - Title: 311431_85069
    - Authors: Scientific Literature
    - Citation Key: `beyond_runs_expectancy_jsm2014`

    **KaTeX Formula**:
    $$
    \theta I j = yj, j = 1, ...,N
    $$

    Args:
        j (float): Input parameter `j`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(j*y)


def expr_theta_i_j_beyond(j: str = "j", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_theta_i_j_beyond`."""
    return (pl.col(j)*pl.col(y))


def calc_theta_m_l_j_beyond(j: float, mu: float, sigma: float, tau: float, y: float) -> float:
    r"""Compute mathematical metric extracted from beyond_runs_expectancy_jsm2014.

    **Source**:
    - Title: 311431_85069
    - Authors: Scientific Literature
    - Citation Key: `beyond_runs_expectancy_jsm2014`

    **KaTeX Formula**:
    $$
    \theta ML j = 1/\sigma 2 j 1/\sigma 2 j + 1/ \tau  2 yj + 1/ \tau  2 1/\sigma 2 j + 1/ \tau  2 \mu
    $$

    Args:
        j (float): Input parameter `j`.
        mu (float): Input parameter `mu`.
        sigma (float): Input parameter `sigma`.
        tau (float): Input parameter `tau`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float((1/2)/(mu*tau) + (1/2)/(j*tau*y) + (1/42)/(j*sigma*tau) + (1/4)/(j**2*sigma**2))


def expr_theta_m_l_j_beyond(j: str = "j", mu: str = "mu", sigma: str = "sigma", tau: str = "tau", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_theta_m_l_j_beyond`."""
    return ((1/2)/(pl.col(mu)*pl.col(tau)) + (1/2)/(pl.col(j)*pl.col(tau)*pl.col(y)) + (1/42)/(pl.col(j)*pl.col(sigma)*pl.col(tau)) + (1/4)/(pl.col(j)**2*pl.col(sigma)**2))


def calc_c_theta_theta_c_1_beyond(beta: float, c: float, gamma: float, x: float) -> float:
    r"""Compute mathematical metric extracted from beyond_runs_expectancy_jsm2014.

    **Source**:
    - Title: 311431_85069
    - Authors: Scientific Literature
    - Citation Key: `beyond_runs_expectancy_jsm2014`

    **KaTeX Formula**:
    $$
    \theta c 1 - \theta c = \exp (\gamma c + x\beta )
    $$

    Args:
        beta (float): Input parameter `beta`.
        c (float): Input parameter `c`.
        gamma (float): Input parameter `gamma`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.exp(beta*x + c*gamma))


def expr_c_theta_theta_c_1_beyond(beta: str = "beta", c: str = "c", gamma: str = "gamma", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_theta_theta_c_1_beyond`."""
    return ((pl.col(beta).exp()*pl.col(x) + pl.col(c)*pl.col(gamma)))


def calc_beta_m_l_j_beyond(beta: float, j: float, mu: float, sigma: float, tau: float) -> float:
    r"""Compute mathematical metric extracted from beyond_runs_expectancy_jsm2014.

    **Source**:
    - Title: 311431_85069
    - Authors: Scientific Literature
    - Citation Key: `beyond_runs_expectancy_jsm2014`

    **KaTeX Formula**:
    $$
    \beta ML j = 1/\sigma 2 j 1/\sigma 2 j + 1/ \tau  2  \beta j + 1/ \tau  2 1/\sigma 2 j + 1/ \tau  2 \mu
    $$

    Args:
        beta (float): Input parameter `beta`.
        j (float): Input parameter `j`.
        mu (float): Input parameter `mu`.
        sigma (float): Input parameter `sigma`.
        tau (float): Input parameter `tau`.

    Returns:
        float: Calculated metric value.
    """
    return float(((1/((21*tau)))/(((2*j)*sigma)) + (1/((tau*(2*(beta*j)))) + (1/((sigma*(2*(1*j)))))/(((2*j)*sigma)))) + 1/(((2*mu)*tau)))


def expr_beta_m_l_j_beyond(beta: str = "beta", j: str = "j", mu: str = "mu", sigma: str = "sigma", tau: str = "tau") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_beta_m_l_j_beyond`."""
    return (((1/((21*pl.col(tau))))/(((2*pl.col(j))*pl.col(sigma))) + (1/((pl.col(tau)*(2*(pl.col(beta)*pl.col(j))))) + (1/((pl.col(sigma)*(2*(1*pl.col(j))))))/(((2*pl.col(j))*pl.col(sigma))))) + 1/(((2*pl.col(mu))*pl.col(tau))))


def calc_beyond_runs_expectancy_jsm2014_beyond(beta: float) -> float:
    r"""Compute mathematical metric extracted from beyond_runs_expectancy_jsm2014.

    **Source**:
    - Title: 311431_85069
    - Authors: Scientific Literature
    - Citation Key: `beyond_runs_expectancy_jsm2014`

    **KaTeX Formula**:
    $$
    \log ( \theta H c 1 - \theta H c ) - \log ( \theta A c 1 - \theta A c ) = \beta
    $$

    Args:
        beta (float): Input parameter `beta`.

    Returns:
        float: Calculated metric value.
    """
    return float(beta)


def expr_beyond_runs_expectancy_jsm2014_beyond(beta: str = "beta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_beyond_runs_expectancy_jsm2014_beyond`."""
    return (pl.col(beta))


def calc_delta_0_x_1_i_brown_(X: float, i: float) -> float:
    r"""Compute mathematical metric extracted from brown_2008_aoas.

    **Source**:
    - Title: Supplement to 'In-season prediction of batting averages...': Major league batting records for 2005 (2008)
    - Authors: Brown, L. D.
    - Citation Key: `brown_2008_aoas`

    **KaTeX Formula**:
    $$
    \delta 0(X1i ) = X1i
    $$

    Args:
        X (float): Input parameter `X`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(X*i)


def expr_delta_0_x_1_i_brown_(X: str = "X", i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_0_x_1_i_brown_`."""
    return (pl.col(X)*pl.col(i))


def calc_z_i_brown_(X: float, i: float) -> float:
    r"""Compute mathematical metric extracted from brown_2008_aoas.

    **Source**:
    - Title: Supplement to 'In-season prediction of batting averages...': Major league batting records for 2005 (2008)
    - Authors: Brown, L. D.
    - Citation Key: `brown_2008_aoas`

    **KaTeX Formula**:
    $$
    Zi = X1i -X2i \sqrt 1/4N1i + 1/4N2i
    $$

    Args:
        X (float): Input parameter `X`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(-X*i)


def expr_z_i_brown_(X: str = "X", i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_i_brown_`."""
    return (-pl.col(X)*pl.col(i))


def calc_p_s_i_bt_sec(i: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    pS(i) = \pi i \sum k\in S \pi k
    $$

    Args:
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.pi*i)


def expr_p_s_i_bt_sec(i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_s_i_bt_sec`."""
    return (math.pi*pl.col(i))


def calc_p_i_j_p_i_j_bt_sec(a: float, f: float, i: float, j: float, l: float, o: float, r: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    pij pji = \pi i \pi j for all i, j
    $$

    Args:
        a (float): Input parameter `a`.
        f (float): Input parameter `f`.
        i (float): Input parameter `i`.
        j (float): Input parameter `j`.
        l (float): Input parameter `l`.
        o (float): Input parameter `o`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.pi**2*a*f*i**2*j*l**2*o*r)


def expr_p_i_j_p_i_j_bt_sec(a: str = "a", f: str = "f", i: str = "i", j: str = "j", l: str = "l", o: str = "o", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_j_p_i_j_bt_sec`."""
    return (math.pi**2*pl.col(a)*pl.col(f)*pl.col(i)**2*pl.col(j)*pl.col(l)**2*pl.col(o)*pl.col(r))


def calc_f_i_x_bt_sec(e: float, i: float, x: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    Fi(x) = 1 - e- x \pi i , x\in R+
    $$

    Args:
        e (float): Input parameter `e`.
        i (float): Input parameter `i`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(-e - math.pi*i*x + 1)


def expr_f_i_x_bt_sec(e: str = "e", i: str = "i", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_i_x_bt_sec`."""
    return (-pl.col(e) - math.pi*pl.col(i)*pl.col(x) + 1)


def calc_mu_i_j_bt_sec(P: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    \mu ij = P(yij = 1) logit(\mu ij ; \delta i, \gamma j , fij ) = \delta i + \gamma j + fij
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_mu_i_j_bt_sec(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_mu_i_j_bt_sec`."""
    return (pl.col(P))


def calc_alpha_p_r_bt_sec(C: float, D: float, P: float, R: float, alpha: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    \alpha PR = CD-1\alpha PR
    $$

    Args:
        C (float): Input parameter `C`.
        D (float): Input parameter `D`.
        P (float): Input parameter `P`.
        R (float): Input parameter `R`.
        alpha (float): Input parameter `alpha`.

    Returns:
        float: Calculated metric value.
    """
    return float(C*D - P*R*alpha)


def expr_alpha_p_r_bt_sec(C: str = "C", D: str = "D", P: str = "P", R: str = "R", alpha: str = "alpha") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_alpha_p_r_bt_sec`."""
    return (pl.col(C)*pl.col(D) - pl.col(P)*pl.col(R)*pl.col(alpha))


def calc_i_p_form_9(Pi: float, i: float) -> float:
    r"""Compute mathematical metric extracted from strumbelj_2014_ijf.

    **Source**:
    - Title: Strumbelj_WorkingPaper2013
    - Authors: Scientific Literature
    - Citation Key: `strumbelj_2014_ijf`

    **KaTeX Formula**:
    $$
    pi = \pi i \Pi
    $$

    Args:
        Pi (float): Input parameter `Pi`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.pi*Pi*i)


def expr_i_p_form_9(Pi: str = "Pi", i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_p_form_9`."""
    return (math.pi*pl.col(Pi)*pl.col(i))


def calc_pi_form_c(n: float) -> float:
    r"""Compute mathematical metric extracted from strumbelj_2014_ijf.

    **Source**:
    - Title: Strumbelj_WorkingPaper2013
    - Authors: Scientific Literature
    - Citation Key: `strumbelj_2014_ijf`

    **KaTeX Formula**:
    $$
    \Pi  = n\sum  i=1 \pi i
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(n)


def expr_pi_form_c(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_pi_form_c`."""
    return (pl.col(n))


def calc_k_alpha_k_w_bt_sec(C: float, e: float, k: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    k\alpha WK = C k e
    $$

    Args:
        C (float): Input parameter `C`.
        e (float): Input parameter `e`.
        k (float): Input parameter `k`.

    Returns:
        float: Calculated metric value.
    """
    return float(C*e*k)


def expr_k_alpha_k_w_bt_sec(C: str = "C", e: str = "e", k: str = "k") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_alpha_k_w_bt_sec`."""
    return (pl.col(C)*pl.col(e)*pl.col(k))


def calc_alpha_k_w_bt_sec(i: float, k: float, l: float, m: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    \alpha WK = lim k\to \infty  ( C\rho  )k e
    $$

    Args:
        i (float): Input parameter `i`.
        k (float): Input parameter `k`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*k*l*m)


def expr_alpha_k_w_bt_sec(i: str = "i", k: str = "k", l: str = "l", m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_alpha_k_w_bt_sec`."""
    return (pl.col(i)*pl.col(k)*pl.col(l)*pl.col(m))


def calc_pi_bt_sec(i: float, k: float, l: float, m: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    \pi = lim k\to \infty   C k e
    $$

    Args:
        i (float): Input parameter `i`.
        k (float): Input parameter `k`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*k*l*m)


def expr_pi_bt_sec(i: str = "i", k: str = "k", l: str = "l", m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_pi_bt_sec`."""
    return (pl.col(i)*pl.col(k)*pl.col(l)*pl.col(m))


def calc_r_i_p_bt_sec(M: float, x: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    RPI =0.25x+0.5 Mx+0.25 M 2x
    $$

    Args:
        M (float): Input parameter `M`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(1.0*M*x + 0.25*x)


def expr_r_i_p_bt_sec(M: str = "M", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_i_p_bt_sec`."""
    return (1.0*pl.col(M)*pl.col(x) + 0.25*pl.col(x))


def calc_alpha_1_bt_sec(C: float, e: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    \alpha 1 =  Ce
    $$

    Args:
        C (float): Input parameter `C`.
        e (float): Input parameter `e`.

    Returns:
        float: Calculated metric value.
    """
    return float(C*e)


def expr_alpha_1_bt_sec(C: str = "C", e: str = "e") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_alpha_1_bt_sec`."""
    return (pl.col(C)*pl.col(e))


def calc_theta_bt_sec(X: float, a: float, beta: float) -> float:
    r"""Compute mathematical metric extracted from bt_secondary_many_routes_2023.

    **Source**:
    - Title: arxiv_2312.13619
    - Authors: Scientific Literature
    - Citation Key: `bt_secondary_many_routes_2023`

    **KaTeX Formula**:
    $$
    \theta  = a +X\beta
    $$

    Args:
        X (float): Input parameter `X`.
        a (float): Input parameter `a`.
        beta (float): Input parameter `beta`.

    Returns:
        float: Calculated metric value.
    """
    return float(X*beta + a)


def expr_theta_bt_sec(X: str = "X", a: str = "a", beta: str = "beta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_theta_bt_sec`."""
    return (pl.col(X)*pl.col(beta) + pl.col(a))


def calc_v_buchda(A: float, D: float, H: float) -> float:
    r"""Compute mathematical metric extracted from buchdahl_wisdom_of_the_crowd.

    **Source**:
    - Title: wisdom_of_the_crowd_updated
    - Authors: Scientific Literature
    - Citation Key: `buchdahl_wisdom_of_the_crowd`

    **KaTeX Formula**:
    $$
    V = 1H + 1D + 1A
    $$

    Args:
        A (float): Input parameter `A`.
        D (float): Input parameter `D`.
        H (float): Input parameter `H`.

    Returns:
        float: Calculated metric value.
    """
    return float(A + D + H)


def expr_v_buchda(A: str = "A", D: str = "D", H: str = "H") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_buchda`."""
    return (pl.col(A) + pl.col(D) + pl.col(H))


def calc_m_i_buchda(M: float, O: float, i: float, n: float) -> float:
    r"""Compute mathematical metric extracted from buchdahl_wisdom_of_the_crowd.

    **Source**:
    - Title: wisdom_of_the_crowd_updated
    - Authors: Scientific Literature
    - Citation Key: `buchdahl_wisdom_of_the_crowd`

    **KaTeX Formula**:
    $$
    Mi = MOi n
    $$

    Args:
        M (float): Input parameter `M`.
        O (float): Input parameter `O`.
        i (float): Input parameter `i`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(M*(O*(i*n)))


def expr_m_i_buchda(M: str = "M", O: str = "O", i: str = "i", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_i_buchda`."""
    return (pl.col(M)*(pl.col(O)*(pl.col(i)*pl.col(n))))


def calc_h_m_buchda(H: float, M: float, f: float) -> float:
    r"""Compute mathematical metric extracted from buchdahl_wisdom_of_the_crowd.

    **Source**:
    - Title: wisdom_of_the_crowd_updated
    - Authors: Scientific Literature
    - Citation Key: `buchdahl_wisdom_of_the_crowd`

    **KaTeX Formula**:
    $$
    MH = MHf 3
    $$

    Args:
        H (float): Input parameter `H`.
        M (float): Input parameter `M`.
        f (float): Input parameter `f`.

    Returns:
        float: Calculated metric value.
    """
    return float(3*H*M*f)


def expr_h_m_buchda(H: str = "H", M: str = "M", f: str = "f") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_m_buchda`."""
    return (3*pl.col(H)*pl.col(M)*pl.col(f))


def calc_d_m_buchda(D: float, M: float, f: float) -> float:
    r"""Compute mathematical metric extracted from buchdahl_wisdom_of_the_crowd.

    **Source**:
    - Title: wisdom_of_the_crowd_updated
    - Authors: Scientific Literature
    - Citation Key: `buchdahl_wisdom_of_the_crowd`

    **KaTeX Formula**:
    $$
    MD = MDf 3
    $$

    Args:
        D (float): Input parameter `D`.
        M (float): Input parameter `M`.
        f (float): Input parameter `f`.

    Returns:
        float: Calculated metric value.
    """
    return float(3*D*M*f)


def expr_d_m_buchda(D: str = "D", M: str = "M", f: str = "f") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_m_buchda`."""
    return (3*pl.col(D)*pl.col(M)*pl.col(f))


def calc_a_m_buchda(A: float, M: float, f: float) -> float:
    r"""Compute mathematical metric extracted from buchdahl_wisdom_of_the_crowd.

    **Source**:
    - Title: wisdom_of_the_crowd_updated
    - Authors: Scientific Literature
    - Citation Key: `buchdahl_wisdom_of_the_crowd`

    **KaTeX Formula**:
    $$
    MA = MAf 3
    $$

    Args:
        A (float): Input parameter `A`.
        M (float): Input parameter `M`.
        f (float): Input parameter `f`.

    Returns:
        float: Calculated metric value.
    """
    return float(3*A*M*f)


def expr_a_m_buchda(A: str = "A", M: str = "M", f: str = "f") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_m_buchda`."""
    return (3*pl.col(A)*pl.col(M)*pl.col(f))


def calc_x_buchda(c: float, p: float) -> float:
    r"""Compute mathematical metric extracted from buchdahl_wisdom_of_the_crowd.

    **Source**:
    - Title: wisdom_of_the_crowd_updated
    - Authors: Scientific Literature
    - Citation Key: `buchdahl_wisdom_of_the_crowd`

    **KaTeX Formula**:
    $$
    x = cp 1 -p + cp
    $$

    Args:
        c (float): Input parameter `c`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*c*p - p)


def expr_x_buchda(c: str = "c", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_buchda`."""
    return (2*pl.col(c)*pl.col(p) - pl.col(p))


def calc_y_buchda(c: float, q: float) -> float:
    r"""Compute mathematical metric extracted from buchdahl_wisdom_of_the_crowd.

    **Source**:
    - Title: wisdom_of_the_crowd_updated
    - Authors: Scientific Literature
    - Citation Key: `buchdahl_wisdom_of_the_crowd`

    **KaTeX Formula**:
    $$
    y = cq 1- q + cq
    $$

    Args:
        c (float): Input parameter `c`.
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*c*q - q)


def expr_y_buchda(c: str = "c", q: str = "q") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_y_buchda`."""
    return (2*pl.col(c)*pl.col(q) - pl.col(q))


def calc_p_buchda(x: float) -> float:
    r"""Compute mathematical metric extracted from buchdahl_wisdom_of_the_crowd.

    **Source**:
    - Title: wisdom_of_the_crowd_updated
    - Authors: Scientific Literature
    - Citation Key: `buchdahl_wisdom_of_the_crowd`

    **KaTeX Formula**:
    $$
    p = x c + x - cx
    $$

    Args:
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(x)


def expr_p_buchda(x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_buchda`."""
    return (pl.col(x))


def calc_glickman_1999_applstat_parameter_estimation_form_9(g: float) -> float:
    r"""Compute mathematical metric extracted from glickman_1999_applstat_parameter_estimation.

    **Source**:
    - Title: Parameter estimation in large dynamic paired comparison experiments (1999)
    - Authors: Glickman, M. E.
    - Citation Key: `glickman_1999_applstat_parameter_estimation`

    **KaTeX Formula**:
    $$
    \log fL  js  g   P m j 1 P nj k 1 f q g   2 j  sjk      j    \log 1   10 g   2 j       j =400  g
    $$

    Args:
        g (float): Input parameter `g`.

    Returns:
        float: Calculated metric value.
    """
    return float(400*g)


def expr_glickman_1999_applstat_parameter_estimation_form_9(g: str = "g") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_glickman_1999_applstat_parameter_estimation_form_9`."""
    return (400*pl.col(g))


def calc_q_buchda(y: float) -> float:
    r"""Compute mathematical metric extracted from buchdahl_wisdom_of_the_crowd.

    **Source**:
    - Title: wisdom_of_the_crowd_updated
    - Authors: Scientific Literature
    - Citation Key: `buchdahl_wisdom_of_the_crowd`

    **KaTeX Formula**:
    $$
    q = y c + y - cy
    $$

    Args:
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(y)


def expr_q_buchda(y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_buchda`."""
    return (pl.col(y))


def calc_false_buchda(n: float) -> float:
    r"""Compute mathematical metric extracted from buchdahl_wisdom_of_the_crowd.

    **Source**:
    - Title: wisdom_of_the_crowd_updated
    - Authors: Scientific Literature
    - Citation Key: `buchdahl_wisdom_of_the_crowd`

    **KaTeX Formula**:
    $$
    Logxp = Logyq = Logzr = n
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(n)


def expr_false_buchda(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_false_buchda`."""
    return (pl.col(n))


def calc_i_pi_egidi_(beta: float, i: float, o: float) -> float:
    r"""Compute mathematical metric extracted from egidi_2018_arxiv1802.

    **Source**:
    - Title: arxiv1802.08848
    - Authors: Scientific Literature
    - Citation Key: `egidi_2018_arxiv1802`

    **KaTeX Formula**:
    $$
    \pi i = oi \beta  , i \in  ∆m
    $$

    Args:
        beta (float): Input parameter `beta`.
        i (float): Input parameter `i`.
        o (float): Input parameter `o`.

    Returns:
        float: Calculated metric value.
    """
    return float(o*(beta*i))


def expr_i_pi_egidi_(beta: str = "beta", i: str = "i", o: str = "o") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_pi_egidi_`."""
    return (pl.col(o)*(pl.col(beta)*pl.col(i)))


def calc_d_r_glickm(i: float, m: float, n: float) -> float:
    r"""Compute mathematical metric extracted from glickman_1999_glicko1.

    **Source**:
    - Title: glicko (1999)
    - Authors: Mark E. Glickman, "The Glicko system" (Harvard University, 6-page description of Glicko-1 with worked examples). Date not printed in the PDF et al.
    - Citation Key: `glickman_1999_glicko1`

    **KaTeX Formula**:
    $$
    RD = min(\sqrt RD2old + c2 , 350)
    $$

    Args:
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*m*n)


def expr_d_r_glickm(i: str = "i", m: str = "m", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_r_glickm`."""
    return (pl.col(i)*pl.col(m)*pl.col(n))


def calc_math_0509698_form_9(R_A: float, R_S: float, beta: float, gamma: float) -> float:
    r"""Compute mathematical metric extracted from math_0509698.

    **Source**:
    - Title: A Derivation of the Pythagorean Won-Loss Formula in Baseball (2005)
    - Authors: Steven J. Miller
    - Citation Key: `math_0509698`

    **KaTeX Formula**:
    $$
    Won-Loss Percentage(R_{S},R_{A}, \beta , \gamma ) = (R_{S} - \beta )\gamma  (R_{S} - \beta )\gamma  + (R_{A} - \beta )\gamma
    $$

    Args:
        R_A (float): Input parameter `R_A`.
        R_S (float): Input parameter `R_S`.
        beta (float): Input parameter `beta`.
        gamma (float): Input parameter `gamma`.

    Returns:
        float: Calculated metric value.
    """
    return float(gamma*(R_A - beta) + (gamma*math.gamma(R_S - beta))*(R_S - beta))


def expr_math_0509698_form_9(R_A: str = "R_A", R_S: str = "R_S", beta: str = "beta", gamma: str = "gamma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_math_0509698_form_9`."""
    return (pl.col(gamma)*(pl.col(R_A) - pl.col(beta)) + (pl.col(gamma)*math.gamma(pl.col(R_S) - pl.col(beta)))*(pl.col(R_S) - pl.col(beta)))


def calc_e_glickm(g: float) -> float:
    r"""Compute mathematical metric extracted from glickman_1999_glicko1.

    **Source**:
    - Title: glicko (1999)
    - Authors: Mark E. Glickman, "The Glicko system" (Harvard University, 6-page description of Glicko-1 with worked examples). Date not printed in the PDF et al.
    - Citation Key: `glickman_1999_glicko1`

    **KaTeX Formula**:
    $$
    E = 1 1 + 10-g(\sqrt RD2i +RD2j )(ri-rj )/400
    $$

    Args:
        g (float): Input parameter `g`.

    Returns:
        float: Calculated metric value.
    """
    return float(21 - g)


def expr_e_glickm(g: str = "g") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_glickm`."""
    return (21 - pl.col(g))


def calc_s_n_theta_gneiti(n: float) -> float:
    r"""Compute mathematical metric extracted from gneiting_raftery_2007_jasa.

    **Source**:
    - Title: gneiting2007jasa
    - Authors: Scientific Literature
    - Citation Key: `gneiting_raftery_2007_jasa`

    **KaTeX Formula**:
    $$
    Sn(\theta  ) = 1 n n\sum  i=1 S(P\theta  , Xi)
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(n*n))


def expr_s_n_theta_gneiti(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_n_theta_gneiti`."""
    return (1*(pl.col(n)*pl.col(n)))


def calc_s_n_gneiti(n: float) -> float:
    r"""Compute mathematical metric extracted from gneiting_raftery_2007_jasa.

    **Source**:
    - Title: gneiting2007jasa
    - Authors: Scientific Literature
    - Citation Key: `gneiting_raftery_2007_jasa`

    **KaTeX Formula**:
    $$
    Sn = 1 n n\sum  i=1 S(Pi , xi)
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(n*n))


def expr_s_n_gneiti(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_n_gneiti`."""
    return (1*(pl.col(n)*pl.col(n)))


def calc_s_p_i_gneiti(m: float) -> float:
    r"""Compute mathematical metric extracted from gneiting_raftery_2007_jasa.

    **Source**:
    - Title: gneiting2007jasa
    - Authors: Scientific Literature
    - Citation Key: `gneiting_raftery_2007_jasa`

    **KaTeX Formula**:
    $$
    S(p, i) = - m\sum  j=1 (\delta ij - pj) 2 = 2pi - m\sum  j=1 p 2 j -1
    $$

    Args:
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(-m)


def expr_s_p_i_gneiti(m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_p_i_gneiti`."""
    return (-pl.col(m))


def calc_s_p_1_gneiti(i: float, l: float, m: float, q: float) -> float:
    r"""Compute mathematical metric extracted from gneiting_raftery_2007_jasa.

    **Source**:
    - Title: gneiting2007jasa
    - Authors: Scientific Literature
    - Citation Key: `gneiting_raftery_2007_jasa`

    **KaTeX Formula**:
    $$
    S(p, 1) = lim q\to 1 G(q)- \int  1 p (G ' (q) - G ' (p)) dq
    $$

    Args:
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        m (float): Input parameter `m`.
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*l*m*q)


def expr_s_p_1_gneiti(i: str = "i", l: str = "l", m: str = "m", q: str = "q") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_p_1_gneiti`."""
    return (pl.col(i)*pl.col(l)*pl.col(m)*pl.col(q))


def calc_c_r_p_s_n_mu_sigma_2_x_gneiti(sigma: float) -> float:
    r"""Compute mathematical metric extracted from gneiting_raftery_2007_jasa.

    **Source**:
    - Title: gneiting2007jasa
    - Authors: Scientific Literature
    - Citation Key: `gneiting_raftery_2007_jasa`

    **KaTeX Formula**:
    $$
    CRPS(N(\mu ,\sigma  2 ), x) =\sigma  [ 1 \sqrt \pi  - 2\phi  ( x - \mu  \sigma  ) - x - \mu  \sigma  ( 2Phi1 ( x-\mu  \sigma  ) -1 )]
    $$

    Args:
        sigma (float): Input parameter `sigma`.

    Returns:
        float: Calculated metric value.
    """
    return float(sigma)


def expr_c_r_p_s_n_mu_sigma_2_x_gneiti(sigma: str = "sigma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_r_p_s_n_mu_sigma_2_x_gneiti`."""
    return (pl.col(sigma))


def calc_e_s_p_x_gneiti(mu: float, p: float, x: float) -> float:
    r"""Compute mathematical metric extracted from gneiting_raftery_2007_jasa.

    **Source**:
    - Title: gneiting2007jasa
    - Authors: Scientific Literature
    - Citation Key: `gneiting_raftery_2007_jasa`

    **KaTeX Formula**:
    $$
    ES(P, x) = -|\mu p - x| 2
    $$

    Args:
        mu (float): Input parameter `mu`.
        p (float): Input parameter `p`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(-2*abs(mu*p - x))


def expr_e_s_p_x_gneiti(mu: str = "mu", p: str = "p", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_s_p_x_gneiti`."""
    return (-2*abs(pl.col(mu)*pl.col(p) - pl.col(x)))


def calc_math_0509698_form_3(R_A: float, R_S: float, beta: float, gamma: float) -> float:
    r"""Compute mathematical metric extracted from math_0509698.

    **Source**:
    - Title: A Derivation of the Pythagorean Won-Loss Formula in Baseball (2005)
    - Authors: Steven J. Miller
    - Citation Key: `math_0509698`

    **KaTeX Formula**:
    $$
    Won-Loss Percentage(R_{S},R_{A}, \beta , \gamma ) = (R_{S} - \beta )\gamma  (R_{S} - \beta )\gamma  + (R_{A} - \beta )\gamma
    $$

    Args:
        R_A (float): Input parameter `R_A`.
        R_S (float): Input parameter `R_S`.
        beta (float): Input parameter `beta`.
        gamma (float): Input parameter `gamma`.

    Returns:
        float: Calculated metric value.
    """
    return float(gamma*(R_A - beta) + (gamma*math.gamma(R_S - beta))*(R_S - beta))


def expr_math_0509698_form_3(R_A: str = "R_A", R_S: str = "R_S", beta: str = "beta", gamma: str = "gamma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_math_0509698_form_3`."""
    return (pl.col(gamma)*(pl.col(R_A) - pl.col(beta)) + (pl.col(gamma)*math.gamma(pl.col(R_S) - pl.col(beta)))*(pl.col(R_S) - pl.col(beta)))


def calc_miller_2007_pythag_weibull_form_5(R_A: float, R_S: float, beta: float, gamma: float) -> float:
    r"""Compute mathematical metric extracted from miller_2007_pythag_weibull.

    **Source**:
    - Title: 40-48 (journal reference on the abs page) (2007)
    - Authors: Steven J. Miller, "A Derivation of the Pythagorean Won-Loss Formula in Baseball", arXiv:math/0509698v4 [math.ST] (v1 2005-09-29 et al.
    - Citation Key: `miller_2007_pythag_weibull`

    **KaTeX Formula**:
    $$
    Won-Loss Percentage(R_{S},R_{A}, \beta , \gamma ) = (R_{S} - \beta )\gamma  (R_{S} - \beta )\gamma  + (R_{A} - \beta )\gamma
    $$

    Args:
        R_A (float): Input parameter `R_A`.
        R_S (float): Input parameter `R_S`.
        beta (float): Input parameter `beta`.
        gamma (float): Input parameter `gamma`.

    Returns:
        float: Calculated metric value.
    """
    return float(gamma*(R_A - beta) + (gamma*math.gamma(R_S - beta))*(R_S - beta))


def expr_miller_2007_pythag_weibull_form_5(R_A: str = "R_A", R_S: str = "R_S", beta: str = "beta", gamma: str = "gamma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_miller_2007_pythag_weibull_form_5`."""
    return (pl.col(gamma)*(pl.col(R_A) - pl.col(beta)) + (pl.col(gamma)*math.gamma(pl.col(R_S) - pl.col(beta)))*(pl.col(R_S) - pl.col(beta)))


def calc_miller_2007_pythag_weibull_form_c(R_A: float, R_S: float, beta: float, gamma: float) -> float:
    r"""Compute mathematical metric extracted from miller_2007_pythag_weibull.

    **Source**:
    - Title: 40-48 (journal reference on the abs page) (2007)
    - Authors: Steven J. Miller, "A Derivation of the Pythagorean Won-Loss Formula in Baseball", arXiv:math/0509698v4 [math.ST] (v1 2005-09-29 et al.
    - Citation Key: `miller_2007_pythag_weibull`

    **KaTeX Formula**:
    $$
    Won-Loss Percentage(R_{S},R_{A}, \beta , \gamma ) = (R_{S} - \beta )\gamma  (R_{S} - \beta )\gamma  + (R_{A} - \beta )\gamma
    $$

    Args:
        R_A (float): Input parameter `R_A`.
        R_S (float): Input parameter `R_S`.
        beta (float): Input parameter `beta`.
        gamma (float): Input parameter `gamma`.

    Returns:
        float: Calculated metric value.
    """
    return float(gamma*(R_A - beta) + (gamma*math.gamma(R_S - beta))*(R_S - beta))


def expr_miller_2007_pythag_weibull_form_c(R_A: str = "R_A", R_S: str = "R_S", beta: str = "beta", gamma: str = "gamma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_miller_2007_pythag_weibull_form_c`."""
    return (pl.col(gamma)*(pl.col(R_A) - pl.col(beta)) + (pl.col(gamma)*math.gamma(pl.col(R_S) - pl.col(beta)))*(pl.col(R_S) - pl.col(beta)))


def calc_miller_2005_pythag_derivation_form_c(R_A: float, R_S: float, beta: float, gamma: float) -> float:
    r"""Compute mathematical metric extracted from miller_2005_pythag_derivation.

    **Source**:
    - Title: 'A Derivation of the Pythagorean Won-Loss Formula in Baseball', arXiv math/0509698 (2005)
    - Authors: Miller, S.J.
    - Citation Key: `miller_2005_pythag_derivation`

    **KaTeX Formula**:
    $$
    Won-Loss Percentage(R_{S},R_{A}, \beta , \gamma ) = (R_{S} - \beta )\gamma  (R_{S} - \beta )\gamma  + (R_{A} - \beta )\gamma
    $$

    Args:
        R_A (float): Input parameter `R_A`.
        R_S (float): Input parameter `R_S`.
        beta (float): Input parameter `beta`.
        gamma (float): Input parameter `gamma`.

    Returns:
        float: Calculated metric value.
    """
    return float(gamma*(R_A - beta) + (gamma*math.gamma(R_S - beta))*(R_S - beta))


def expr_miller_2005_pythag_derivation_form_c(R_A: str = "R_A", R_S: str = "R_S", beta: str = "beta", gamma: str = "gamma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_miller_2005_pythag_derivation_form_c`."""
    return (pl.col(gamma)*(pl.col(R_A) - pl.col(beta)) + (pl.col(gamma)*math.gamma(pl.col(R_S) - pl.col(beta)))*(pl.col(R_S) - pl.col(beta)))


def calc_p_m_c_c_gneiti(n: float) -> float:
    r"""Compute mathematical metric extracted from gneiting_raftery_2007_jasa.

    **Source**:
    - Title: gneiting2007jasa
    - Authors: Scientific Literature
    - Citation Key: `gneiting_raftery_2007_jasa`

    **KaTeX Formula**:
    $$
    PMCC = n\sum  i=1 (xi - \mu i) 2 + n\sum  i=1 \sigma  2 i
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(n)


def expr_p_m_c_c_gneiti(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_m_c_c_gneiti`."""
    return (pl.col(n))


def calc_x_t_1_gneiti(X: float, epsilon: float, t: float) -> float:
    r"""Compute mathematical metric extracted from gneiting_raftery_2007_jasa.

    **Source**:
    - Title: gneiting2007jasa
    - Authors: Scientific Literature
    - Citation Key: `gneiting_raftery_2007_jasa`

    **KaTeX Formula**:
    $$
    Xt+1 = 1 2 Xt + 1 2 Xt\epsilon t + \epsilon t
    $$

    Args:
        X (float): Input parameter `X`.
        epsilon (float): Input parameter `epsilon`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(12*X*epsilon*t**2 + 12*X*t + epsilon*t)


def expr_x_t_1_gneiti(X: str = "X", epsilon: str = "epsilon", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_t_1_gneiti`."""
    return (12*pl.col(X)*pl.col(epsilon)*pl.col(t)**2 + 12*pl.col(X)*pl.col(t) + pl.col(epsilon)*pl.col(t))


def calc_e_p_pi_form_0(n: float) -> float:
    r"""Compute mathematical metric extracted from shin_family_2024_cambridge.

    **Source**:
    - Title: shin_family_2024
    - Authors: Scientific Literature
    - Citation Key: `shin_family_2024_cambridge`

    **KaTeX Formula**:
    $$
    EP (\pi ) = 1 - n\sum  i=1 zpi + (1 - z)p2i \pi i
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(1 - n)


def expr_e_p_pi_form_0(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_p_pi_form_0`."""
    return (1 - pl.col(n))


def calc_p_n_e_n_w_form_0(P: float, dg: float, e: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_21639.

    **Source**:
    - Title: Liquid-Nitrogen Micropillar-Wick Cooling for Cryogenic Electronics: A Numerical Study of Thermal Performance and Capillary Dry-Out Limits (2026)
    - Authors: Felix Mende, Marcus Wislicenus, Dianping Jiang et al.
    - Citation Key: `arxiv_2609_21639`

    **KaTeX Formula**:
    $$
    P new n = Pedge,n-1 + Pedge,n 2
    $$

    Args:
        P (float): Input parameter `P`.
        dg (float): Input parameter `dg`.
        e (float): Input parameter `e`.

    Returns:
        float: Calculated metric value.
    """
    return float(P*dg*e**2)


def expr_p_n_e_n_w_form_0(P: str = "P", dg: str = "dg", e: str = "e") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_n_e_n_w_form_0`."""
    return (pl.col(P)*pl.col(dg)*pl.col(e)**2)


def calc_delta_p_c_e_l_l_form_1(l: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_21639.

    **Source**:
    - Title: Liquid-Nitrogen Micropillar-Wick Cooling for Cryogenic Electronics: A Numerical Study of Thermal Performance and Capillary Dry-Out Limits (2026)
    - Authors: Felix Mende, Marcus Wislicenus, Dianping Jiang et al.
    - Citation Key: `arxiv_2609_21639`

    **KaTeX Formula**:
    $$
    \Delta pcell = pl,edge,n-1 - pl,edge,n
    $$

    Args:
        l (float): Input parameter `l`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(l*p)


def expr_delta_p_c_e_l_l_form_1(l: str = "l", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_p_c_e_l_l_form_1`."""
    return (pl.col(l)*pl.col(p))


def calc_r_p_s_form_1(r: float) -> float:
    r"""Compute mathematical metric extracted from shin_family_2024_cambridge.

    **Source**:
    - Title: shin_family_2024
    - Authors: Scientific Literature
    - Citation Key: `shin_family_2024_cambridge`

    **KaTeX Formula**:
    $$
    RPS = 1 r - 1 r\sum  i=1 ( i\sum  j=1 pj - i\sum  j=1 ej )2
    $$

    Args:
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(-1*r + 1*r)


def expr_r_p_s_form_1(r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_p_s_form_1`."""
    return (-1*pl.col(r) + 1*pl.col(r))


def calc_p_form_1(P: float, c: float, i: float, r: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_21639.

    **Source**:
    - Title: Liquid-Nitrogen Micropillar-Wick Cooling for Cryogenic Electronics: A Numerical Study of Thermal Performance and Capillary Dry-Out Limits (2026)
    - Authors: Felix Mende, Marcus Wislicenus, Dianping Jiang et al.
    - Citation Key: `arxiv_2609_21639`

    **KaTeX Formula**:
    $$
    P = Pcrit
    $$

    Args:
        P (float): Input parameter `P`.
        c (float): Input parameter `c`.
        i (float): Input parameter `i`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(P*c*i*r*t)


def expr_p_form_1(P: str = "P", c: str = "c", i: str = "i", r: str = "r", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_form_1`."""
    return (pl.col(P)*pl.col(c)*pl.col(i)*pl.col(r)*pl.col(t))


def calc_h_p_form_1(P: float) -> float:
    r"""Compute mathematical metric extracted from strumbelj_2014_ijf.

    **Source**:
    - Title: Strumbelj_WorkingPaper2013
    - Authors: Scientific Literature
    - Citation Key: `strumbelj_2014_ijf`

    **KaTeX Formula**:
    $$
    pH = P(\mu 2 < Y ) pD = P(\mu 1 < Y < \mu 2) pA = P(Y < \mu 1)
    $$

    Args:
        P (float): Input parameter `P`.

    Returns:
        float: Calculated metric value.
    """
    return float(P)


def expr_h_p_form_1(P: str = "P") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_p_form_1`."""
    return (pl.col(P))


def calc_m_f_form_2(i: float, m: float) -> float:
    r"""Compute mathematical metric extracted from niculescu_mizil_caruana_2005.

    **Source**:
    - Title: nmc2005
    - Authors: Scientific Literature
    - Citation Key: `niculescu_mizil_caruana_2005`

    **KaTeX Formula**:
    $$
    m(f) = mi,j, for fi < f \le  fj
    $$

    Args:
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(i*m)


def expr_m_f_form_2(i: str = "i", m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_f_form_2`."""
    return (pl.col(i)*pl.col(m))


def calc_l_k_form_2(A: float, C: float, L: float, m: float, rho: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_30305.

    **Source**:
    - Title: Exact turning invariants for projectile motion under quadratic drag and a vertical-axis Magnus force (2026)
    - Authors: Pragyaan Gaur
    - Citation Key: `arxiv_2609_30305`

    **KaTeX Formula**:
    $$
    kL = \rho CLA 2m , kD = \rho CDA 2m , \mu  \equiv  kD kL = CD CL
    $$

    Args:
        A (float): Input parameter `A`.
        C (float): Input parameter `C`.
        L (float): Input parameter `L`.
        m (float): Input parameter `m`.
        rho (float): Input parameter `rho`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*A*C*L*m*rho)


def expr_l_k_form_2(A: str = "A", C: str = "C", L: str = "L", m: str = "m", rho: str = "rho") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_k_form_2`."""
    return (2*pl.col(A)*pl.col(C)*pl.col(L)*pl.col(m)*pl.col(rho))


def calc_m_z_1_form_2(n: float) -> float:
    r"""Compute mathematical metric extracted from shin_family_2024_cambridge.

    **Source**:
    - Title: shin_family_2024
    - Authors: Scientific Literature
    - Citation Key: `shin_family_2024_cambridge`

    **KaTeX Formula**:
    $$
    zm+1 = n\sum  i=1 (\sqrt z2m + 4(1 - zm) \pi 2 i \beta  ) - 2
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(n)


def expr_m_z_1_form_2(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_z_1_form_2`."""
    return (pl.col(n))


def calc_b_s_form_2(m: float, n: float) -> float:
    r"""Compute mathematical metric extracted from strumbelj_2014_ijf.

    **Source**:
    - Title: Strumbelj_WorkingPaper2013
    - Authors: Scientific Literature
    - Citation Key: `strumbelj_2014_ijf`

    **KaTeX Formula**:
    $$
    BS = 1n m\sum  k=1 nk\sum  j=1 (fkj - okj)2 = 1n m\sum  k=1 nk(f k - ok)2 - 1n m\sum  k=1 nk(ok - o)2 + o(1 - o) + 1n m\sum  k=1 nk\sum  j=1 (fkj - f k )2 - 2n m\sum  k=1 nk\sum  j=1 (fkj - f k )(okj - ok)
    $$

    Args:
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(m*n))


def expr_b_s_form_2(m: str = "m", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_b_s_form_2`."""
    return (1*(pl.col(m)*pl.col(n)))


def calc_f_x_form_2(T: float) -> float:
    r"""Compute mathematical metric extracted from niculescu_mizil_caruana_2005.

    **Source**:
    - Title: nmc2005
    - Authors: Scientific Literature
    - Citation Key: `niculescu_mizil_caruana_2005`

    **KaTeX Formula**:
    $$
    F (x) = T\sum  i=1 \alpha ihi(x)
    $$

    Args:
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(T)


def expr_f_x_form_2(T: str = "T") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_x_form_2`."""
    return (pl.col(T))


def calc_i_p_form_3(i: float, p: float) -> float:
    r"""Compute mathematical metric extracted from shin_family_2024_cambridge.

    **Source**:
    - Title: shin_family_2024
    - Authors: Scientific Literature
    - Citation Key: `shin_family_2024_cambridge`

    **KaTeX Formula**:
    $$
    pi = p*i 3\sum  i=1 p*i
    $$

    Args:
        i (float): Input parameter `i`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(3*i*p)


def expr_i_p_form_3(i: str = "i", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_p_form_3`."""
    return (3*pl.col(i)*pl.col(p))


def calc_h_form_3(m: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_0911_4503.

    **Source**:
    - Title: A Bayesian Variable Selection Approach to Major League Baseball Hitting Metrics (2009)
    - Authors: Blakeley B. McShane, Alexander Braunstein, James Piette et al.
    - Citation Key: `arxiv_0911_4503`

    **KaTeX Formula**:
    $$
    -H = 1m m\sum  i=1 [ ̂ \gamma i \log(̂ \gamma i) + (1 - ̂ \gamma i) \log(1 - ̂ \gamma i)]
    $$

    Args:
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(m**2)


def expr_h_form_3(m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_form_3`."""
    return (pl.col(m)**2)


def calc_e_c_e_form_5(K: float) -> float:
    r"""Compute mathematical metric extracted from naeini_2015_aaai.

    **Source**:
    - Title: naeini2015
    - Authors: Scientific Literature
    - Citation Key: `naeini_2015_aaai`

    **KaTeX Formula**:
    $$
    ECE = K\sum  i=1 P(i) \cdot  |oi - ei| , MCE = K max i=1 (|oi - ei|)
    $$

    Args:
        K (float): Input parameter `K`.

    Returns:
        float: Calculated metric value.
    """
    return float(K)


def expr_e_c_e_form_5(K: str = "K") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_c_e_form_5`."""
    return (pl.col(K))


def calc_l_dr_y_o_t_u_form_5(N: float, c: float, i: float, l: float, r: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_21639.

    **Source**:
    - Title: Liquid-Nitrogen Micropillar-Wick Cooling for Cryogenic Electronics: A Numerical Study of Thermal Performance and Capillary Dry-Out Limits (2026)
    - Authors: Felix Mende, Marcus Wislicenus, Dianping Jiang et al.
    - Citation Key: `arxiv_2609_21639`

    **KaTeX Formula**:
    $$
    Ldry-out = Ncrit l
    $$

    Args:
        N (float): Input parameter `N`.
        c (float): Input parameter `c`.
        i (float): Input parameter `i`.
        l (float): Input parameter `l`.
        r (float): Input parameter `r`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(N*(c*(r*(i*(l*t)))))


def expr_l_dr_y_o_t_u_form_5(N: str = "N", c: str = "c", i: str = "i", l: str = "l", r: str = "r", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_dr_y_o_t_u_form_5`."""
    return (pl.col(N)*(pl.col(c)*(pl.col(r)*(pl.col(i)*(pl.col(l)*pl.col(t))))))


def calc_t_pi_form_5(n: float) -> float:
    r"""Compute mathematical metric extracted from strumbelj_2014_ijf.

    **Source**:
    - Title: Strumbelj_WorkingPaper2013
    - Authors: Scientific Literature
    - Citation Key: `strumbelj_2014_ijf`

    **KaTeX Formula**:
    $$
    T (\pi ) = 1 - n\sum  i=1 pi \pi i (pi(1 - z) + z)
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(1 - n)


def expr_t_pi_form_5(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_pi_form_5`."""
    return (1 - pl.col(n))


def calc_i_p_form_6(n: float) -> float:
    r"""Compute mathematical metric extracted from shin_family_2024_cambridge.

    **Source**:
    - Title: shin_family_2024
    - Authors: Scientific Literature
    - Citation Key: `shin_family_2024_cambridge`

    **KaTeX Formula**:
    $$
    pi = 1 n (\sqrt z*2+ 4\beta  n2 (1-z* )-z* 2(1-z* ) ) \sqrt z2 i + 4(1 - zi) \pi 2 i \beta  - zi 2(1 - zi)
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(n)


def expr_i_p_form_6(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_p_form_6`."""
    return (pl.col(n))


def calc_dt_dv_form_6(A: float, C: float, D: float, L: float, g: float, m: float, omega: float, rho: float, v: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_30305.

    **Source**:
    - Title: Exact turning invariants for projectile motion under quadratic drag and a vertical-axis Magnus force (2026)
    - Authors: Pragyaan Gaur
    - Citation Key: `arxiv_2609_30305`

    **KaTeX Formula**:
    $$
    dv dt = -g z - \rho CDA 2m |v| v + \rho CLA 2m |v| ( \omega \times v)
    $$

    Args:
        A (float): Input parameter `A`.
        C (float): Input parameter `C`.
        D (float): Input parameter `D`.
        L (float): Input parameter `L`.
        g (float): Input parameter `g`.
        m (float): Input parameter `m`.
        omega (float): Input parameter `omega`.
        rho (float): Input parameter `rho`.
        v (float): Input parameter `v`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(-2*A*C*D*m*omega*rho*v*abs(v**2*abs(2*A*C*L*m*rho + v)) - g*z)


def expr_dt_dv_form_6(A: str = "A", C: str = "C", D: str = "D", L: str = "L", g: str = "g", m: str = "m", omega: str = "omega", rho: str = "rho", v: str = "v", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_dt_dv_form_6`."""
    return (-2*pl.col(A)*pl.col(C)*pl.col(D)*pl.col(m)*pl.col(omega)*pl.col(rho)*pl.col(v)*abs(pl.col(v)**2*abs(2*pl.col(A)*pl.col(C)*pl.col(L)*pl.col(m)*pl.col(rho) + pl.col(v))) - pl.col(g)*pl.col(z))


def calc_l_c_e_form_6(n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2607_26440.

    **Source**:
    - Title: Explicit Note-Event Tokenization and Pitch-Validity Constrained Decoding for MIDI-to-Tablature Transcription (2026)
    - Authors: Ting-Kai Hsu, Wei-Chin Wang, Kai-Xi Hong et al.
    - Citation Key: `arxiv_2607_26440`

    **KaTeX Formula**:
    $$
    LCE = - n\sum  i=1 \log p (yi | y<i, x)
    $$

    Args:
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(-n)


def expr_l_c_e_form_6(n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_c_e_form_6`."""
    return (-pl.col(n))


def calc_q_h_e_a_t_form_6(C: float, Delta: float, T: float, c: float, n: float, u: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_21639.

    **Source**:
    - Title: Liquid-Nitrogen Micropillar-Wick Cooling for Cryogenic Electronics: A Numerical Study of Thermal Performance and Capillary Dry-Out Limits (2026)
    - Authors: Felix Mende, Marcus Wislicenus, Dianping Jiang et al.
    - Citation Key: `arxiv_2609_21639`

    **KaTeX Formula**:
    $$
    qheat = Cnuc\Delta T 2.5
    $$

    Args:
        C (float): Input parameter `C`.
        Delta (float): Input parameter `Delta`.
        T (float): Input parameter `T`.
        c (float): Input parameter `c`.
        n (float): Input parameter `n`.
        u (float): Input parameter `u`.

    Returns:
        float: Calculated metric value.
    """
    return float(2.5*C*Delta*T*c*n*u)


def expr_q_h_e_a_t_form_6(C: str = "C", Delta: str = "Delta", T: str = "T", c: str = "c", n: str = "n", u: str = "u") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_h_e_a_t_form_6`."""
    return (2.5*pl.col(C)*pl.col(Delta)*pl.col(T)*pl.col(c)*pl.col(n)*pl.col(u))


def calc_nabla_a_f_dagger_form_7(F: float, J: float, T: float, dagger: float, kappa: float, n: float, nabla: float, omega: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    \nabla a  F\dagger  = \kappa \dagger  1 + \kappa \dagger  JT\omega  [n]\nabla \omega   F\dagger
    $$

    Args:
        F (float): Input parameter `F`.
        J (float): Input parameter `J`.
        T (float): Input parameter `T`.
        dagger (float): Input parameter `dagger`.
        kappa (float): Input parameter `kappa`.
        n (float): Input parameter `n`.
        nabla (float): Input parameter `nabla`.
        omega (float): Input parameter `omega`.

    Returns:
        float: Calculated metric value.
    """
    return float(F*J*T*dagger**2*kappa*n*nabla*omega**2 + dagger*kappa)


def expr_nabla_a_f_dagger_form_7(F: str = "F", J: str = "J", T: str = "T", dagger: str = "dagger", kappa: str = "kappa", n: str = "n", nabla: str = "nabla", omega: str = "omega") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_nabla_a_f_dagger_form_7`."""
    return (pl.col(F)*pl.col(J)*pl.col(T)*pl.col(dagger)**2*pl.col(kappa)*pl.col(n)*pl.col(nabla)*pl.col(omega)**2 + pl.col(dagger)*pl.col(kappa))


def calc_m_q_form_9(N: float, q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_03021.

    **Source**:
    - Title: MeloCodec: Harnessing Melodic Priors for High-Fidelity Singing Voice Representation (2026)
    - Authors: Yizhong Geng, Wenxin Fu, Kecan Mao et al.
    - Citation Key: `arxiv_2608_03021`

    **KaTeX Formula**:
    $$
    Mq = Nq\sum  k=1 zk, where zk = Quantizek M - k-1 \sum  j=1 zj 
    $$

    Args:
        N (float): Input parameter `N`.
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float(N*q)


def expr_m_q_form_9(N: str = "N", q: str = "q") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_q_form_9`."""
    return (pl.col(N)*pl.col(q))


def calc_equiv_tan_gamma_u_q_u_form_9(v: float, w: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_30305.

    **Source**:
    - Title: Exact turning invariants for projectile motion under quadratic drag and a vertical-axis Magnus force (2026)
    - Authors: Pragyaan Gaur
    - Citation Key: `arxiv_2609_30305`

    **KaTeX Formula**:
    $$
    Q(u) \equiv  \tan\gamma (u) = vz |w|
    $$

    Args:
        v (float): Input parameter `v`.
        w (float): Input parameter `w`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(v*(z*abs(w)))


def expr_equiv_tan_gamma_u_q_u_form_9(v: str = "v", w: str = "w", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_equiv_tan_gamma_u_q_u_form_9`."""
    return (pl.col(v)*(pl.col(z)*abs(pl.col(w))))


def calc_f_t_y_0_sigma_y_y_0_form_c(h: float, omega: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    f T (  y* 0 ,\sigma ) y (  y* 0 ) = h-1 \omega  (x* , \sigma )
    $$

    Args:
        h (float): Input parameter `h`.
        omega (float): Input parameter `omega`.

    Returns:
        float: Calculated metric value.
    """
    return float(h - omega)


def expr_f_t_y_0_sigma_y_y_0_form_c(h: str = "h", omega: str = "omega") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_t_y_0_sigma_y_y_0_form_c`."""
    return (pl.col(h) - pl.col(omega))


def calc_a_phi_z_form_e(A: float, D: float, S: float, phi: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    A(z\phi ) = S-1 A AASAz\phi  +S-1 A DA
    $$

    Args:
        A (float): Input parameter `A`.
        D (float): Input parameter `D`.
        S (float): Input parameter `S`.
        phi (float): Input parameter `phi`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(-1*A*(A*D) + (S + (S - 1*A*(A*(A*(S*(A*(phi*z))))))))


def expr_a_phi_z_form_e(A: str = "A", D: str = "D", S: str = "S", phi: str = "phi", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_phi_z_form_e`."""
    return (-1*pl.col(A)*(pl.col(A)*pl.col(D)) + (pl.col(S) + (pl.col(S) - 1*pl.col(A)*(pl.col(A)*(pl.col(A)*(pl.col(S)*(pl.col(A)*(pl.col(phi)*pl.col(z)))))))))


def calc_nabla_p_f_dagger_form_7(F: float, dagger: float, kappa: float, nabla: float, p: float, sim: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    \nabla p  F\dagger  = \kappa \dagger  1 + \kappa \dagger  \nabla p  F\dagger  + 1 1 + \kappa \dagger  \nabla p \sim  F\dagger
    $$

    Args:
        F (float): Input parameter `F`.
        dagger (float): Input parameter `dagger`.
        kappa (float): Input parameter `kappa`.
        nabla (float): Input parameter `nabla`.
        p (float): Input parameter `p`.
        sim (float): Input parameter `sim`.

    Returns:
        float: Calculated metric value.
    """
    return float(F*dagger**2*kappa*nabla*p*sim + F*dagger**2*kappa*nabla*p + dagger*kappa + 11)


def expr_nabla_p_f_dagger_form_7(F: str = "F", dagger: str = "dagger", kappa: str = "kappa", nabla: str = "nabla", p: str = "p", sim: str = "sim") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_nabla_p_f_dagger_form_7`."""
    return (pl.col(F)*pl.col(dagger)**2*pl.col(kappa)*pl.col(nabla)*pl.col(p)*pl.col(sim) + pl.col(F)*pl.col(dagger)**2*pl.col(kappa)*pl.col(nabla)*pl.col(p) + pl.col(dagger)*pl.col(kappa) + 11)


def calc_q_c_f_h_form_e(W: float, c: float, m: float, pm: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_21639.

    **Source**:
    - Title: Liquid-Nitrogen Micropillar-Wick Cooling for Cryogenic Electronics: A Numerical Study of Thermal Performance and Capillary Dry-Out Limits (2026)
    - Authors: Felix Mende, Marcus Wislicenus, Dianping Jiang et al.
    - Citation Key: `arxiv_2609_21639`

    **KaTeX Formula**:
    $$
    qCHF = (19.3 \pm  4.7)Wcm-2
    $$

    Args:
        W (float): Input parameter `W`.
        c (float): Input parameter `c`.
        m (float): Input parameter `m`.
        pm (float): Input parameter `pm`.

    Returns:
        float: Calculated metric value.
    """
    return float(90.71*W*c*m*pm - 2)


def expr_q_c_f_h_form_e(W: str = "W", c: str = "c", m: str = "m", pm: str = "pm") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_c_f_h_form_e`."""
    return (90.71*pl.col(W)*pl.col(c)*pl.col(m)*pl.col(pm) - 2)


def calc_i_z_form_e(B: float, Q: float, R: float, i: float) -> float:
    r"""Compute mathematical metric extracted from naeini_2015_aaai.

    **Source**:
    - Title: naeini2015
    - Authors: Scientific Literature
    - Citation Key: `naeini_2015_aaai`

    **KaTeX Formula**:
    $$
    zi = (Ri -RBBQ) \sqrt  k(k+1) 6N
    $$

    Args:
        B (float): Input parameter `B`.
        Q (float): Input parameter `Q`.
        R (float): Input parameter `R`.
        i (float): Input parameter `i`.

    Returns:
        float: Calculated metric value.
    """
    return float(R*i - R*B*(B*Q))


def expr_i_z_form_e(B: str = "B", Q: str = "Q", R: str = "R", i: str = "i") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_z_form_e`."""
    return (pl.col(R)*pl.col(i) - pl.col(R)*pl.col(B)*(pl.col(B)*pl.col(Q)))


def calc_m_form_f(a: float, g: float, i: float, m: float, n: float, r: float, z: float) -> float:
    r"""Compute mathematical metric extracted from niculescu_mizil_caruana_2005.

    **Source**:
    - Title: nmc2005
    - Authors: Scientific Literature
    - Citation Key: `niculescu_mizil_caruana_2005`

    **KaTeX Formula**:
    $$
    m = argmin z \sum (yi - z(fi))2
    $$

    Args:
        a (float): Input parameter `a`.
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*g*i*m*n*r*z)


def expr_m_form_f(a: str = "a", g: str = "g", i: str = "i", m: str = "m", n: str = "n", r: str = "r", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_form_f`."""
    return (pl.col(a)*pl.col(g)*pl.col(i)*pl.col(m)*pl.col(n)*pl.col(r)*pl.col(z))


def calc_u_form_f(m: float) -> float:
    r"""Compute mathematical metric extracted from nguyen_matthews_2022_aging.

    **Source**:
    - Title: 2210.02383
    - Authors: Scientific Literature
    - Citation Key: `nguyen_matthews_2022_aging`

    **KaTeX Formula**:
    $$
    U = 1m m\sum  i=1 ̂Ui
    $$

    Args:
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(m**2)


def expr_u_form_f(m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_form_f`."""
    return (pl.col(m)**2)


def calc_f_dagger_n_form_0(F: float, dagger: float, kappa: float, n: float, sim: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    F\dagger [n] = \kappa \dagger  1 + \kappa \dagger   F\dagger [n] + 1 1 + \kappa \dagger  \sim  F\dagger [n]
    $$

    Args:
        F (float): Input parameter `F`.
        dagger (float): Input parameter `dagger`.
        kappa (float): Input parameter `kappa`.
        n (float): Input parameter `n`.
        sim (float): Input parameter `sim`.

    Returns:
        float: Calculated metric value.
    """
    return float(F*dagger**2*kappa*n*sim + F*dagger**2*kappa*n + dagger*kappa + 11)


def expr_f_dagger_n_form_0(F: str = "F", dagger: str = "dagger", kappa: str = "kappa", n: str = "n", sim: str = "sim") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_dagger_n_form_0`."""
    return (pl.col(F)*pl.col(dagger)**2*pl.col(kappa)*pl.col(n)*pl.col(sim) + pl.col(F)*pl.col(dagger)**2*pl.col(kappa)*pl.col(n) + pl.col(dagger)*pl.col(kappa) + 11)


def calc_n_omega_form_0(n: float, phi: float, psi: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    \omega [n] = \cos \psi [n] \sin \theta [n] \cos \phi [n] + \sin \psi [n] \sin \phi [n] \sin \psi [n] \sin \theta [n] \cos \phi [n] - \cos \psi [n] \sin \phi [n] \cos \theta [n] \cos \phi [n]
    $$

    Args:
        n (float): Input parameter `n`.
        phi (float): Input parameter `phi`.
        psi (float): Input parameter `psi`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.sin(n*phi)*math.sin(n*psi)**2*math.sin(n*theta)*math.cos(n*phi) - math.sin(n*phi)*math.cos(n*phi)*math.cos(n*psi)*math.cos(n*theta) + math.sin(n*theta)*math.cos(n*phi)*math.cos(n*psi))


def expr_n_omega_form_0(n: str = "n", phi: str = "phi", psi: str = "psi", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_n_omega_form_0`."""
    return (math.sin(pl.col(n)*pl.col(phi))*math.sin(pl.col(n)*pl.col(psi))**2*math.sin(pl.col(n)*pl.col(theta))*math.cos(pl.col(n)*pl.col(phi)) - math.sin(pl.col(n)*pl.col(phi))*math.cos(pl.col(n)*pl.col(phi))*math.cos(pl.col(n)*pl.col(psi))*math.cos(pl.col(n)*pl.col(theta)) + math.sin(pl.col(n)*pl.col(theta))*math.cos(pl.col(n)*pl.col(phi))*math.cos(pl.col(n)*pl.col(psi)))


def calc_m_z_form_0(Delta: float, m: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27193.

    **Source**:
    - Title: Low Residuals, Wrong Value: Learning the Viscosity Solution of Hamilton-Jacobi-Isaacs Equations with PINNs (2026)
    - Authors: Raul Jimenez, Pablo Tejerina-Pérez, Leonid Sarieddine et al.
    - Citation Key: `arxiv_2610_27193`

    **KaTeX Formula**:
    $$
    zm = \Delta  - sm, (sm)i = Lbm,i sgn\Delta i, bm \in  {0, 1}n
    $$

    Args:
        Delta (float): Input parameter `Delta`.
        m (float): Input parameter `m`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(Delta - m*s)


def expr_m_z_form_0(Delta: str = "Delta", m: str = "m", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_z_form_0`."""
    return (pl.col(Delta) - pl.col(m)*pl.col(s))


def calc_r_b_p_a_form_1(N: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    Rb(P,A) = 1N N\sum  n=1 Rb(p[n], a[n])
    $$

    Args:
        N (float): Input parameter `N`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(N*N))


def expr_r_b_p_a_form_1(N: str = "N") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_b_p_a_form_1`."""
    return (1*(pl.col(N)*pl.col(N)))


def calc_l_t_e_o_form_3(dcos: float, g: float, m: float, phi: float, r: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    Ltoe = (d \cos \phi  + r \sin \theta )mg
    $$

    Args:
        dcos (float): Input parameter `dcos`.
        g (float): Input parameter `g`.
        m (float): Input parameter `m`.
        phi (float): Input parameter `phi`.
        r (float): Input parameter `r`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(g*m*(dcos*phi + r*math.sin(theta)))


def expr_l_t_e_o_form_3(dcos: str = "dcos", g: str = "g", m: str = "m", phi: str = "phi", r: str = "r", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_t_e_o_form_3`."""
    return (pl.col(g)*pl.col(m)*(pl.col(dcos)*pl.col(phi) + pl.col(r)*math.sin(pl.col(theta))))


def calc_sim_a_sigma_form_4(A: float, epsilon: float, sigma: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_39364.

    **Source**:
    - Title: Imperfect bifurcations in a laminar 3D bluff body wake: effect of pitch and yaw (2026)
    - Authors: Atharva Lagwankar, Alessandro Chiarini, François Gallaire et al.
    - Citation Key: `arxiv_2609_39364`

    **KaTeX Formula**:
    $$
    \sim \sigma A = \sigma A \epsilon  2 , \sim \sigma B = \sigma B \epsilon  2 , (A 1)
    $$

    Args:
        A (float): Input parameter `A`.
        epsilon (float): Input parameter `epsilon`.
        sigma (float): Input parameter `sigma`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*A*epsilon*sigma)


def expr_sim_a_sigma_form_4(A: str = "A", epsilon: str = "epsilon", sigma: str = "sigma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sim_a_sigma_form_4`."""
    return (2*pl.col(A)*pl.col(epsilon)*pl.col(sigma))


def calc_dmu_k_form_4(Delta: float, k: float, mu: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_05080.

    **Source**:
    - Title: Tracing a Sparse Emotion-Control Circuit in LLM-Based Text-to-Speech (2026)
    - Authors: Hongfei Du, Jiacheng Shi, Yanfu Zhang et al.
    - Citation Key: `arxiv_2610_05080`

    **KaTeX Formula**:
    $$
    d\mu k = \Delta \mu k /|\Delta \mu k |2, Ck(\tau  ) = 〈\mu (\tau  ) - \mu (\tau  (n) i ),  d\mu k 〉
    $$

    Args:
        Delta (float): Input parameter `Delta`.
        k (float): Input parameter `k`.
        mu (float): Input parameter `mu`.

    Returns:
        float: Calculated metric value.
    """
    return float((1/2)*Delta*k*mu/abs(Delta*k*mu))


def expr_dmu_k_form_4(Delta: str = "Delta", k: str = "k", mu: str = "mu") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_dmu_k_form_4`."""
    return ((1/2)*pl.col(Delta)*pl.col(k)*pl.col(mu)/abs(pl.col(Delta)*pl.col(k)*pl.col(mu)))


def calc_k_form_4(O: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27416.

    **Source**:
    - Title: Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization (2026)
    - Authors: Koichi Miyamoto
    - Citation Key: `arxiv_2610_27416`

    **KaTeX Formula**:
    $$
    K = O (\log ( (\sqrt \sigma 2T + \sigma X)(\alpha AT + \sqrt N) ¯ C \epsilon c(1 - c) ))
    $$

    Args:
        O (float): Input parameter `O`.

    Returns:
        float: Calculated metric value.
    """
    return float(O)


def expr_k_form_4(O: str = "O") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_form_4`."""
    return (pl.col(O))


def calc_e_f_sim_form_4(gamma: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27416.

    **Source**:
    - Title: Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization (2026)
    - Authors: Koichi Miyamoto
    - Citation Key: `arxiv_2610_27416`

    **KaTeX Formula**:
    $$
    E[ \sim  f] = 1 \gamma  r\sum  n=1 N\sum  i=1 Cn,iMn,i Y,hist , \sim  f := 1 \gamma  r\sum  n=1 N\sum  i=1 Cn,iY 1,i tn
    $$

    Args:
        gamma (float): Input parameter `gamma`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(gamma*r))


def expr_e_f_sim_form_4(gamma: str = "gamma", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_f_sim_form_4`."""
    return (1*(pl.col(gamma)*pl.col(r)))


def calc_delta_n_p_form_4(d: float, k: float, l: float, mu: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_21639.

    **Source**:
    - Title: Liquid-Nitrogen Micropillar-Wick Cooling for Cryogenic Electronics: A Numerical Study of Thermal Performance and Capillary Dry-Out Limits (2026)
    - Authors: Felix Mende, Marcus Wislicenus, Dianping Jiang et al.
    - Citation Key: `arxiv_2609_21639`

    **KaTeX Formula**:
    $$
    \Delta pn = \mu l kd,l,ℎ l lℎ ̇Vn = \mu l ℎkd,l,ℎ qheat l2 (N - n + 1) \rho lℎlv
    $$

    Args:
        d (float): Input parameter `d`.
        k (float): Input parameter `k`.
        l (float): Input parameter `l`.
        mu (float): Input parameter `mu`.

    Returns:
        float: Calculated metric value.
    """
    return float(d*k*l*mu)


def expr_delta_n_p_form_4(d: str = "d", k: str = "k", l: str = "l", mu: str = "mu") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_n_p_form_4`."""
    return (pl.col(d)*pl.col(k)*pl.col(l)*pl.col(mu))


def calc_val_1_gamma_form_5(O: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27416.

    **Source**:
    - Title: Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization (2026)
    - Authors: Koichi Miyamoto
    - Citation Key: `arxiv_2610_27416`

    **KaTeX Formula**:
    $$
    1 \gamma  = O (\sqrt \sigma 2T c \log ( (\sqrt \sigma 2T + \sigma X)(\alpha AT + \sqrt N) ¯ C \epsilon c(1 - c) ))
    $$

    Args:
        O (float): Input parameter `O`.

    Returns:
        float: Calculated metric value.
    """
    return float(O)


def expr_val_1_gamma_form_5(O: str = "O") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1_gamma_form_5`."""
    return (pl.col(O))


def calc_gamma_dagger_n_form_5(F: float, dagger: float, n: float, rho: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_01307.

    **Source**:
    - Title: Exploiting UAV Attitude for Covert Communications: Dynamics-Consistent Trajectory-Attitude Co-Design (2026)
    - Authors: Jinpeng Xu, Lin Zhou, Xin Xie et al.
    - Citation Key: `arxiv_2610_01307`

    **KaTeX Formula**:
    $$
    \gamma \dagger [n] = \rho 0  F\dagger [n]
    $$

    Args:
        F (float): Input parameter `F`.
        dagger (float): Input parameter `dagger`.
        n (float): Input parameter `n`.
        rho (float): Input parameter `rho`.

    Returns:
        float: Calculated metric value.
    """
    return float(rho*(0*(F*(dagger*n))))


def expr_gamma_dagger_n_form_5(F: str = "F", dagger: str = "dagger", n: str = "n", rho: str = "rho") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_gamma_dagger_n_form_5`."""
    return (pl.col(rho)*(0*(pl.col(F)*(pl.col(dagger)*pl.col(n)))))


def calc_delta_m_form_6(a: float, g: float, i: float, m: float, n: float, r: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27193.

    **Source**:
    - Title: Low Residuals, Wrong Value: Learning the Viscosity Solution of Hamilton-Jacobi-Isaacs Equations with PINNs (2026)
    - Authors: Raul Jimenez, Pablo Tejerina-Pérez, Leonid Sarieddine et al.
    - Citation Key: `arxiv_2610_27193`

    **KaTeX Formula**:
    $$
    m* (\Delta ) = argmin m |zm| , z*(\Delta ) := zm* (\Delta ) , |z*| = d
    $$

    Args:
        a (float): Input parameter `a`.
        g (float): Input parameter `g`.
        i (float): Input parameter `i`.
        m (float): Input parameter `m`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(a*g*i*m**2*n*r*abs(m*z))


def expr_delta_m_form_6(a: str = "a", g: str = "g", i: str = "i", m: str = "m", n: str = "n", r: str = "r", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_m_form_6`."""
    return (pl.col(a)*pl.col(g)*pl.col(i)*pl.col(m)**2*pl.col(n)*pl.col(r)*abs(pl.col(m)*pl.col(z)))


def calc_partial_t_u_3_sim_l_u_3_form_7(F: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_39364.

    **Source**:
    - Title: Imperfect bifurcations in a laminar 3D bluff body wake: effect of pitch and yaw (2026)
    - Authors: Atharva Lagwankar, Alessandro Chiarini, François Gallaire et al.
    - Citation Key: `arxiv_2609_39364`

    **KaTeX Formula**:
    $$
    \partial tu3 + \sim Lu3 = F3
    $$

    Args:
        F (float): Input parameter `F`.

    Returns:
        float: Calculated metric value.
    """
    return float(3*F)


def expr_partial_t_u_3_sim_l_u_3_form_7(F: str = "F") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_partial_t_u_3_sim_l_u_3_form_7`."""
    return (3*pl.col(F))


def calc_z_form_8(beta: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_21163.

    **Source**:
    - Title: Simultaneous Estimation of Ballpark Effects and Team Defense Using Total Bases Residuals (2026)
    - Authors: Jhe-Jia Wu, Tian-Li Yan, Ting-Li Chen
    - Citation Key: `arxiv_2603_21163`

    **KaTeX Formula**:
    $$
    z =  \beta  -  \beta  s\beta
    $$

    Args:
        beta (float): Input parameter `beta`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(-beta*beta*s + beta)


def expr_z_form_8(beta: str = "beta", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_form_8`."""
    return (-pl.col(beta)*pl.col(beta)*pl.col(s) + pl.col(beta))


def calc_g_delta_form_8(do: float, n_14: float, p: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_04813.

    **Source**:
    - Title: A Markov Chain Approach to Modeling Rugby Union (2026)
    - Authors: Kenny Watts, Jonathan Pipping-Gamón
    - Citation Key: `arxiv_2610_04813`

    **KaTeX Formula**:
    $$
    g(\delta ) =  down_14p
    $$

    Args:
        do (float): Input parameter `do`.
        n_14 (float): Input parameter `n_14`.
        p (float): Input parameter `p`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(do*(w*(n_14*p)))


def expr_g_delta_form_8(do: str = "do", n_14: str = "n_14", p: str = "p", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_delta_form_8`."""
    return (pl.col(do)*(pl.col(w)*(pl.col(n_14)*pl.col(p))))


def calc_l_t_e_o_form_a(Upsilon: float, g: float, m: float, r: float, tau: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    Ltoe = \tau  + mgr \sin \theta  + \Upsilon
    $$

    Args:
        Upsilon (float): Input parameter `Upsilon`.
        g (float): Input parameter `g`.
        m (float): Input parameter `m`.
        r (float): Input parameter `r`.
        tau (float): Input parameter `tau`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(Upsilon + g*m*r*math.sin(theta) + tau)


def expr_l_t_e_o_form_a(Upsilon: str = "Upsilon", g: str = "g", m: str = "m", r: str = "r", tau: str = "tau", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_t_e_o_form_a`."""
    return (pl.col(Upsilon) + pl.col(g)*pl.col(m)*pl.col(r)*math.sin(pl.col(theta)) + pl.col(tau))


def calc_l_t_e_o_form_9(Upsilon: float, m: float, r: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    Ltoe =mr2  \theta  +\Upsilon
    $$

    Args:
        Upsilon (float): Input parameter `Upsilon`.
        m (float): Input parameter `m`.
        r (float): Input parameter `r`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(Upsilon + 2*m*r*theta)


def expr_l_t_e_o_form_9(Upsilon: str = "Upsilon", m: str = "m", r: str = "r", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_t_e_o_form_9`."""
    return (pl.col(Upsilon) + 2*pl.col(m)*pl.col(r)*pl.col(theta))


def calc_q_0_x_form_d(epsilon: float, q: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_39364.

    **Source**:
    - Title: Imperfect bifurcations in a laminar 3D bluff body wake: effect of pitch and yaw (2026)
    - Authors: Atharva Lagwankar, Alessandro Chiarini, François Gallaire et al.
    - Citation Key: `arxiv_2609_39364`

    **KaTeX Formula**:
    $$
    q0(x) = q0(x) + \epsilon q1(x)
    $$

    Args:
        epsilon (float): Input parameter `epsilon`.
        q (float): Input parameter `q`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(epsilon*q*x)


def expr_q_0_x_form_d(epsilon: str = "epsilon", q: str = "q", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_0_x_form_d`."""
    return (pl.col(epsilon)*pl.col(q)*pl.col(x))


def calc_sim_a_lambda_form_d(A: float, delta: float, sigma: float, sim: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_39364.

    **Source**:
    - Title: Imperfect bifurcations in a laminar 3D bluff body wake: effect of pitch and yaw (2026)
    - Authors: Atharva Lagwankar, Alessandro Chiarini, François Gallaire et al.
    - Citation Key: `arxiv_2609_39364`

    **KaTeX Formula**:
    $$
    \sim \lambda A = \sim \sigma A + \sim  \delta \langle u A\dagger  1 , -C( u A 1 , u \delta  2 ) - \nabla  2 u A 1 \rangle , (A 16)
    $$

    Args:
        A (float): Input parameter `A`.
        delta (float): Input parameter `delta`.
        sigma (float): Input parameter `sigma`.
        sim (float): Input parameter `sim`.

    Returns:
        float: Calculated metric value.
    """
    return float(delta*sim + sim*(A*sigma))


def expr_sim_a_lambda_form_d(A: str = "A", delta: str = "delta", sigma: str = "sigma", sim: str = "sim") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sim_a_lambda_form_d`."""
    return (pl.col(delta)*pl.col(sim) + pl.col(sim)*(pl.col(A)*pl.col(sigma)))


def calc_beta_p_a_r_k_p_form_e(a: float, beta: float, k: float, p: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2603_21163.

    **Source**:
    - Title: Simultaneous Estimation of Ballpark Effects and Team Defense Using Total Bases Residuals (2026)
    - Authors: Jhe-Jia Wu, Tian-Li Yan, Ting-Li Chen
    - Citation Key: `arxiv_2603_21163`

    **KaTeX Formula**:
    $$
    \beta park p =  \beta park p -  \beta park , \sim  \beta def d =  \beta def d -  \beta def
    $$

    Args:
        a (float): Input parameter `a`.
        beta (float): Input parameter `beta`.
        k (float): Input parameter `k`.
        p (float): Input parameter `p`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(-beta*p*(a*(k*r)) + beta*(p*(a*(r*(k*p)))))


def expr_beta_p_a_r_k_p_form_e(a: str = "a", beta: str = "beta", k: str = "k", p: str = "p", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_beta_p_a_r_k_p_form_e`."""
    return (-pl.col(beta)*pl.col(p)*(pl.col(a)*(pl.col(k)*pl.col(r))) + pl.col(beta)*(pl.col(p)*(pl.col(a)*(pl.col(r)*(pl.col(k)*pl.col(p))))))


def calc_delta_t_form_0(delta: float, n: float, r: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_20558.

    **Source**:
    - Title: Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction (2026)
    - Authors: Songyang Liu, Shuai Li
    - Citation Key: `arxiv_2609_20558`

    **KaTeX Formula**:
    $$
    \delta t =   \delta rn,t \delta q ^T t  ^T
    $$

    Args:
        delta (float): Input parameter `delta`.
        n (float): Input parameter `n`.
        r (float): Input parameter `r`.

    Returns:
        float: Calculated metric value.
    """
    return float(delta*n*r)


def expr_delta_t_form_0(delta: str = "delta", n: str = "n", r: str = "r") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_t_form_0`."""
    return (pl.col(delta)*pl.col(n)*pl.col(r))


def calc_t_c_form_2(M: float, T: float, c: float, q: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    Tc = 12 qTMc q, Vc = 1 2 qTKcq
    $$

    Args:
        M (float): Input parameter `M`.
        T (float): Input parameter `T`.
        c (float): Input parameter `c`.
        q (float): Input parameter `q`.

    Returns:
        float: Calculated metric value.
    """
    return float(12*M*T*c*q**2)


def expr_t_c_form_2(M: str = "M", T: str = "T", c: str = "c", q: str = "q") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_c_form_2`."""
    return (12*pl.col(M)*pl.col(T)*pl.col(c)*pl.col(q)**2)


def calc_delta_m_s_e_e_form_3(B: float, C: float, E: float, G: float, M: float, R: float, S: float, U: float, e: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    \Delta MSE e =MSEGRU e -MSEBCS e
    $$

    Args:
        B (float): Input parameter `B`.
        C (float): Input parameter `C`.
        E (float): Input parameter `E`.
        G (float): Input parameter `G`.
        M (float): Input parameter `M`.
        R (float): Input parameter `R`.
        S (float): Input parameter `S`.
        U (float): Input parameter `U`.
        e (float): Input parameter `e`.

    Returns:
        float: Calculated metric value.
    """
    return float(-M*S*(E*(B*(C*(S*e)))) + M*(S*(E*(G*(R*(U*e))))))


def expr_delta_m_s_e_e_form_3(B: str = "B", C: str = "C", E: str = "E", G: str = "G", M: str = "M", R: str = "R", S: str = "S", U: str = "U", e: str = "e") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_m_s_e_e_form_3`."""
    return (-pl.col(M)*pl.col(S)*(pl.col(E)*(pl.col(B)*(pl.col(C)*(pl.col(S)*pl.col(e))))) + pl.col(M)*(pl.col(S)*(pl.col(E)*(pl.col(G)*(pl.col(R)*(pl.col(U)*pl.col(e)))))))


def calc_r_f_l_a_k_t_form_3(L: float, W: float, p: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_02306.

    **Source**:
    - Title: Contact-Constrained Lower-Limb Joint-Offset Calibration for Humanoid Robots (2026)
    - Authors: Kaixiang Lu, Haiyu Lan, Chunxiao Qiao et al.
    - Citation Key: `arxiv_2609_02306`

    **KaTeX Formula**:
    $$
    rflat k =  pWL,z - pWR,z zW L,x zW L,y zW R,x zW R,y  \in  R5
    $$

    Args:
        L (float): Input parameter `L`.
        W (float): Input parameter `W`.
        p (float): Input parameter `p`.

    Returns:
        float: Calculated metric value.
    """
    return float(L*W*p)


def expr_r_f_l_a_k_t_form_3(L: str = "L", W: str = "W", p: str = "p") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_f_l_a_k_t_form_3`."""
    return (pl.col(L)*pl.col(W)*pl.col(p))


def calc_t_x_phi_form_4(phi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_26548.

    **Source**:
    - Title: Camera Calibration Using Inaccurate and Asynchronous Discrete GPS Trajectory from Drones (2026)
    - Authors: R. Yang, Y. Bar-Shalom, H. A. J. Huang
    - Citation Key: `arxiv_2608_26548`

    **KaTeX Formula**:
    $$
    Tx (\phi ) =  1 0 0 0 \cos\phi  \sin\phi  0 -\sin\phi  \cos\phi
    $$

    Args:
        phi (float): Input parameter `phi`.

    Returns:
        float: Calculated metric value.
    """
    return float(-math.sin(phi)*math.cos(phi))


def expr_t_x_phi_form_4(phi: str = "phi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_x_phi_form_4`."""
    return (-math.sin(pl.col(phi))*math.cos(pl.col(phi)))


def calc_h_form_8(h: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_26548.

    **Source**:
    - Title: Camera Calibration Using Inaccurate and Asynchronous Discrete GPS Trajectory from Drones (2026)
    - Authors: R. Yang, Y. Bar-Shalom, H. A. J. Huang
    - Citation Key: `arxiv_2608_26548`

    **KaTeX Formula**:
    $$
    H =   h1[\alpha , \epsilon , \rho , ˘x(t1)] . . . hn[\alpha , \epsilon , \rho , ˘x(tn)]
    $$

    Args:
        h (float): Input parameter `h`.

    Returns:
        float: Calculated metric value.
    """
    return float(h)


def expr_h_form_8(h: str = "h") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_form_8`."""
    return (pl.col(h))


def calc_x_form_8(S: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_38730.

    **Source**:
    - Title: Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics (2026)
    - Authors: Haichuan Li
    - Citation Key: `arxiv_2609_38730`

    **KaTeX Formula**:
    $$
    x = 1S S\sum  i=1 xi, sx = \sqrt \sqrt \sqrt \sqrt  1 S - 1 S\sum  i=1 (xi - x)2
    $$

    Args:
        S (float): Input parameter `S`.

    Returns:
        float: Calculated metric value.
    """
    return float(1*(S*S))


def expr_x_form_8(S: str = "S") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_form_8`."""
    return (1*(pl.col(S)*pl.col(S)))


def calc_t_alpha_epsilon_rho_form_8(alpha: float, c: float, epsilon: float, rho: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_26548.

    **Source**:
    - Title: Camera Calibration Using Inaccurate and Asynchronous Discrete GPS Trajectory from Drones (2026)
    - Authors: R. Yang, Y. Bar-Shalom, H. A. J. Huang
    - Citation Key: `arxiv_2608_26548`

    **KaTeX Formula**:
    $$
    T(\alpha , \epsilon , \rho ) =  c\alpha c\rho  + s\alpha s\epsilon s\rho  c\alpha s\epsilon s\rho  - s\alpha c\rho  -c\epsilon s\rho  s\alpha s\epsilon c\rho  - c\alpha s\rho  s\alpha s\rho  + c\alpha s\epsilon c\rho  -c\epsilon c\rho  s\alpha c\epsilon  c\alpha c\epsilon  s\epsilon
    $$

    Args:
        alpha (float): Input parameter `alpha`.
        c (float): Input parameter `c`.
        epsilon (float): Input parameter `epsilon`.
        rho (float): Input parameter `rho`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(-alpha**2*c**5*epsilon**4*rho*s**2 + alpha**2*c*epsilon**2*rho**2*s**5 - alpha**2*c*rho**2*s**3 - alpha*c**2*epsilon**2*rho**2*s**3 + alpha*c**2*epsilon*rho*s + alpha*c**2*rho - alpha*c*rho*s)


def expr_t_alpha_epsilon_rho_form_8(alpha: str = "alpha", c: str = "c", epsilon: str = "epsilon", rho: str = "rho", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_alpha_epsilon_rho_form_8`."""
    return (-pl.col(alpha)**2*pl.col(c)**5*pl.col(epsilon)**4*pl.col(rho)*pl.col(s)**2 + pl.col(alpha)**2*pl.col(c)*pl.col(epsilon)**2*pl.col(rho)**2*pl.col(s)**5 - pl.col(alpha)**2*pl.col(c)*pl.col(rho)**2*pl.col(s)**3 - pl.col(alpha)*pl.col(c)**2*pl.col(epsilon)**2*pl.col(rho)**2*pl.col(s)**3 + pl.col(alpha)*pl.col(c)**2*pl.col(epsilon)*pl.col(rho)*pl.col(s) + pl.col(alpha)*pl.col(c)**2*pl.col(rho) - pl.col(alpha)*pl.col(c)*pl.col(rho)*pl.col(s))


def calc_e_m_p_j_e_p_form_8(J: float, T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_20558.

    **Source**:
    - Title: Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction (2026)
    - Authors: Songyang Liu, Shuai Li
    - Citation Key: `arxiv_2609_20558`

    **KaTeX Formula**:
    $$
    EMPJPE = 1 |T |J \sum  t \in T J\sum  j =1      x exec j ,t - x ref j ,t       2
    $$

    Args:
        J (float): Input parameter `J`.
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(J*abs(T))


def expr_e_m_p_j_e_p_form_8(J: str = "J", T: str = "T") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_m_p_j_e_p_form_8`."""
    return (pl.col(J)*abs(pl.col(T)))


def calc_l_p_r_i_o_r_form_9(T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_20558.

    **Source**:
    - Title: Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction (2026)
    - Authors: Songyang Liu, Shuai Li
    - Citation Key: `arxiv_2609_20558`

    **KaTeX Formula**:
    $$
    Lprior = T\sum  t=1 |\delta t | 2 W
    $$

    Args:
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(T)


def expr_l_p_r_i_o_r_form_9(T: str = "T") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_p_r_i_o_r_form_9`."""
    return (pl.col(T))


def calc_d_i_form_a(delta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_26548.

    **Source**:
    - Title: Camera Calibration Using Inaccurate and Asynchronous Discrete GPS Trajectory from Drones (2026)
    - Authors: R. Yang, Y. Bar-Shalom, H. A. J. Huang
    - Citation Key: `arxiv_2608_26548`

    **KaTeX Formula**:
    $$
    Di =  Ti-\delta  -0.5T 2i-\delta  . . . . . . Ti-1 -0.5T 2i-1
    $$

    Args:
        delta (float): Input parameter `delta`.

    Returns:
        float: Calculated metric value.
    """
    return float(-2*delta)


def expr_d_i_form_a(delta: str = "delta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_i_form_a`."""
    return (-2*pl.col(delta))


def calc_m_form_c(q: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_20558.

    **Source**:
    - Title: Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction (2026)
    - Authors: Songyang Liu, Shuai Li
    - Citation Key: `arxiv_2609_20558`

    **KaTeX Formula**:
    $$
    M =   qt ,  qt , p b t , R b t  T t=1
    $$

    Args:
        q (float): Input parameter `q`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(q*t)


def expr_m_form_c(q: str = "q", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_form_c`."""
    return (pl.col(q)*pl.col(t))


def calc_j_theta_form_d(T: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_20558.

    **Source**:
    - Title: Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction (2026)
    - Authors: Songyang Liu, Shuai Li
    - Citation Key: `arxiv_2609_20558`

    **KaTeX Formula**:
    $$
    J(\theta ) = E\pi \theta    T-1\sum  t=0 \gamma  t rt
    $$

    Args:
        T (float): Input parameter `T`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e*math.pi*T*theta - 1)


def expr_j_theta_form_d(T: str = "T", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_theta_form_d`."""
    return (math.e*math.pi*pl.col(T)*pl.col(theta) - 1)


def calc_m_y_t_form_d(Y: float, t: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2610_27416.

    **Source**:
    - Title: Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization (2026)
    - Authors: Koichi Miyamoto
    - Citation Key: `arxiv_2610_27416`

    **KaTeX Formula**:
    $$
    mY(t) = E[Y1 t ] ... E[YJ t ]
    $$

    Args:
        Y (float): Input parameter `Y`.
        t (float): Input parameter `t`.

    Returns:
        float: Calculated metric value.
    """
    return float(math.e*Y*t)


def expr_m_y_t_form_d(Y: str = "Y", t: str = "t") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_y_t_form_d`."""
    return (math.e*pl.col(Y)*pl.col(t))


def calc_e_w_o_k_r_form_d(T: float, w: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_20558.

    **Source**:
    - Title: Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction (2026)
    - Authors: Songyang Liu, Shuai Li
    - Citation Key: `arxiv_2609_20558`

    **KaTeX Formula**:
    $$
    Ework = 1 |Tw | \sum  t \in Tw    dhand,t - dw
    $$

    Args:
        T (float): Input parameter `T`.
        w (float): Input parameter `w`.

    Returns:
        float: Calculated metric value.
    """
    return float(abs(T*w))


def expr_e_w_o_k_r_form_d(T: str = "T", w: str = "w") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_w_o_k_r_form_d`."""
    return (abs(pl.col(T)*pl.col(w)))


def calc_x_form_e(A: float, B: float, r: float, x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_17701.

    **Source**:
    - Title: Barrier Functions Against Safety Drift in Shared Control (2026)
    - Authors: M. Yusuf Uzun, Yildiray Yildiz
    - Citation Key: `arxiv_2609_17701`

    **KaTeX Formula**:
    $$
    x = A x+Br r, x(t0) = x(t0)
    $$

    Args:
        A (float): Input parameter `A`.
        B (float): Input parameter `B`.
        r (float): Input parameter `r`.
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(A*x + B*r**2)


def expr_x_form_e(A: str = "A", B: str = "B", r: str = "r", x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_form_e`."""
    return (pl.col(A)*pl.col(x) + pl.col(B)*pl.col(r)**2)


def calc_eta_k_t_form_e(C: float, m: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_11476.

    **Source**:
    - Title: 3D Euler-Angle Orientation Control for Two-Ray Fading Mitigation in Maritime Air-to-Sea Communications (2026)
    - Authors: Mohammed Bajja, Abdoul Karim A. H. Saliah, Hajar El Hammouti et al.
    - Citation Key: `arxiv_2609_11476`

    **KaTeX Formula**:
    $$
    k^T\eta  = Cm, Cm = (2m+1)\pi  -\Delta \Phi 0, m \in  Z
    $$

    Args:
        C (float): Input parameter `C`.
        m (float): Input parameter `m`.

    Returns:
        float: Calculated metric value.
    """
    return float(C*m)


def expr_eta_k_t_form_e(C: str = "C", m: str = "m") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_eta_k_t_form_e`."""
    return (pl.col(C)*pl.col(m))


def calc_l_dagger_form_e(C: float, dagger: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_39364.

    **Source**:
    - Title: Imperfect bifurcations in a laminar 3D bluff body wake: effect of pitch and yaw (2026)
    - Authors: Atharva Lagwankar, Alessandro Chiarini, François Gallaire et al.
    - Citation Key: `arxiv_2609_39364`

    **KaTeX Formula**:
    $$
    L \dagger  =   C \dagger  (\cdot , u0) - Re -1 \nabla  2 (\cdot ) \nabla (\cdot ) \nabla  \cdot  (\cdot ) 0
    $$

    Args:
        C (float): Input parameter `C`.
        dagger (float): Input parameter `dagger`.

    Returns:
        float: Calculated metric value.
    """
    return float(C*dagger)


def expr_l_dagger_form_e(C: str = "C", dagger: str = "dagger") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_dagger_form_e`."""
    return (pl.col(C)*pl.col(dagger))


def calc_partial_z_c_k_alpha_partial_form_e(Delta: float, alpha: float, c: float, epsilon: float, k: float, s: float, x: float, y: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_26548.

    **Source**:
    - Title: Camera Calibration Using Inaccurate and Asynchronous Discrete GPS Trajectory from Drones (2026)
    - Authors: R. Yang, Y. Bar-Shalom, H. A. J. Huang
    - Citation Key: `arxiv_2608_26548`

    **KaTeX Formula**:
    $$
    \partial zC k \partial \alpha  = \Delta xkc\alpha c\epsilon  -\Delta yks\alpha c\epsilon
    $$

    Args:
        Delta (float): Input parameter `Delta`.
        alpha (float): Input parameter `alpha`.
        c (float): Input parameter `c`.
        epsilon (float): Input parameter `epsilon`.
        k (float): Input parameter `k`.
        s (float): Input parameter `s`.
        x (float): Input parameter `x`.
        y (float): Input parameter `y`.

    Returns:
        float: Calculated metric value.
    """
    return float(Delta*alpha*c**2*epsilon*k*x - Delta*alpha*c*epsilon*k*s*y)


def expr_partial_z_c_k_alpha_partial_form_e(Delta: str = "Delta", alpha: str = "alpha", c: str = "c", epsilon: str = "epsilon", k: str = "k", s: str = "s", x: str = "x", y: str = "y") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_partial_z_c_k_alpha_partial_form_e`."""
    return (pl.col(Delta)*pl.col(alpha)*pl.col(c)**2*pl.col(epsilon)*pl.col(k)*pl.col(x) - pl.col(Delta)*pl.col(alpha)*pl.col(c)*pl.col(epsilon)*pl.col(k)*pl.col(s)*pl.col(y))


def calc_omega_t_a_alpha_form_f(A: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2604_21851.

    **Source**:
    - Title: Betting on Bets: Anytime-Valid Tests for Stochastic Dominance (2026)
    - Authors: Sebastian Arnold, Yo Joong Choe, Marco Scarsini et al.
    - Citation Key: `arxiv_2604_21851`

    **KaTeX Formula**:
    $$
    \omega t(A, \alpha ) = A\sqrt \log \log(et∕tmin) + C(A, \alpha ) t
    $$

    Args:
        A (float): Input parameter `A`.

    Returns:
        float: Calculated metric value.
    """
    return float(A)


def expr_omega_t_a_alpha_form_f(A: str = "A") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_omega_t_a_alpha_form_f`."""
    return (pl.col(A))


def calc_val_2609_24299_form_0(Q: float, gamma: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    d dt ( \partial L \partial  \gamma  ) - \partial L \partial \gamma  = Q\gamma
    $$

    Args:
        Q (float): Input parameter `Q`.
        gamma (float): Input parameter `gamma`.

    Returns:
        float: Calculated metric value.
    """
    return float(Q*gamma)


def expr_val_2609_24299_form_0(Q: str = "Q", gamma: str = "gamma") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_24299_form_0`."""
    return (pl.col(Q)*pl.col(gamma))


def calc_delta_0_form_0(R: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_27423.

    **Source**:
    - Title: High-order stabilized matrix-free simulation of rotating mixing devices using the Mortar Element Method (2026)
    - Authors: B. Campos, P. Munch, V. O. Ferreira et al.
    - Citation Key: `arxiv_2608_27423`

    **KaTeX Formula**:
    $$
    \delta 0 =  2\pi R nR , for aligned meshes, \alpha  or 2\pi R nR -\alpha , for misaligned meshes
    $$

    Args:
        R (float): Input parameter `R`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*math.pi*R**2*n)


def expr_delta_0_form_0(R: str = "R", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_delta_0_form_0`."""
    return (2*math.pi*pl.col(R)**2*pl.col(n))


def calc_k_phi_c_form_1(M: float, Omega: float, Phi: float, c: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    Kc\Phi  = Mc\Phi \Omega 2
    $$

    Args:
        M (float): Input parameter `M`.
        Omega (float): Input parameter `Omega`.
        Phi (float): Input parameter `Phi`.
        c (float): Input parameter `c`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*M*Omega*Phi*c)


def expr_k_phi_c_form_1(M: str = "M", Omega: str = "Omega", Phi: str = "Phi", c: str = "c") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_phi_c_form_1`."""
    return (2*pl.col(M)*pl.col(Omega)*pl.col(Phi)*pl.col(c))


def calc_a_q_form_4(phi: float, tau: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_10387.

    **Source**:
    - Title: Hip Energized Monopedal Hopping (2026)
    - Authors: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
    - Citation Key: `arxiv_2608_10387`

    **KaTeX Formula**:
    $$
    q* a = \phi * \phi *  \tau  *  =  \phi d 0 mg r0 (\chi dx - r0 \sin (\Xi \theta ,g))
    $$

    Args:
        phi (float): Input parameter `phi`.
        tau (float): Input parameter `tau`.

    Returns:
        float: Calculated metric value.
    """
    return float(phi**2*tau)


def expr_a_q_form_4(phi: str = "phi", tau: str = "tau") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_q_form_4`."""
    return (pl.col(phi)**2*pl.col(tau))


def calc_x_1_form_4(x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    x1 = x2, x2 = M(x1)-1(G u - d(x1, x2))
    $$

    Args:
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*x)


def expr_x_1_form_4(x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_1_form_4`."""
    return (2*pl.col(x))


def calc_i_omega_omega_i_omega_form_8(M: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_23163.

    **Source**:
    - Title: Spinning Quadrotor: Hover Thrust Augmentation with Passive Lifting Surfaces (2026)
    - Authors: Aniketh Parkala, Harikumar Kandath
    - Citation Key: `arxiv_2608_23163`

    **KaTeX Formula**:
    $$
    I \omega +\omega \times  (I\omega ) =M
    $$

    Args:
        M (float): Input parameter `M`.

    Returns:
        float: Calculated metric value.
    """
    return float(M)


def expr_i_omega_omega_i_omega_form_8(M: str = "M") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_omega_omega_i_omega_form_8`."""
    return (pl.col(M))


def calc_epsilon_n_form_9(T: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_27423.

    **Source**:
    - Title: High-order stabilized matrix-free simulation of rotating mixing devices using the Mortar Element Method (2026)
    - Authors: B. Campos, P. Munch, V. O. Ferreira et al.
    - Citation Key: `arxiv_2608_27423`

    **KaTeX Formula**:
    $$
    -\epsilon n = 1 T (\int  \Omega  \partial  \partial t ( 12 u2) d\Omega  + \int  \partial \Omega  n \cdot  ([\tau  + p* ] \cdot  u)d\partial \Omega + \int  \Omega (-\tau  : \nabla u)d\Omega )
    $$

    Args:
        T (float): Input parameter `T`.

    Returns:
        float: Calculated metric value.
    """
    return float(T)


def expr_epsilon_n_form_9(T: str = "T") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_epsilon_n_form_9`."""
    return (pl.col(T))


def calc_p_i_n_form_a(F: float, M: float, h: float, theta: float, y: float, z: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_05500.

    **Source**:
    - Title: Performance comparison of tethered and self-propelled models of fish locomotion using unsteady thin airfoil theory (2026)
    - Authors: Anshul Nayak, Emad Masroor, Hodjat Pendar
    - Citation Key: `arxiv_2609_05500`

    **KaTeX Formula**:
    $$
    Pin = Fy h+Mz  \theta
    $$

    Args:
        F (float): Input parameter `F`.
        M (float): Input parameter `M`.
        h (float): Input parameter `h`.
        theta (float): Input parameter `theta`.
        y (float): Input parameter `y`.
        z (float): Input parameter `z`.

    Returns:
        float: Calculated metric value.
    """
    return float(F*h*y + M*theta*z)


def expr_p_i_n_form_a(F: str = "F", M: str = "M", h: str = "h", theta: str = "theta", y: str = "y", z: str = "z") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_n_form_a`."""
    return (pl.col(F)*pl.col(h)*pl.col(y) + pl.col(M)*pl.col(theta)*pl.col(z))


def calc_val_2609_24299_form_a(Q: float, phi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    d dt ( \partial L \partial  \phi  ) - \partial L \partial \phi  = Q\phi
    $$

    Args:
        Q (float): Input parameter `Q`.
        phi (float): Input parameter `phi`.

    Returns:
        float: Calculated metric value.
    """
    return float(Q*phi)


def expr_val_2609_24299_form_a(Q: str = "Q", phi: str = "phi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_24299_form_a`."""
    return (pl.col(Q)*pl.col(phi))


def calc_val_2609_24299_form_b(Q: float, s: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    d dt ( \partial L \partial  s ) - \partial L \partial s = Qs
    $$

    Args:
        Q (float): Input parameter `Q`.
        s (float): Input parameter `s`.

    Returns:
        float: Calculated metric value.
    """
    return float(Q*s)


def expr_val_2609_24299_form_b(Q: str = "Q", s: str = "s") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_2609_24299_form_b`."""
    return (pl.col(Q)*pl.col(s))


def calc_omega_form_e(Omega: float, cup: float, n: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2608_27423.

    **Source**:
    - Title: High-order stabilized matrix-free simulation of rotating mixing devices using the Mortar Element Method (2026)
    - Authors: B. Campos, P. Munch, V. O. Ferreira et al.
    - Citation Key: `arxiv_2608_27423`

    **KaTeX Formula**:
    $$
    \Omega  = \cup  \Omega n, \Omega l \cap  \Omega m = \emptyset , \forall  l,m, l ̸=m, n = 1, \cdot  \cdot  \cdot  ,N
    $$

    Args:
        Omega (float): Input parameter `Omega`.
        cup (float): Input parameter `cup`.
        n (float): Input parameter `n`.

    Returns:
        float: Calculated metric value.
    """
    return float(Omega*cup*n)


def expr_omega_form_e(Omega: str = "Omega", cup: str = "cup", n: str = "n") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_omega_form_e`."""
    return (pl.col(Omega)*pl.col(cup)*pl.col(n))


def calc_x_1_form_f(x: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    x1 = x2, x2 = M(x1)-1( Gu-  d(x1, x2))
    $$

    Args:
        x (float): Input parameter `x`.

    Returns:
        float: Calculated metric value.
    """
    return float(2*x)


def expr_x_1_form_f(x: str = "x") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_1_form_f`."""
    return (2*pl.col(x))


def calc_sim_b_lambda_form_f(B: float, delta: float, sigma: float, sim: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_39364.

    **Source**:
    - Title: Imperfect bifurcations in a laminar 3D bluff body wake: effect of pitch and yaw (2026)
    - Authors: Atharva Lagwankar, Alessandro Chiarini, François Gallaire et al.
    - Citation Key: `arxiv_2609_39364`

    **KaTeX Formula**:
    $$
    \sim \lambda B = \sim \sigma B + \sim  \delta \langle u B\dagger  1 , -C( u B 1 , u \delta  2 ) - \nabla  2 u B 1 \rangle , (A 19)
    $$

    Args:
        B (float): Input parameter `B`.
        delta (float): Input parameter `delta`.
        sigma (float): Input parameter `sigma`.
        sim (float): Input parameter `sim`.

    Returns:
        float: Calculated metric value.
    """
    return float(delta*sim + sim*(B*sigma))


def expr_sim_b_lambda_form_f(B: str = "B", delta: str = "delta", sigma: str = "sigma", sim: str = "sim") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_sim_b_lambda_form_f`."""
    return (pl.col(delta)*pl.col(sim) + pl.col(sim)*(pl.col(B)*pl.col(sigma)))


def calc_r_x_phi_form_f(phi: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    Rx(\phi ) = 1 0 0 0 \cos\phi  -\sin\phi  0 \sin\phi  \cos\phi
    $$

    Args:
        phi (float): Input parameter `phi`.

    Returns:
        float: Calculated metric value.
    """
    return float(1000*math.cos(phi))


def expr_r_x_phi_form_f(phi: str = "phi") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_x_phi_form_f`."""
    return (1000*math.cos(pl.col(phi)))


def calc_m_xi_form_f(M: float, gamma: float, phi: float, q: float, s: float, theta: float) -> float:
    r"""Compute mathematical metric extracted from arxiv_2609_24299.

    **Source**:
    - Title: Nonlinear Dynamic Modeling and Receding-Horizon NMPC of an Electric Unicycle on a Tensioned Cable (2026)
    - Authors: Yousef Sweiti, Jasem Tamimi
    - Citation Key: `arxiv_2609_24299`

    **KaTeX Formula**:
    $$
    M(\xi ) =  Mqq Mqs Mq\phi  Mq\theta  0 Msq Mss Ms\phi  Ms\theta  0 M\phi q M\phi s M\phi \phi  0 M\phi \gamma  M\theta q M\theta s 0 M\theta \theta  0 0 0 M\gamma \phi  0 M\gamma \gamma
    $$

    Args:
        M (float): Input parameter `M`.
        gamma (float): Input parameter `gamma`.
        phi (float): Input parameter `phi`.
        q (float): Input parameter `q`.
        s (float): Input parameter `s`.
        theta (float): Input parameter `theta`.

    Returns:
        float: Calculated metric value.
    """
    return float(M*(q*(q*(M*(q*(s*(M*(q*(phi*(M*(q*(theta*(0*(M*(s*(q*(M*(s*(s*(M*(s*(phi*(M*(s*(theta*(0*(M*(phi*(q*(M*(phi*(s*(M*(phi*(phi*(0*(M*(phi*(gamma*(M*(theta*(q*(M*(theta*(s*(0*(M*(theta*(theta*(0*(M*(gamma*(phi*(0*(M*(gamma*gamma))))))))))))))))))))))))))))))))))))))))))))))))))))))))


def expr_m_xi_form_f(M: str = "M", gamma: str = "gamma", phi: str = "phi", q: str = "q", s: str = "s", theta: str = "theta") -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_xi_form_f`."""
    return (pl.col(M)*(pl.col(q)*(pl.col(q)*(pl.col(M)*(pl.col(q)*(pl.col(s)*(pl.col(M)*(pl.col(q)*(pl.col(phi)*(pl.col(M)*(pl.col(q)*(pl.col(theta)*(0*(pl.col(M)*(pl.col(s)*(pl.col(q)*(pl.col(M)*(pl.col(s)*(pl.col(s)*(pl.col(M)*(pl.col(s)*(pl.col(phi)*(pl.col(M)*(pl.col(s)*(pl.col(theta)*(0*(pl.col(M)*(pl.col(phi)*(pl.col(q)*(pl.col(M)*(pl.col(phi)*(pl.col(s)*(pl.col(M)*(pl.col(phi)*(pl.col(phi)*(0*(pl.col(M)*(pl.col(phi)*(pl.col(gamma)*(pl.col(M)*(pl.col(theta)*(pl.col(q)*(pl.col(M)*(pl.col(theta)*(pl.col(s)*(0*(pl.col(M)*(pl.col(theta)*(pl.col(theta)*(0*(pl.col(M)*(pl.col(gamma)*(pl.col(phi)*(0*(pl.col(M)*(pl.col(gamma)*pl.col(gamma)))))))))))))))))))))))))))))))))))))))))))))))))))))))))

