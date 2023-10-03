/**
 * File              : dut.sv
 * License           : MIT license <Check LICENSE>
 * Author            : Anderson Ignacio da Silva (aignacio) <anderson@aignacio.com>
 * Date              : 01.10.2023
 * Last Modified Date: 03.10.2023
 */
module ahb_template #(
  parameter ADDR_WIDTH = 32,
  parameter DATA_WIDTH = 32
)(
  input                             hclk,
  input                             hresetn,
  //----------------------------------------
  // SLAVE - IN
  //---------------------------------------
  // From master/interconnect to slave/decoder 
  input   logic                     slave_hsel,
  input   logic [(ADDR_WIDTH-1):0]  slave_haddr,
  input   logic [2:0]               slave_hburst,
  input   logic                     slave_hmastlock,
  input   logic [6:0]               slave_hprot,
  input   logic [2:0]               slave_hsize,
  input   logic                     slave_hnonsec,
  input   logic                     slave_hexcl,
  input   logic [3:0]               slave_hmaster,
  input   logic [1:0]               slave_htrans,
  input   logic [(DATA_WIDTH-1):0]  slave_hwdata,
  input   logic                     slave_hwrite,
  // From slave to interconnect/master 
  output  logic [(DATA_WIDTH-1):0]  slave_hrdata,
  output  logic                     slave_hready,
  output  logic                     slave_hresp,
  output  logic                     slave_hexokay,
  //----------------------------------------
  // MASTER - OUT
  //---------------------------------------
  // From master/interconnect to slave/decoder 
  output  logic [(ADDR_WIDTH-1):0]  master_haddr,
  output  logic [2:0]               master_hburst,
  output  logic                     master_hmastlock,
  output  logic [6:0]               master_hprot,
  output  logic [2:0]               master_hsize,
  output  logic                     master_hnonsec,
  output  logic                     master_hexcl,
  output  logic [3:0]               master_hmaster,
  output  logic [1:0]               master_htrans,
  output  logic [(DATA_WIDTH-1):0]  master_hwdata,
  output  logic                     master_hwrite,
  // From slave to interconnect/master
  input   logic [(DATA_WIDTH-1):0]  master_hrdata,
  input   logic                     master_hready,
  input   logic                     master_hresp,
  input   logic                     master_hexokay
);
  always_comb begin
    master_haddr     = slave_haddr; 
    master_hburst    = slave_hburst;
    master_hmastlock = slave_hmastlock;
    master_hprot     = slave_hprot;
    master_hsize     = slave_hsize;
    master_hnonsec   = slave_hnonsec;
    master_hexcl     = slave_hexcl;
    master_hmaster   = slave_hmaster;
    master_htrans    = slave_htrans;
    master_hwdata    = slave_hwdata;
    master_hwrite    = slave_hwrite;
    
    slave_hrdata    = master_hrdata;
    slave_hready    = master_hready;
    slave_hresp     = master_hresp;
    slave_hexokay   = master_hexokay;
  end
endmodule
