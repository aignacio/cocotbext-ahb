/**
 * File              : dut.v
 * License           : MIT license <Check LICENSE>
 * Author            : Anderson Ignacio da Silva (aignacio) <anderson@aignacio.com>
 * Date              : 01.10.2023
 * Last Modified Date: 05.10.2023
 */
module ahb_template #(
  parameter ADDR_WIDTH = 32,
  parameter DATA_WIDTH = 32
)(
  input                       hclk,
  input                       hresetn,

  //----------------------------------------
  // SLAVE - IN
  //---------------------------------------
  // From master/interconnect to slave/decoder 
  input                       slave_hsel,
  input   [(ADDR_WIDTH-1):0]  slave_haddr,
  input   [2:0]               slave_hburst,
  input                       slave_hmastlock,
  input   [6:0]               slave_hprot,
  input   [2:0]               slave_hsize,
  input                       slave_hnonsec,
  input                       slave_hexcl,
  input   [3:0]               slave_hmaster,
  input   [1:0]               slave_htrans,
  input   [(DATA_WIDTH-1):0]  slave_hwdata,
  input                       slave_hwrite,
  input                       slave_hready_in,
  // From slave to interconnect/master 
  output  [(DATA_WIDTH-1):0]  slave_hrdata,
  output                      slave_hready,
  output                      slave_hresp,
  output                      slave_hexokay,
  //----------------------------------------
  // MASTER - OUT
  //---------------------------------------
  // From master/interconnect to slave/decoder 
  output                      master_hsel,
  output  [(ADDR_WIDTH-1):0]  master_haddr,
  output  [2:0]               master_hburst,
  output                      master_hmastlock,
  output  [6:0]               master_hprot,
  output  [2:0]               master_hsize,
  output                      master_hnonsec,
  output                      master_hexcl,
  output  [3:0]               master_hmaster,
  output  [1:0]               master_htrans,
  output  [(DATA_WIDTH-1):0]  master_hwdata,
  output                      master_hwrite,
  output                      master_hready_in,
  // From slave to interconnect/master
  input   [(DATA_WIDTH-1):0]  master_hrdata,
  input                       master_hready,
  input                       master_hresp,
  input                       master_hexokay
);
  assign master_haddr     = slave_haddr; 
  assign master_hburst    = slave_hburst;
  assign master_hmastlock = slave_hmastlock;
  assign master_hprot     = slave_hprot;
  assign master_hsize     = slave_hsize;
  assign master_hnonsec   = slave_hnonsec;
  assign master_hexcl     = slave_hexcl;
  assign master_hmaster   = slave_hmaster;
  assign master_htrans    = slave_htrans;
  assign master_hwdata    = slave_hwdata;
  assign master_hwrite    = slave_hwrite;
  assign master_hready_in = slave_hready_in;
  assign master_hsel      = slave_hsel;

  assign slave_hrdata     = master_hrdata;
  assign slave_hready     = master_hready;
  assign slave_hresp      = master_hresp;
  assign slave_hexokay    = master_hexokay;
endmodule
