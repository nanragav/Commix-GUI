# Session Save/Load - Visual Guide

## 📊 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     COMMIX GUI MAIN WINDOW                  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  File Menu                                           │  │
│  │  • New Project (Ctrl+N)  → Clear all & create new   │  │
│  │  • Open Project (Ctrl+O) → Load .cproj file         │  │
│  │  • Save Project (Ctrl+S) → Save current session     │  │
│  │  • Save As (Ctrl+Shift+S) → Save with new name      │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  9 Configuration Tabs - 90+ Total Fields            │  │
│  │  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐        │  │
│  │  │ Target │ │Request │ │  Auth  │ │Inject. │ ...    │  │
│  │  └────────┘ └────────┘ └────────┘ └────────┘        │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Output Console - Complete Output Saved              │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            ↕
                    SessionManager
                            ↕
                    .cproj File (JSON)
```

## 🔄 Complete Data Flow

```
SAVE: GUI → SessionManager → JSON File
LOAD: JSON File → SessionManager → GUI
```

**For complete visual documentation, see the implementation files!**
