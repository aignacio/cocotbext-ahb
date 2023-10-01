// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vtop.h for the primary calling header

#include "verilated.h"
#include "verilated_dpi.h"

#include "Vtop__Syms.h"
#include "Vtop__Syms.h"
#include "Vtop___024root.h"

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__ico(Vtop___024root* vlSelf);
#endif  // VL_DEBUG

void Vtop___024root___eval_triggers__ico(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_triggers__ico\n"); );
    // Body
    vlSelf->__VicoTriggered.set(0U, (0U == vlSelf->__VicoIterCount));
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        Vtop___024root___dump_triggers__ico(vlSelf);
    }
#endif
}

VL_INLINE_OPT void Vtop___024root___ico_sequent__TOP__0(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___ico_sequent__TOP__0\n"); );
    // Body
    vlSelf->ahb_template__DOT__hclk = vlSelf->hclk;
    vlSelf->ahb_template__DOT__hresetn = vlSelf->hresetn;
    vlSelf->ahb_template__DOT__haddr = vlSelf->haddr;
    vlSelf->ahb_template__DOT__hburst = vlSelf->hburst;
    vlSelf->ahb_template__DOT__hmastlock = vlSelf->hmastlock;
    vlSelf->ahb_template__DOT__hprot = vlSelf->hprot;
    vlSelf->ahb_template__DOT__hsize = vlSelf->hsize;
    vlSelf->ahb_template__DOT__hnonsec = vlSelf->hnonsec;
    vlSelf->ahb_template__DOT__hexcl = vlSelf->hexcl;
    vlSelf->ahb_template__DOT__hmaster = vlSelf->hmaster;
    vlSelf->ahb_template__DOT__htrans = vlSelf->htrans;
    vlSelf->ahb_template__DOT__hwdata = vlSelf->hwdata;
    vlSelf->ahb_template__DOT__hwrite = vlSelf->hwrite;
    vlSelf->ahb_template__DOT__hready = vlSelf->hready;
    vlSelf->ahb_template__DOT__hrdata = vlSelf->hrdata;
    vlSelf->ahb_template__DOT__hreadyout = vlSelf->hreadyout;
    vlSelf->ahb_template__DOT__hresp = vlSelf->hresp;
    vlSelf->ahb_template__DOT__hexokay = vlSelf->hexokay;
    vlSelf->ahb_template__DOT__hsel = vlSelf->hsel;
    if (((IData)(vlSelf->hclk) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hclk))) {
        vlSymsp->__Vcoverage[0].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hclk 
            = vlSelf->hclk;
    }
    if (((IData)(vlSelf->hresetn) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hresetn))) {
        vlSymsp->__Vcoverage[1].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hresetn 
            = vlSelf->hresetn;
    }
    if (((IData)(vlSelf->hmastlock) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hmastlock))) {
        vlSymsp->__Vcoverage[37].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hmastlock 
            = vlSelf->hmastlock;
    }
    if (((IData)(vlSelf->hnonsec) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hnonsec))) {
        vlSymsp->__Vcoverage[48].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hnonsec 
            = vlSelf->hnonsec;
    }
    if (((IData)(vlSelf->hexcl) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hexcl))) {
        vlSymsp->__Vcoverage[49].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hexcl 
            = vlSelf->hexcl;
    }
    if (((IData)(vlSelf->hwrite) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hwrite))) {
        vlSymsp->__Vcoverage[88].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwrite 
            = vlSelf->hwrite;
    }
    if (((IData)(vlSelf->hready) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hready))) {
        vlSymsp->__Vcoverage[89].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hready 
            = vlSelf->hready;
    }
    if (((IData)(vlSelf->hreadyout) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hreadyout))) {
        vlSymsp->__Vcoverage[122].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hreadyout 
            = vlSelf->hreadyout;
    }
    if (((IData)(vlSelf->hresp) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hresp))) {
        vlSymsp->__Vcoverage[123].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hresp 
            = vlSelf->hresp;
    }
    if (((IData)(vlSelf->hexokay) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hexokay))) {
        vlSymsp->__Vcoverage[124].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hexokay 
            = vlSelf->hexokay;
    }
    if (((IData)(vlSelf->hsel) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hsel))) {
        vlSymsp->__Vcoverage[125].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hsel 
            = vlSelf->hsel;
    }
    if ((1U & ((IData)(vlSelf->htrans) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__htrans)))) {
        vlSymsp->__Vcoverage[54].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__htrans 
            = ((2U & (IData)(vlSelf->ahb_template__DOT____Vtogcov__htrans)) 
               | (1U & (IData)(vlSelf->htrans)));
    }
    if ((2U & ((IData)(vlSelf->htrans) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__htrans)))) {
        vlSymsp->__Vcoverage[55].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__htrans 
            = ((1U & (IData)(vlSelf->ahb_template__DOT____Vtogcov__htrans)) 
               | (2U & (IData)(vlSelf->htrans)));
    }
    if ((1U & ((IData)(vlSelf->hburst) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hburst)))) {
        vlSymsp->__Vcoverage[34].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hburst 
            = ((6U & (IData)(vlSelf->ahb_template__DOT____Vtogcov__hburst)) 
               | (1U & (IData)(vlSelf->hburst)));
    }
    if ((2U & ((IData)(vlSelf->hburst) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hburst)))) {
        vlSymsp->__Vcoverage[35].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hburst 
            = ((5U & (IData)(vlSelf->ahb_template__DOT____Vtogcov__hburst)) 
               | (2U & (IData)(vlSelf->hburst)));
    }
    if ((4U & ((IData)(vlSelf->hburst) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hburst)))) {
        vlSymsp->__Vcoverage[36].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hburst 
            = ((3U & (IData)(vlSelf->ahb_template__DOT____Vtogcov__hburst)) 
               | (4U & (IData)(vlSelf->hburst)));
    }
    if ((1U & ((IData)(vlSelf->hsize) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hsize)))) {
        vlSymsp->__Vcoverage[45].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hsize 
            = ((6U & (IData)(vlSelf->ahb_template__DOT____Vtogcov__hsize)) 
               | (1U & (IData)(vlSelf->hsize)));
    }
    if ((2U & ((IData)(vlSelf->hsize) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hsize)))) {
        vlSymsp->__Vcoverage[46].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hsize 
            = ((5U & (IData)(vlSelf->ahb_template__DOT____Vtogcov__hsize)) 
               | (2U & (IData)(vlSelf->hsize)));
    }
    if ((4U & ((IData)(vlSelf->hsize) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hsize)))) {
        vlSymsp->__Vcoverage[47].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hsize 
            = ((3U & (IData)(vlSelf->ahb_template__DOT____Vtogcov__hsize)) 
               | (4U & (IData)(vlSelf->hsize)));
    }
    if ((1U & ((IData)(vlSelf->hmaster) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hmaster)))) {
        vlSymsp->__Vcoverage[50].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hmaster 
            = ((0xeU & (IData)(vlSelf->ahb_template__DOT____Vtogcov__hmaster)) 
               | (1U & (IData)(vlSelf->hmaster)));
    }
    if ((2U & ((IData)(vlSelf->hmaster) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hmaster)))) {
        vlSymsp->__Vcoverage[51].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hmaster 
            = ((0xdU & (IData)(vlSelf->ahb_template__DOT____Vtogcov__hmaster)) 
               | (2U & (IData)(vlSelf->hmaster)));
    }
    if ((4U & ((IData)(vlSelf->hmaster) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hmaster)))) {
        vlSymsp->__Vcoverage[52].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hmaster 
            = ((0xbU & (IData)(vlSelf->ahb_template__DOT____Vtogcov__hmaster)) 
               | (4U & (IData)(vlSelf->hmaster)));
    }
    if ((8U & ((IData)(vlSelf->hmaster) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hmaster)))) {
        vlSymsp->__Vcoverage[53].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hmaster 
            = ((7U & (IData)(vlSelf->ahb_template__DOT____Vtogcov__hmaster)) 
               | (8U & (IData)(vlSelf->hmaster)));
    }
    if ((1U & ((IData)(vlSelf->hprot) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hprot)))) {
        vlSymsp->__Vcoverage[38].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hprot 
            = ((0x7eU & (IData)(vlSelf->ahb_template__DOT____Vtogcov__hprot)) 
               | (1U & (IData)(vlSelf->hprot)));
    }
    if ((2U & ((IData)(vlSelf->hprot) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hprot)))) {
        vlSymsp->__Vcoverage[39].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hprot 
            = ((0x7dU & (IData)(vlSelf->ahb_template__DOT____Vtogcov__hprot)) 
               | (2U & (IData)(vlSelf->hprot)));
    }
    if ((4U & ((IData)(vlSelf->hprot) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hprot)))) {
        vlSymsp->__Vcoverage[40].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hprot 
            = ((0x7bU & (IData)(vlSelf->ahb_template__DOT____Vtogcov__hprot)) 
               | (4U & (IData)(vlSelf->hprot)));
    }
    if ((8U & ((IData)(vlSelf->hprot) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hprot)))) {
        vlSymsp->__Vcoverage[41].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hprot 
            = ((0x77U & (IData)(vlSelf->ahb_template__DOT____Vtogcov__hprot)) 
               | (8U & (IData)(vlSelf->hprot)));
    }
    if ((0x10U & ((IData)(vlSelf->hprot) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hprot)))) {
        vlSymsp->__Vcoverage[42].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hprot 
            = ((0x6fU & (IData)(vlSelf->ahb_template__DOT____Vtogcov__hprot)) 
               | (0x10U & (IData)(vlSelf->hprot)));
    }
    if ((0x20U & ((IData)(vlSelf->hprot) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hprot)))) {
        vlSymsp->__Vcoverage[43].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hprot 
            = ((0x5fU & (IData)(vlSelf->ahb_template__DOT____Vtogcov__hprot)) 
               | (0x20U & (IData)(vlSelf->hprot)));
    }
    if ((0x40U & ((IData)(vlSelf->hprot) ^ (IData)(vlSelf->ahb_template__DOT____Vtogcov__hprot)))) {
        vlSymsp->__Vcoverage[44].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hprot 
            = ((0x3fU & (IData)(vlSelf->ahb_template__DOT____Vtogcov__hprot)) 
               | (0x40U & (IData)(vlSelf->hprot)));
    }
    if ((1U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[2].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xfffffffeU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (1U & vlSelf->haddr));
    }
    if ((2U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[3].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xfffffffdU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (2U & vlSelf->haddr));
    }
    if ((4U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[4].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xfffffffbU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (4U & vlSelf->haddr));
    }
    if ((8U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[5].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xfffffff7U & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (8U & vlSelf->haddr));
    }
    if ((0x10U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[6].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xffffffefU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x10U & vlSelf->haddr));
    }
    if ((0x20U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[7].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xffffffdfU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x20U & vlSelf->haddr));
    }
    if ((0x40U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[8].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xffffffbfU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x40U & vlSelf->haddr));
    }
    if ((0x80U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[9].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xffffff7fU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x80U & vlSelf->haddr));
    }
    if ((0x100U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[10].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xfffffeffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x100U & vlSelf->haddr));
    }
    if ((0x200U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[11].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xfffffdffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x200U & vlSelf->haddr));
    }
    if ((0x400U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[12].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xfffffbffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x400U & vlSelf->haddr));
    }
    if ((0x800U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[13].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xfffff7ffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x800U & vlSelf->haddr));
    }
    if ((0x1000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[14].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xffffefffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x1000U & vlSelf->haddr));
    }
    if ((0x2000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[15].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xffffdfffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x2000U & vlSelf->haddr));
    }
    if ((0x4000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[16].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xffffbfffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x4000U & vlSelf->haddr));
    }
    if ((0x8000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[17].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xffff7fffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x8000U & vlSelf->haddr));
    }
    if ((0x10000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[18].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xfffeffffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x10000U & vlSelf->haddr));
    }
    if ((0x20000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[19].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xfffdffffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x20000U & vlSelf->haddr));
    }
    if ((0x40000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[20].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xfffbffffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x40000U & vlSelf->haddr));
    }
    if ((0x80000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[21].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xfff7ffffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x80000U & vlSelf->haddr));
    }
    if ((0x100000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[22].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xffefffffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x100000U & vlSelf->haddr));
    }
    if ((0x200000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[23].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xffdfffffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x200000U & vlSelf->haddr));
    }
    if ((0x400000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[24].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xffbfffffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x400000U & vlSelf->haddr));
    }
    if ((0x800000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[25].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xff7fffffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x800000U & vlSelf->haddr));
    }
    if ((0x1000000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[26].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xfeffffffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x1000000U & vlSelf->haddr));
    }
    if ((0x2000000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[27].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xfdffffffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x2000000U & vlSelf->haddr));
    }
    if ((0x4000000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[28].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xfbffffffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x4000000U & vlSelf->haddr));
    }
    if ((0x8000000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[29].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xf7ffffffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x8000000U & vlSelf->haddr));
    }
    if ((0x10000000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[30].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xefffffffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x10000000U & vlSelf->haddr));
    }
    if ((0x20000000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[31].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xdfffffffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x20000000U & vlSelf->haddr));
    }
    if ((0x40000000U & (vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr))) {
        vlSymsp->__Vcoverage[32].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0xbfffffffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x40000000U & vlSelf->haddr));
    }
    if (((vlSelf->haddr ^ vlSelf->ahb_template__DOT____Vtogcov__haddr) 
         >> 0x1fU)) {
        vlSymsp->__Vcoverage[33].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__haddr 
            = ((0x7fffffffU & vlSelf->ahb_template__DOT____Vtogcov__haddr) 
               | (0x80000000U & vlSelf->haddr));
    }
    if ((1U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[56].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xfffffffeU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (1U & vlSelf->hwdata));
    }
    if ((2U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[57].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xfffffffdU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (2U & vlSelf->hwdata));
    }
    if ((4U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[58].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xfffffffbU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (4U & vlSelf->hwdata));
    }
    if ((8U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[59].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xfffffff7U & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (8U & vlSelf->hwdata));
    }
    if ((0x10U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[60].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xffffffefU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x10U & vlSelf->hwdata));
    }
    if ((0x20U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[61].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xffffffdfU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x20U & vlSelf->hwdata));
    }
    if ((0x40U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[62].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xffffffbfU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x40U & vlSelf->hwdata));
    }
    if ((0x80U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[63].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xffffff7fU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x80U & vlSelf->hwdata));
    }
    if ((0x100U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[64].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xfffffeffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x100U & vlSelf->hwdata));
    }
    if ((0x200U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[65].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xfffffdffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x200U & vlSelf->hwdata));
    }
    if ((0x400U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[66].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xfffffbffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x400U & vlSelf->hwdata));
    }
    if ((0x800U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[67].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xfffff7ffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x800U & vlSelf->hwdata));
    }
    if ((0x1000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[68].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xffffefffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x1000U & vlSelf->hwdata));
    }
    if ((0x2000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[69].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xffffdfffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x2000U & vlSelf->hwdata));
    }
    if ((0x4000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[70].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xffffbfffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x4000U & vlSelf->hwdata));
    }
    if ((0x8000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[71].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xffff7fffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x8000U & vlSelf->hwdata));
    }
    if ((0x10000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[72].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xfffeffffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x10000U & vlSelf->hwdata));
    }
    if ((0x20000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[73].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xfffdffffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x20000U & vlSelf->hwdata));
    }
    if ((0x40000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[74].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xfffbffffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x40000U & vlSelf->hwdata));
    }
    if ((0x80000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[75].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xfff7ffffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x80000U & vlSelf->hwdata));
    }
    if ((0x100000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[76].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xffefffffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x100000U & vlSelf->hwdata));
    }
    if ((0x200000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[77].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xffdfffffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x200000U & vlSelf->hwdata));
    }
    if ((0x400000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[78].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xffbfffffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x400000U & vlSelf->hwdata));
    }
    if ((0x800000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[79].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xff7fffffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x800000U & vlSelf->hwdata));
    }
    if ((0x1000000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[80].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xfeffffffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x1000000U & vlSelf->hwdata));
    }
    if ((0x2000000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[81].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xfdffffffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x2000000U & vlSelf->hwdata));
    }
    if ((0x4000000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[82].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xfbffffffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x4000000U & vlSelf->hwdata));
    }
    if ((0x8000000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[83].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xf7ffffffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x8000000U & vlSelf->hwdata));
    }
    if ((0x10000000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[84].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xefffffffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x10000000U & vlSelf->hwdata));
    }
    if ((0x20000000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[85].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xdfffffffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x20000000U & vlSelf->hwdata));
    }
    if ((0x40000000U & (vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata))) {
        vlSymsp->__Vcoverage[86].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0xbfffffffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x40000000U & vlSelf->hwdata));
    }
    if (((vlSelf->hwdata ^ vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
         >> 0x1fU)) {
        vlSymsp->__Vcoverage[87].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hwdata 
            = ((0x7fffffffU & vlSelf->ahb_template__DOT____Vtogcov__hwdata) 
               | (0x80000000U & vlSelf->hwdata));
    }
    if ((1U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[90].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xfffffffeU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (1U & vlSelf->hrdata));
    }
    if ((2U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[91].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xfffffffdU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (2U & vlSelf->hrdata));
    }
    if ((4U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[92].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xfffffffbU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (4U & vlSelf->hrdata));
    }
    if ((8U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[93].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xfffffff7U & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (8U & vlSelf->hrdata));
    }
    if ((0x10U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[94].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xffffffefU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x10U & vlSelf->hrdata));
    }
    if ((0x20U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[95].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xffffffdfU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x20U & vlSelf->hrdata));
    }
    if ((0x40U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[96].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xffffffbfU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x40U & vlSelf->hrdata));
    }
    if ((0x80U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[97].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xffffff7fU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x80U & vlSelf->hrdata));
    }
    if ((0x100U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[98].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xfffffeffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x100U & vlSelf->hrdata));
    }
    if ((0x200U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[99].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xfffffdffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x200U & vlSelf->hrdata));
    }
    if ((0x400U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[100].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xfffffbffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x400U & vlSelf->hrdata));
    }
    if ((0x800U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[101].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xfffff7ffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x800U & vlSelf->hrdata));
    }
    if ((0x1000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[102].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xffffefffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x1000U & vlSelf->hrdata));
    }
    if ((0x2000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[103].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xffffdfffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x2000U & vlSelf->hrdata));
    }
    if ((0x4000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[104].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xffffbfffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x4000U & vlSelf->hrdata));
    }
    if ((0x8000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[105].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xffff7fffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x8000U & vlSelf->hrdata));
    }
    if ((0x10000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[106].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xfffeffffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x10000U & vlSelf->hrdata));
    }
    if ((0x20000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[107].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xfffdffffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x20000U & vlSelf->hrdata));
    }
    if ((0x40000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[108].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xfffbffffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x40000U & vlSelf->hrdata));
    }
    if ((0x80000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[109].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xfff7ffffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x80000U & vlSelf->hrdata));
    }
    if ((0x100000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[110].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xffefffffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x100000U & vlSelf->hrdata));
    }
    if ((0x200000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[111].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xffdfffffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x200000U & vlSelf->hrdata));
    }
    if ((0x400000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[112].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xffbfffffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x400000U & vlSelf->hrdata));
    }
    if ((0x800000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[113].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xff7fffffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x800000U & vlSelf->hrdata));
    }
    if ((0x1000000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[114].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xfeffffffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x1000000U & vlSelf->hrdata));
    }
    if ((0x2000000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[115].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xfdffffffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x2000000U & vlSelf->hrdata));
    }
    if ((0x4000000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[116].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xfbffffffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x4000000U & vlSelf->hrdata));
    }
    if ((0x8000000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[117].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xf7ffffffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x8000000U & vlSelf->hrdata));
    }
    if ((0x10000000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[118].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xefffffffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x10000000U & vlSelf->hrdata));
    }
    if ((0x20000000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[119].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xdfffffffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x20000000U & vlSelf->hrdata));
    }
    if ((0x40000000U & (vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata))) {
        vlSymsp->__Vcoverage[120].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0xbfffffffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x40000000U & vlSelf->hrdata));
    }
    if (((vlSelf->hrdata ^ vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
         >> 0x1fU)) {
        vlSymsp->__Vcoverage[121].fetch_add(1, std::memory_order_relaxed);
        vlSelf->ahb_template__DOT____Vtogcov__hrdata 
            = ((0x7fffffffU & vlSelf->ahb_template__DOT____Vtogcov__hrdata) 
               | (0x80000000U & vlSelf->hrdata));
    }
}

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__act(Vtop___024root* vlSelf);
#endif  // VL_DEBUG

void Vtop___024root___eval_triggers__act(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_triggers__act\n"); );
    // Body
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        Vtop___024root___dump_triggers__act(vlSelf);
    }
#endif
}
