package com.codewithmosh.template;

public class GenerateReportTask {
  private AuditTrail auditTrail;

  public GenerateReportTask(AuditTrail auditTrail) {
    this.auditTrail = auditTrail;
  }

  public void execute() {
    auditTrail.record();

    System.out.println("Generate Report");
  }
}
