// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Tracing implementation internals
#include "verilated_fst_c.h"
#include "Vtop__Syms.h"


void Vtop___024root__trace_chg_sub_0(Vtop___024root* vlSelf, VerilatedFst::Buffer* bufp);

void Vtop___024root__trace_chg_top_0(void* voidSelf, VerilatedFst::Buffer* bufp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_chg_top_0\n"); );
    // Init
    Vtop___024root* const __restrict vlSelf VL_ATTR_UNUSED = static_cast<Vtop___024root*>(voidSelf);
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    if (VL_UNLIKELY(!vlSymsp->__Vm_activity)) return;
    // Body
    Vtop___024root__trace_chg_sub_0((&vlSymsp->TOP), bufp);
}

void Vtop___024root__trace_chg_sub_0(Vtop___024root* vlSelf, VerilatedFst::Buffer* bufp) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_chg_sub_0\n"); );
    // Init
    uint32_t* const oldp VL_ATTR_UNUSED = bufp->oldp(vlSymsp->__Vm_baseCode + 1);
    // Body
    bufp->chgBit(oldp+0,(vlSelf->hclk));
    bufp->chgBit(oldp+1,(vlSelf->hresetn));
    bufp->chgIData(oldp+2,(vlSelf->haddr),32);
    bufp->chgCData(oldp+3,(vlSelf->hburst),3);
    bufp->chgBit(oldp+4,(vlSelf->hmastlock));
    bufp->chgCData(oldp+5,(vlSelf->hprot),7);
    bufp->chgCData(oldp+6,(vlSelf->hsize),3);
    bufp->chgBit(oldp+7,(vlSelf->hnonsec));
    bufp->chgBit(oldp+8,(vlSelf->hexcl));
    bufp->chgCData(oldp+9,(vlSelf->hmaster),4);
    bufp->chgCData(oldp+10,(vlSelf->htrans),2);
    bufp->chgIData(oldp+11,(vlSelf->hwdata),32);
    bufp->chgBit(oldp+12,(vlSelf->hwrite));
    bufp->chgBit(oldp+13,(vlSelf->hready));
    bufp->chgIData(oldp+14,(vlSelf->hrdata),32);
    bufp->chgBit(oldp+15,(vlSelf->hreadyout));
    bufp->chgBit(oldp+16,(vlSelf->hresp));
    bufp->chgBit(oldp+17,(vlSelf->hexokay));
    bufp->chgBit(oldp+18,(vlSelf->hsel));
    bufp->chgBit(oldp+19,(vlSelf->ahb_template__DOT__hclk));
    bufp->chgBit(oldp+20,(vlSelf->ahb_template__DOT__hresetn));
    bufp->chgIData(oldp+21,(vlSelf->ahb_template__DOT__haddr),32);
    bufp->chgCData(oldp+22,(vlSelf->ahb_template__DOT__hburst),3);
    bufp->chgBit(oldp+23,(vlSelf->ahb_template__DOT__hmastlock));
    bufp->chgCData(oldp+24,(vlSelf->ahb_template__DOT__hprot),7);
    bufp->chgCData(oldp+25,(vlSelf->ahb_template__DOT__hsize),3);
    bufp->chgBit(oldp+26,(vlSelf->ahb_template__DOT__hnonsec));
    bufp->chgBit(oldp+27,(vlSelf->ahb_template__DOT__hexcl));
    bufp->chgCData(oldp+28,(vlSelf->ahb_template__DOT__hmaster),4);
    bufp->chgCData(oldp+29,(vlSelf->ahb_template__DOT__htrans),2);
    bufp->chgIData(oldp+30,(vlSelf->ahb_template__DOT__hwdata),32);
    bufp->chgBit(oldp+31,(vlSelf->ahb_template__DOT__hwrite));
    bufp->chgBit(oldp+32,(vlSelf->ahb_template__DOT__hready));
    bufp->chgIData(oldp+33,(vlSelf->ahb_template__DOT__hrdata),32);
    bufp->chgBit(oldp+34,(vlSelf->ahb_template__DOT__hreadyout));
    bufp->chgBit(oldp+35,(vlSelf->ahb_template__DOT__hresp));
    bufp->chgBit(oldp+36,(vlSelf->ahb_template__DOT__hexokay));
    bufp->chgBit(oldp+37,(vlSelf->ahb_template__DOT__hsel));
}

void Vtop___024root__trace_cleanup(void* voidSelf, VerilatedFst* /*unused*/) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_cleanup\n"); );
    // Init
    Vtop___024root* const __restrict vlSelf VL_ATTR_UNUSED = static_cast<Vtop___024root*>(voidSelf);
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VlUnpacked<CData/*0:0*/, 1> __Vm_traceActivity;
    for (int __Vi0 = 0; __Vi0 < 1; ++__Vi0) {
        __Vm_traceActivity[__Vi0] = 0;
    }
    // Body
    vlSymsp->__Vm_activity = false;
    __Vm_traceActivity[0U] = 0U;
}
