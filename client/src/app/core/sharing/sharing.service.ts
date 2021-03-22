import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SharingService {
  /**
   * Tries to share the text using the sharing API for smartphone. If
   * not possible, copies a sharable text to the clipboard. Returns false
   * if it is not possible to use the sharing api.
   * @param title a title for the text
   * @param text the body of the text
   * @param url a url to share
   */
  public shareContent(title: string, text: string, url: string): boolean {
    let sharingApiAvailable = false;
    const completeText = title + ' ' + text + ' ' + url;

    if (navigator.share) {
      navigator.share({ title, text, url }).then(() => {
        console.log('Thanks for sharing!');
      }).catch(console.error);

      sharingApiAvailable = true;
    } else {
      // fallback
      this.copyToClipboard(completeText);
    }

    return sharingApiAvailable;
  }


  /**
   * Copies a text to the clipboard of the user, such as with ctrl+c.
   * @param text the copied text
   */
  public copyToClipboard(text: string): void {
    // Create new element
    const el = document.createElement('textarea');
    // Set value (string to be copied)
    el.value = text;
    // Set non-editable to avoid focus and move outside of view
    el.setAttribute('readonly', '');

    document.body.appendChild(el);
    // Select text inside element
    el.select();
    // Copy text to clipboard
    document.execCommand('copy');
    // Remove temporary element
    document.body.removeChild(el);
  }
}
