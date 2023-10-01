// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Tracing implementation internals
#include "verilated_fst_c.h"
#include "Vtop__Syms.h"


VL_ATTR_COLD void Vtop___024root__trace_init_sub__TOP__0(Vtop___024root* vlSelf, VerilatedFst* tracep) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_init_sub__TOP__0\n"); );
    // Init
    const int c = vlSymsp->__Vm_baseCode;
    // Body
    tracep->declBit(c+1,"hclk",-1,FST_VD_INPUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBit(c+2,"hresetn",-1,FST_VD_INPUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBus(c+3,"haddr",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1, 31,0);
    tracep->declBus(c+4,"hburst",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1, 2,0);
    tracep->declBit(c+5,"hmastlock",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBus(c+6,"hprot",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1, 6,0);
    tracep->declBus(c+7,"hsize",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1, 2,0);
    tracep->declBit(c+8,"hnonsec",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBit(c+9,"hexcl",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBus(c+10,"hmaster",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1, 3,0);
    tracep->declBus(c+11,"htrans",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1, 1,0);
    tracep->declBus(c+12,"hwdata",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1, 31,0);
    tracep->declBit(c+13,"hwrite",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBit(c+14,"hready",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBus(c+15,"hrdata",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1, 31,0);
    tracep->declBit(c+16,"hreadyout",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBit(c+17,"hresp",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBit(c+18,"hexokay",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBit(c+19,"hsel",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1);
    tracep->pushNamePrefix("ahb_template ");
    tracep->declBus(c+39,"ADDR_WIDTH",-1, FST_VD_IMPLICIT,FST_VT_VCD_PARAMETER, false,-1, 31,0);
    tracep->declBus(c+39,"DATA_WIDTH",-1, FST_VD_IMPLICIT,FST_VT_VCD_PARAMETER, false,-1, 31,0);
    tracep->declBit(c+20,"hclk",-1,FST_VD_INPUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBit(c+21,"hresetn",-1,FST_VD_INPUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBus(c+22,"haddr",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1, 31,0);
    tracep->declBus(c+23,"hburst",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1, 2,0);
    tracep->declBit(c+24,"hmastlock",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBus(c+25,"hprot",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1, 6,0);
    tracep->declBus(c+26,"hsize",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1, 2,0);
    tracep->declBit(c+27,"hnonsec",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBit(c+28,"hexcl",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBus(c+29,"hmaster",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1, 3,0);
    tracep->declBus(c+30,"htrans",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1, 1,0);
    tracep->declBus(c+31,"hwdata",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1, 31,0);
    tracep->declBit(c+32,"hwrite",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBit(c+33,"hready",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBus(c+34,"hrdata",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1, 31,0);
    tracep->declBit(c+35,"hreadyout",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBit(c+36,"hresp",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBit(c+37,"hexokay",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1);
    tracep->declBit(c+38,"hsel",-1,FST_VD_INOUT,FST_VT_VCD_WIRE, false,-1);
    tracep->popNamePrefix(1);
}

VL_ATTR_COLD void Vtop___024root__trace_init_top(Vtop___024root* vlSelf, VerilatedFst* tracep) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_init_top\n"); );
    // Body
    Vtop___024root__trace_init_sub__TOP__0(vlSelf, tracep);
}

VL_ATTR_COLD void Vtop___024root__trace_full_top_0(void* voidSelf, VerilatedFst::Buffer* bufp);
void Vtop___024root__trace_chg_top_0(void* voidSelf, VerilatedFst::Buffer* bufp);
void Vtop___024root__trace_cleanup(void* voidSelf, VerilatedFst* /*unused*/);

VL_ATTR_COLD void Vtop___024root__trace_register(Vtop___024root* vlSelf, VerilatedFst* tracep) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_register\n"); );
    // Body
    tracep->addFullCb(&Vtop___024root__trace_full_top_0, vlSelf);
    tracep->addChgCb(&Vtop___024root__trace_chg_top_0, vlSelf);
    tracep->addCleanupCb(&Vtop___024root__trace_cleanup, vlSelf);
}

VL_ATTR_COLD void Vtop___024root__trace_full_sub_0(Vtop___024root* vlSelf, VerilatedFst::Buffer* bufp);

VL_ATTR_COLD void Vtop___024root__trace_full_top_0(void* voidSelf, VerilatedFst::Buffer* bufp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_full_top_0\n"); );
    // Init
    Vtop___024root* const __restrict vlSelf VL_ATTR_UNUSED = static_cast<Vtop___024root*>(voidSelf);
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    // Body
    Vtop___024root__trace_full_sub_0((&vlSymsp->TOP), bufp);
}

VL_ATTR_COLD void Vtop___024root__trace_full_sub_0(Vtop___024root* vlSelf, VerilatedFst::Buffer* bufp) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_full_sub_0\n"); );
    // Init
    uint32_t* const oldp VL_ATTR_UNUSED = bufp->oldp(vlSymsp->__Vm_baseCode);
    // Body
    bufp->fullBit(oldp+1,(vlSelf->hclk));
    bufp->fullBit(oldp+2,(vlSelf->hresetn));
    bufp->fullIData(oldp+3,(vlSelf->haddr),32);
    bufp->fullCData(oldp+4,(vlSelf->hburst),3);
    bufp->fullBit(oldp+5,(vlSelf->hmastlock));
    bufp->fullCData(oldp+6,(vlSelf->hprot),7);
    bufp->fullCData(oldp+7,(vlSelf->hsize),3);
    bufp->fullBit(oldp+8,(vlSelf->hnonsec));
    bufp->fullBit(oldp+9,(vlSelf->hexcl));
    bufp->fullCData(oldp+10,(vlSelf->hmaster),4);
    bufp->fullCData(oldp+11,(vlSelf->htrans),2);
    bufp->fullIData(oldp+12,(vlSelf->hwdata),32);
    bufp->fullBit(oldp+13,(vlSelf->hwrite));
    bufp->fullBit(oldp+14,(vlSelf->hready));
    bufp->fullIData(oldp+15,(vlSelf->hrdata),32);
    bufp->fullBit(oldp+16,(vlSelf->hreadyout));
    bufp->fullBit(oldp+17,(vlSelf->hresp));
    bufp->fullBit(oldp+18,(vlSelf->hexokay));
    bufp->fullBit(oldp+19,(vlSelf->hsel));
    bufp->fullBit(oldp+20,(vlSelf->ahb_template__DOT__hclk));
    bufp->fullBit(oldp+21,(vlSelf->ahb_template__DOT__hresetn));
    bufp->fullIData(oldp+22,(vlSelf->ahb_template__DOT__haddr),32);
    bufp->fullCData(oldp+23,(vlSelf->ahb_template__DOT__hburst),3);
    bufp->fullBit(oldp+24,(vlSelf->ahb_template__DOT__hmastlock));
    bufp->fullCData(oldp+25,(vlSelf->ahb_template__DOT__hprot),7);
    bufp->fullCData(oldp+26,(vlSelf->ahb_template__DOT__hsize),3);
    bufp->fullBit(oldp+27,(vlSelf->ahb_template__DOT__hnonsec));
    bufp->fullBit(oldp+28,(vlSelf->ahb_template__DOT__hexcl));
    bufp->fullCData(oldp+29,(vlSelf->ahb_template__DOT__hmaster),4);
    bufp->fullCData(oldp+30,(vlSelf->ahb_template__DOT__htrans),2);
    bufp->fullIData(oldp+31,(vlSelf->ahb_template__DOT__hwdata),32);
    bufp->fullBit(oldp+32,(vlSelf->ahb_template__DOT__hwrite));
    bufp->fullBit(oldp+33,(vlSelf->ahb_template__DOT__hready));
    bufp->fullIData(oldp+34,(vlSelf->ahb_template__DOT__hrdata),32);
    bufp->fullBit(oldp+35,(vlSelf->ahb_template__DOT__hreadyout));
    bufp->fullBit(oldp+36,(vlSelf->ahb_template__DOT__hresp));
    bufp->fullBit(oldp+37,(vlSelf->ahb_template__DOT__hexokay));
    bufp->fullBit(oldp+38,(vlSelf->ahb_template__DOT__hsel));
    bufp->fullIData(oldp+39,(0x20U),32);
}
