// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vtop.h for the primary calling header

#include "verilated.h"
#include "verilated_dpi.h"

#include "Vtop__Syms.h"
#include "Vtop___024root.h"

VL_ATTR_COLD void Vtop___024root___eval_static(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_static\n"); );
}

VL_ATTR_COLD void Vtop___024root___eval_initial__TOP(Vtop___024root* vlSelf);

VL_ATTR_COLD void Vtop___024root___eval_initial(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_initial\n"); );
    // Body
    Vtop___024root___eval_initial__TOP(vlSelf);
}

VL_ATTR_COLD void Vtop___024root___eval_initial__TOP(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_initial__TOP\n"); );
    // Body
    vlSelf->haddr = 0U;
    vlSelf->hburst = 0U;
    vlSelf->hmastlock = 0U;
    vlSelf->hprot = 0U;
    vlSelf->hsize = 0U;
    vlSelf->hnonsec = 0U;
    vlSelf->hexcl = 0U;
    vlSelf->hmaster = 0U;
    vlSelf->htrans = 0U;
    vlSelf->hwdata = 0U;
    vlSelf->hwrite = 0U;
    vlSelf->hready = 0U;
    vlSelf->hrdata = 0U;
    vlSelf->hreadyout = 0U;
    vlSelf->hresp = 0U;
    vlSelf->hexokay = 0U;
    vlSelf->hsel = 0U;
}

VL_ATTR_COLD void Vtop___024root___eval_final(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_final\n"); );
}

VL_ATTR_COLD void Vtop___024root___eval_triggers__stl(Vtop___024root* vlSelf);
#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__stl(Vtop___024root* vlSelf);
#endif  // VL_DEBUG
VL_ATTR_COLD void Vtop___024root___eval_stl(Vtop___024root* vlSelf);

VL_ATTR_COLD void Vtop___024root___eval_settle(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_settle\n"); );
    // Init
    CData/*0:0*/ __VstlContinue;
    // Body
    vlSelf->__VstlIterCount = 0U;
    __VstlContinue = 1U;
    while (__VstlContinue) {
        __VstlContinue = 0U;
        Vtop___024root___eval_triggers__stl(vlSelf);
        if (vlSelf->__VstlTriggered.any()) {
            __VstlContinue = 1U;
            if (VL_UNLIKELY((0x64U < vlSelf->__VstlIterCount))) {
#ifdef VL_DEBUG
                Vtop___024root___dump_triggers__stl(vlSelf);
#endif
                VL_FATAL_MT("/src/tests/dut/dut.sv", 8, "", "Settle region did not converge.");
            }
            vlSelf->__VstlIterCount = ((IData)(1U) 
                                       + vlSelf->__VstlIterCount);
            Vtop___024root___eval_stl(vlSelf);
        }
    }
}

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__stl(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___dump_triggers__stl\n"); );
    // Body
    if ((1U & (~ (IData)(vlSelf->__VstlTriggered.any())))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
    if ((1ULL & vlSelf->__VstlTriggered.word(0U))) {
        VL_DBG_MSGF("         'stl' region trigger index 0 is active: Internal 'stl' trigger - first iteration\n");
    }
}
#endif  // VL_DEBUG

void Vtop___024root___ico_sequent__TOP__0(Vtop___024root* vlSelf);

VL_ATTR_COLD void Vtop___024root___eval_stl(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_stl\n"); );
    // Body
    if ((1ULL & vlSelf->__VstlTriggered.word(0U))) {
        Vtop___024root___ico_sequent__TOP__0(vlSelf);
    }
}

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__ico(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___dump_triggers__ico\n"); );
    // Body
    if ((1U & (~ (IData)(vlSelf->__VicoTriggered.any())))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
    if ((1ULL & vlSelf->__VicoTriggered.word(0U))) {
        VL_DBG_MSGF("         'ico' region trigger index 0 is active: Internal 'ico' trigger - first iteration\n");
    }
}
#endif  // VL_DEBUG

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__act(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___dump_triggers__act\n"); );
    // Body
    if ((1U & (~ (IData)(vlSelf->__VactTriggered.any())))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
}
#endif  // VL_DEBUG

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__nba(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___dump_triggers__nba\n"); );
    // Body
    if ((1U & (~ (IData)(vlSelf->__VnbaTriggered.any())))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
}
#endif  // VL_DEBUG

VL_ATTR_COLD void Vtop___024root___ctor_var_reset(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___ctor_var_reset\n"); );
    // Body
    vlSelf->hclk = VL_RAND_RESET_I(1);
    vlSelf->hresetn = VL_RAND_RESET_I(1);
    vlSelf->haddr = VL_RAND_RESET_I(32);
    vlSelf->hburst = VL_RAND_RESET_I(3);
    vlSelf->hmastlock = VL_RAND_RESET_I(1);
    vlSelf->hprot = VL_RAND_RESET_I(7);
    vlSelf->hsize = VL_RAND_RESET_I(3);
    vlSelf->hnonsec = VL_RAND_RESET_I(1);
    vlSelf->hexcl = VL_RAND_RESET_I(1);
    vlSelf->hmaster = VL_RAND_RESET_I(4);
    vlSelf->htrans = VL_RAND_RESET_I(2);
    vlSelf->hwdata = VL_RAND_RESET_I(32);
    vlSelf->hwrite = VL_RAND_RESET_I(1);
    vlSelf->hready = VL_RAND_RESET_I(1);
    vlSelf->hrdata = VL_RAND_RESET_I(32);
    vlSelf->hreadyout = VL_RAND_RESET_I(1);
    vlSelf->hresp = VL_RAND_RESET_I(1);
    vlSelf->hexokay = VL_RAND_RESET_I(1);
    vlSelf->hsel = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT__hclk = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT__hresetn = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT__haddr = VL_RAND_RESET_I(32);
    vlSelf->ahb_template__DOT__hburst = VL_RAND_RESET_I(3);
    vlSelf->ahb_template__DOT__hmastlock = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT__hprot = VL_RAND_RESET_I(7);
    vlSelf->ahb_template__DOT__hsize = VL_RAND_RESET_I(3);
    vlSelf->ahb_template__DOT__hnonsec = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT__hexcl = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT__hmaster = VL_RAND_RESET_I(4);
    vlSelf->ahb_template__DOT__htrans = VL_RAND_RESET_I(2);
    vlSelf->ahb_template__DOT__hwdata = VL_RAND_RESET_I(32);
    vlSelf->ahb_template__DOT__hwrite = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT__hready = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT__hrdata = VL_RAND_RESET_I(32);
    vlSelf->ahb_template__DOT__hreadyout = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT__hresp = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT__hexokay = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT__hsel = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT____Vtogcov__hclk = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT____Vtogcov__hresetn = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT____Vtogcov__haddr = VL_RAND_RESET_I(32);
    vlSelf->ahb_template__DOT____Vtogcov__hburst = VL_RAND_RESET_I(3);
    vlSelf->ahb_template__DOT____Vtogcov__hmastlock = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT____Vtogcov__hprot = VL_RAND_RESET_I(7);
    vlSelf->ahb_template__DOT____Vtogcov__hsize = VL_RAND_RESET_I(3);
    vlSelf->ahb_template__DOT____Vtogcov__hnonsec = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT____Vtogcov__hexcl = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT____Vtogcov__hmaster = VL_RAND_RESET_I(4);
    vlSelf->ahb_template__DOT____Vtogcov__htrans = VL_RAND_RESET_I(2);
    vlSelf->ahb_template__DOT____Vtogcov__hwdata = VL_RAND_RESET_I(32);
    vlSelf->ahb_template__DOT____Vtogcov__hwrite = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT____Vtogcov__hready = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT____Vtogcov__hrdata = VL_RAND_RESET_I(32);
    vlSelf->ahb_template__DOT____Vtogcov__hreadyout = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT____Vtogcov__hresp = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT____Vtogcov__hexokay = VL_RAND_RESET_I(1);
    vlSelf->ahb_template__DOT____Vtogcov__hsel = VL_RAND_RESET_I(1);
}
