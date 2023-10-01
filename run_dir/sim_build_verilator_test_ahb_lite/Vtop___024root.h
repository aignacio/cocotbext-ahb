// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design internal header
// See Vtop.h for the primary calling header

#ifndef VERILATED_VTOP___024ROOT_H_
#define VERILATED_VTOP___024ROOT_H_  // guard

#include "verilated.h"
#include "verilated_cov.h"


class Vtop__Syms;

class alignas(VL_CACHE_LINE_BYTES) Vtop___024root final : public VerilatedModule {
  public:

    // DESIGN SPECIFIC STATE
    VL_IN8(hclk,0,0);
    VL_IN8(hresetn,0,0);
    VL_INOUT8(hburst,2,0);
    VL_INOUT8(hmastlock,0,0);
    VL_INOUT8(hprot,6,0);
    VL_INOUT8(hsize,2,0);
    VL_INOUT8(hnonsec,0,0);
    VL_INOUT8(hexcl,0,0);
    VL_INOUT8(hmaster,3,0);
    VL_INOUT8(htrans,1,0);
    VL_INOUT8(hwrite,0,0);
    VL_INOUT8(hready,0,0);
    VL_INOUT8(hreadyout,0,0);
    VL_INOUT8(hresp,0,0);
    VL_INOUT8(hexokay,0,0);
    VL_INOUT8(hsel,0,0);
    CData/*0:0*/ ahb_template__DOT__hclk;
    CData/*0:0*/ ahb_template__DOT__hresetn;
    CData/*2:0*/ ahb_template__DOT__hburst;
    CData/*0:0*/ ahb_template__DOT__hmastlock;
    CData/*6:0*/ ahb_template__DOT__hprot;
    CData/*2:0*/ ahb_template__DOT__hsize;
    CData/*0:0*/ ahb_template__DOT__hnonsec;
    CData/*0:0*/ ahb_template__DOT__hexcl;
    CData/*3:0*/ ahb_template__DOT__hmaster;
    CData/*1:0*/ ahb_template__DOT__htrans;
    CData/*0:0*/ ahb_template__DOT__hwrite;
    CData/*0:0*/ ahb_template__DOT__hready;
    CData/*0:0*/ ahb_template__DOT__hreadyout;
    CData/*0:0*/ ahb_template__DOT__hresp;
    CData/*0:0*/ ahb_template__DOT__hexokay;
    CData/*0:0*/ ahb_template__DOT__hsel;
    CData/*0:0*/ ahb_template__DOT____Vtogcov__hclk;
    CData/*0:0*/ ahb_template__DOT____Vtogcov__hresetn;
    CData/*2:0*/ ahb_template__DOT____Vtogcov__hburst;
    CData/*0:0*/ ahb_template__DOT____Vtogcov__hmastlock;
    CData/*6:0*/ ahb_template__DOT____Vtogcov__hprot;
    CData/*2:0*/ ahb_template__DOT____Vtogcov__hsize;
    CData/*0:0*/ ahb_template__DOT____Vtogcov__hnonsec;
    CData/*0:0*/ ahb_template__DOT____Vtogcov__hexcl;
    CData/*3:0*/ ahb_template__DOT____Vtogcov__hmaster;
    CData/*1:0*/ ahb_template__DOT____Vtogcov__htrans;
    CData/*0:0*/ ahb_template__DOT____Vtogcov__hwrite;
    CData/*0:0*/ ahb_template__DOT____Vtogcov__hready;
    CData/*0:0*/ ahb_template__DOT____Vtogcov__hreadyout;
    CData/*0:0*/ ahb_template__DOT____Vtogcov__hresp;
    CData/*0:0*/ ahb_template__DOT____Vtogcov__hexokay;
    CData/*0:0*/ ahb_template__DOT____Vtogcov__hsel;
    CData/*0:0*/ __VactContinue;
    VL_INOUT(haddr,31,0);
    VL_INOUT(hwdata,31,0);
    VL_INOUT(hrdata,31,0);
    IData/*31:0*/ ahb_template__DOT__haddr;
    IData/*31:0*/ ahb_template__DOT__hwdata;
    IData/*31:0*/ ahb_template__DOT__hrdata;
    IData/*31:0*/ ahb_template__DOT____Vtogcov__haddr;
    IData/*31:0*/ ahb_template__DOT____Vtogcov__hwdata;
    IData/*31:0*/ ahb_template__DOT____Vtogcov__hrdata;
    IData/*31:0*/ __VstlIterCount;
    IData/*31:0*/ __VicoIterCount;
    IData/*31:0*/ __VactIterCount;
    VlTriggerVec<1> __VstlTriggered;
    VlTriggerVec<1> __VicoTriggered;
    VlTriggerVec<0> __VactTriggered;
    VlTriggerVec<0> __VnbaTriggered;

    // INTERNAL VARIABLES
    Vtop__Syms* const vlSymsp;

    // PARAMETERS
    static constexpr IData/*31:0*/ ahb_template__DOT__ADDR_WIDTH = 0x00000020U;
    static constexpr IData/*31:0*/ ahb_template__DOT__DATA_WIDTH = 0x00000020U;

    // CONSTRUCTORS
    Vtop___024root(Vtop__Syms* symsp, const char* v__name);
    ~Vtop___024root();
    VL_UNCOPYABLE(Vtop___024root);

    // INTERNAL METHODS
    void __Vconfigure(bool first);
    void __vlCoverInsert(std::atomic<uint32_t>* countp, bool enable, const char* filenamep, int lineno, int column,
        const char* hierp, const char* pagep, const char* commentp, const char* linescovp);
};


#endif  // guard
