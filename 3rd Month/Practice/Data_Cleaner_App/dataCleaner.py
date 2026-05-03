# ===================================
#         Libraries
# ===================================


import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression



# ===================================
#         UI Design
# ===================================


# ===================================
#     Regression Imputation Function
# ===================================

def apply_regression_imputation(df, target_col):
    """
    Impute missing values in target_col using regression.
    Step 1: Fill ALL other columns with mean/mode FIRST
    Step 2: Train model on complete data
    Step 3: Predict missing values for target_col
    """
    
    # Make a copy
    df_clean = df.copy()
    
    # Get count of missing values in target column
    missing_count = df_clean[target_col].isna().sum()
    
    if missing_count == 0:
        return df_clean[target_col], "No missing values found", True
    
    try:
        # ===== STEP 1: Fill ALL other columns FIRST (including the ones that will be features) =====
        for col in df_clean.columns:
            if col != target_col:  # Don't fill target column yet
                if df_clean[col].dtype in [np.float64, np.int64, 'float64', 'int64']:
                    # Numeric column -> fill with mean
                    mean_val = df_clean[col].mean()
                    if pd.isna(mean_val):  # If all values are NaN, use 0
                        mean_val = 0
                    df_clean[col] = df_clean[col].fillna(mean_val)
                else:
                    # Categorical column -> fill with mode
                    if not df_clean[col].mode().empty:
                        mode_val = df_clean[col].mode()[0]
                    else:
                        mode_val = "Unknown"
                    df_clean[col] = df_clean[col].fillna(mode_val)
        
        # ===== DOUBLE CHECK: Make sure NO NaNs remain in feature columns =====
        # This is critical! After filling, verify all columns except target have no NaNs
        for col in df_clean.columns:
            if col != target_col and df_clean[col].isna().sum() > 0:
                # If still have NaNs, force fill with 0 or "Unknown"
                if df_clean[col].dtype in [np.float64, np.int64, 'float64', 'int64']:
                    df_clean[col] = df_clean[col].fillna(0)
                else:
                    df_clean[col] = df_clean[col].fillna("Unknown")
        
        # ===== STEP 2: Separate training and prediction data =====
        # Rows where target column has value (for training)
        train_df = df_clean[df_clean[target_col].notna()]
        # Rows where target column is missing (need prediction)
        predict_df = df_clean[df_clean[target_col].isna()]
        
        # Need at least 3 rows to train
        if len(train_df) < 3:
            # Fallback to mean/mode
            if df_clean[target_col].dtype in [np.float64, np.int64, 'float64', 'int64']:
                fill_value = df_clean[target_col].mean()
                if pd.isna(fill_value):
                    fill_value = 0
                filled_column = df_clean[target_col].fillna(fill_value)
                return filled_column, f"Need at least 3 rows to train (have {len(train_df)}), used mean ({fill_value:.2f})", False
            else:
                if not df_clean[target_col].mode().empty:
                    fill_value = df_clean[target_col].mode()[0]
                else:
                    fill_value = "Unknown"
                filled_column = df_clean[target_col].fillna(fill_value)
                return filled_column, f"Need at least 3 rows to train (have {len(train_df)}), used mode ('{fill_value}')", False
        
        # ===== STEP 3: Prepare features (X) and target (y) =====
        # All columns except target become features
        feature_cols = [col for col in df_clean.columns if col != target_col]
        
        # Keep only numeric columns for features
        numeric_features = []
        for col in feature_cols:
            if df_clean[col].dtype in [np.float64, np.int64, 'float64', 'int64']:
                numeric_features.append(col)
        
        # If no numeric features, can't do regression
        if len(numeric_features) == 0:
            # Fallback to mean/mode
            if df_clean[target_col].dtype in [np.float64, np.int64, 'float64', 'int64']:
                fill_value = df_clean[target_col].mean()
                if pd.isna(fill_value):
                    fill_value = 0
                filled_column = df_clean[target_col].fillna(fill_value)
                return filled_column, f"No numeric features available, used mean ({fill_value:.2f})", False
            else:
                if not df_clean[target_col].mode().empty:
                    fill_value = df_clean[target_col].mode()[0]
                else:
                    fill_value = "Unknown"
                filled_column = df_clean[target_col].fillna(fill_value)
                return filled_column, f"No numeric features available, used mode ('{fill_value}')", False
        
        X_train = train_df[numeric_features]
        y_train = train_df[target_col]
        X_predict = predict_df[numeric_features]
        
        # FINAL CHECK: Ensure X_train has NO NaNs
        if X_train.isna().sum().sum() > 0:
            # If still has NaNs, fill them with 0
            X_train = X_train.fillna(0)
            X_predict = X_predict.fillna(0)
        
        # ===== STEP 4: Choose regression type =====
        target_is_numeric = df_clean[target_col].dtype in [np.float64, np.int64, 'float64', 'int64']
        
        if target_is_numeric:
            # Use Linear Regression for numbers
            model = LinearRegression()
            model.fit(X_train, y_train)
            predictions = model.predict(X_predict)
            predictions = predictions.round(2)
            method = f"Linear Regression (using {len(numeric_features)} features)"
            success = True
        else:
            # Use Logistic Regression for categories
            unique_classes = y_train.nunique()
            
            if unique_classes == 2:
                # Binary classification
                model = LogisticRegression(max_iter=1000)
                model.fit(X_train, y_train)
                predictions = model.predict(X_predict)
                method = f"Binary Logistic Regression (using {len(numeric_features)} features)"
                success = True
            else:
                # Too many classes, fallback to mode
                mode_val = y_train.mode()[0]
                predictions = [mode_val] * len(X_predict)
                method = f"Fallback: Mode imputation (found {unique_classes} classes, need binary for Logistic Regression)"
                success = False
        
        # ===== STEP 5: Create filled column =====
        filled_column = df_clean[target_col].copy()
        
        # Fill the missing positions with predictions
        if len(predictions) > 0:
            missing_indices = df_clean[target_col].isna()
            # Convert predictions to match original data type
            if not target_is_numeric:
                predictions = [str(p) for p in predictions]
            filled_column[missing_indices] = predictions
        
        log_message = f"✨ '{target_col}': Filled {missing_count} missing values using {method}"
        
        return filled_column, log_message, success
        
    except Exception as e:
        # Ultimate fallback - just use mean/mode
        if df_clean[target_col].dtype in [np.float64, np.int64, 'float64', 'int64']:
            fill_value = df_clean[target_col].mean()
            if pd.isna(fill_value):
                fill_value = 0
            filled_column = df_clean[target_col].fillna(fill_value)
            log_message = f"⚠️ '{target_col}': Regression failed ({str(e)[:100]}), used mean ({fill_value:.2f})"
        else:
            if not df_clean[target_col].mode().empty:
                fill_value = df_clean[target_col].mode()[0]
            else:
                fill_value = "Unknown"
            filled_column = df_clean[target_col].fillna(fill_value)
            log_message = f"⚠️ '{target_col}': Regression failed ({str(e)[:100]}), used mode ('{fill_value}')"
        
        return filled_column, log_message, False


def apply_regression_to_all_columns(df):
    """
    Apply regression imputation to ALL columns that have missing values.
    """
    
    df_filled = df.copy()
    logs = []
    
    # Find all columns with missing values
    cols_with_missing = [col for col in df_filled.columns if df_filled[col].isna().sum() > 0]
    
    if not cols_with_missing:
        return df_filled, ["✅ No missing values found in any column"]
    
    # Process each column that has missing values
    for col in cols_with_missing:
        filled_column, log_message, success = apply_regression_imputation(df_filled, col)
        df_filled[col] = filled_column
        logs.append(log_message)
    
    return df_filled, logs


# ===================================
#         UI Design
# ===================================



st.set_page_config(
    page_title="CSV Data Cleaner",
    page_icon="🧹",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    [data-testid="stSidebar"] * { color: #e0e0e0 !important; }

    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
    }
    [data-testid="stFileUploader"] {
        background: rgba(255, 255, 255, 0.03);
        border: 2px dashed rgba(99, 179, 237, 0.5);
        border-radius: 16px;
        padding: 20px;
    }
    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 12px;
        padding: 16px;
    }
    [data-testid="stMetricValue"] {
        color: #63b3ed !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
    }
    [data-testid="stMetricLabel"] { color: #a0aec0 !important; }

    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: 600;
        width: 100%;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    [data-testid="stDownloadButton"] > button {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: 600;
        width: 100%;
    }
    [data-testid="stCheckbox"] {
        background: rgba(255,255,255,0.03);
        border-radius: 8px;
        padding: 8px 12px;
        margin-bottom: 4px;
        border: 1px solid rgba(255,255,255,0.05);
    }
    [data-testid="stCheckbox"]:hover {
        background: rgba(102, 126, 234, 0.15);
        border-color: rgba(102, 126, 234, 0.4);
    }
    h1, h2, h3 { color: white !important; }
    p, label, .stMarkdown { color: #cbd5e0 !important; }
    [data-testid="stDataFrame"] { border-radius: 12px; overflow: hidden; }
    [data-testid="stExpander"] {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 12px;
    }
    hr { border-color: rgba(255,255,255,0.1) !important; }

    .sidebar-section {
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #667eea !important;
        margin: 16px 0 8px 0;
        padding-bottom: 4px;
        border-bottom: 1px solid rgba(102, 126, 234, 0.3);
    }
    .badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        font-size: 11px;
        font-weight: 600;
        padding: 2px 10px;
        border-radius: 20px;
        margin-left: 8px;
        vertical-align: middle;
    }
    .success-box {
        background: rgba(56, 239, 125, 0.1);
        border-left: 3px solid #38ef7d;
        border-radius: 0 8px 8px 0;
        padding: 12px 16px;
        margin: 12px 0;
        color: #c6f6d5 !important;
        font-size: 14px;
    }
    .warning-box {
        background: rgba(246, 173, 85, 0.1);
        border-left: 3px solid #f6ad55;
        border-radius: 0 8px 8px 0;
        padding: 12px 16px;
        margin: 12px 0;
        color: #fefcbf !important;
        font-size: 14px;
    }
    .info-box {
        background: rgba(99, 179, 237, 0.1);
        border-left: 3px solid #63b3ed;
        border-radius: 0 8px 8px 0;
        padding: 12px 16px;
        margin: 12px 0;
        color: #bee3f8 !important;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)


# ---------- SESSION STATE ----------
if "df" not in st.session_state:
    st.session_state.df = None
if "cleaned_df" not in st.session_state:
    st.session_state.cleaned_df = None
if "cleaning_log" not in st.session_state:
    st.session_state.cleaning_log = []


# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("""
        <div style='text-align:center; padding: 10px 0 20px 0;'>
            <div style='font-size:40px;'>🧹</div>
            <div style='font-size:20px; font-weight:800;
                        background: linear-gradient(135deg, #667eea, #a78bfa);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        margin-top:6px;'>CSV Data Cleaner</div>
            <div style='font-size:12px; color:#718096; margin-top:4px;'>
                Professional Data Cleaning Suite
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<p class="sidebar-section">🔧 Cleaning Options</p>', unsafe_allow_html=True)

    # 1. Remove Duplicates
    with st.expander("🗂️  Remove Duplicates", expanded=False):
        remove_dupes = st.checkbox("Remove duplicate rows", key="dedup")

    # 2. Handle Missing Values
    with st.expander("🕳️  Handle Missing Values", expanded=False):
        handle_nulls  = st.checkbox("Fix missing values", key="nulls")
        null_strategy = None
        custom_fill   = ""
        if handle_nulls:
            null_strategy = st.radio(
                "Strategy:",
                ["Drop rows with nulls", "Fill with Mean / Mode", "Fill with custom value","Apply Regression Algorithm"],
                key="null_strat"
            )
            if null_strategy == "Fill with custom value":
                custom_fill = st.text_input("Fill value:", placeholder="e.g. Unknown or 0", key="fill_val")

    # 3. Handle Outliers
    with st.expander("📊  Handle Outliers", expanded=False):
        handle_outliers  = st.checkbox("Handle outliers in numeric columns", key="outliers")
        outlier_strategy = None
        iqr_multiplier   = 1.5
        if handle_outliers:
            outlier_strategy = st.radio(
                "Strategy:",
                ["Remove outlier rows", "Cap to min / max boundary"],
                key="out_strat"
            )
            iqr_multiplier = st.slider(
                "IQR sensitivity", 1.0, 3.0, 1.5, 0.1,
                help="1.5 is standard. Lower = stricter.",
                key="iqr"
            )

    st.markdown("---")
    st.markdown('<p class="sidebar-section">🚀 Actions</p>', unsafe_allow_html=True)
    run_btn   = st.button("▶  Run Cleaning",  use_container_width=True)
    reset_btn = st.button("↺  Reset Data",    use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align:center; font-size:11px; color:#4a5568;'>
            v1.0 · CSV Data Cleaner
        </div>
    """, unsafe_allow_html=True)


# ---------- MAIN HEADER ----------
st.markdown("""
    <h1 style='margin-bottom:4px;'>
        🧹 CSV Data Cleaner
        <span class='badge'>BETA</span>
    </h1>
    <p style='color:#718096; font-size:15px; margin-top:0;'>
        Upload your CSV, pick cleaning options from the sidebar, and download your clean data.
    </p>
""", unsafe_allow_html=True)
st.markdown("---")


# ---------- FILE UPLOAD ----------
st.markdown("### 📂 Upload Your CSV File")
upload_col, _ = st.columns([2, 1])
with upload_col:
    uploaded_file = st.file_uploader("Drag & drop or click to browse", type=["csv"], label_visibility="collapsed")

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.session_state.df = df
        if st.session_state.cleaned_df is None:
            st.session_state.cleaned_df = df.copy()
        st.markdown(
            f"<div class='success-box'>✅ File uploaded: <strong>{uploaded_file.name}</strong> — {len(df):,} rows × {len(df.columns)} columns</div>",
            unsafe_allow_html=True
        )
    except Exception as e:
        st.markdown(f"<div class='warning-box'>⚠️ Could not read file: {e}</div>", unsafe_allow_html=True)

if reset_btn and st.session_state.df is not None:
    st.session_state.cleaned_df = st.session_state.df.copy()
    st.session_state.cleaning_log = []
    st.markdown("<div class='info-box'>↺ Data has been reset to original.</div>", unsafe_allow_html=True)


# ---------- METRICS ----------
if st.session_state.df is not None:
    df = st.session_state.df
    cdf = st.session_state.cleaned_df if st.session_state.cleaned_df is not None else df
    
    st.markdown("### 📊 Dataset Overview")
    m1, m2, m3, m4 = st.columns(4)
    
    # Calculate issues in original vs cleaned
    original_issues = df.duplicated().sum() + df.isnull().sum().sum()
    current_issues = cdf.duplicated().sum() + cdf.isnull().sum().sum()
    
    # Calculate percentage of issues FIXED (0% at start, 100% when clean)
    if original_issues > 0:
        issues_fixed_pct = ((original_issues - current_issues) / original_issues) * 100
    else:
        issues_fixed_pct = 100  # No issues to fix
    
    # Metric 1: Total rows
    rows_removed = len(df) - len(cdf)
    if rows_removed > 0:
        m1.metric("Total Rows", f"{len(cdf):,}", delta=f"-{rows_removed}")
    else:
        m1.metric("Total Rows", f"{len(df):,}")
    
    # Metric 2: Duplicates
    current_dupes = cdf.duplicated().sum()
    original_dupes = df.duplicated().sum()
    if current_dupes > 0:
        m2.metric("Duplicates", f"{current_dupes:,}", delta="⚠️ Present")
    elif original_dupes > 0 and current_dupes == 0:
        m2.metric("Duplicates", "0", delta="✅ Fixed")
    else:
        m2.metric("Duplicates", "0")
    
    # Metric 3: Missing values
    current_missing = cdf.isnull().sum().sum()
    original_missing = df.isnull().sum().sum()
    if current_missing > 0:
        m3.metric("Missing Values", f"{current_missing:,}", delta="⚠️ Present")
    elif original_missing > 0 and current_missing == 0:
        m3.metric("Missing Values", "0", delta="✅ Fixed")
    else:
        m3.metric("Missing Values", "0")
    
    # Metric 4: Issues fixed percentage (0% → 100%)
    if current_issues == 0:
        m4.metric("✨ Issues Fixed", f"{issues_fixed_pct:.0f}%", 
                  delta="✅ Complete", delta_color="normal")
    elif issues_fixed_pct == 0:
        m4.metric("🔧 Issues Fixed", "0%", 
                  delta="Run cleaning →", delta_color="inverse")
    else:
        m4.metric("🔧 Issues Fixed", f"{issues_fixed_pct:.0f}%", 
                  delta=f"{issues_fixed_pct:.0f}% Done", delta_color="normal")
    
    st.markdown("---")

    # ---------- TABS ----------
    tab1, tab2 = st.tabs(["📋 Original Data", "✨ Cleaned Data"])
    with tab1:
        st.markdown(f"**{len(df):,} rows × {len(df.columns):,} columns**")
        st.dataframe(df, use_container_width=True, height=380)
    with tab2:
        if cdf is not None:
            st.markdown(f"**{len(cdf):,} rows × {len(cdf.columns):,} columns**")
            st.dataframe(cdf, use_container_width=True, height=380)
        else:
            st.markdown("<div class='info-box'>ℹ️ Run cleaning to see results here.</div>", unsafe_allow_html=True)

    st.markdown("---")

# ===================================
#         Cleaning Functionalities
# ===================================

    if run_btn:
        cdf = st.session_state.df.copy()
        log = []

#----------------- |Removing Duplicates |-----------------

        if remove_dupes:
            before = len(cdf)
            cdf = cdf.drop_duplicates()
            log.append(f"🗂️ Removed **{before - len(cdf)}** duplicate row(s).")


#----------------- |Filling Missing values |-----------------

        if handle_nulls and null_strategy:
            null_count = cdf.isnull().sum().sum()
            
# -----------| Dropping NA |-----------
            if null_strategy == "Drop rows with nulls":
                cdf = cdf.dropna()
                log.append(f"🕳️ Dropped rows with nulls — **{null_count}** missing value(s) removed.")
            
            
# -----------| Filling NA with mean |-----------
            elif null_strategy == "Fill with Mean / Mode": 
                for col in cdf.columns:
                    if cdf[col].dtype in [np.float64, np.int64]:
                        cdf[col] = cdf[col].fillna(round(cdf[col].mean(), 2))
                    else:
                        if not cdf[col].mode().empty:
                            cdf[col] = cdf[col].fillna(cdf[col].mode()[0])
                            
                log.append(f"🕳️ Filled **{null_count}** missing value(s) — numbers → mean, text → mode.")
            
            

# -----------| Filling With Custom Values |-----------
            elif null_strategy == "Fill with custom value":
                cdf = cdf.fillna(custom_fill)
                log.append(f"🕳️ Filled **{null_count}** missing value(s) with `{custom_fill}`.")
            
            
            
# -----------| Appling Regression Algorithm |-----------
            elif null_strategy == "Apply Regression Algorithm":
                # Show processing message
                with st.spinner("🧠 Applying regression imputation to all columns..."):
                    # Call the function to process ALL columns with missing values
                    cdf, regression_logs = apply_regression_to_all_columns(cdf)
                    log.extend(regression_logs)
                # Show success message
                st.success("✅ Regression imputation completed!")
                
    
#----------------- |Handling Outliers |-----------------
              

        if handle_outliers and outlier_strategy:
            numeric_cols = cdf.select_dtypes(include=[np.number]).columns
            total_removed = 0
            for col in numeric_cols:
                Q1    = cdf[col].quantile(0.25)
                Q3    = cdf[col].quantile(0.75)
                IQR   = Q3 - Q1
                lower = Q1 - iqr_multiplier * IQR
                upper = Q3 + iqr_multiplier * IQR
                if outlier_strategy == "Remove outlier rows":
                    before = len(cdf)
                    cdf = cdf[(cdf[col] >= lower) & (cdf[col] <= upper)]
                    total_removed += before - len(cdf)
                else:
                    cdf[col] = cdf[col].clip(lower=lower, upper=upper)
            if outlier_strategy == "Remove outlier rows":
                log.append(f"📊 Removed **{total_removed}** outlier row(s) (IQR × {iqr_multiplier}).")
            else:
                log.append(f"📊 Capped outliers in **{len(numeric_cols)}** numeric column(s) (IQR × {iqr_multiplier}).")

        st.session_state.cleaned_df = cdf
        st.session_state.cleaning_log = log

        if log:
            st.success("✅ Cleaning complete!")
            st.rerun()
        else:
            st.warning("⚠️ No options selected — tick something in the sidebar first.")


    # ---------- CLEANING LOG ----------
    if st.session_state.cleaning_log:
        st.markdown("### 🪵 Cleaning Log")
        with st.expander("View applied operations", expanded=True):
            for entry in st.session_state.cleaning_log:
                st.markdown(f"- {entry}")
                

    # ---------- DOWNLOAD ----------
    if st.session_state.cleaned_df is not None:
        st.markdown("### 💾 Download Cleaned Data")
        dl_col, _ = st.columns([1, 2])
        with dl_col:
            csv_bytes = st.session_state.cleaned_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇️  Download Cleaned CSV",
                data=csv_bytes,
                file_name="cleaned_data.csv",
                mime="text/csv",
                use_container_width=True
            )

# ---------- EMPTY STATE ----------
if st.session_state.df is None:
    st.markdown("""
        <div class='glass-card' style='text-align:center; padding:60px 20px;'>
            <div style='font-size:64px;'>📂</div>
            <h2 style='color:white;'>No File Uploaded Yet</h2>
            <p style='color:#718096; font-size:15px; max-width:400px; margin:0 auto;'>
                Upload a CSV file above, then choose your cleaning options from the sidebar and click
                <strong>Run Cleaning</strong>.
            </p>
        </div>
    """, unsafe_allow_html=True)
