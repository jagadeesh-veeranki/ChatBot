/**
 * utils.js
 * Utility functions for DOM manipulation, formatting, and performance.
 */

/**
 * Enhanced DOM selector
 * @param {string} selector 
 * @param {Element} scope 
 * @returns {Element|null}
 */
export const $ = (selector, scope = document) => scope.querySelector(selector);

/**
 * Enhanced DOM selector all
 * @param {string} selector 
 * @param {Element} scope 
 * @returns {NodeList}
 */
export const $$ = (selector, scope = document) => scope.querySelectorAll(selector);

/**
 * Format timestamp to HH:MM AM/PM
 * @param {Date} date 
 * @returns {string}
 */
export const formatTime = (date = new Date()) => {
    return date.toLocaleTimeString('en-US', {
        hour: 'numeric',
        minute: 'numeric',
        hour12: true
    });
};

/**
 * Debounce function to limit execution rate
 * @param {Function} func 
 * @param {number} wait 
 * @returns {Function}
 */
export const debounce = (func, wait) => {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
};

/**
 * Escape HTML to prevent XSS (basic)
 * @param {string} unsafe 
 * @returns {string}
 */
export const escapeHTML = (unsafe) => {
    if (!unsafe) return '';
    return unsafe
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
};

/**
 * Generate a random ID
 * @returns {string}
 */
export const generateId = () => {
    return Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
};

/**
 * Save to LocalStorage safely
 */
export const storage = {
    get: (key, fallback = null) => {
        try {
            const item = localStorage.getItem(key);
            return item ? JSON.parse(item) : fallback;
        } catch (e) {
            console.warn('LocalStorage Access Denied', e);
            return fallback;
        }
    },
    set: (key, value) => {
        try {
            localStorage.setItem(key, JSON.stringify(value));
        } catch (e) {
            console.warn('LocalStorage Write Failed', e);
        }
    }
};
