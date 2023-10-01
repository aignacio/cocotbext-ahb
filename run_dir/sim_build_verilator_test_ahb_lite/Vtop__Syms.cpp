// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Symbol table implementation internals

#include "Vtop__Syms.h"
#include "Vtop.h"
#include "Vtop___024root.h"

// FUNCTIONS
Vtop__Syms::~Vtop__Syms()
{

    // Tear down scope hierarchy
    __Vhier.remove(0, &__Vscope_ahb_template);

}

Vtop__Syms::Vtop__Syms(VerilatedContext* contextp, const char* namep, Vtop* modelp)
    : VerilatedSyms{contextp}
    // Setup internal state of the Syms class
    , __Vm_modelp{modelp}
    // Setup module instances
    , TOP{this, namep}
{
    // Configure time unit / time precision
    _vm_contextp__->timeunit(-12);
    _vm_contextp__->timeprecision(-12);
    // Setup each module's pointers to their submodules
    // Setup each module's pointer back to symbol table (for public functions)
    TOP.__Vconfigure(true);
    // Setup scopes
    __Vscope_TOP.configure(this, name(), "TOP", "TOP", 0, VerilatedScope::SCOPE_OTHER);
    __Vscope_ahb_template.configure(this, name(), "ahb_template", "ahb_template", -12, VerilatedScope::SCOPE_MODULE);

    // Set up scope hierarchy
    __Vhier.add(0, &__Vscope_ahb_template);

    // Setup export functions
    for (int __Vfinal = 0; __Vfinal < 2; ++__Vfinal) {
        __Vscope_TOP.varInsert(__Vfinal,"haddr", &(TOP.haddr), false, VLVT_UINT32,VLVD_INOUT|VLVF_PUB_RW,1 ,31,0);
        __Vscope_TOP.varInsert(__Vfinal,"hburst", &(TOP.hburst), false, VLVT_UINT8,VLVD_INOUT|VLVF_PUB_RW,1 ,2,0);
        __Vscope_TOP.varInsert(__Vfinal,"hclk", &(TOP.hclk), false, VLVT_UINT8,VLVD_IN|VLVF_PUB_RW,0);
        __Vscope_TOP.varInsert(__Vfinal,"hexcl", &(TOP.hexcl), false, VLVT_UINT8,VLVD_INOUT|VLVF_PUB_RW,0);
        __Vscope_TOP.varInsert(__Vfinal,"hexokay", &(TOP.hexokay), false, VLVT_UINT8,VLVD_INOUT|VLVF_PUB_RW,0);
        __Vscope_TOP.varInsert(__Vfinal,"hmaster", &(TOP.hmaster), false, VLVT_UINT8,VLVD_INOUT|VLVF_PUB_RW,1 ,3,0);
        __Vscope_TOP.varInsert(__Vfinal,"hmastlock", &(TOP.hmastlock), false, VLVT_UINT8,VLVD_INOUT|VLVF_PUB_RW,0);
        __Vscope_TOP.varInsert(__Vfinal,"hnonsec", &(TOP.hnonsec), false, VLVT_UINT8,VLVD_INOUT|VLVF_PUB_RW,0);
        __Vscope_TOP.varInsert(__Vfinal,"hprot", &(TOP.hprot), false, VLVT_UINT8,VLVD_INOUT|VLVF_PUB_RW,1 ,6,0);
        __Vscope_TOP.varInsert(__Vfinal,"hrdata", &(TOP.hrdata), false, VLVT_UINT32,VLVD_INOUT|VLVF_PUB_RW,1 ,31,0);
        __Vscope_TOP.varInsert(__Vfinal,"hready", &(TOP.hready), false, VLVT_UINT8,VLVD_INOUT|VLVF_PUB_RW,0);
        __Vscope_TOP.varInsert(__Vfinal,"hreadyout", &(TOP.hreadyout), false, VLVT_UINT8,VLVD_INOUT|VLVF_PUB_RW,0);
        __Vscope_TOP.varInsert(__Vfinal,"hresetn", &(TOP.hresetn), false, VLVT_UINT8,VLVD_IN|VLVF_PUB_RW,0);
        __Vscope_TOP.varInsert(__Vfinal,"hresp", &(TOP.hresp), false, VLVT_UINT8,VLVD_INOUT|VLVF_PUB_RW,0);
        __Vscope_TOP.varInsert(__Vfinal,"hsel", &(TOP.hsel), false, VLVT_UINT8,VLVD_INOUT|VLVF_PUB_RW,0);
        __Vscope_TOP.varInsert(__Vfinal,"hsize", &(TOP.hsize), false, VLVT_UINT8,VLVD_INOUT|VLVF_PUB_RW,1 ,2,0);
        __Vscope_TOP.varInsert(__Vfinal,"htrans", &(TOP.htrans), false, VLVT_UINT8,VLVD_INOUT|VLVF_PUB_RW,1 ,1,0);
        __Vscope_TOP.varInsert(__Vfinal,"hwdata", &(TOP.hwdata), false, VLVT_UINT32,VLVD_INOUT|VLVF_PUB_RW,1 ,31,0);
        __Vscope_TOP.varInsert(__Vfinal,"hwrite", &(TOP.hwrite), false, VLVT_UINT8,VLVD_INOUT|VLVF_PUB_RW,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"ADDR_WIDTH", const_cast<void*>(static_cast<const void*>(&(TOP.ahb_template__DOT__ADDR_WIDTH))), true, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"DATA_WIDTH", const_cast<void*>(static_cast<const void*>(&(TOP.ahb_template__DOT__DATA_WIDTH))), true, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"haddr", &(TOP.ahb_template__DOT__haddr), false, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"hburst", &(TOP.ahb_template__DOT__hburst), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,2,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"hclk", &(TOP.ahb_template__DOT__hclk), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"hexcl", &(TOP.ahb_template__DOT__hexcl), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"hexokay", &(TOP.ahb_template__DOT__hexokay), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"hmaster", &(TOP.ahb_template__DOT__hmaster), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"hmastlock", &(TOP.ahb_template__DOT__hmastlock), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"hnonsec", &(TOP.ahb_template__DOT__hnonsec), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"hprot", &(TOP.ahb_template__DOT__hprot), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,6,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"hrdata", &(TOP.ahb_template__DOT__hrdata), false, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"hready", &(TOP.ahb_template__DOT__hready), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"hreadyout", &(TOP.ahb_template__DOT__hreadyout), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"hresetn", &(TOP.ahb_template__DOT__hresetn), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"hresp", &(TOP.ahb_template__DOT__hresp), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"hsel", &(TOP.ahb_template__DOT__hsel), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"hsize", &(TOP.ahb_template__DOT__hsize), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,2,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"htrans", &(TOP.ahb_template__DOT__htrans), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,1,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"hwdata", &(TOP.ahb_template__DOT__hwdata), false, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_ahb_template.varInsert(__Vfinal,"hwrite", &(TOP.ahb_template__DOT__hwrite), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
    }
}
