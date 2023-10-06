module dump();
  initial begin
    $dumpfile("waves.lxt");
    $dumpvars(0, dut);
  end
endmodule
