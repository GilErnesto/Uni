
/*!
 * Color mode toggler for Bootstrap's docs (https://getbootstrap.com/)
 * Copyright 2011-2023 The Bootstrap Authors
 * Licensed under the Creative Commons Attribution 3.0 Unported License.
 */

(() => {
    'use strict';

    const getStoredTheme = () => localStorage.getItem('theme');
    const setStoredTheme = theme => localStorage.setItem('theme', theme);

    const getPreferredTheme = () => {
        const storedTheme = getStoredTheme();
        if (storedTheme) {
            return storedTheme;
        }
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    };

    const setTheme = theme => {
        if (theme === 'auto' && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.documentElement.setAttribute('data-bs-theme', 'dark');
        } else {
            document.documentElement.setAttribute('data-bs-theme', theme);
        }

        const roundedButtons = document.querySelectorAll('.rounded-button');
        roundedButtons.forEach(button => {
            button.classList.toggle('dark-mode', theme === 'dark');
        });

        const logo = document.getElementById('logo');
        const logoP = document.getElementById('logoP');
        if (logo && logoP) {
            // Exibe apenas o logo correspondente ao tema
            logo.hidden = theme === 'dark';
            logoP.hidden = theme !== 'dark';

            // Aplica a classe 'dark-mode' se o tema for escuro
            logo.classList.toggle('dark-mode', theme === 'dark');
            logoP.classList.toggle('dark-mode', theme === 'dark');
        }


        showActiveTheme(theme);
    };

    const showActiveTheme = (theme, focus = false) => {
        const themeSwitcher = document.querySelector('#bd-theme');
        if (!themeSwitcher) {
            return;
        }

        const btnToActive = document.querySelector(`[data-bs-theme-value="${theme}"]`);
        document.querySelectorAll('[data-bs-theme-value]').forEach(element => {
            element.classList.add('opacity-50');
            element.setAttribute('aria-pressed', 'false');
        });

        if (btnToActive) {
            btnToActive.classList.remove('opacity-50');
            btnToActive.setAttribute('aria-pressed', 'true');
        }

        if (focus) {
            themeSwitcher.focus();
        }
    };

    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
        const storedTheme = getStoredTheme();
        if (storedTheme !== 'light' && storedTheme !== 'dark') {
            setTheme(getPreferredTheme());
        }
    });

    window.addEventListener('DOMContentLoaded', () => {
        const preferredTheme = getPreferredTheme();
        setTheme(preferredTheme);
        showActiveTheme(preferredTheme);

        document.querySelectorAll('[data-bs-theme-value]').forEach(toggle => {
            toggle.addEventListener('click', () => {
                const theme = toggle.getAttribute('data-bs-theme-value');
                setStoredTheme(theme);
                setTheme(theme);
                showActiveTheme(theme, true);
            });
        });
    });
})();