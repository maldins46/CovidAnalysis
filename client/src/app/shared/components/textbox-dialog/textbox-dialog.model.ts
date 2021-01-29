export interface TextboxDialogData {
  content: string;
  textBoxTitle: string;
  textBoxHint: string;
  minimumTextLength?: number;
  textType?: string;
  positiveAction: {
    text: string,
    execute: ((textBoxValue: string) => void)
  };
  negativeAction: {
    text: string,
    execute: ((textBoxValue: string) => void)
  };
}
