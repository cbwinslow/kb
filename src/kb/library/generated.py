# ruff: noqa
"""Auto-generated standalone scientific formula library.

Compiled directly from peer-reviewed research preprints in the Knowledge Base.
Each formula provides typed Python scalar execution and vectorized Polars expressions.
"""

from __future__ import annotations

import math

import polars as pl

__all__ = [
    "calc_val_1205_4750_1205_4",
    "expr_val_1205_4750_1205_4",
    "calc_w_a_r_q_1312_7",
    "expr_w_a_r_q_1312_7",
    "calc_w_p_c_t_p_r_s_r_a_1312_7",
    "expr_w_p_c_t_p_r_s_r_a_1312_7",
    "calc_val_1406_3402_1406_3",
    "expr_val_1406_3402_1406_3",
    "calc_d_a_h_1603_0",
    "expr_d_a_h_1603_0",
    "calc_t_2210_0",
    "expr_t_2210_0",
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
    "calc_p_i_j_p_i_j_p_j_k_p_j_k_bt_sec",
    "expr_p_i_j_p_i_j_p_j_k_p_j_k_bt_sec",
    "calc_bt_secondary_many_routes_2023_bt_sec",
    "expr_bt_secondary_many_routes_2023_bt_sec",
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
    "calc_f_diebol",
    "expr_f_diebol",
    "calc_r_diebol",
    "expr_r_diebol",
    "calc_a_p_m_efron_",
    "expr_a_p_m_efron_",
    "calc_b_p_egidi_",
    "expr_b_p_egidi_",
    "calc_s_s_k_i_l_l_n_gneiti",
    "expr_s_s_k_i_l_l_n_gneiti",
    "calc_s_c_p_1_gneiti",
    "expr_s_c_p_1_gneiti",
    "calc_g_p_gneiti",
    "expr_g_p_gneiti",
    "calc_b_gneiti",
    "expr_b_gneiti",
    "calc_l_o_b_g_gneiti",
    "expr_l_o_b_g_gneiti",
    "calc_s_2_harvey",
    "expr_s_2_harvey",
    "calc_val_1_12_2_harvey",
    "expr_val_1_12_2_harvey",
    "calc_c_i_maher_",
    "expr_c_i_maher_",
    "calc_z_l_y_u_c_c_u_x_i_k_2_j_r_maher_",
    "expr_z_l_y_u_c_c_u_x_i_k_2_j_r_maher_",
    "calc_t_form_c",
    "expr_t_form_c",
    "calc_f_x_form_5",
    "expr_f_x_form_5",
    "calc_h_p_form_6",
    "expr_h_p_form_6",
    "calc_q_s_form_9",
    "expr_q_s_form_9",
    "calc_w_e_s_form_9",
    "expr_w_e_s_form_9",
    "calc_v_v_1_form_e",
    "expr_v_v_1_form_e",
    "calc_eq_e_x_e_f_y_form_8",
    "expr_eq_e_x_e_f_y_form_8",
    "calc_l_z_form_a",
    "expr_l_z_form_a",
    "calc_begin_x_k_a_l_i_g_n_d_e_form_4",
    "expr_begin_x_k_a_l_i_g_n_d_e_form_4",
    "calc_p_i_j_form_6",
    "expr_p_i_j_form_6",
    "calc_w_a_p_form_9",
    "expr_w_a_p_form_9",
    "calc_i_n_de_x_form_0",
    "expr_i_n_de_x_form_0",
    "calc_s_form_e",
    "expr_s_form_e",
    "calc_l_a_a_i_form_6",
    "expr_l_a_a_i_form_6",
    "calc_z_form_4",
    "expr_z_form_4",
    "calc_l_v_a_l_form_4",
    "expr_l_v_a_l_form_4",
    "calc_e_r_e_c_n_o_form_c",
    "expr_e_r_e_c_n_o_form_c",
    "calc_e_b_a_e_s_form_3",
    "expr_e_b_a_e_s_form_3",
    "calc_e_f_i_n_a_l_form_e",
    "expr_e_f_i_n_a_l_form_e",
    "calc_g_s_p_e_c_t_r_a_l_form_5",
    "expr_g_s_p_e_c_t_r_a_l_form_5",
    "calc_l_f_m_form_8",
    "expr_l_f_m_form_8",
    "calc_l_b_a_e_s_form_a",
    "expr_l_b_a_e_s_form_a",
    "calc_p_u_form_5",
    "expr_p_u_form_5",
    "calc_y_r_s_h_s_y_p_s_form_1",
    "expr_y_r_s_h_s_y_p_s_form_1",
    "calc_h_y_form_2",
    "expr_h_y_form_2",
    "calc_l_0_p_w_form_0",
    "expr_l_0_p_w_form_0",
    "calc_l_g_a_p_w_form_8",
    "expr_l_g_a_p_w_form_8",
    "calc_a_t_w_o_w_a_o_form_9",
    "expr_a_t_w_o_w_a_o_form_9",
    "calc_u_l_s_o_form_4",
    "expr_u_l_s_o_form_4",
    "calc_r_s_form_6",
    "expr_r_s_form_6",
    "calc_l_form_9",
    "expr_l_form_9",
    "calc_m_q_q_form_5",
    "expr_m_q_q_form_5",
    "calc_c_p_form_a",
    "expr_c_p_form_a",
    "calc_c_t_form_0",
    "expr_c_t_form_0",
    "calc_l_form_c",
    "expr_l_form_c",
    "calc_ds_dw_form_d",
    "expr_ds_dw_form_d",
    "calc_w_form_a",
    "expr_w_form_a",
    "calc_dt_dw_form_f",
    "expr_dt_dw_form_f",
    "calc_j_form_5",
    "expr_j_form_5",
    "calc_p_b_a_s_e_l_i_e_n_form_9",
    "expr_p_b_a_s_e_l_i_e_n_form_9",
    "calc_a_l_r_form_a",
    "expr_a_l_r_form_a",
    "calc_c_2_s_r_z_form_9",
    "expr_c_2_s_r_z_form_9",
    "calc_a_form_2",
    "expr_a_form_2",
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
    "calc_p_i_t_form_6",
    "expr_p_i_t_form_6",
    "calc_c_g_f_r_form_c",
    "expr_c_g_f_r_form_c",
    "calc_l_r_o_l_l_j_o_i_n_form_9",
    "expr_l_r_o_l_l_j_o_i_n_form_9",
    "calc_l_r_o_l_l_e_x_c_e_s_s_form_c",
    "expr_l_r_o_l_l_e_x_c_e_s_s_form_c",
    "calc_p_c_i_j_form_9",
    "expr_p_c_i_j_form_9",
    "calc_k_1_form_3",
    "expr_k_1_form_3",
    "calc_s_w_form_8",
    "expr_s_w_form_8",
    "calc_w_b_x_form_1",
    "expr_w_b_x_form_1",
    "calc_w_b_r_form_3",
    "expr_w_b_r_form_3",
    "calc_w_c_x_form_9",
    "expr_w_c_x_form_9",
    "calc_w_c_r_form_1",
    "expr_w_c_r_form_1",
    "calc_w_b_r_form_0",
    "expr_w_b_r_form_0",
    "calc_q_dt_p_form_c",
    "expr_q_dt_p_form_c",
    "calc_r_m_d_i_form_5",
    "expr_r_m_d_i_form_5",
    "calc_e_p_form_3",
    "expr_e_p_form_3",
    "calc_f_c_d_m_form_a",
    "expr_f_c_d_m_form_a",
    "calc_e_form_1",
    "expr_e_form_1",
    "calc_h_a_p_e_x_form_b",
    "expr_h_a_p_e_x_form_b",
    "calc_e_p_form_1",
    "expr_e_p_form_1",
    "calc_t_p_x_p_y_p_z_1_form_5",
    "expr_t_p_x_p_y_p_z_1_form_5",
    "calc_j_p_form_d",
    "expr_j_p_form_d",
    "calc_c_e_x_a_c_t_form_f",
    "expr_c_e_x_a_c_t_form_f",
    "calc_u_o_t_v_form_c",
    "expr_u_o_t_v_form_c",
    "calc_a_form_4",
    "expr_a_form_4",
    "calc_l_v_r_r_e_e_2223_form_7",
    "expr_l_v_r_r_e_e_2223_form_7",
    "calc_l_i_m_i_n_f_n_b_n_form_0",
    "expr_l_i_m_i_n_f_n_b_n_form_0",
    "calc_z_m_i_x_form_7",
    "expr_z_m_i_x_form_7",
    "calc_e_j_form_6",
    "expr_e_j_form_6",
    "calc_p_form_2",
    "expr_p_form_2",
    "calc_r_p_o_s_form_9",
    "expr_r_p_o_s_form_9",
    "calc_u_2_s_1_form_f",
    "expr_u_2_s_1_form_f",
    "calc_u_2_s_3_form_2",
    "expr_u_2_s_3_form_2",
    "calc_u_2_s_4_form_7",
    "expr_u_2_s_4_form_7",
    "calc_d_q_form_2",
    "expr_d_q_form_2",
    "calc_eq_a_p_b_p_form_e",
    "expr_eq_a_p_b_p_form_e",
    "calc_s_form_c",
    "expr_s_form_c",
    "calc_v_n_t_k_x_form_4",
    "expr_v_n_t_k_x_form_4",
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
    "calc_p_w_t_form_9",
    "expr_p_w_t_form_9",
    "calc_t_a_b_form_0",
    "expr_t_a_b_form_0",
    "calc_k_p_form_c",
    "expr_k_p_form_c",
    "calc_p_t_form_4",
    "expr_p_t_form_4",
    "calc_f_m_x_form_1",
    "expr_f_m_x_form_1",
    "calc_p_0_x_form_5",
    "expr_p_0_x_form_5",
    "calc_f_form_e",
    "expr_f_form_e",
    "calc_f_s_form_0",
    "expr_f_s_form_0",
    "calc_b_p_k_form_0",
    "expr_b_p_k_form_0",
    "calc_o_n_e_t_h_i_r_df_o_m_r_form_1",
    "expr_o_n_e_t_h_i_r_df_o_m_r_form_1",
    "calc_t_w_o_t_h_i_r_df_o_m_r_form_e",
    "expr_t_w_o_t_h_i_r_df_o_m_r_form_e",
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
    "calc_c_p_q_form_c",
    "expr_c_p_q_form_c",
    "calc_f_r_e_q_p_i_t_c_h_form_1",
    "expr_f_r_e_q_p_i_t_c_h_form_1",
    "calc_m_t_form_d",
    "expr_m_t_form_d",
    "calc_k_p_form_8",
    "expr_k_p_form_8",
    "calc_c_l_form_b",
    "expr_c_l_form_b",
]

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


def expr_val_1205_4750_1205_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1205_4750_1205_4`."""
    return (11*pl.col("r")**4)


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


def expr_w_a_r_q_1312_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_a_r_q_1312_7`."""
    return (-10*pl.col("A")**2*pl.col("R")*pl.col("e")*pl.col("l")*pl.col("p")*pl.col("q")*pl.col("r") + pl.col("A")**2*pl.col("R")*pl.col("q"))


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


def expr_w_p_c_t_p_r_s_r_a_1312_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_p_c_t_p_r_s_r_a_1312_7`."""
    return (pl.col("p")*(pl.col("R_A")*pl.col("R_S")) + 11)


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


def expr_val_1406_3402_1406_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_val_1406_3402_1406_3`."""
    return (pl.col("R")*(2*pl.col("A")) + pl.col("R")*(pl.col("S")*(2*(pl.col("R")*(2*pl.col("S"))))))


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


def expr_d_a_h_1603_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_a_h_1603_0`."""
    return (-pl.col("A")*pl.col("D") + pl.col("D")*pl.col("H"))


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
    return float(B*(m + 1) + U)


def expr_t_2210_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_2210_0`."""
    return (pl.col("B")*(pl.col("m") + 1) + pl.col("U"))


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


def expr_w_1_2511_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_1_2511_1`."""
    return (3*pl.col("h")*pl.col("k") - 1)


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
    return (pl.col("x"))


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


def expr_r_x_2511_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_x_2511_1`."""
    return (pl.col("n")*pl.col("x"))


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


def expr_f_l_x_2511_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_l_x_2511_1`."""
    return (pl.col("L")*pl.col("f"))


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


def expr_f_r_x_2511_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_r_x_2511_1`."""
    return (pl.col("R")*pl.col("f"))


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


def expr_i_n_de_x_2603_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_n_de_x_2603_2`."""
    return (20*pl.col("z") + 100)


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


def expr_p_brier_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_brier_`."""
    return (-pl.col("B")*pl.col("c")*pl.col("f")*pl.col("t")*pl.col("z"))


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


def expr_p_t_brier_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_t_brier_`."""
    return (-pl.col("i")*pl.col("p") + pl.col("l"))


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
    return float(H*(j*(i*(N*(i*j)))))


def expr_r_i_j_brown_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_i_j_brown_`."""
    return (pl.col("H")*(pl.col("j")*(pl.col("i")*(pl.col("N")*(pl.col("i")*pl.col("j"))))))


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
    return float(14*(N*(1*i)) + 14*(N*(2*i)))


def expr_v_a_r_x_1_i_x_2_i_brown_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_a_r_x_1_i_x_2_i_brown_`."""
    return (14*(pl.col("N")*(1*pl.col("i"))) + 14*(pl.col("N")*(2*pl.col("i"))))


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


def expr_p_i_brown_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_brown_`."""
    return (-pl.col("U")*pl.col("i") + 1)


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


def expr_p_i_j_p_i_j_p_j_k_p_j_k_bt_sec() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_j_p_i_j_p_j_k_p_j_k_bt_sec`."""
    return (pl.col("i")**2*pl.col("k")**2*pl.col("p")**2)


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


def expr_bt_secondary_many_routes_2023_bt_sec() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_bt_secondary_many_routes_2023_bt_sec`."""
    return (pl.col("g")*pl.col("i")**2*pl.col("k")**2*pl.col("l")*pl.col("o")*pl.col("p")**2)


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


def expr_f_x_bt_sec() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_x_bt_sec`."""
    return (2*pl.col("x"))


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
    return (pl.col("P"))


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


def expr_c_i_j_bt_sec() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_i_j_bt_sec`."""
    return (pl.col("a")*pl.col("i")**2*pl.col("j")*pl.col("s"))


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


def expr_c_bt_sec() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_bt_sec`."""
    return (pl.col("A")*pl.col("S"))


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
    return (pl.col("T"))


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


def expr_f_diebol() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_diebol`."""
    return (pl.col("T")*pl.col("e")**2*pl.col("i")**2*pl.col("j")**2)


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


def expr_r_diebol() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_diebol`."""
    return (math.e*pl.col("P")*pl.col("p"))


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
    return (pl.col("P"))


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
    return (pl.col("P"))


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


def expr_s_s_k_i_l_l_n_gneiti() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_s_k_i_l_l_n_gneiti`."""
    return (-pl.col("S")*pl.col("r")*(pl.col("e")*(pl.col("f")*pl.col("n"))) + (pl.col("S")*(pl.col("f")*(pl.col("c")*(pl.col("s")*(pl.col("n")*pl.col("t"))))) - pl.col("S")*pl.col("r")*(pl.col("e")*(pl.col("f")*(pl.col("n")*(pl.col("S")*(pl.col("o")*(pl.col("p")*(pl.col("n")*pl.col("t"))))))))))


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


def expr_s_c_p_1_gneiti() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_c_p_1_gneiti`."""
    return (1*(1 - pl.col("c")))


def calc_g_p_gneiti(P: float, S: float, a: float, de: float, g: float, i: float, l: float, m: float, o: float, t: float) -> float:
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
    return float(-l*o*(g*(de*(t*(S*(i*(g*(m*((1*P)*a)))))))) - m)


def expr_g_p_gneiti() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_p_gneiti`."""
    return (-pl.col("l")*pl.col("o")*(pl.col("g")*(pl.col("de")*(pl.col("t")*(pl.col("S")*(pl.col("i")*(pl.col("g")*(pl.col("m")*((1*pl.col("P"))*pl.col("a"))))))))) - pl.col("m"))


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
    return (pl.col("P"))


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


def expr_l_o_b_g_gneiti() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_o_b_g_gneiti`."""
    return (-pl.col("H")*pl.col("L")*pl.col("g")*pl.col("o"))


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


def expr_s_2_harvey() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_2_harvey`."""
    return ((1 - pl.col("Z")*pl.col("r"))/(pl.col("n") - 1) - 1/(2*pl.col("r")))


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
    return (pl.col("n"))


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


def expr_c_i_maher_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_i_maher_`."""
    return (pl.col("u")*pl.col("x"))


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


def expr_z_l_y_u_c_c_u_x_i_k_2_j_r_maher_() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_l_y_u_c_c_u_x_i_k_2_j_r_maher_`."""
    return (-pl.col("i")**2*pl.col("j"))


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
    return float(B*(m + 1) + U)


def expr_t_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_form_c`."""
    return (pl.col("B")*(pl.col("m") + 1) + pl.col("U"))


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


def expr_f_x_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_x_form_5`."""
    return (12*pl.col("P")*pl.col("g")*pl.col("l")*pl.col("o"))


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
    return (-pl.col("U") + pl.col("e") + 11)


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


def expr_q_s_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_s_form_9`."""
    return (pl.col("P")*pl.col("r"))


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


def expr_w_e_s_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_e_s_form_9`."""
    return (pl.col("W")*(pl.col("s")*(pl.col("N")*pl.col("s"))))


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


def expr_v_v_1_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_v_1_form_e`."""
    return (pl.col("a")*pl.col("m")*pl.col("x"))


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
    return (pl.col("f"))


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
    return (abs(pl.col("y") - pl.col("z")))


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


def expr_begin_x_k_a_l_i_g_n_d_e_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_begin_x_k_a_l_i_g_n_d_e_form_4`."""
    return ((-pl.col("c_x") + pl.col("u_k"))/pl.col("r"))


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


def expr_p_i_j_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_j_form_6`."""
    return (pl.col("P")*pl.col("r"))


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


def expr_w_a_p_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_a_p_form_9`."""
    return (math.e*pl.col("W")*pl.col("a")*pl.col("e")*pl.col("f")*pl.col("r")*pl.col("t") - math.e*pl.col("W")*pl.col("b")*pl.col("e")**2*pl.col("f")*pl.col("o")*pl.col("r"))


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


def expr_i_n_de_x_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_i_n_de_x_form_0`."""
    return (20*pl.col("z") + 100)


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


def expr_s_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_form_e`."""
    return (pl.col("G")*(pl.col("F")*pl.col("T")))


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


def expr_l_a_a_i_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_a_a_i_form_6`."""
    return (pl.col("L")*(pl.col("P")*(pl.col("C")*pl.col("C"))) + pl.col("L")*(pl.col("M")*(pl.col("E")*pl.col("S"))))


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


def expr_z_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_form_4`."""
    return (pl.col("c")*pl.col("e")*pl.col("v"))


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


def expr_l_v_a_l_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_v_a_l_form_4`."""
    return (pl.col("L")*pl.col("i")*pl.col("k")*pl.col("n"))


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


def expr_e_r_e_c_n_o_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_r_e_c_n_o_form_c`."""
    return (pl.col("a")*pl.col("m")*pl.col("s")*pl.col("x"))


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


def expr_e_b_a_e_s_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_b_a_e_s_form_3`."""
    return (math.e*pl.col("s"))


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


def expr_e_f_i_n_a_l_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_f_i_n_a_l_form_e`."""
    return (math.e*pl.col("s"))


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


def expr_g_s_p_e_c_t_r_a_l_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_s_p_e_c_t_r_a_l_form_5`."""
    return (-pl.col("a")**2*pl.col("b")*pl.col("e")*pl.col("f")*pl.col("i")*pl.col("l")*pl.col("n")*pl.col("s")*math.exp(2) + 100*math.e*pl.col("a")*pl.col("b")*pl.col("e")*pl.col("s"))


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


def expr_l_f_m_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_f_m_form_8`."""
    return (math.e*pl.col("t"))


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


def expr_l_b_a_e_s_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_b_a_e_s_form_a`."""
    return (math.e*pl.col("c"))


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


def expr_p_u_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_u_form_5`."""
    return (pl.col("a")*pl.col("y") + pl.col("h")*pl.col("y"))


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


def expr_y_r_s_h_s_y_p_s_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_y_r_s_h_s_y_p_s_form_1`."""
    return (pl.col("T")*pl.col("k")*pl.col("p")**2*pl.col("s") + pl.col("T")*pl.col("s")*pl.col("z") + 1)


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


def expr_h_y_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_y_form_2`."""
    return (pl.col("c")*pl.col("h")**2*pl.col("x") + pl.col("dh")*(-pl.col("p")*pl.col("y") + pl.col("r")))


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


def expr_l_0_p_w_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_0_p_w_form_0`."""
    return (4*pl.col("y")**2)


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


def expr_l_g_a_p_w_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_g_a_p_w_form_8`."""
    return (2*pl.col("A")*pl.col("B")*pl.col("H")*pl.col("a")*pl.col("y")**2)


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


def expr_a_t_w_o_w_a_o_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_t_w_o_w_a_o_form_9`."""
    return (-pl.col("S")*pl.col("S")*pl.col("T"))


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


def expr_u_l_s_o_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_l_s_o_form_4`."""
    return (-pl.col("a")*pl.col("p") + pl.col("p")*pl.col("s"))


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


def expr_r_s_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_s_form_6`."""
    return (pl.col("N")*(pl.col("s")*(pl.col("u")*(pl.col("c")*(pl.col("c")*(pl.col("N")*(pl.col("e")*(pl.col("v")*(pl.col("a")*pl.col("l"))))))))))


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


def expr_l_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_form_9`."""
    return (pl.col("T")*pl.col("a") + pl.col("T")*pl.col("b") + pl.col("T")*pl.col("c") + pl.col("T")*pl.col("w") - pl.col("V")*pl.col("a") - pl.col("V")*pl.col("b") - pl.col("V")*pl.col("c") - pl.col("V")*pl.col("w"))


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


def expr_m_q_q_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_q_q_form_5`."""
    return (pl.col("m")*(pl.col("u")*(pl.col("N")*(pl.col("T")*(pl.col("w")*(pl.col("N")*pl.col("w")))))) + (pl.col("M")*pl.col("c") + pl.col("m")*(pl.col("u")*(pl.col("N")*(pl.col("T")*(pl.col("v")*(pl.col("N")*pl.col("v"))))))))


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


def expr_c_p_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_p_form_a`."""
    return (360*pl.col("P")*pl.col("U")*pl.col("i")*pl.col("n"))


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


def expr_c_t_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_t_form_0`."""
    return (240*pl.col("T")*pl.col("U"))


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


def expr_l_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_form_c`."""
    return (pl.col("L")*pl.col("a")**2*pl.col("de")*pl.col("i")*pl.col("l")*pl.col("m")**2*pl.col("x"))


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


def expr_ds_dw_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_ds_dw_form_d`."""
    return (pl.col("w")*(-pl.col("D")*pl.col("k") + pl.col("L")*pl.col("i")*pl.col("k")))


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


def expr_w_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_form_a`."""
    return (pl.col("i")*pl.col("v")*pl.col("y") + pl.col("v")*pl.col("x"))


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


def expr_dt_dw_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_dt_dw_form_f`."""
    return (pl.col("w")*(-pl.col("D")*pl.col("k") + pl.col("L")*pl.col("i")*pl.col("k"))*abs(pl.col("v")))


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


def expr_j_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_form_5`."""
    return (0.5*pl.col("C")**2*pl.col("d")*pl.col("l") + 0.3*pl.col("C")*pl.col("l") + 0.2*pl.col("C")*pl.col("p"))


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


def expr_p_b_a_s_e_l_i_e_n_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_b_a_s_e_l_i_e_n_form_9`."""
    return (pl.col("W")*pl.col("i")*pl.col("v"))


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


def expr_a_l_r_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_l_r_form_a`."""
    return (6*pl.col("L")**3*pl.col("R")**3*pl.col("a")**3)


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
    return float(2*c*s)


def expr_c_2_s_r_z_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_2_s_r_z_form_9`."""
    return (2*pl.col("c")*pl.col("s"))


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


def expr_a_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_form_2`."""
    return (3*pl.col("c")*pl.col("m")*pl.col("r")**2)


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


def expr_p_m_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_m_form_9`."""
    return (pl.col("V")*pl.col("i")*pl.col("m"))


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


def expr_c_p_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_p_form_f`."""
    return (0.03*pl.col("m"))


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


def expr_p_s_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_s_form_b`."""
    return ((1.3296*pl.col("W"))/pl.col("N"))


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


def expr_p_s_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_s_form_5`."""
    return ((0.1325*pl.col("W"))/pl.col("N"))


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
    return float(618.0*d*r)


def expr_t_s_p_i_n_do_n_w_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_s_p_i_n_do_n_w_form_c`."""
    return (618.0*pl.col("d")*pl.col("r"))


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
    return float(-4*D**2*g**2 + (L*g - 2)*(L*g - 1/2))


def expr_x_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_form_c`."""
    return (-4*pl.col("D")**2*pl.col("g")**2 + (pl.col("L")*pl.col("g") - 2)*(pl.col("L")*pl.col("g") - 1/2))


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


def expr_y_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_y_form_f`."""
    return (-4*pl.col("D")*pl.col("g")*(pl.col("L")*pl.col("g") - 1/2) + (pl.col("L")*pl.col("g") - 2)*(pl.col("L")*pl.col("g") - 1/2) - 1)


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
    return float(b*d*v - d*dm)


def expr_l_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_form_6`."""
    return (pl.col("b")*pl.col("d")*pl.col("v") - pl.col("d")*pl.col("dm"))


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


def expr_d_f_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_f_form_4`."""
    return ((pl.col("C")*pl.col("D"))*(pl.col("S")*pl.col("q")))


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


def expr_f_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_form_4`."""
    return (pl.col("D")*pl.col("F") + pl.col("F")*pl.col("L"))


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


def expr_f_r_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_r_form_4`."""
    return (-pl.col("R")*pl.col("k")*pl.col("r"))


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


def expr_d_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_form_6`."""
    return (-pl.col("A")*pl.col("R")*pl.col("e")*pl.col("p")*pl.col("x") + pl.col("C")*pl.col("G")*pl.col("R"))


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
    return (-pl.col("V") + pl.col("W"))


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
    return (pl.col("M"))


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


def expr_a_j_h_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_j_h_form_8`."""
    return (0.1129*pl.col("a")**2*pl.col("di")*pl.col("i")**2*pl.col("l")**2*pl.col("m")*pl.col("n")*pl.col("r")*pl.col("s"))


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


def expr_e_v_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_v_form_3`."""
    return ((2*pl.col("v"))*(pl.col("m")/2))


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


def expr_f_m_a_x_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_m_a_x_form_9`."""
    return ((pl.col("R")*(pl.col("M")*(pl.col("S")*(pl.col("K")*(pl.col("R")*(pl.col("G")*(pl.col("M")*(pl.col("K")*pl.col("S")))))))))*(((pl.col("M")*(pl.col("F")*(pl.col("G")*(pl.col("m")*(pl.col("a")*pl.col("x"))))))/((pl.col("H")*(pl.col("G")*pl.col("M")))))/((pl.col("G")*pl.col("H")))))


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
    return (pl.col("p") + pl.col("w"))


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


def expr_p_i_t_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_i_t_form_6`."""
    return (pl.col("i")*pl.col("p"))


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


def expr_c_g_f_r_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_g_f_r_form_c`."""
    return (pl.col("L")*pl.col("c") - 1.2)


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


def expr_l_r_o_l_l_j_o_i_n_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_r_o_l_l_j_o_i_n_form_9`."""
    return (12*pl.col("R"))


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
    return (pl.col("R"))


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


def expr_p_c_i_j_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_c_i_j_form_9`."""
    return (pl.col("J")*pl.col("c")*pl.col("i")*pl.col("j") - pl.col("c")*pl.col("i")*pl.col("r"))


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


def expr_k_1_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_1_form_3`."""
    return (4*pl.col("L")**2)


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


def expr_s_w_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_s_w_form_8`."""
    return (-pl.col("l")*pl.col("w") + 1)


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


def expr_w_b_x_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_b_x_form_1`."""
    return (pl.col("B")**2*pl.col("W")**2*pl.col("y")*pl.col("z"))


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


def expr_w_b_r_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_b_r_form_3`."""
    return (pl.col("B")**3*pl.col("W")**3*pl.col("x")*pl.col("y")*pl.col("z"))


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


def expr_w_c_x_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_c_x_form_9`."""
    return (pl.col("C")**2*pl.col("W")**2*pl.col("y")*pl.col("z"))


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


def expr_w_c_r_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_c_r_form_1`."""
    return (pl.col("C")**3*pl.col("W")**3*pl.col("x")*pl.col("y")*pl.col("z"))


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


def expr_w_b_r_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_w_b_r_form_0`."""
    return (pl.col("B")**3*pl.col("W")**3*pl.col("x")*pl.col("y")*pl.col("z"))


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


def expr_q_dt_p_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_q_dt_p_form_c`."""
    return (pl.col("a")*pl.col("t") + pl.col("c")*pl.col("dt")*pl.col("m")*pl.col("q"))


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


def expr_r_m_d_i_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_m_d_i_form_5`."""
    return (12*pl.col("e")**2*pl.col("h")*pl.col("l")*pl.col("r") + 12*pl.col("e")*pl.col("o")*pl.col("r")*pl.col("t"))


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


def expr_e_p_form_3() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_p_form_3`."""
    return (pl.col("e")*pl.col("f")*pl.col("r")*pl.col("x") - pl.col("x"))


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


def expr_f_c_d_m_form_a() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_c_d_m_form_a`."""
    return (pl.col("K")*pl.col("e")*pl.col("i")**2 + pl.col("K")*pl.col("e")*pl.col("p")**2 + pl.col("K")*pl.col("e")*pl.col("v")**2 + pl.col("M")*pl.col("da")*pl.col("x")*pl.col("y"))


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


def expr_e_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_form_1`."""
    return (0.08*pl.col("e")**2)


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


def expr_h_a_p_e_x_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_h_a_p_e_x_form_b`."""
    return (pl.col("c")*pl.col("m")*pl.col("o")*pl.col("p"))


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


def expr_e_p_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_p_form_1`."""
    return ((pl.col("p")*(pl.col("z")*(2*pl.col("c"))) + (pl.col("p")*(pl.col("x")*(2*pl.col("a"))) + pl.col("p")*(pl.col("y")*(2*pl.col("b"))))) - 1)


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


def expr_t_p_x_p_y_p_z_1_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_p_x_p_y_p_z_1_form_5`."""
    return (pl.col("C")*pl.col("T")**2*pl.col("u")*pl.col("v")*pl.col("w"))


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


def expr_j_p_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_j_p_form_d`."""
    return (2*pl.col("A")*pl.col("j")**2*pl.col("x") + pl.col("W")*pl.col("j"))


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


def expr_c_e_x_a_c_t_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_e_x_a_c_t_form_f`."""
    return (2*pl.col("a")*pl.col("g")*pl.col("l")*pl.col("o") + 280*pl.col("g")*pl.col("l")*pl.col("o") + (math.e*pl.col("C") + math.e*pl.col("L"))*(22660*pl.col("g")*pl.col("l")*pl.col("o") + 15) + 27)


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


def expr_u_o_t_v_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_o_t_v_form_c`."""
    return (2*pl.col("T") + pl.col("r"))


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


def expr_a_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_a_form_4`."""
    return (16*pl.col("m")**4*pl.col("x")**3*pl.col("y")**3)


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


def expr_l_v_r_r_e_e_2223_form_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_v_r_r_e_e_2223_form_7`."""
    return (21252*pl.col("C")*pl.col("H")*pl.col("Z")*pl.col("e")*pl.col("g")*pl.col("m")*pl.col("v") + 8*pl.col("C")*pl.col("e")**2)


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


def expr_l_i_m_i_n_f_n_b_n_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_l_i_m_i_n_f_n_b_n_form_0`."""
    return (pl.col("A")*pl.col("f")*pl.col("i")**2*pl.col("k")*pl.col("l")*pl.col("m")**3*pl.col("n"))


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


def expr_z_m_i_x_form_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_z_m_i_x_form_7`."""
    return (pl.col("a")*pl.col("de")*pl.col("i")*pl.col("l")*pl.col("n")**2*pl.col("o")*pl.col("z") + pl.col("a")*pl.col("de")*pl.col("i")*pl.col("l")*pl.col("z"))


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


def expr_e_j_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_e_j_form_6`."""
    return (pl.col("R")*pl.col("T")*pl.col("e")**2*pl.col("j")**2)


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


def expr_p_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_form_2`."""
    return (3*pl.col("M")*pl.col("P")*pl.col("T"))


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


def expr_r_p_o_s_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_p_o_s_form_9`."""
    return (pl.col("R")**2*pl.col("c")*pl.col("o")*pl.col("p")*pl.col("s"))


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


def expr_u_2_s_1_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_2_s_1_form_f`."""
    return (2*pl.col("L")*pl.col("M")*pl.col("P")*pl.col("u"))


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


def expr_u_2_s_3_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_2_s_3_form_2`."""
    return (pl.col("u")*(2*(pl.col("G")*(pl.col("P")*pl.col("S")))))


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


def expr_u_2_s_4_form_7() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_u_2_s_4_form_7`."""
    return (2*(pl.col("u")*(2*(pl.col("G")*(pl.col("P")*pl.col("S"))))))


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
    return float(4*q**2 - 2*q + 2)


def expr_d_q_form_2() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_d_q_form_2`."""
    return (4*pl.col("q")**2 - 2*pl.col("q") + 2)


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
    return (pl.col("p"))


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
    return (pl.col("R"))


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


def expr_v_n_t_k_x_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_v_n_t_k_x_form_4`."""
    return (pl.col("i")*pl.col("m")*pl.col("n"))


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
    return float((0*S)*c - s)


def expr_f_s_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_s_form_5`."""
    return ((0*pl.col("S"))*pl.col("c") - pl.col("s"))


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
    return (pl.col("k"))


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
    return (pl.col("c"))


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
    return (pl.col("a") - pl.col("b"))


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


def expr_t_a_b_form_6() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_a_b_form_6`."""
    return (pl.col("a")*pl.col("b"))


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


def expr_t_a_b_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_a_b_form_b`."""
    return (-pl.col("a")*pl.col("b") + 2)


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
    return (pl.col("P"))


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


def expr_t_a_b_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_a_b_form_0`."""
    return (-pl.col("a")*pl.col("b") + 2)


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
    return (pl.col("P"))


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
    return (pl.col("P"))


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
    return (pl.col("P"))


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
    return (pl.col("P"))


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


def expr_f_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_form_e`."""
    return (pl.col("f")*pl.col("t"))


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


def expr_f_s_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_s_form_0`."""
    return (pl.col("f")*pl.col("s"))


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


def expr_b_p_k_form_0() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_b_p_k_form_0`."""
    return (pl.col("a")*pl.col("m")*pl.col("x"))


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


def expr_o_n_e_t_h_i_r_df_o_m_r_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_o_n_e_t_h_i_r_df_o_m_r_form_1`."""
    return (23*(pl.col("C")*(pl.col("a")*(pl.col("r")*(pl.col("e")*(pl.col("e")*(pl.col("r")*(pl.col("P")*(pl.col("o")*(pl.col("i")*(pl.col("n")*(pl.col("s")*pl.col("t")))))))))))) + 13*(pl.col("F")*(pl.col("o")*(pl.col("m")*pl.col("r")))))


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


def expr_t_w_o_t_h_i_r_df_o_m_r_form_e() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_t_w_o_t_h_i_r_df_o_m_r_form_e`."""
    return (13*pl.col("C")*pl.col("P")*pl.col("a")*pl.col("e")**2*pl.col("i")*pl.col("n")*pl.col("o")*pl.col("r")**2*pl.col("s")*pl.col("t") + 23*pl.col("F")*pl.col("m")*pl.col("o")*pl.col("r"))


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


def expr_x_l_o_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_x_l_o_form_d`."""
    return (pl.col("m")*(pl.col("a")*pl.col("x")))


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


def expr_r_form_5() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_form_5`."""
    return (-math.e*pl.col("P")*pl.col("a")**2*pl.col("c")*pl.col("l")*pl.col("t")*pl.col("u") + math.e*pl.col("P")*pl.col("a")*pl.col("i")*pl.col("l")*pl.col("m")*pl.col("o")*pl.col("p")*pl.col("t"))


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


def expr_p_r_i_w_i_n_s_o_v_e_j_r_form_f() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_p_r_i_w_i_n_s_o_v_e_j_r_form_f`."""
    return (-1/40*pl.col("i")*pl.col("s") + (1/40)*pl.col("j")*pl.col("s") + 11)


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


def expr_r_w_c_i_form_4() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_r_w_c_i_form_4`."""
    return (pl.col("a")*pl.col("i")*pl.col("p")*pl.col("s")*pl.col("t")**2)


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


def expr_g_x_form_9() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_g_x_form_9`."""
    return (pl.col("e") - pl.col("t")*pl.col("w")*pl.col("x") + 11)


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


def expr_c_p_q_form_c() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_p_q_form_c`."""
    return (2*pl.col("g")*pl.col("l")*pl.col("o")*pl.col("p")*pl.col("q"))


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


def expr_f_r_e_q_p_i_t_c_h_form_1() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_f_r_e_q_p_i_t_c_h_form_1`."""
    return (880*pl.col("c")*pl.col("h")*pl.col("i")*pl.col("p")*pl.col("t") - 6912)


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


def expr_m_t_form_d() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_m_t_form_d`."""
    return (pl.col("a")*pl.col("k")**2*pl.col("m")*pl.col("t")*pl.col("x")**2)


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


def expr_k_p_form_8() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_k_p_form_8`."""
    return (12*pl.col("B")*pl.col("k") + pl.col("c")*pl.col("h")*pl.col("i")**2*pl.col("m")*pl.col("n")*pl.col("p")*pl.col("t"))


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


def expr_c_l_form_b() -> pl.Expr:
    r"""Return vectorized Polars expression for `calc_c_l_form_b`."""
    return (math.e*pl.col("x"))

