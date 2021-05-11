export interface SummaryTableModel {
  heads: string[];
  rows: {
    title: string;
    isIncrementPositive?: boolean;
    isPercFormat: boolean;
    values: {
      increment: number;
      value: number;
    }[];
  }[];
}
