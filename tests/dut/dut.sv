/**
 * File              : dut.sv
 * License           : MIT license <Check LICENSE>
 * Author            : Anderson Ignacio da Silva (aignacio) <anderson@aignacio.com>
 * Date              : 01.10.2023
 * Last Modified Date: 01.10.2023
 */
module ahb_template #(
  parameter ADDR_WIDTH = 32,
  parameter DATA_WIDTH = 32
)(
  input                           hclk,
  input                           hresetn,
  // From master/interconnect to slave/decoder 
  inout logic [(ADDR_WIDTH-1):0]  haddr,
  inout logic [2:0]               hburst,
  inout logic                     hmastlock,
  inout logic [6:0]               hprot,
  inout logic [2:0]               hsize,
  inout logic                     hnonsec,
  inout logic                     hexcl,
  inout logic [3:0]               hmaster,
  inout logic [1:0]               htrans,
  inout logic [(DATA_WIDTH-1):0]  hwdata,
  inout logic                     hwrite,
  inout logic                     hready,
  // From slave to interconnect/master 
  inout logic [(DATA_WIDTH-1):0]  hrdata,
  inout logic                     hreadyout,
  inout logic                     hresp,
  inout logic                     hexokay,
  inout logic                     hsel
);
endmodule
