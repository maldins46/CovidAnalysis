export class PointsCalculator {
  private static readonly IUNP_TARGET = 10000;
  private static readonly NEW_CUSTOMERS_TARGET = 15;
  private static readonly N_PAC_TARGET = 15;
  private static readonly VAL_PAC_TARGET = 36000;
  private static readonly N_PENS_FUND_TARGET = 15;
  private static readonly VAL_PENS_FUND_TARGET = 18000;
  private static readonly COMM_INN_TARGET = 10;
  private static readonly N_PARAMS = 7;

  static computePoints(iunp: number, newCustomers: number, nPac: number,
                       valPac: number, nPensFund: number, valPensFund: number, commInn: number): number {
    const effectivePoints = this.computeSingle(iunp, this.IUNP_TARGET) +
      this.computeSingle(newCustomers, this.NEW_CUSTOMERS_TARGET) +
      this.computeSingle(nPac, this.N_PAC_TARGET) +
      this.computeSingle(valPac, this.VAL_PAC_TARGET) +
      this.computeSingle(nPensFund, this.N_PENS_FUND_TARGET) +
      this.computeSingle(valPensFund, this.VAL_PENS_FUND_TARGET) +
      this.computeSingle(commInn, this.COMM_INN_TARGET);

    // points rounded at the third decimal
    return Math.round((effectivePoints + Number.EPSILON) * 1000) / 1000;
  }

  private static computeSingle(value: number, target: number): number {
    return (100 / this.N_PARAMS) * (value / target);
  }
}
